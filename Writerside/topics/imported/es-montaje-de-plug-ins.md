# Montaje de Plug-ins

Última actualización: Jun. 01, 2026

---

---

## Descripción

El montaje define cómo se mostrará el contenido en los cines, considerando la creación de *playlists* y el uso de *plug-ins*, los cuales son responsables de organizar y mostrar los diferentes tipos de contenido en el *player*.

Los detalles de formato de cada *plug-in* se pueden encontrar en  [Regras de Formatação](es-reglas-de-formato.md).

---

## 1. Montagje

El montaje de los *players* debe tener en cuenta si el contenido se mostrará en modo *videowall* o no:

- **Sin videowall:**
  - La cantidad de monitores corresponde al número de salidas de video de la máquina.
  - La resolución configurada debe ser equivalente a la resolución del monitor.
- **Con videowall:**
  - Cada salida de video puede admitir hasta 4 monitores.
  - La resolución se divide entre los cuadrantes.

**Ejemplo:** Una salida de video con resolución *Full HD* puede dividirse en cuatro monitores, cada uno con la mitad de la resolución total.

A continuación, se muestra una ilustración:

<img src="imported/shared/8cdedb1790ef9e33.png" alt="divisaosaidas.png"/>

---

## 1.1 Pantalla de Montaje

En la pantalla de montaje tenemos:

<img src="imported/shared/f21cdb4725191019.png" alt="image-20250916-173602.png"/>

1. **Nuevo layout:**Crea un nuevo layout para el player, que puede utilizarse como layout alternativo.
2. **Menu Layouts:**Selección del layout que se configurará/mostrará.
  - El *player* mostrará el contenido del último *layout* creado
  - Cuando existen varias opciones de *layout*, se muestra un ícono al lado para eliminarlo.
3. **Box Width (Ancho):** Define el ancho de la resolución del televisor/monitor donde se mostrará el *player*.
  - Para *players* 1x1, se utiliza el valor completo de la resolución (ej.: 1920).
  - Para *players* con más de una pantalla en la misma salida de video, el valor debe dividirse por dos (ej.: 1920 ÷ 2 = 960).
4. **Box Height (Altura):** Define la altura de la resolución del televisor/monitor donde se mostrará el *player*.
  - Para *players* 1x1, se utiliza el valor completo de la resolución (ej.: 1080).
  - Para *players* con más de una pantalla en la misma salida de video, el valor debe dividirse por dos (ej.: 1080 ÷ 2 = 540).
5. **Columns:**Número de columnas que se utilizarán en el montaje del *player*.
6. **Rows:** Número de filas que se utilizarán en el montaje del *player*.
7. **Week Days:** Días de la semana en que se mostrará el contenido. Cuando la letra correspondiente al día aparece en verde, significa que ese día está activo.

---

## 2. Plug-ins

Los *plug-ins* son módulos funcionales responsables de mostrar diferentes tipos de contenido en los *players*.

Cada *plug-in* está asociado a un tipo específico de medio o información (por ejemplo: películas, combos, precios, horarios), y el montaje del *player* se realiza combinando estos *plug-ins* dentro de un *layout*.

Los *plug-ins* son:

1. **Showtimes**
2. **Boxoffice**
3. **Player**
4. **Postercase** y **Smartpostercase**
5. **Combos**
6. **Menu**
7. **Prices**
8. **Mixplugins**
9. **Inactive**
10. **Orderscreen** – no utilizado

<img src="imported/shared/ce667e532a2577a8.png" alt="image-20250917-145540.png"/>

---

### 2.1 Showtimes

Muestra el horario y el tipo de las funciones, y pueden ordenarse alfabéticamente, por prioridad o por número de sesiones.

También es posible filtrar para que se muestren solo las funciones **regulares** o **prime**.

<img src="imported/shared/6bbe9242b3c4676e.png" alt="image-20250917-145630.png"/>

1. **Plug-in Screen:** Indica qué pantalla del *plug-in* debe mostrarse (varía entre 1 y 2 en *Showtimes 2.0*).
2. **Videowall Screen:** Posición dentro del *videowall* (de 1 a 16).
3. **Version:** 1.0 y 2.0.
4. **Switch Page Time:** Tiempo de cambio de página (n.º de películas × tiempo configurado en segundos).
5. **Show Only Next Sessions:** Oculta las funciones que ya han sido exhibidas.
6. **Filter:** Define si se mostrarán solo funciones **regulares**, **prime**, o **ambas** al seleccionar *none*.
7. **Order By:** Orden de exhibición (*alfabética*, *n.º de sesiones* o *prioridad*)
  - **Alphabetical:** Muestra las películas en orden alfabético.
  - **Number of Sessions:** Muestra las películas por número de funciones en orden descendente.
  - **Priority:** Muestra las películas según la prioridad configurada en *Settings | Order*
8. **Clone Screens:** No utilizado.
9. **Preview:** Vista previa de la exhibición en el *player*.

Ejemplo:

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Ejemplo

El **Showtimes 2.0** cuenta con una pantalla auxiliar, pudiendo funcionar como **1x1** o **2x1**.
Para mostrarla, la segunda pantalla del *plug-in* debe tener el número **2** en la configuración **Plugin Screen**

<img src="imported/shared/e3afe0dbc1082553.png" alt="2.png"/>

---

### 2.2 Boxoffice

Muestra los horarios de las funciones junto con el póster de la película.

<img src="imported/shared/2a8398aa4130458b.png" alt="image-20260323-235524.png"/>

1. **Plug-in Screen:** Pantalla del *plug-in* (de 1 hasta el número total de pantallas utilizadas).
  Es necesario que cada pantalla tenga asignado su número correspondiente para evitar duplicidad o ausencia de contenido.
2. **Videowall Screen:** Posición dentro del *videowall* (de 1 a 16).
3. **Version:** 1.0 y 2.0.
4. **Split Movies by Exhibitions:** Separa los ítems entre subtitulados y doblados.
5. **Agrupar películas por idioma:** Agrupa las sesiones por idioma.
  - Al activarlo, las sesiones se organizan por idioma (ej.: DOB / SUB).
6. **Activar multi carrusel:** Activa el multi carrusel.
  - Permite definir cuántas películas están “rotando” al mismo tiempo en el carrusel.
7. **Cantidad de películas en el carrusel:** Selecciona cuántas películas se muestran en rotación simultánea.
8. **Filtro:** Oculta las sesiones ya mostradas.
9. **Diseños (Layouts):** Número de sesiones mostradas por pantalla.
  - El plugin realiza un conteo automáticamente para que todas las sesiones se distribuyan entre los diseños disponibles.
10. **Ordenar por:**
  - **Primero:** Define el orden de los elementos.
    - **Alfabético:** Las sesiones se muestran en orden alfabético.
    - **Sesión:** Las sesiones se ordenan por cantidad de sesiones.
  - **Segundo:** Crea un suborden cuando los elementos tienen la misma prioridad según el primer criterio.
    - **Alfabético:** Las sesiones se muestran en orden alfabético.
    - **Sesión:** Las sesiones se ordenan por cantidad de sesiones.

**Ejemplo**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Ejemplo

El **BoxOffice** cuenta con pantallas que pueden mostrar **1, 3, 4 o 8 películas**.

La configuración de pantallas del *BoxOffice* debe tener en cuenta la cantidad de *plug-ins* que serán utilizados por el *player*.
**Ejemplo:** En un *player* con **4 BoxOffice**, el **Plugin Screen** debe configurarse de **1 a 4**.

<img src="imported/shared/84dca33473e1303c.png" alt="3.png"/>

**Ilustración de combinaciones**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Ilustración de combinaciones

Se permiten diferentes combinaciones de *layout* y, en caso de que se seleccione más de un tipo de *layout*, el *player* adapta la cantidad de películas/sesiones según el número de pantallas disponibles.

##### BoxOffice 1 Película

<img src="imported/shared/0c4e909bb41e685c.png" alt="5.png"/>

##### BoxOffice 3 Películas

<img src="imported/shared/c86c1fed979da94c.png" alt="6.png"/>

##### BoxOffice 4 Películas

<img src="imported/shared/a3ccfb874733aa0c.png" alt="7.png"/>

##### BoxOffice 8 Películas

<img src="imported/shared/a29382d24728db42.png" alt="8.png"/>

---

### 2.3 Player

Utilizado para la exhibición de videos o imágenes programados en una *playlist*.

<img src="imported/shared/40841ea8f77db26b.png" alt="image-20250917-150150.png"/>

1. **Plug-in Screen:**Corresponde ao quadrante do vídeo exibido.
2. **Position:**Posición en videowall.
3. **SV Size:**Configuración para el *Smartviewer*.
  - La primera pantalla muestra el número de cuadrantes del vídeo, y las siguientes se inicializan a cero.
  - Ejemplo: En un vídeo 4x1, la primera pantalla del plugin recibirá el número 4 en Tamaño SV, y las siguientes recibirán 0..
4. **Version:**Disponible solo en la versión 2.0.
5. **Screen Line / Screen Col:** Línea y columna del vídeo mostrado.
6. **Player Width / Player Height:** Ancho y altura del jugador
7. **Hide on Player:**Se utiliza en pantallas que son una extensión directa a la derecha.
8. **It's an extension:**Esto indica que el monitor es una extensión de otro monitor cuando no están en la misma línea.
9. **Extendeds Monitors:**Se utiliza para indicar en qué monitor se mostrará este vídeo.
  - Si la pantalla es una extensión, debe especificar el número de monitor donde comienza el vídeo..

---

**Instrucciones de montaje**

Este complemento se puede configurar en formatos 1x1, 2x1, 3x1 y 4x1 y en 3 situaciones diferentes:

1. **Cuando se utiliza la misma salida de vídeo**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

**PLAYER 1X1**

Los campos del plugin se rellenan con el número 1, excepto la pantalla del *Plugin Screen*, que siempre se rellenará con la posición de la pantalla en el videowall.

<img src="imported/shared/bdb5da4c2d7f18fe.png" alt="9-10.png"/>

**PLAYER 2X1**

La primera pantalla del plugin muestra los campos *Player Width* y *Player Height*, se rellenan según el tamaño del vídeo que se mostrará.

En la segunda pantalla del plugin, el campo se modifica *Plugin Screen* y *Screen Col* para indicar al reproductor que debe mostrar el segundo cuadrante del vídeo, es necesario activar el botón. *Hide on Player*.

<img src="imported/shared/32b4b82159f0c37f.png" alt="11-12.png"/>

**PLAYER 3X1**

Los campos se rellenan como en el formato 2x1, sin embargo, la primera pantalla del plug-in recibe en *Extendeds Monitors* el número de la pantalla que será una extensión de la misma.

La tercera pantalla, además de los campos de *Plugin Screen* y *Screen Col*, es necesario activar el botón *It's an extension* para indicar que esa pantalla es una extensión del monitor que se introducirá en el campo *Extended Monitors*.

<img src="imported/shared/f6a3856ed6e3e071.png" alt="13-14.png"/>

**PLAYER 4X1**

Los campos *Player Width* e *Player Height* estos campos se rellenan para posicionar el vídeo como un 2x2; los demás plugins reciben la posición del vídeo y *Player Col* Según el cuadrante del vídeo, además de *Hide on player* activado.

<img src="imported/shared/f5740c1167e6b364.png" alt="15-16.png"/>

##### **2. Cuando se encuentran en diferentes salidas de vídeo, pero están en la misma línea.**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

La primera pantalla del plugin muestra el tamaño del vídeo en los campos *Player Width* y *Player Height*.

En los casos restantes, los campos *Plugin Screen* y *Player Col* se rellenan según el cuadrante de vídeo y con la opción *Hide on player* activado.

**PLAYER 2X1**

<img src="imported/shared/4245cc420a54b588.png" alt="17-18.png"/>

**PLAYER 3X1**

<img src="imported/shared/e033fffe449e02be.png" alt="19-20.png"/>

**PLAYER 4X1**

<img src="imported/shared/0f260f1daa9ec6c3.png" alt="21-22.png"/>

##### **3. Al utilizar diferentes salidas de vídeo pero en líneas diferentes:**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

**PLAYER 2X1**

Los campos “*Screen Line*, *Screen Col*, *Player Width* e *Player Height”*, en la primera pantalla del complemento se rellenan con 1, y “*Extendeds Monitors”*recibe el número del monitor que será una extensión del mismo.

En la segunda pantalla, el contenido se llena de la misma manera que los otros complementos 2x1, pero con “*It's an extension”* activo, y “*Extendeds Monitors”* recibe el número de monitor correspondiente a la primera pantalla del complemento.

<img src="imported/shared/f5005585a3a8c575.png" alt="23-24.png"/>

**PLAYER 3X1 - Ejemplo 1**

En la primera pantalla, los campos *Screen Line* y *Screen Col* reciben el número y los campos *Player Width* y *Player Height* se rellenan para indicar que la sección es de 2x1. Los campos *Extendeds Monitors* recibe el número de pantalla que será una extensión de la misma; en este caso, la primera pantalla después del salto de línea del complemento, que en la imagen de abajo es el monitor 3.

La segunda pantalla está llena de campos *Screen Line* y *Screen Col* indicando que este será el segundo cuadrante del video y el *Hide on player* Es necesario activarlo.

Finalmente, la tercera pantalla se llena con los campos *Screen Line* y *Screen Col* indicando que este será el tercer cuadrante del video, el campo *Extendeds Monitors* Recibe el número de monitor correspondiente a la primera pantalla del complemento y lo activa *It's an extension*.

<img src="imported/shared/2532937dbdd83f29.png" alt="25-26.png"/>

**PLAYER 3X1 - Ejemplo 2**

os campos de Screen Line, Screen Col, Player Width y Player Height de la primera pantalla del complemento se rellenan con 1, y el campo Extendeds Monitors recibe el número del monitor que será una extensión de esta, que en la imagen de abajo es el monitor 3.

La segunda pantalla se rellena con los campos Screen Line y Screen Col, indicando que será el segundo cuadrante del video, y con los campos Player Width y Player Height, indicando que esa sección es 2x1.

El campo Extendeds Monitors recibe el número del monitor correspondiente a la primera pantalla del complemento y se activa la opción It's an extension.

Por último, la tercera pantalla se rellena con los campos Screen Line y Screen Col, indicando que será el tercer cuadrante del video, y con la opción Hide on player activada.

<img src="imported/shared/98d35c9303c79e9a.png" alt="27-28.png"/>

**PLAYER 4X1**

En la primera pantalla, los campos Screen Line y Screen Col reciben el número, y los campos Player Width y Player Height se rellenan indicando que esa sección es 2x1. El campo Extendeds Monitors recibe el número de la pantalla que será una extensión de esta, en este caso, la primera pantalla después del salto de línea del complemento, que en la imagen de abajo es el monitor 3.

La segunda pantalla se rellena con los campos Screen Line y Screen Col, indicando que será el segundo cuadrante del video, y Hide on player debe estar activado.

La tercera pantalla se rellena con los campos Screen Line y Screen Col, indicando que será el tercer cuadrante del video, y con los campos Player Width y Player Height, indicando que esa sección es 2x1.

El campo Extendeds Monitors recibe el número del monitor correspondiente a la primera pantalla del complemento y se activa It's an extension.

Por último, la cuarta pantalla se rellena con los campos Screen Line y Screen Col, indicando que será el tercer cuadrante del video, y con Hide on player activado.

<img src="imported/shared/7b0488fe8070ae64.png" alt="29-30.png"/>

---

### 2.4 Postercase y Smartpostercase

#### 2.4.1 Postercase

Se utiliza en las puertas de las salas de cine para mostrar el póster de la película que se está proyectando en esa sala.a.

<img src="imported/shared/563e9f9a21eb6fd2.png" alt="image-20250917-150235.png"/>

1. **Version:**1.0 y 2.0.
2. **Room:**El número correspondiente a la sala de cine donde se encuentra el player.
3. **Use BR Layout:**Activa el layout del *postercase* del Brazil.
4. **Smartpostercase:**Activa el plug-in *Smartpostercase*
5. **Preview:** Vista previa de la pantalla en el player.

#### 2.4.2 Smartpostercase

Muestra tráileres, carteles y otra información sobre las películas.

- *Presentando*, Muestra las películas que se están proyectando actualmente en el cine con sus horarios.
- *Proximamente*, Muestra películas que aún no se han estrenado y no tiene un horario fijo.

<img src="imported/shared/b250052b488aa29f.png" alt="image-20250917-150422.png"/>

1. **Version:**1.0, 2.0 y 2.1.
2. **Plug-in Screen:**Se utiliza para indicar qué pantalla de plug-in debe mostrarse.
  - En este caso, no es necesario cambiar el número de pantalla para que se muestre todo el contenido.
3. **Alineación de la sinopsis:** Left (izquierda), Center (centrado) y Justified (justificado).
4. **Presentando XML/API Path:**Camino de archivo/API para las películas que se están mostrando actualmente.
5. **Proximamente XML/API Path:**Camino de archivos/API para futuras versiones..
6. **Poster Change:**Tiempo de visualización de cada película contenida en el archivo.
7. **Smartpostercase ordering:**Orden en el que se proyectarán las películas.
8. **Mostrar director y país:** Cuando está desactivado, oculta la información del director y del país en el plugin

**Ejemplos - Postercase**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Ejemplos - Postercase

**Versión 1.0**

<img src="imported/shared/c0883e30b9880026.png" alt="postercase1BR.png"/>

**Versión 2.0**

<img src="imported/shared/31718fcab2acec85.png" alt="postercase2BR.png"/>

---

### 2.5 Combos

Muestra combos promocionales de películas.

Los campos iniciales se rellenan de forma estandarizada, independientemente de la versión.

El campo *Combos/XML* recibe la dirección de la API o el archivo JSON local.

<img src="imported/shared/606a73c75bcb6008.png" alt="image-20260601-130621.png"/>

1. **Plug-in Screen:**Indica qué pantalla del plugin debe mostrarse..
  - Las dos versiones de plug-in tienen la opción 2x1.
2. **Videowall Screen:**Posición en el *videowall*
3. **Versión:**1.0, 2.0 y 2.1.
4. **Width:**Largura de la pantalla de combos.
  - Siempre “1” en la versión 2.0 (incluso en 2x1)
5. **Is extends:**Esto indica que el vídeo será más largo.
  - Opción dirigida a la **versión 1.0.**
6. **Dual Monitor:**Se utiliza para indicar que el plug-in será 2x1.
7. **Combos XML:**DIRECCIÓN del XML/API de combos.
8. **Seconds to combo switch:**Hora en que se mostrará el combo.
  - En la **versión 1.0**, indica cuánto tiempo permanecerá estacionario el carrusel..
9. **Layout:**Tipo de layout.
  - Utilizado únicamente en la **versión 1.0.**
10. **Combo Header Font Size:**Tamaño de fuente del nombre de combos.
11. **Combo Price Font Size:**Tamaño de fuente para los precios.
12. **Gold Percent / Pro Percent:** Descuentos para clientes GOLD y PRO.
13. **Price Label:**Leyenda debajo del precio.
  - Utilizado únicamente en la **versión 1.0**.
14. **Special Color Price:**Color especial de los precios.
  - Utilizado únicamente en la **versión 1.0**.
15. **Invert price with special price:**Invierte el precio original con el precio promocional.
16. **Line through original price:**Inserte una línea roja sobre el precio original de combos.
  - Utilizado únicamente en la **versión  1.0.**
17. **Hidden Cents:**Oculta los céntimos de los precios.
  - Utilizado únicamente en la **versión 1.0.**

Los cambios en la API solo se reflejarán en el complemento en una hora, independientemente del tiempo de sincronización configurado.

**Instrucciones de configuración**

1. **REGULAR 1x1**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Los campos iniciales se rellenan de forma estandarizada, independientemente de la versión de plugin.

El campo Combos/XML recibe la dirección de la API o el archivo JSON local, como en el ejemplo siguiente.

<img src="imported/shared/27a5084cd9349f5d.png" alt="31-32.png"/>

##### Versión 2.1

Versión 2.1 de Combo se incluyó para mostrar la distribución por países.

Este valor diferenciado proviene directamente de la API y se muestra con el logotipo correspondiente al precio.

Actualmente, Cineplus se utiliza en cines de Centroamérica, y Gold y Pro en Colombia.

<img src="imported/shared/69e590267b689088.png" alt="combos21.png"/>

1. **REGULAR 2x1**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

**Versión 1.0**

En la primera pantalla, el campo **width**recibe el valor **2**, indicando el ancho del video que será programado en la playlist.

En la segunda pantalla, se activa el botón Is extends para que el video de la playlist se extienda, siguiendo la misma lógica del plug-in player.

**Versión 2.0**

Para la versión 2.0, el campo width seguirá recibiendo el valor 1, pero el botón Dual Monitor se activa en ambas pantallas del plug-in.

El campo Plugin Screen recibe los números 1 y 2, respectivamente.

<img src="imported/shared/dfb32456413f73d6.png" alt="33-34.png"/>

---

### 2.6 Menu

Muestra los artículos restantes en el mostrador de dulces (palomitas, bebidas, productos individuales).

Los campos iniciales se rellenan de forma estandarizada, independientemente de la versión.

<img src="imported/shared/844eaa6c3c6bed21.png" alt="1.png"/>

1. **Plug-in Screen:** Indica qué pantalla del plug-in debe mostrarse.
2. **Videowall Screen:** Posición en el videowall.
3. **Version:** 1.0, 1.1, Kosher (menú con layout personalizado), 2.0.
4. **Read old Smarthub xml:** No se utiliza.
5. **Xml Config:** Selección del diseño del xml/API e inclusión de la dirección de la API o del archivo json local que proporcionará la información del menú del cine.

#### 2.6.1 Areas config

<img src="imported/shared/54b43ddc861d5e55.png" alt="image-20250917-153124.png"/>

1. **Box Layout:**Campo completado con el tipo de layout utilizado por el plug-in..
2. **Code:**Define la categoría principal del producto, siempre representada por una sola letra.
  - La categoría **Palomitas** será siempre **A**.
  - La categoría **Bebidas** será siempre **B**.
  - Estas dos categorías no pueden tener variables.
3. **Variables:** Define las categorías secundarias.
  - Puede contener más de una letra.
  - Las letras deben estar separadas por comas, sin espacio (ej.: **F,G,H**).
4. **Background:**Define el color del cuadrante del plug-in.
  - Campo utilizado solo en la versión **2.0** del plug-in
  - Colores disponibles: **Red, Red2, White**.
5. **Show Video:**Permite elegir si se mostrará o no una playlist en el pie de página.
  - Funcionalidad exclusiva de la versión**2.0** del plug-in.
6. **Categorie Images:**Permite seleccionar qué categorías mostrarán una imagen del producto promocionado
  - Campo disponible solo en la versión**1.0** del plug-in.

---

**Box layout**

El campo *box layout* puedes seleccionar entre:

1. **REGULAR**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

<img src="imported/shared/8f69e8a1c33a2e65.png" alt="configmenuRegular.png"/>

***Show video*****activado**

<img src="imported/shared/d78a2784e7e119e5.png" alt="menuRegular2-video.png"/>

***Show video*****desactivado**

<img src="imported/shared/cbc7f56e2b5dc602.png" alt="menuRegular2-svideo.png"/>

1. **REGULAR-BISTRO**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Utiliza las mismas configuraciones del Menu Regular, modificando solo los layouts en la configuración del plug-in.

Este plug-in tiene un layout diferente y es utilizado por cines Bistro

<img src="imported/shared/a042b558ad611c30.png" alt="configmenuRegBistro.png"/>

<img src="imported/shared/7162e11b4cd2dbe2.png" alt="menuRegular-Bistro.png"/>

1. **REGULAR-PREMIERMIX**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Utiliza las mismas configuraciones del **menu Regular**, modificando solo los layouts en la configuración del plug-in.

Este plug-in tiene un layout diferente y es utilizado por cines PremierMix que desean mostrar videos en el pie de página del plug-in.

<img src="imported/shared/1cc2ef4c62b9349c.png" alt="configmenuRegPremier.png"/>

<img src="imported/shared/a04a7e75451ffeb5.png" alt="menuRegular-PremierMix.png"/>

1. **BISTRO**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Este plug-in no tiene productos específicos para las categorías (Palomitas A, Bebidas B) y muestra 3 ítems a la vez en cada pantalla, siendo posible agregar variables y configurar diferentes pantallas con diferentes categorías.

Tampoco tiene un video en el pie de página, pero es necesario agregar los nombres de los videos que se mostrarán en la pantalla utilizando el campo *Bistro Videos*. Si hay más de un video, los nombres deben estar separados por comas, sin espacio, según la imagen de abajo.

<img src="imported/shared/29ff50d7da7f8c37.png" alt="configmenuBistro.png"/>

<img src="imported/shared/58df00b6eb2c8025.png" alt="menuBistro.png"/>

1. **PREMIERMIX**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Utiliza las mismas configuraciones del Menu Regular, modificando solo los layouts en la configuración del plug-in.

Este plug-in tiene un layout diferente y es utilizado por cines PremierMix sin video en el pie de página.

<img src="imported/shared/104997538d99d953.png" alt="configmenuPremiermix.png"/>

<img src="imported/shared/b5b3580b946a1c09.png" alt="menuPremier-Mix.png"/>

1. **SELFSERVICE**

> Imagem não encontrada no ZIP: `wiki/images/icons/grey_arrow_down.png`

Expandir

Posee solo un campo obligatorio de categoría, que es el de Palomitas. Los demás ítems se distribuirán en el segundo box.

Tampoco tiene un video en el pie de página, pero cuenta con un video predeterminado que se muestra automáticamente en el pie del plug-in.

<img src="imported/shared/557cf2db6b73f488.png" alt="configmenuSelfService.png"/>

<img src="imported/shared/ecdd34d5c1f23206.png" alt="menuSelf-Service.png"/>

#### 2.6.2 Font Size

Permite al usuario seleccionar el tamaño de fuente que se mostrará, con tres opciones disponibles. Además, incluye una función de vista previa que permite ver cómo se verá la pantalla con el tamaño de fuente elegido.

<img src="imported/shared/e0db605f4a8beb97.png" alt="menusize4.png"/>

---

### 2.7 Prices

Muestra los precios de las entradas de cine, separados por tipo de sesión y sala.

<img src="imported/shared/ec99c7dd7ff74ead.jpg" alt="Prices.jpg"/>

1. **Plug-in Screen:**Indica qué pantalla del **plug-in** debe mostrarse.
  - Este **plug-in** posee solo pantallas **1x1**.
2. **Videowall Screen:** Posición en el videowall.
3. **Version:** Versión del **plug-in**.
4. **Prices XML (Today):** Dirección de la API de precios diarios.
5. **Prices XML (Weekly):** Dirección de la API de precios semanales.
6. **Token:** Clave de la API.
7. **Seconds to page switch:** Tiempo de visualización por página.
8. **Seconds to message switch:** Tiempo de visualización por línea del mensaje del encabezado.
9. **Customer font size:** Tamaño personalizado de la fuente.
10. **Hidden Cents:** Oculta los centavos.

---

### 2.8 Mixplugins

Utilizado para mostrar dos **plug-ins** diferentes en la misma pantalla.

1. **Plug-ins:**Selección de los dos plug-ins que se mostrarán en el mismo monitor.
  **Defina las duraciones** (Opción exibida após a escolha dos plug-ins): Define la duración de visualización de cada plug-in.

---

### 2.9 Inactive

Usado para **quadrantes** que no están en uso y no requieren configuración de **plug-in**.
