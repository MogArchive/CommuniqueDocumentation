#!/usr/bin/env python3
"""Import Confluence HTML exports into generated Writerside Markdown topics."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

from lxml import html


ROOT = Path(__file__).resolve().parents[1]
TOPICS_ROOT = ROOT / "Writerside" / "topics" / "imported"
IMAGES_ROOT = ROOT / "Writerside" / "images" / "imported"
LEGACY_TREE_PATH = ROOT / "Writerside" / "hi.tree"
TREE_START = "    <!-- BEGIN GENERATED CONFLUENCE IMPORTS -->"
TREE_END = "    <!-- END GENERATED CONFLUENCE IMPORTS -->"
DEFAULT_EXPORTS = {
    "br": ROOT / "CommuniqueBR.html.zip",
    "es": ROOT / "CommuniqueES.html.zip",
}


def slugify(value: str) -> str:
    import unicodedata

    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or "pagina"


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def page_title(doc, fallback: str) -> str:
    nodes = doc.xpath('//*[@id="title-text"]')
    title = clean_text(nodes[0].text_content()) if nodes else fallback
    return re.sub(r"^[^:]+:\s*", "", title).strip() or fallback


def page_id(path: Path) -> str:
    match = re.search(r"_(\d+)\.html$|^(\d+)\.html$", path.name)
    return next((g for g in match.groups() if g), path.stem) if match else path.stem


def unique_slugs(pages: list[dict]) -> None:
    used: set[str] = set()
    for page in pages:
        base = slugify(page["title"])
        candidate = base
        if candidate in used:
            candidate = f"{base}-{page['id']}"
        used.add(candidate)
        page["slug"] = candidate


class MarkdownConverter:
    def __init__(self, source_root: Path, links: dict[str, str], image_dir: Path):
        self.source_root = source_root
        self.links = links
        self.image_dir = image_dir
        self.copied_images: list[str] = []

    def children(self, node) -> str:
        result = node.text or ""
        for child in node:
            result += self.convert(child)
            result += child.tail or ""
        return result

    def image(self, node) -> str:
        raw_src = node.get("data-image-src") or node.get("src") or ""
        relative = unquote(urlsplit(raw_src).path).lstrip("/")
        if (
            relative == "wiki/images/icons/grey_arrow_down.png"
            and "expand-control-image" in (node.get("class") or "").split()
        ):
            return ""
        source = self.source_root / relative
        if not source.is_file():
            return f"\n\n> Imagem não encontrada no ZIP: `{relative}`\n\n"
        alt = clean_text(node.get("alt")) or source.name
        # Content-addressed names make identical attachments shared by both
        # languages and across different Confluence attachment directories.
        content = source.read_bytes()
        digest = hashlib.sha256(content).hexdigest()[:16]
        suffix = source.suffix.lower()
        if not suffix:
            if content.startswith(b"\x89PNG\r\n\x1a\n"):
                suffix = ".png"
            elif content.startswith(b"\xff\xd8\xff"):
                suffix = ".jpg"
            elif content[:6] in {b"GIF87a", b"GIF89a"}:
                suffix = ".gif"
            elif content.lstrip().startswith(b"<svg"):
                suffix = ".svg"
        name = f"{digest}{suffix}"
        self.image_dir.mkdir(parents=True, exist_ok=True)
        destination = self.image_dir / name
        if not destination.exists():
            shutil.copy2(source, destination)
        dark_destination = destination.with_name(f"{destination.stem}_dark{destination.suffix}")
        if not dark_destination.exists():
            shutil.copy2(source, dark_destination)
        self.copied_images.append(name)
        return f'\n\n<img src="../../images/imported/shared/{name}" alt="{alt}"/>\n\n'

    def link(self, node) -> str:
        label = clean_text(self.children(node)) or clean_text(node.get("href"))
        href = node.get("href") or ""
        parsed = urlsplit(href)
        target = Path(unquote(parsed.path)).name
        if target in self.links:
            href = self.links[target] + ".md"
            if parsed.fragment:
                href += "#" + slugify(parsed.fragment)
        elif href.startswith("attachments/"):
            return label
        return f"[{label}]({href})" if href else label

    def convert(self, node) -> str:
        tag = node.tag.lower() if isinstance(node.tag, str) else ""
        if tag in {"script", "style"}:
            return ""
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1]) + 1  # The page title already occupies H1.
            return f"\n\n{'#' * min(level, 6)} {clean_text(self.children(node))}\n\n"
        if tag == "p":
            value = self.children(node).strip()
            return f"\n\n{value}\n\n" if value else ""
        if tag == "br":
            return "  \n"
        if tag in {"strong", "b"}:
            return f"**{self.children(node).strip()}**"
        if tag in {"em", "i"}:
            return f"*{self.children(node).strip()}*"
        if tag == "code":
            return f"`{self.children(node).strip()}`"
        if tag == "pre":
            return f"\n\n```\n{node.text_content().strip()}\n```\n\n"
        if tag == "a":
            return self.link(node)
        if tag == "img":
            return self.image(node)
        if tag in {"ul", "ol"}:
            ordered = tag == "ol"
            lines = []
            for index, li in enumerate(node.xpath("./li"), 1):
                body = self.children(li).strip()
                body = re.sub(r"\n{2,}", "\n", body)
                body = body.replace("\n", "\n  ")
                lines.append(f"{index if ordered else '-'}{'.' if ordered else ''} {body}")
            return "\n\n" + "\n".join(lines) + "\n\n"
        if tag == "table":
            rows = []
            for tr in node.xpath(".//tr"):
                cells = [clean_text(cell.text_content()).replace("|", "\\|") for cell in tr.xpath("./th|./td")]
                if cells:
                    rows.append(cells)
            if not rows:
                return ""
            width = max(map(len, rows))
            rows = [row + [""] * (width - len(row)) for row in rows]
            output = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
            output.extend("| " + " | ".join(row) + " |" for row in rows[1:])
            return "\n\n" + "\n".join(output) + "\n\n"
        if tag == "hr":
            return "\n\n---\n\n"
        if tag == "li":
            return self.children(node)
        value = self.children(node)
        if tag in {"div", "section", "blockquote"}:
            return f"\n\n{value.strip()}\n\n" if value.strip() else ""
        return value


def normalize_markdown(value: str) -> str:
    value = value.replace("\u00a0", " ").replace("\ufeff", "")
    value = re.sub(r"[ \t]+\n", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip() + "\n"


def import_export(language: str, archive: Path, output: Path) -> dict:
    if not archive.is_file():
        raise FileNotFoundError(f"ZIP não encontrado: {archive}")
    topic_dir = output
    legacy_topic_dir = output / language
    if legacy_topic_dir.exists():
        shutil.rmtree(legacy_topic_dir)
    for old_topic in topic_dir.glob(f"{language}-*.md"):
        old_topic.unlink()
    topic_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix=f"communique-{language}-") as temp:
        temp_root = Path(temp)
        with zipfile.ZipFile(archive) as source_zip:
            members = [
                entry for entry in source_zip.infolist()
                if not (entry.is_dir() and not entry.filename.strip("/\\"))
            ]
            source_zip.extractall(temp_root, members=members)
        html_files = sorted(p for p in temp_root.rglob("*.html") if p.name.lower() != "index.html")
        pages = []
        for path in html_files:
            # Confluence exports declare UTF-8 in a legacy META tag that some
            # HTML parsers miss, so force the encoding instead of guessing.
            parser = html.HTMLParser(encoding="utf-8")
            doc = html.fromstring(path.read_bytes(), parser=parser)
            pages.append({"path": path, "name": path.name, "id": page_id(path), "title": page_title(doc, path.stem), "doc": doc})
        unique_slugs(pages)
        links = {page["name"]: f"{language}-{page['slug']}" for page in pages}
        report_pages = []
        for page in pages:
            content = page["doc"].xpath('//*[@id="main-content"]')
            if not content:
                continue
            for unwanted in content[0].xpath('.//*[contains(concat(" ", normalize-space(@class), " "), " toc-macro ")]'):
                unwanted.getparent().remove(unwanted)
            converter = MarkdownConverter(page["path"].parent, links, IMAGES_ROOT / "shared")
            body = normalize_markdown(converter.children(content[0]))
            destination = topic_dir / f"{language}-{page['slug']}.md"
            destination.write_text(f"# {page['title']}\n\n{body}", encoding="utf-8", newline="\n")
            report_pages.append({"source": page["name"], "topic": destination.name, "title": page["title"], "images": len(converter.copied_images)})

    index_title = "Documentação importada (Português)" if language == "br" else "Documentación importada (Español)"
    index_lines = [f"# {index_title}", "", "Conteúdo gerado automaticamente a partir da exportação do Confluence.", ""]
    index_lines.extend(f"- [{page['title']}]({page['topic']})" for page in report_pages)
    (topic_dir / f"{language}-index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8", newline="\n")
    return {"language": language, "archive": archive.name, "pages": report_pages, "images": sum(p["images"] for p in report_pages)}


def update_tree(reports: list[dict]) -> None:
    """Generate one complete Writerside instance per language."""
    for report in reports:
        language = report["language"]
        name = "Communique 5.3 — Português" if language == "br" else "Communique 5.3 — Español"
        start_page = "br-glossario.md" if language == "br" else "es-glosario.md"
        pages = report["pages"]
        if not any(page["topic"] == start_page for page in pages):
            raise ValueError(f"Página inicial não encontrada para {language}: {start_page}")
        ordered_pages = sorted(pages, key=lambda page: page["topic"] != start_page)
        sections = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<!DOCTYPE instance-profile SYSTEM "https://resources.jetbrains.com/writerside/1.0/product-profile.dtd">',
            "",
            f'<instance-profile id="{language}" name="{name}" start-page="{start_page}">',
        ]
        for page in ordered_pages:
            sections.append(f'    <toc-element topic="{page["topic"]}"/>')
        sections.extend([f'    <toc-element topic="{language}-index.md"/>', "</instance-profile>", ""])
        (ROOT / "Writerside" / f"{language}.tree").write_text("\n".join(sections), encoding="utf-8", newline="\n")

    if LEGACY_TREE_PATH.is_file():
        tree = LEGACY_TREE_PATH.read_text(encoding="utf-8")
        pattern = re.compile(r"\n?" + re.escape(TREE_START) + r".*?" + re.escape(TREE_END) + r"\n?", re.DOTALL)
        tree = pattern.sub("\n", tree)
        LEGACY_TREE_PATH.write_text(tree, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--br", type=Path, default=DEFAULT_EXPORTS["br"], help="ZIP da exportação em português")
    parser.add_argument("--es", type=Path, default=DEFAULT_EXPORTS["es"], help="ZIP da exportação em espanhol")
    parser.add_argument("--language", choices=["br", "es", "all"], default="all")
    args = parser.parse_args()

    TOPICS_ROOT.mkdir(parents=True, exist_ok=True)
    selected = ["br", "es"] if args.language == "all" else [args.language]
    archives = {"br": args.br.resolve(), "es": args.es.resolve()}
    if args.language == "all" and IMAGES_ROOT.exists():
        shutil.rmtree(IMAGES_ROOT)
    # Remove directories produced by versions of the importer before images
    # became content-addressed and shared between languages.
    for legacy_language in ("br", "es"):
        legacy_dir = IMAGES_ROOT / legacy_language
        if legacy_dir.exists():
            shutil.rmtree(legacy_dir)
    reports = [import_export(lang, archives[lang], TOPICS_ROOT) for lang in selected]
    # For a partial import, retain the last report for the other language so
    # its existing topics remain registered in the Writerside instance.
    report_path = TOPICS_ROOT / "import-report.json"
    if args.language != "all" and report_path.is_file():
        previous = json.loads(report_path.read_text(encoding="utf-8"))
        by_language = {report["language"]: report for report in previous}
        by_language.update({report["language"]: report for report in reports})
        reports = [by_language[lang] for lang in ("br", "es") if lang in by_language]
    update_tree(reports)
    report_path.write_text(json.dumps(reports, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for report in reports:
        print(f"{report['language'].upper()}: {len(report['pages'])} páginas, {report['images']} imagens")
    unique_images = len([p for p in (IMAGES_ROOT / "shared").glob("*") if not p.stem.endswith("_dark")])
    print(f"Imagens únicas compartilhadas: {unique_images}")
    print(f"Relatório: {report_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
