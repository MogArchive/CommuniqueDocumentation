# Lobby Domination

Última atualização: Ago. 18, 2026.

---

---

## Descrição

Seção destinada à programação do **Lobby Domination**, modalidade em que as mídias são exibidas simultaneamente em todos os players do cinema, interrompendo temporariamente a programação padrão.
Essa ação ocorre dentro de um **i**ntervalo de tempo pré-definido (por exemplo, 3 minutos) e em um período determinado previamente, garantindo destaque total ao conteúdo durante esse momento.

---

## 1. Regra de negócio

Atenção às regras de programação para diferentes tipos de Lobby Domination

1. É permitido a programação de apenas um advertiser por horário, isto é, caso dois advertisers precisem ser programados para um mesmo cinema o período precisa ser diferente para cada programação. Ex.: Avertiser A, das 10h às 18h. Avertiser B, das 18h às 24h.
2. Cada LD permite programar até duas mídias simultâneas. As mídias irão ser alternadas de acordo com o intervalo selecionado.

---

## 2. Lobby Domination - Tela inicial

<img src="imported/shared/642c6cc6bc448ef0.png" alt="image-20251030-153103.png"/>

1. **Botão de criação (+):**Inicia o processo para criar uma nova programação de Lobby Domination.
2. **Card principal em destaque:**Exibe a programação atual/selecionada com:
  - Nome.
  - Descrição.
  - Data e horário de início e término.
  - Nome do cliente.
  - Quantidade de cinemas e players selecionados
3. **Botões de navegação (⟵ / ⟶):**Permitem navegar entre as programações agendadas.
4. **Filtros:**
  - **Todos**: Exibe todos os registros disponíveis.
  - **Hoje**: Filtra e mostra apenas os registros correspondentes ao dia atual.
  - **Esta semana**: Apresenta os registros gerados durante a semana vigente, considerando o período de segunda-feira até a data atual.
  - **Este mês**: Exibe os registros referentes ao mês atual, abrangendo do primeiro ao último dia do mês.
  - **Mês (seleção manual)**: Permite ao usuário selecionar manualmente um mês específico para visualizar os registros associados a esse período.
5. **Barra de pesquisa:**Permite localizar programações pelo nome.
6. **Listagem de cards inferiores:**Mostra todas as campanhas programadas com miniaturas e ações (detalhar / excluir).

---

## 3. Programação de Lobby Domination

Clique no ícone

<img src="imported/shared/d92d1616d6ae888d.png" alt="image-20251029-180815.png"/>

 para iniciar a **programação de*****Lobby Domination***.

<img src="imported/shared/a53af6c7d76f90c3.png" alt="image-20260818-145609.png"/>

A programação é dividida em 4 fases:

- **Detalhes**
- **Media**
- **Players**
- **Resumo**

---

### 3.1 Detalhes

<img src="imported/shared/a53af6c7d76f90c3.png" alt="image-20260818-145646.png"/>

1. **Nome:**Campo para inserir o nome da programação.
2. **Descrição:**Campo opcional para adicionar uma breve descrição da programação.
3. **Cliente:**Seleção do cliente responsável pela campanha.
4. **Anunciante:**Seleção do anunciante vinculado à campanha.
5. **Data de Início:**Define a data em que a programação será iniciada.
6. **Data Final:**Define a data em que a programação será finalizada.
7. **Hora Inicial:**Define o horário inicial em que a programação será iniciada
8. **Hora Final:**Define o horário final em que a programação será finalizada
9. **Intervalo (min):**Determina o intervalo, em minutos, entre as exibições durante o período definido.
10. **Atraso:**Campo opcional utilizado para atrasar o início da programação no player, também em minutos.
  - Serve para evitar conflitos quando duas programações precisam começar no mesmo horário no mesmo player, permitindo que uma delas seja levemente postergada.

---

### 3.2 Media

Esta seção é destinada à **seleção das mídias** que serão vinculadas à programação.
O usuário poderá selecionar uma ou mais mídias disponíveis na lista.
Caso uma mesma mídia possua versões em diferentes formatos, é possível selecionar****todos os formatos desejados.

<img src="imported/shared/d1c595b8626edc52.png" alt="image-20251029-190208.png"/>

1. **Campo “Buscar”:**Permite localizar uma mídia específica pelo nome.
2. **Caixa de seleção:**A caixa de seleção permite selecionar ou desmarcar todas as mídias listadas.
3. **Nome:**Exibe o título ou identificação da mídia disponível.
4. **Formato:**Indica a proporção e a orientação da mídia.
5. **Pré-visualização:**Exibe o tempo de duração da mídia (em segundos) e um ícone de **play**, que permite visualizar o conteúdo antes de selecioná-lo.
6. **Botão “VOLTAR”:**Retorna à etapa anterior sem salvar alterações.
7. **Botão “CONTINUAR”:**Avança para a próxima etapa do processo após selecionar as mídias desejadas.

---

### 3.3 Players

Esta seção é responsável pela seleção dos **players** onde as mídias da programação serão exibidas.
A lista é organizada por cinema e permite definir quais players estão aptos a receber a mídia selecionada na etapa anterior.

<img src="imported/shared/99c59de941f58bb9.png" alt="image-20251030-163151.png"/>

1. **Barra de Busca:**Campo para localizar cinemas rapidamente digitando nome ou código.
  - Inclui ícone de lupa para confirmar a pesquisa.
2. **Cinema:**Lista de cinemas disponíveis.
  - Cada item possui um botão de seleção, permitindo escolher mais de um cinema por vez.
3. **Player:**Ao selecionar um cinema, os players disponíveis serão exibidos nesta coluna.
  - Apenas players com *playlist* compatível com a mídia selecionada são listados por padrão.
4. **Mostrar incompatíveis:**Checkbox que, quando ativado, exibe todos os players do cinema, incluindo aqueles com *playlist* **incompatível** com a mídia selecionada.
5. **Mídia:**Exibe qual mídia é compatível com a playlist daquele player.
  - Se há **uma mídia compatível**, ela aparecerá automaticamente selecionada.
  - Se houver **mais de uma mídia compatível**, todas serão exibidas **não selecionadas**, e o usuário deve escolher a correta.

---

### 3.4 Resumo

Tela final que apresenta uma pré-visualização completa das informações inseridas nas etapas anteriores antes da criação do evento.

<img src="imported/shared/0bab26612b2340b5.png" alt="image-20251030-144715.png"/>

1. **Detalhes:**Exibe os dados gerais da programação:
  - Nome.
  - Descrição.
  - Data e horário de início.
  - Data e horário de término.
  - Cliente selecionado.
2. **Media:**Listagem das mídias incluídas na progração:
  - Arquivos de mídia selecionados.
  - Formatos/variações correspondentes.
3. **Players:**Informações sobre onde a programação será exibido:
  - Quantidade total de cinemas selecionados (*Theaters*).
  - Quantidade total de players selecionados.
  - Lista de players exibidos por cinema:
    - *(Código do cinema → Nome do cinema → Player).*
4. **Criar**: Confirma e registra a programação com as informações apresentadas.
