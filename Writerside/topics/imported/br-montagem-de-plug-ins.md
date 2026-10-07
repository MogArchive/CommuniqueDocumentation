# Montagem de Plug-ins

Última atualização: Set. 18, 2025

---

---

## Descrição

A montagem define como o conteúdo será exibido nos cinemas, considerando a [**criação de playlists**](br-criacao-de-playlists.md) e a utilização de **plug-ins**, responsáveis por organizar e exibir os diferentes tipos de conteúdo no player.

Os detalhes de formatação de cada plug-in podem ser encontrados em [Regras de Formatação](br-regras-de-formatacao.md).

---

## 1. Montagem

A montagem dos players deve levar em conta se o conteúdo será exibido em modo **videowall** ou não:

- **Sem videowall:**
  - A quantidade de monitores corresponde ao número de saídas de vídeo da máquina.
  - A resolução configurada deve ser equivalente à resolução do monitor.
- **Com videowall:**
  - Cada saída de vídeo pode comportar até 4 monitores.
  - A resolução é dividida entre os quadrantes.

Exemplo: Uma saída de vídeo em resolução **Full HD** pode ser dividida em quatro monitores, cada um com metade da resolução total.

Segue ilustração:

<img src="imported/shared/8cdedb1790ef9e33.png" alt="divisaosaidas.png"/>

---

## 1.1 Tela de Montagem

Na tela de montagem temos:

<img src="imported/shared/f21cdb4725191019.png" alt="image-20250916-173602.png"/>

1. **Novo layout:**Cria um novo layout para o player, que pode ser usado como layout alternativo.
2. **Menu Layouts:**Seleção do layout que será configurado/visualizado.
  - O player exibirá o conteúdo do último layout criado.
  - Quando existe mais de uma opção de layout, um ícone de para deletar o layout é exibido ao lado.
3. **Box Width (Largura):** Define a largura da resolução da TV/Monitor em que o player será exibido.
  - Para players **1x1**, utiliza-se o valor inteiro da resolução (ex.: 1920).
  - Para players com mais de uma tela na mesma saída de vídeo, o valor deve ser dividido por dois (ex.: 1920 ÷ 2 = 960).
4. **Box Height (Altura):** Define a altura da resolução da TV/Monitor em que o player será exibido.
  - Para players **1x1**, utiliza-se o valor inteiro da resolução (ex.: 1080).
  - Para players com mais de uma tela na mesma saída de vídeo, o valor deve ser dividido por dois (ex.: 1080 ÷ 2 = 540).
5. **Columns:**Número de colunas que serão utilizadas na montagem do player.
6. **Rows:** Número de linhas que serão utilizadas na montagem do player.
7. **Week Days:** Dias da semana em que o conteúdo será exibido. Quando a letra referente ao dia da semana está verde, significa que esse dia está ativo.

---

## 2. Plug-ins

Os *plug-ins* são módulos funcionais responsáveis por exibir diferentes tipos de conteúdo nos players.

Cada plug-in é associado a um tipo específico de mídia ou informação (ex.: filmes, combos, preços, horários), e a montagem do player é feita a partir da combinação desses plug-ins dentro de um layout.

Os plug-ins são:

1. Showtimes
2. Boxoffice
3. Player
4. Postercase e Smartpostercase
5. Combos
6. Menu
7. Prices
8. Mixplugins
9. Inactive
10. Orderscreen - não utilizado

<img src="imported/shared/ce667e532a2577a8.png" alt="image-20250917-145540.png"/>

---

### 2.1 Showtimes

Exibe o horário e tipo das sessões e elas podem ser ordenadas alfabeticamente, por prioridade ou número de sessões.

Também é possível filtrar para que exiba apenas sessões regulares ou prime.

<img src="imported/shared/6bbe9242b3c4676e.png" alt="image-20250917-145630.png"/>

1. **Plug-in Screen:**Indica qual tela do plug-in deve ser exibida (varia entre 1 e 2 no Showtimes 2.0).
2. **Videowall Screen:**Posição no videowall (1 a 16).
3. **Version**: 1.0 e 2.0.
4. **Switch Page Time:**Tempo para troca de página (nº de filmes × tempo configurado em segundos).
5. **Show Only Next Sessions:**Oculta sessões já exibidas.
6. **Filter:**Define se serão exibidas apenas sessões regulares, prime ou ambas ao selecionar *none*.
7. **Order By:**Ordem de exibição (alfabética, nº de sessões, prioridade).
  - Alphabetical: Exibe os filmes em ordem alfabética.
  - Number of Sessions: Exibe o filme por número de sessões em ordem decrescente.
  - Priority: Exibe os filmes de acordo com a prioridade inserida em **Settings | Order**.
8. **Clone Screens** - não utilizado.
9. **Preview:** Prévia de exibição no player.

**Exemplo**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Exemplo

O **Showtimes 2.0**, possui uma tela auxiliar, podendo funcionar como 1x1 ou 2x1. Para exibi-la, a segunda tela do plug-in deve ter o número 2 na configuração *Plugin Screen*.

<img src="imported/shared/e3afe0dbc1082553.png" alt="2.png"/>

---

### 2.2 Boxoffice

Exibe horários de sessões junto ao pôster do filme.

<img src="imported/shared/25dcee9cea9a68e5.png" alt="image-20260224-161318.png"/>

1. **Plug-in Screen**: Tela do plug-in (1 até nº de telas utilizadas).
  - É necessário que cada tela seja preenchida com o número correspondente para que não haja duplicidade ou falta de conteúdo.
2. **Videowall Screen:**Posição no videowall (1 a 16).
3. **Version:** 1.0 e 2.0.
4. **Split Movies by Exihibitions:**Separa os itens por legendado e dublado.
5. **Juntar Filmes Por Idioma:** Agrupa sessões por idioma.
  - Ao ativar, as sessões são organizadas por idioma (ex.: DUB / LEG).
6. **Ligar Multi Carrossel:** Ativa o multi carrossel
  - Permite definir quantos filmes ficam “rodando” ao mesmo tempo no carrossel.
7. **Quantos Filmes No Carrossel:** Seleciona a quantidade de filmes exibidos em rotação simultânea.
8. **Filter:**Oculta sessões já exibidas.
9. **Layouts:**Número de sessões exibidas por tela.
  - O plug-in faz uma contagem automaticamente para que todas as sessões sejam distribuídas entre os layouts disponíveis.
10. **Order By:**
  - Primeiro: Define a ordem dos itens.
    - Alphabetical: As sessões são exibidas por ordem alfabética.
    - Session: As seções são ordenadas por quantidade de seção.
  - Segundo: Cria uma subordem quando os itens possuem a mesma prioridade com base na primeira seção.
    - Alphabetical: As sessões são exibidas por ordem alfabética.
    - Session: As sessões são ordenadas por quantidade de seção.

**Exemplo**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Exemplo

O **BoxOffice**, possui telas com 1, 3, 4 e 8 filmes.

A configuração de telas do Boxoffice precisa levar em conta a quantidade de plug-ins que serão utilizados pelo player. Ex.: Em um player com 4 BoxOffice, o *Plugin Screen* será de 1 à 4.

<img src="imported/shared/84dca33473e1303c.png" alt="3.png"/>

**Ilustração de combinações**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Ilustração de combinações

Diferentes combinações de layout são permitidas e, no caso de mais de um tipo de layout selecionado, o player adapta a quantidade de filmes/sessões de acordo com a quantidade de telas disponíveis.

##### BoxOffice 1 Filme

<img src="imported/shared/0c4e909bb41e685c.png" alt="5.png"/>

##### BoxOffice 3 Filmes

<img src="imported/shared/c86c1fed979da94c.png" alt="6.png"/>

##### BoxOffice 4 Filmes

<img src="imported/shared/a3ccfb874733aa0c.png" alt="7.png"/>

##### BoxOffice 8 Filmes

<img src="imported/shared/a29382d24728db42.png" alt="8.png"/>

---

### 2.3 Player

Utilizado para exibição de vídeos ou imagens programados em uma **playlist**.

<img src="imported/shared/40841ea8f77db26b.png" alt="image-20250917-150150.png"/>

1. **Plug-in Screen:**Corresponde ao quadrante do vídeo exibido.
2. **Position:**Posição no videowall.
3. **SV Size:**Configuração para o *Smartviewer*.
  - Na primeira tela é inserido o número de quadrantes do vídeo e nas demais coloca-se zero.
  - Exemplo: Em um vídeo 4x1, a primeira tela do plug-in receberá o número 4 no *SV Size*, as demais receberão 0.
4. **Version:**Disponível somente na versão 2.0.
5. **Screen Line / Screen Col:** Linha e coluna do vídeo exibido.
6. **Player Width / Player Height:** Largura e altura do player
7. **Hide on Player:**Utilizado nas telas que são uma extensão diretamente à direita.
8. **It's an extension:**Indica que aquele monitor é uma extensão de outro quando não estão na mesma linha.
9. **Extendeds Monitors:**Utilizado para indicar para qual monitor esse vídeo será estendido.
  - Se a tela for uma extensão, é necessário indicar o número do monitor em que o vídeo inicia.

---

**Instruções de montagem**

Este plug-in pode ser configurado nos formatos **1x1, 2x1, 3x1 e 4x1** e em 3 situações diferentes:

##### **1. Quando na mesma saída de vídeo**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

**PLAYER 1X1**

Os campos do plug-in são preenchidos com o número 1, com exceção do *Plugin Screen*, que sempre vai ser preenchido com a posição da tela no videowall.

<img src="imported/shared/bdb5da4c2d7f18fe.png" alt="9-10.png"/>

**PLAYER 2X1**

Na primeira tela do plug-in os campos *Player Width* e *Player Height*, são preenchidos de acordo com o tamanho do vídeo que será exibido por ele.

Na segunda tela do plug-in, altera-se o campo *Plugin Screen* e *Screen Col* para indicar ao player que ele deve exibir o segundo quadrante do vídeo e é necessário ativar o botão *Hide on Player*.

<img src="imported/shared/32b4b82159f0c37f.png" alt="11-12.png"/>

**PLAYER 3X1**

Os campos são preenchidos como no formato 2x1, porém a primeira tela do plug-in recebe em *Extendeds Monitors* o número da tela que será uma extensão dela.

Já a terceira tela, além dos campos de *Plugin Screen* e *Screen Col*, é necessário ativar o botão *It's an extension* para indicar que aquela tela é uma extensão do monitor que será inserido no campo *Extended Monitors*.

<img src="imported/shared/f6a3856ed6e3e071.png" alt="13-14.png"/>

**PLAYER 4X1**

Os campos *Player Width* e *Player Height* são preenchidos para posicionar o vídeo como um 2x2 os demais plug-ins recebem a posição do vídeo e *Player Col* de acordo com o quadrante do vídeo, além do *Hide on player* ativado.

<img src="imported/shared/f5740c1167e6b364.png" alt="15-16.png"/>

##### **2. Quando em diferentes saídas de vídeo, mas estão na mesma linha**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

A primeira tela do plug-in leva o tamanho do vídeo nos campos *Player Width* e *Player Height*.

Nas demais são preenchidos os campos *Plugin Screen* e *Player Col* de acordo com o quadrante do vídeo e com o *Hide on player* ativado.

**PLAYER 2X1**

<img src="imported/shared/4245cc420a54b588.png" alt="17-18.png"/>

**PLAYER 3X1**

<img src="imported/shared/e033fffe449e02be.png" alt="19-20.png"/>

**PLAYER 4X1**

<img src="imported/shared/0f260f1daa9ec6c3.png" alt="21-22.png"/>

##### **3. Quando em diferentes saídas de vídeo, mas em linhas diferentes:**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

**PLAYER 2X1**

Os campos de *Screen Line*, *Screen Col*, *Player Width* e *Player Height*, da primeira tela do plug-in, são preenchidos com 1 e o *Extendeds Monitors* recebe o número do monitor que será uma extensão dela.

Já na segunda tela, o conteúdo é preenchido conforme os demais 2x1, porém com o *It's an extension* ativo e o *Extendeds Monitors* recebe o número do monitor referente à primeira tela do plug-in.

<img src="imported/shared/f5005585a3a8c575.png" alt="23-24.png"/>

**PLAYER 3X1 - Exemplo 1**

Na primeira tela, os campos *Screen Line* e *Screen Col* recebem o número e os campos *Player Width* e *Player Height* são preenchidos indicando que aquela seção é 2x1. O campo *Extendeds Monitors* recebe o número da tela que será uma extensão dela, neste caso, a primeira tela após a quebra de linha do plug-in, que na imagem abaixo é o monitor 3.

A segunda tela é preenchida com os campos *Screen Line* e *Screen Col* indicando que aquele será o segundo quadrante do vídeo e o *Hide on player* precisa estar ativado.

Por fim, a terceira tela é preenchida com os campos *Screen Line* e *Screen Col* indicando que aquele será o terceiro quadrante do vídeo, o campo *Extendeds Monitors* recebe o número do monitor referente à primeira tela do plug-in e ativa-se o *It's an extension*.

<img src="imported/shared/2532937dbdd83f29.png" alt="25-26.png"/>

**PLAYER 3X1 - Exemplo 2**

Os campos de *Screen Line*, *Screen Col*, *Player Width* e *Player Height*, da primeira tela do plug-in, são preenchidos com 1 e o *Extendeds Monitors* recebe o número do monitor que será uma extensão dela, que na imagem abaixo é o monitor 3.

A segunda tela é preenchida com os campos *Screen Line* e *Screen Col* indicando que aquele será o segundo quadrante do vídeo e os campos *Player Width* e *Player Height* indicando que aquela seção é 2x1.

O campo *Extendeds Monitors* recebe o número do monitor referente à primeira tela do plug-in e ativa-se o *It's an extension*.

Por fim, a terceira tela é preenchida com os campos *Screen Line* e *Screen Col* indicando que aquele será o terceiro quadrante do vídeo e com o *Hide on player* ativado.

<img src="imported/shared/98d35c9303c79e9a.png" alt="27-28.png"/>

**PLAYER 4X1**

Na primeira tela, os campos *Screen Line* e *Screen Col* recebem o número e os campos *Player Width* e *Player Height* são preenchidos indicando que aquela seção é 2x1. O campo *Extendeds Monitors* recebe o número da tela que será uma extensão dela, neste caso, a primeira tela após a quebra de linha do plug-in, que na imagem abaixo é o monitor 3.

A segunda tela é preenchida com os campos *Screen Line* e *Screen Col* indicando que aquele será o segundo quadrante do vídeo e o *Hide on player* precisa estar ativado.

A terceira tela é preenchida com os campos *Screen Line* e *Screen Col* indicando que aquele será o terceiro quadrante do vídeo e os campos *Player Width* e *Player Height* indicando que aquela seção é 2x1.

O campo *Extendeds Monitors* recebe o número do monitor referente à primeira tela do plug-in e ativa-se o *It's an extension*.

Por fim, a quarta tela é preenchida com os campos *Screen Line* e *Screen Col* indicando que aquele será o terceiro quadrante do vídeo e com o *Hide on player* ativado.

<img src="imported/shared/7b0488fe8070ae64.png" alt="29-30.png"/>

---

### 2.4 Postercase e Smartpostercase

#### 2.4.1 Postercase

Utilizado nas portas de sala dos cinemas, exibe o pôster do filme que está em exibição naquela sala.

<img src="imported/shared/563e9f9a21eb6fd2.png" alt="image-20250917-150235.png"/>

1. **Version:**1.0 e 2.0.
2. **Room:**Número correspondente à sala do cinema em que o player está localizado.
3. **Use BR Layout:**Ativa o layout de *postercase* do Brasil.
4. **Smartpostercase:**Ativa o plug-in *Smartpostercase*
5. **Preview:** Prévia de exibição no player.

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Exemplos - Postercase

**Versão 1.0**

<img src="imported/shared/c0883e30b9880026.png" alt="postercase1BR.png"/>

**Versão 2.0**

<img src="imported/shared/31718fcab2acec85.png" alt="postercase2BR.png"/>

#### 2.4.2 Smartpostercase

Exibe trailer, pôster e outras informações dos filmes.

- *Presentando*, exibe filmes em cartaz do cinema com os horários das sessões.
- *Proximamente*, exibe filmes que ainda serão lançados e não possui horário.

<img src="imported/shared/56349ba1f0ad29a4.png" alt="image-20260224-163523.png"/>

1. **Version:**2.1.
2. **Plug-in Screen:**Utilizado para indicar qual tela do plug-in deve ser exibida.
  - Neste caso não é necessário alterar o número da tela para que todo o conteúdo seja exibido.
3. **Synopsis Alignment:** Left (esquerda), Center (centralizado) e Justified (justificado).
4. **Presentando XML/API Path:**Caminho do arquivo/API para filmes em cartaz.
5. **Proximamente XML/API Path:**Caminho do arquivo/API para próximos lançamentos.
6. **Poster Change:**Tempo de exibição de cada filme contido no arquivo.
  - O ideal é que o plugin tenha no mínimo 40s de exibição.
7. **Smartpostercase ordering:**Ordem de exibição dos filmes.
8. **Mostrar diretor e país:**Quando desativado, oculta a informação de diretor e país do plugin.

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Exemplos - Smartpostercase

**Smartpostercase com diretor e país**

<img src="imported/shared/e27216dc363e3fed.jpg" alt="smartposter2-20260224-180014.jpg"/>

**Smartpostercase sem diretor e país**

<img src="imported/shared/dfc0ac1cededf362.jpg" alt="poster2-20260224-180336.jpg"/>

---

### 2.5 Combos

Exibe combos promocionais do cinema.

Os campos iniciais são preenchidos de forma padronizada, independente da versão.

O campo *Combos/XML* recebe o endereço da API ou do arquivo json local.

<img src="imported/shared/07ea52f56cbd64c0.png" alt="image-20260601-125657.png"/>

1. **Plug-in Screen:**Indica qual tela do plug-in deve ser exibida.
  - As duas versões do plug-in possuem opção 2x1.
2. **Videowall Screen:**Posição no *videowall*
3. **Version:**1.0, 2.0 e 2.1.
4. **Width:**Largura da tela de combos.
  - Sempre “1” na versão 2.0 (mesmo em 2x1)
5. **Is extends:**Indica que o vídeo será estendido.
  - Opção direcionada a **versão 1.0.**
6. **Dual Monitor:**Utilizado para indicar que o plug-in será 2x1.
7. **Combos XML:**Endereço do XML/API de combos.
8. **Seconds to combo switch:**Tempo em que o combo será exibido.
  - Na **versão 1.0**, indica quanto tempo o carrossel ficará parado.
9. **Layout:**Tipo de layout.
  - Utilizado apenas na **versão** **1.0.**
10. **Combo Header Font Size:**Tamanho da fonte do nome dos combos.
11. **Combo Price Font Size:**Tamanho da fonte dos preços.
12. **Gold Percent / Pro Percent:** Descontos para clientes GOLD e PRO.
13. **Price Label:**Legenda abaixo do preço.
  - Utilizado apenas na **versão 1.0**.
14. **Special Color Price:**Cor especial dos preços.
  - Utilizado apenas na **versão 1.0**.
15. **Invert price with special price:**Inverte o preço original com o preço promocional.
16. **Line through original price:**Insere uma linha vermelha no preço original dos combos.
  - Utilizado apenas na **versão 1.0.**
17. **Hidden Cents:**Oculta os centavos dos preços.
  - Utilizado apenas na **versão 1.0.**

As alterações na API só será refletidas no plug-in somente em uma hora, independente do tempo de sync configurado.

**Instruções de configuração**

1. **REGULAR 1x1**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Os campos iniciais são preenchidos de forma padronizada, independente da versão do plugin.

O campo *Combos/XML* recebe o endereço da API ou do arquivo json local, conforme no exemplo abaixo.

<img src="imported/shared/27a5084cd9349f5d.png" alt="31-32.png"/>

##### Versão 2.1

A versão 2.1 do Combo foi incluída para exibir os Layouts dos países.

Esse valor diferenciado vêm direto da API e é exibido com a logo referente ao preço.

Atualmente utiliza-se Cineplus nos cinemas da América Central e Gold e Pró para a Colômbia.

<img src="imported/shared/69e590267b689088.png" alt="combos21.png"/>

1. **REGULAR 2x1**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

**Versão 1.0**

Na primeira tela o campo *width* recebe o valor 2 , indicando a largura do vídeo que será programado na playlist.

Na segunda tela o botão *Is extends* é ativado para que o vídeo da playlist seja estendido, seguindo a mesma lógica do plug-in *player*.

**Versão 2.0**

Para a versão 2.0, o campo *width* continuará recebendo o valor 1, porém o botão *Dual Monitor* é ligado em ambas as telas do plug-in.

O campo *Plugin Screen* recebe o número 1 e 2, respectivamente.

<img src="imported/shared/dfb32456413f73d6.png" alt="33-34.png"/>

---

### 2.6 Menu

Exibe os demais itens da bomboniere (pipoca, bebida, produtos avulsos).

Os campos iniciais são preenchidos de forma padronizada, independente da versão.

<img src="imported/shared/844eaa6c3c6bed21.png" alt="1.png"/>

1. **Plug-in Screen:**Indica qual tela do plug-in deve ser exibida.
2. **Videowall Screen:**Posição no *videowall*
3. **Version:**1.0, 1.1, Kosher (menu com layout customizado), 2.0
4. **Read old Smarthub xml** - não utilizado.
5. **Xml Config**: Seleção de layout do xml/API e inclusão do endereço da API ou arquivo json local que fornecerá as informações de menu do cinema.

#### 2.6.1 Areas config

<img src="imported/shared/54b43ddc861d5e55.png" alt="image-20250917-153124.png"/>

1. **Box Layout:**Campo preenchido com o tipo de layout utilizado pelo plug-in.
2. **Code:**Define a categoria principal do produto, sempre representada por uma única letra.
  - A categoria **Pipocas** será sempre **A**.
  - A categoria **Bebidas** será sempre **B**.
  - Essas duas categorias não podem ter variáveis.
3. **Variables:** Define as categorias secundárias.
  - Pode conter mais de uma letra.
  - As letras devem ser separadas por vírgula, sem espaço (ex.: `F,G,H`).
4. **Background:**Define a cor do quadrante do plug-in.
  - Campo utilizado apenas na versão **2.0** do plug-in.
  - Cores disponíveis: **Red, Red2, White**.
5. **Show Video:**Permite escolher se será exibida ou não uma playlist no rodapé.
  - Funcionalidade exclusiva da versão **2.0** do plug-in.
6. **Categorie Images:**Permite selecionar quais categorias exibirão uma imagem de produto divulgado.
  - Campo disponível apenas na versão **1.0** do plug-in.

---

**Box layout**

O Campo *box layout* pode ser selecionado entre:

1. **REGULAR**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

<img src="imported/shared/8f69e8a1c33a2e65.png" alt="configmenuRegular.png"/>

***Show video*****ativado**

<img src="imported/shared/d78a2784e7e119e5.png" alt="menuRegular2-video.png"/>

***Show video*****desativado**

<img src="imported/shared/cbc7f56e2b5dc602.png" alt="menuRegular2-svideo.png"/>

1. **REGULAR-BISTRO**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Utiliza as mesmas configurações do Menu Regular, alterando apenas os layouts na configuração do plug-in.

Este plug-in tem um layout diferente e é utilizado por cinemas Bistro.

<img src="imported/shared/a042b558ad611c30.png" alt="configmenuRegBistro.png"/>

<img src="imported/shared/7162e11b4cd2dbe2.png" alt="menuRegular-Bistro.png"/>

1. **REGULAR-PREMIERMIX**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Utiliza as mesmas configurações do menu **Regular**, alterando apenas os layouts na configuração do plug-in.

Este plugin tem um layout diferente e é utilizado por cinemas PremierMix que desejam exibir vídeos no rodapé do plug-in.p

<img src="imported/shared/1cc2ef4c62b9349c.png" alt="configmenuRegPremier.png"/>

<img src="imported/shared/a04a7e75451ffeb5.png" alt="menuRegular-PremierMix.png"/>

1. **BISTRO**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Este plug-in não tem produtos específicos para categorias (Pipocas A, Bebidas B) e exibe 3 itens por vez em cada tela, sendo possível acrescentar variáveis e configurar diferentes telas com diferentes categorias.

Também não possui um vídeo de rodapé, mas é necessário acrescentar o nome dos vídeos que serão exibidos na tela utilizando o campo *Bistro Videos*. Caso haja mais de um vídeo, os nomes devem ser separados por vírgula sem espaço, conforme imagem abaixo.

<img src="imported/shared/29ff50d7da7f8c37.png" alt="configmenuBistro.png"/>

<img src="imported/shared/58df00b6eb2c8025.png" alt="menuBistro.png"/>

1. **PREMIERMIX**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Utiliza as mesmas configurações do Menu Regular, alterando apenas os layouts na configuração do plug-in.

Este plug-in tem um layout diferente e é utilizado por cinemas PremierMix sem vídeo de rodapé.

<img src="imported/shared/104997538d99d953.png" alt="configmenuPremiermix.png"/>

<img src="imported/shared/b5b3580b946a1c09.png" alt="menuPremier-Mix.png"/>

1. **SELFSERVICE**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Possui apenas um campo obrigatório de categoria, que é o de pipocas. Os demais itens serão distribuídos no segundo box.

Ele também não possui um vídeo de rodapé, mas possui um vídeo padrão que é exibido no rodapé do plug-in automaticamente.

<img src="imported/shared/557cf2db6b73f488.png" alt="configmenuSelfService.png"/>

<img src="imported/shared/ecdd34d5c1f23206.png" alt="menuSelf-Service.png"/>

#### 2.6.2 Font Size

Permite ao usuário selecionar o tamanho da fonte exibida, com três opções disponíveis. Além disso, há uma funcionalidade de pré-visualização que permite verificar como a tela ficará com o tamanho de fonte escolhido.

<img src="imported/shared/e0db605f4a8beb97.png" alt="menusize4.png"/>

---

### 2.7 Prices

Exibe os preços dos ingressos do cinema, separado por tipo de seção e sala.

<img src="imported/shared/ec99c7dd7ff74ead.jpg" alt="Prices.jpg"/>

1. **Plug-in Screen:**Indica qual tela do plug-in deve ser exibida.
  - Este plug-in possui apenas telas 1x1.
2. **Videowall Screen:**Posição no videowall
3. **Version:**Versão do plug-in.
4. **Prices XML (Today):**Endereço da API de preços diários.
5. **Prices XML (Weekly)**: Endereço da API de preços semanais.
6. **Token:**Chave da API.
7. **Seconds to page switch:**Tempo de exibição por página.
8. **Seconds to message switch:**Tempo de exibição por linha da mensagem de cabeçalho.
9. **Customer font size:**Tamanho customizado da fonte.
10. **Hidden Cents:**Oculta os centavos.

---

### 2.8 Mixplugins

Utilizado para exibir dois plug-ins diferentes na mesma tela.

1. **Plug-ins:**Seleção dos dois plug-ins que serão exibidos no mesmo monitor.
2. **Defina as durações** (Opção exibida após a escolha dos plug-ins): Define a duração da exibição de cada plug-in.

---

### 2.9 Inactive

Usado para quadrantes que **não estão em uso** e não precisam de configuração de plug-in.
