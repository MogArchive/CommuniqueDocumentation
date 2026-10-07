# Players

Última atualização: Out. 30, 2025

---

---

## Descrição

Seção destinada à criação dos player utilizados no sistema.

Dividida em “**All Players**” e “**Player Group**”.

<img src="$WRS_MODULE$/images/imported/shared/a4be1d6bc552b3b7.png" alt="image-20250912-200041.png"/>

---

## 1. All Players

Tela de cadastro dos players.

<img src="$WRS_MODULE$/images/imported/shared/f78291c7aeba97ea.png" alt="image-20250912-195556.png"/>

---

### 1.1 Parte superior

Campos de pesquisa dos players cadastrados.

<img src="$WRS_MODULE$/images/imported/shared/386284ca33ac3138.png" alt="image-20250912-202318.png"/>

1. **Search:**Busca na coluna *Player.*
2. **Owner:**Busca na coluna *Owner.*
3. **Theater:** Busca na coluna *Theater.*
4. **Locate:**Busca na coluna *Locate - Category.*
5. **Player Category:**Busca na coluna *Locate - Category.*

---

### 1.2 Parte inferior

Gerenciamento dos players cadastrados.

<img src="$WRS_MODULE$/images/imported/shared/64e7cec5379b1217.png" alt="image-20250912-203453.png"/>

1. **Owner:** Empresa responsável pelo player.
2. **Theater:** Nome do cinema onde o player está instalado.
3. **Player:** Identificação do player.
4. **Hostname:** Nome atribuído ao dispositivo dentro de uma rede, podendo ser um computador, servidor ou outro equipamento. Pode ser verificado digitando o comando `hostname` no prompt de comando.
5. **Locate - Category:** Localização e categoria do player.
6. **Layout:** Layout associado ao player.
7. **Screens:** Quantidade de telas vinculadas ao player.

---

### 1.3 Criação de Player

Ao clicar no ícone “

<img src="$WRS_MODULE$/images/imported/shared/05e9b78f34d3bc0b.png" alt="image-20250912-204757.png"/>

” a tela para a criação de um novo player será exibida:

<img src="$WRS_MODULE$/images/imported/shared/026d5f65f97d788c.png" alt="image-20250912-204630.png"/>

<img src="$WRS_MODULE$/images/imported/shared/a43a6c0247b79cea.png" alt="image-20250912-204648.png"/>

#### 1.3.1 Information

<img src="$WRS_MODULE$/images/imported/shared/0ab9991c00b954cb.png" alt="image-20250912-210605.png"/>

1. **Name:** Nome dado ao player para melhor identificação.
2. **Hostname:** Nome atribuído ao dispositivo dentro de uma rede, podendo ser um computador, servidor ou outro equipamento. Pode ser verificado digitando o comando `hostname` no prompt de comando.
3. **MacAddress:**Endereço físico da placa de rede do dispositivo. Pode ser consultado digitando o comando `getmac` no prompt de comando.
4. **Theater:**Cinema onde está localizada a máquina. Ao clicar nessa seção, uma lista de cinemas é exibida.
5. **Player Category:**Categoria do player que pode ser definida pelo tipo de cinema:
6. **Locate:**Local do cinema onde o player será exibido.

#### 1.3.2 Display

<img src="$WRS_MODULE$/images/imported/shared/634681f3f8237167.png" alt="image-20250912-210701.png"/>

1. **Monitor:** Modelo do monitor utilizado.
2. **Inches:**Quantidade de polegadas do monitor.
3. **Screens (campo ao lado direito de inches):**Quantidade de monitores do player
4. **Screen Resolution:**Resolução dos monitores.
5. **Format:**Disposição das telas do player no local.
6. **Videowall:**Disposição das telas do player para montagem do diagrama. Pode ser o mesmo do item anterior ou possuir um formato diferente em caso de telas espelhadas.
7. **Orientação:**Indica se o monitor está posicionado na horizontal ou vertical.

#### 1.3.3 Montage

Definição de quantas máquinas e/ou saídas de vídeo serão utilizadas por este player.

É necessário que haja ao menos uma máquina e uma saída de vídeo.

<img src="$WRS_MODULE$/images/imported/shared/a9c24fcf315aea7f.png" alt="image-20250912-211037.png"/>

#### 1.3.4 Options

<img src="$WRS_MODULE$/images/imported/shared/3c444d3ef59ef5ed.png" alt="image-20250912-211215.png"/>

1. **Prevent:**Item de segurança que ao ser ativado, previne que o player faça algum tipo de download.
  1. **Config Prevent Sync:**Bloqueio de atualização das configurações no player.
  2. **Playlist Prevent Sync:** Bloqueio de atualização das playlists no player.
  3. **Sync Hour:**Horário de sincronização do player.
2. **Advertising:**Ativado por padrão. Utilizado em players que exibem campanhas, esta opção permite que o player registre e envie a contagem de exibição das mídias para o report de campanhas.
3. **Mix Template:**Utilizado para informar se o player possui o plug-in *Mix Template* ativado.
4. **Lobby Domination:**Utilizado em players que estão aptos à programação do *Lobby Domination.*
5. **Layer:**Utilizado em players que estão aptos à programação de *Layer.*

#### 1.3.5 Observation e Image

<img src="$WRS_MODULE$/images/imported/shared/b00de49dc3a27f04.png" alt="image-20250912-212203.png"/>

1. **Observation:**Campo destinado à alguma anotação específica do player.
2. **Image:**Foto do player sendo exibido no cinema.

---

### 1.4 Criação de playlists

Continue clicando [**aqui**](https://mogdesign.atlassian.net/wiki/x/AoAiAQ)**.**

---

### 1.5 Montagem de Plug-ins

Continue clicando [**aqui**](br-montagem-de-plug-ins.md)**.**

---

#### 1.5.1 Regras de Formatação

Continue clicando [**aqui**](br-regras-de-formatacao.md)**.**

---

## 2. Players Group

Agrupamento de players para programação de mídias e campanhas.

<img src="$WRS_MODULE$/images/imported/shared/381a9ba230ca6f42.png" alt="image-20250918-183300.png"/>

1. **Name:**Nome do grupo.
2. **Description**:****Descrição do grupo ou conteúdo.
3. **Duplicate**
  <img src="$WRS_MODULE$/images/imported/shared/1295b2b2af3c8e6b.png" alt="Duplica pg"/>
  : Duplica um playergroup já existente
4. **Delete**
  <img src="$WRS_MODULE$/images/imported/shared/045b7f531c2bb73f.png" alt="Delete pg"/>
  : Deleta o playergroup

O recurso conta com filtros por nome de player, cinema, locate e categoria. Ao clicar em um player da lista Players, ele é automaticamente enviado para a lista Players selected. Também é possível utilizar o botão

<img src="$WRS_MODULE$/images/imported/shared/7540b4fdbee23019.png" alt="Ida pg"/>

 para que todos os players filtrados sejam eviados para a lista da direita. Ao clicar em

<img src="$WRS_MODULE$/images/imported/shared/63f3decc3d2b1b3d.png" alt="Volta pg"/>

, os players saem da lista de selecionados e voltam para a lista geral.

<img src="$WRS_MODULE$/images/imported/shared/759005f8a35af28b.png" alt="image-20250918-183420.png"/>
