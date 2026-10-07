# Atualização pelos ZIPs do Confluence

Os arquivos `CommuniqueBR.html.zip` e `CommuniqueES.html.zip` são exportações HTML do Confluence. Eles não podem substituir diretamente os fontes do Writerside: as páginas precisam ser convertidas, os links reescritos e os anexos copiados.

## Atualizar

1. Substitua os dois ZIPs na raiz, mantendo os nomes atuais.
2. Instale a dependência (somente na primeira vez):

   ```powershell
   python -m pip install -r requirements-import.txt
   ```

3. Execute:

   ```powershell
   python scripts/import_confluence_exports.py
   ```

O comando recria somente estas pastas geradas:

- `Writerside/topics/imported/br-*.md`
- `Writerside/topics/imported/es-*.md`
- `Writerside/images/imported/shared`

As imagens recebem nomes baseados no conteúdo. Se BR e ES utilizarem a mesma imagem, somente uma cópia será armazenada.

Arquivos manuais em `Writerside/topics` e `Writerside/images` não são removidos nem sobrescritos. O resumo da importação fica em `Writerside/topics/imported/import-report.json`.

O importador também gera automaticamente duas instâncias completas: `Writerside/br.tree` e `Writerside/es.tree`. Isso permite validar os links separadamente e publicar cada idioma em sua própria URL. A instância manual legada `hi` é preservada.

Para atualizar apenas um idioma, use `--language br` ou `--language es`. Também é possível informar outro arquivo com `--br caminho.zip` ou `--es caminho.zip`.

## Publicação

O projeto atual publica as instâncias `Writerside/br` e `Writerside/es`, cujas navegações estão em `Writerside/br.tree` e `Writerside/es.tree`. A instância manual legada `Writerside/hi` é preservada no projeto, mas não faz parte dessa publicação.

Depois de importar, revise o relatório e as páginas geradas. Os índices e seus tópicos serão incluídos automaticamente na navegação de cada idioma.

O site publicado usa a versão 5.3 e disponibiliza um seletor BR/ES no cabeçalho. O português é publicado na raiz, preservando `/communique5.html`, enquanto o espanhol fica em `/es/`. O workflow também publica `versions.json` na raiz.

O endereço em português continua sendo https://mogarchive.github.io/CommuniqueDocumentation/communique5.html. O workflow copia o índice BR para esse caminho a cada publicação.

Com o builder `241.18775`, os arquivos gerados são `webHelpBR2-all.zip` e `webHelpES2-all.zip`. O build, o upload e a montagem do site devem usar esses mesmos nomes. Se um ZIP não for encontrado, o upload falha explicitamente em vez de continuar sem artefatos.

O build e a publicação continuam sendo feitos pelo workflow `.github/workflows/build-docs.yml` após o push na branch `main`.

Os ZIPs são apenas arquivos de entrada e estão no `.gitignore`; não é necessário enviá-los ao Git. Devem ser guardados fora do repositório caso seja necessário manter um histórico das exportações originais.
