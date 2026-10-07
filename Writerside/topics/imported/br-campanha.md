# Campanha

Última atualização: Out. 30, 2025

---

---

## Descrição

Seção utilizada para o gerenciamento de campanhas comerciais.

As campanhas representam anúncios publicitários de produtos, serviços ou marcas, que são contratados pelos clientes e inseridos na programação conforme datas e parâmetros definidos.

Nesta tela, o usuário pode visualizar todas as campanhas cadastradas, acompanhar seu status, identificar quem criou cada campanha e acessar detalhes individuais. Além disso, é possível filtrar, pesquisar e criar novas campanhas a partir deste módulo.

---

## 1. Campanha - Tela inicial

<img src="$WRS_MODULE$/images/imported/shared/3a0b593f54f84a7a.png" alt="image-20251030-173516.png"/>

#### **1. Menu de Navegação**

- **Visão Geral** - visão resumida do andamento das campanhas
- **Lista** - exibição detalhada de todas as campanhas cadastradas
- **Calendário** - visualização das campanhas no formato de agenda/período

#### **2. Botão** <img src="$WRS_MODULE$/images/imported/shared/d92d1616d6ae888d.png" alt="image-20251029-180815.png"/> **(Criar Campanha)**

Permite iniciar o cadastro de uma nova campanha publicitária.

#### **3. Campo de Pesquisa**

Permite localizar campanhas específicas utilizando termos como:

- Nome/Título da campanha
- Nome do criador
- Período

#### **4. Tabela de Campanhas**

Apresenta a listagem completa das campanhas registradas, com as seguintes colunas:

| Coluna | Descrição |
| --- | --- |
| Título | Nome identificador da campanha |
| Data de Início | Data programada para início da veiculação |
| Data Final | Data programada para encerramento da veiculação |
| Intervalo | Duração total da campanha (em dias) |
| Status | Situação atual da campanha:Em andamentoPausadaFinalizada |
| Criado por | Nome do usuário responsável pelo cadastro |

---

## 2. Criação de Campanha

Clique no ícone

<img src="$WRS_MODULE$/images/imported/shared/d92d1616d6ae888d.png" alt="image-20251029-180815.png"/>

 para iniciar a **programação de*****Campanha***.

A programação é dividida em 4 fases:

- **Informações da Campanha**
- **Mídia**
- **Players**
- **Resumo**

---

### 2.1 Informações da Campanha

Nesta etapa é definido o cadastro inicial da campanha, com informações essenciais como nome, cliente/anunciante, período de veiculação e quantidade de inserções diárias.

Após preenchidos os dados, o usuário segue para as próximas etapas de configuração.

<img src="$WRS_MODULE$/images/imported/shared/051985d4bb93ad8b.png" alt="image-20251030-173724.png"/>

#### **1. Nome**

Campo para inserir o nome da campanha.
Usado para identificação e pesquisa no sistema.

#### **2. Descrição**

Campo livre para detalhamento opcional da campanha, como observações internas ou informações sobre o conteúdo anunciado.

#### **3. Inserções por dia**

Quantidade de exibições desejadas por dia para essa campanha.

#### **4. Cliente**

Campo de busca e seleção do cliente responsável pela campanha.

- Digitação para busca.
- Lista suspensa com nomes cadastrados.

#### **5. Anunciante**

Seleção do anunciante (marca/produto) relacionado à campanha.
Pode ser o mesmo do cliente ou uma marca vinculada.

- Campo de busca.
- Lista suspensa.
- **Botão “+”**  permite cadastrar um novo anunciante sem sair do fluxo.

#### **6. Calendário**

Seletor de datas para definir o período de veiculação.

- Navegação por mês e ano
- Seleção da **data inicial**
- Seleção da **data final**

#### **7. Dias da semana**

Seleção dos dias em que a campanha será exibida.

#### **8. Botão “CONTINUAR”**

Avança para a próxima etapa de configuração da campanha (mídia).

---

### 2.2 Mídia

Nesta etapa o usuário seleciona quais mídias serão vinculados à campanha.

As mídias correspondem aos arquivos previamente cadastrados no sistema.

O objetivo desta tela é definir qual conteúdo será reproduzido durante a execução da campanha.

<img src="$WRS_MODULE$/images/imported/shared/c4de96357c0e8034.png" alt="image-20251030-174940.png"/>

#### **1. Busca**

Campo para localizar mídias por nome.
Útil para encontrar rapidamente conteúdos específicos em listas extensas.

#### **1. Filtro “Tipo de mídia”**

Permite filtrar a listagem conforme o tipo de arquivo/mídia disponível.

#### **2. Filtro “Cliente”**

Lista apenas as mídias relacionadas ao cliente selecionado.

#### **4. Lista de Mídias Disponíveis**

Área com todas as mídias cadastradas no sistema que atendem aos filtros aplicados.
Cada item exibe:

- Nome da mídia
- Informações de formato (ex.: 1x1, 2x1, H/V)
- Categoria ou tipo
- Cliente

#### **5. “Flix Media” (check box)**

Filtro específico para listar conteúdos da Flix Media (quando aplicável ao ambiente).
Habilita/Desabilita esse tipo de conteúdo na lista.

#### **6. Coluna “Mídias selecionadas” (lado direito)**

Lista das mídias escolhidas pelo usuário para compor a campanha.

À medida que itens são selecionados na coluna da esquerda, passam a aparecer aqui.

#### **7. Botão “VOLTAR”**

Retorna à etapa anterior (**Informações da Campanha**).

#### **8. Botão “CONTINUE”**

Avança para a próxima etapa: **Players**.

---

### 2.3 Players

Nesta etapa o usuário seleciona **players**onde a campanha será exibida.

A seleção correta do player garante que a mídia escolhida será exibida no local desejado.

<img src="$WRS_MODULE$/images/imported/shared/82d306fd3905066e.png" alt="image-20251030-175724.png"/>

#### **1. Campo “Buscar”**

Busca rápida para localizar players específicos pelo nome, código ou descrição do local.

#### **2. Filtro “Empresa”**

Exibe e filtra os players pertencentes a uma empresa específica.

#### **3. Filtro “Cinema”**

Permite selecionar players apenas de um cinema específico.

#### **4. Filtro “Local”**

Filtra os players por localidade dentro do cinema.

**5. Filtro “Categoria do player”**

Filtra os players de acordo com sua categoria.

#### **6. Filtro “Player Group”**

Permite selecionar grupos de players pré-definidos, facilitando campanhas que devem rodar em conjuntos específicos de telas.

#### **7. Ícones de legenda**

Indicadores que exibem o tipo/funcionalidade do player:

- 🅼 MixTemplate - players com plug-ins MixTemplate
- 🅻 Lobby Domination - player que permitem a exibição de Lobby Domination

Players com MixTemplate e Lobby Domination diminuem a quantidade de inserções de Campanha.

#### **8. Lista de Players Disponíveis**

Mostra todos os players que atendem aos filtros aplicados.

Cada player contém informações como:

- Código do player
- Nome do local
- Formato/Resolução (1x1, 3x1 etc.)
- Tipo (V/H — vertical ou horizontal)
- Empresa

Além de ícones indicando capacidades especiais (MixTemplate, Lobby Domination).

#### **11. Lista “Players selected”**

Mostra os players já escolhidos.
Também exibe o número total de players e empresas selecionadas.

#### **12. Botão “VOLTAR”**

Retorna à tela de seleção de mídias.

#### **13. Botão “CONTINUE”**

Avança para a próxima etapa: **Resumo**.

---

### 2.4 Resumo

Esta tela apresenta uma visão consolidada de todas as informações definidas nas etapas anteriores do cadastro de campanha.
O objetivo é permitir que o usuário valide as informações inseridas antes de finalizar e criar a campanha.

<img src="$WRS_MODULE$/images/imported/shared/4d3fdf037a46a0c3.png" alt="image-20251030-181013.png"/>

#### **1. Bloco de Informações Gerais**

- **Descrição:**Descrição da Campanha preenchida no passo 1.
- **Cliente:**Empresa contratante.
- **Anunciante:**Anunciante vinculado à campanha.
- **Intervalo:**Duração em dias de exibição da Campanha.
- **Status:**Situação atual da campanha
- **Data de Início / Data Final:**Período de veiculação definido no calendário

#### **2. Bloco de Players selecionados**

Resumo da distribuição da campanha.

- **Quantidade de empresas**
- **Quantidade de cinemas**
- **Quantidade de players**

Abaixo, lista cada player selecionado com:

- Código e nome do cinema.
- Nome do player

#### **4. Bloco de Mídias Selecionadas**

Indica quantidade total de mídias

Lista cada item com:

- Nome da mídia
- Formato (ex.: 3x1, 1x1)
- Orientação (H = horizontal / V = vertical)
- Duração

#### **5. Botão "VOLTAR"**

Retorna à etapa anterior (Players) caso seja necessário editar informações antes de confirmar.

#### **6. Botão “CRIAR CAMPANHA”**

Conclui o cadastro e grava a campanha no sistema.
A partir daqui ela passa a existir como campanha ativa ou planejada conforme data e status.

---
