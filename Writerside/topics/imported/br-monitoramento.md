# Monitoramento

Última atualização: Nov. 3, 2025

---

---

## Descrição

A seção de **Monitoramento** é responsável pelo acompanhamento em tempo real do funcionamento e da conectividade dos componentes do sistema. Por meio dela, é possível monitorar o status das **APIs**, a atividade dos **players**, os períodos **offline** e a **saúde geral do sistema**. Essa sessão fornece uma visão centralizada do desempenho operacional, permitindo a identificação rápida de falhas e a adoção de ações corretivas para garantir a estabilidade e a continuidade dos serviços.

<img src="$WRS_MODULE$/images/imported/shared/a8fe0d48a6857868.png" alt="image-20251031-192829.png"/>

Dividida em:

- **API**
- **Players**
- **Offline**
- **Saúde do sistema**

---

## 1. API

Na tela de **Monitoramento de API**, cada ícone circular representa o status da API de um cinema. O ícone verde indica que a comunicação está estável e operando corretamente, enquanto o ícone vermelho sinaliza instabilidade ou ocorrência de erros de conexão.

Ao clicar em qualquer um desses ícones, será exibido um card que apresenta uma visão detalhada das APIs configuradas para o cinema selecionado. Nessa visualização, é possível identificar quais APIs estão ativas, consultar os registros de requisições recentes, visualizar o código de retorno da API e, caso necessário, alterar o endereço da API clicando no ícone de engrenagem.

---

## 2. **Players**

A tela de **Monitoramento – Players** permite acompanhar em tempo real o status de conexão e as informações técnicas dos players instalados nos cinemas.

Cada **círculo** exibido na tela principal representa um **cinema**, e a cor do ícone indica o estado de conectividade dos players vinculados:

- **Azul** – todos os players do cinema estão conectados e funcionando normalmente.
- **Laranja** – um ou mais players do cinema estão desconectados.
- **Vermelho** – todos os players do cinema estão desconectados.

Na parte superior, indicadores gerais mostram os percentuais de sincronização dos players em diferentes intervalos de tempo (**Synced**, **Synced 3H**, **Synced 1D**, **Synced 1W**), bem como o número total de **cinemas (Theaters)** e **players (Players)** monitorados.

Ao clicar em um **cinema**, o sistema exibe, no painel lateral direito, os **detalhes do local selecionado**, incluindo:

- **Código do cinema (Code)**
- **Nome do cinema**
- **Horário de operação (Operations)**
- **Quantidade de players associados (Players)**

Logo abaixo, é exibida uma **lista lateral de players** pertencentes a esse cinema. Cada player é identificado por um ícone colorido que representa seu status:

- **Azul** – player conectado.
- **Vermelho** – player desconectado.

Ao selecionar um **player específico**, são apresentadas suas **informações técnicas detalhadas**, incluindo:

- **Localização (Locate)**
- **Status de conexão e horário da última atualização**
- **Hostname e endereço MAC**
- **Sistema operacional (OS)**
- **Processador (Processor)**
- **Memória (Memory)**
- **Armazenamento (Storage)**
- **Placa gráfica (Graphics)**
- **Resolução da tela (Resolution)**

Essa visualização fornece um diagnóstico completo do estado operacional de cada player, permitindo identificar falhas, monitorar desempenho e garantir o correto funcionamento da infraestrutura de exibição nos cinemas.

---

## 3. Offline

<img src="$WRS_MODULE$/images/imported/shared/c5ea4b5734c11004.png" alt="image-20251103-144741.png"/>

A tela de **Monitoramento – Offline** exibe um relatório detalhado gerado a partir do cinema selecionado e dos players associados a ele. O relatório apresenta informações sobre o status de **sincronização (Sync)**, **downloads** e **conexões de API**, permitindo acompanhar o funcionamento e a disponibilidade de cada player.

Para cada player listado, são exibidos os seguintes dados:

- **Sync (Sincronização)** – indica a data e hora da última sincronização das configurações (**Config**) e playlists (**Playlist**) do player.
- **Download** – mostra o status de download dos diferentes tipos de mídia vinculados ao player, como **pôsteres (Posters)**, **trailers (Trailers)** e **vídeos (Videos)**.
- **API** – apresenta o status de comunicação das APIs integradas ao sistema, incluindo **BoxOffice**, **Smartprice**, **Menu** e **Próximamente**, sinalizando se estão **sincronizadas (Synched)** ou com falhas.

Os ícones de marcação verde indicam que o componente está operando corretamente, enquanto eventuais alertas ou ausências de marcação apontam possíveis falhas de sincronização ou conectividade.

Essa tela permite ao usuário monitorar, de forma consolidada, o estado operacional dos players de um cinema específico, garantindo o controle e a rápida identificação de eventuais indisponibilidades.
