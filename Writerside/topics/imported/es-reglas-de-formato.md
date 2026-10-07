# Reglas de Formato.

Última actualización: Set. 18, 2025

---

---

## **1. Combos**

### **1.1 Versión 2.0**

#### Layout 1x1 (CONFIG)

- **Linea legal:**200 caracteres - Base 35px (3,3%), disminuye a 25px si el número de caracteres es mayor que 70 ***(CONFIG)***
- **Loyalty:**hasta 3 tipos ***(API)***
- **Precio Loyalty:**32px o 3% ***(API)***
- **Ícono Loyalty:**Altura máxima 119px o 11% ***(CONFIG)***
- **Nombre del combo:**26 caracteres - 97px o 9% ***(API)***
- **Precio do combo:**32px ou 4% ***(API)***
- **Lista de productos:**9 combos con 3 lineas - 30 caracteres - 57px o 5.3% ***(CONFIG)***
- **Still:**692 x 540 ***(CONFIG)***
- **Fuente:**Oswald ***(SOFTWARE)***

<img src="$WRS_MODULE$/images/imported/shared/366be0029520403f.png" alt="image-20250918-175138.png"/>

#### Layout 2x1 (CONFIG)

- **Linea legal:**200 caracteres - Base 38px (3,5%), disminuye a 27px si el número de caracteres es mayor que 70 ***(CONFIG)***
- **Loyalty:**hasta****3 tipos ***(API)***
- **Precio Loyalty:**32px ou 3% ***(API)***
- **Ícono Loyalty:**Altura máxima 119px o 11% ***(CONFIG)***
- **Nombre del combo:**38 caracteres - 97px o 9% ***(API)***
- **Precio del combo:**54px o 5% ***(API)***
- **Lista de produtos:**9 combos con 2 lineas - 40 caracteres - 57px o 5.3% ***(CONFIG)***
- **Still:**692 x 540 ***(CONFIG)***
- **Fuente:**Oswald ***(SOFTWARE)***

<img src="$WRS_MODULE$/images/imported/shared/48f4601cc3ff2e40.png" alt="image-20250918-175408.png"/>

---

### **1.2 Versión 1.0**

**Parte superior:**

- Playlist 2x1 (1920x540) o 4x1 (3840x540) ***(CONFIG)***

**Parte inferior:**

- **Quantidad de combos:**No hay límite.  ***(API)***
- **Tiempo de transición:**5s ***(CONFIG)***
- **Nombre del combo:**26 caracteres - Base 60px, disminuye según el número de caracteres. ***(API)***
- **Precio:**Máximo 6 caracteres - Base 60px, disminuye según el número de caracteres.  ***(API)***
- **Loyalty:**Máximo 2 tipos - Base 60px, disminuye según el número de caracteres.  ***(API)***
- **Still:**640 x 441 ***(CONFIG)***
- **Fuente:**Sinkin Sans ***(SOFTWARE)***

<img src="$WRS_MODULE$/images/imported/shared/438a1b59bc2b70d2.png" alt="image-20250918-175541.png"/>

---

## **2. Menus**

### **2.1 PremierMix**

- ***NOMBRES DE LAS CATEGORIAS (API)***
  - **A:** 21 caracteres - Pipocas
  - **B:** 15 caracteres - Bebidas
  - **C:** 21 caracteres
  - **D:** 15 caracteres
  - **Valores:** 06 caracteres
- ***NOMBRES DE LOS ITENS (API)***
  - **A:** 26 caracteres (Nombre de la subcategoría + Nombre del producto)
  - **B:** 22 caracteres (sIN Amount o Nome del Producto + Amount)
  - **C:**27 caracteres
  - **D:** 22 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versión:**1.0 ***(CONFIG)***
- **Tiempo de transición de categoría:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:** No tiene
- **Fuentes:** GaramondItalic, Garamond
- **Categoria:** 100px
- **Nombre del Producto:** 48px
- **Precio:** 48px

<img src="$WRS_MODULE$/images/imported/shared/7c169c649206ab58.png" alt="image-20250918-175814.png"/>

### **2.2 SelfService**

- ***NOMBRES de CATEGORIAS (API)***
  - **A:** 17 caracteres - Pipocas
  - **A2:** 9 caracteres (nombres en la misma línea que el nombre de la categoría) - Salado, Dulce
  - **B:** 21 caracteres - Bebidas
  - **C-Z:** 22 caracteres
  - **Valores:**  06 caracteres
- ***NOMBRES ITENS (API)***
  - **A:** 29 caracteres - Mediano, Grande
  - **B-Z:** 24 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versão:**1.0 ***(CONFIG)***
- **Tempo de transición das las categorias:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:** No tiene
- **Fontes:** Norwester, Sinkin Sans
  - **Pipoca**
    - **Categoria:**58px
    - **Subcategoria:** 56px
    - **Nombre del Producto:** 41px
    - **Precio:** 41px
  - **Demais categorias**
    - **Categoria:** 48px
    - **Nombre del Producto:** 38px
    - **Precio:** 38px

<img src="$WRS_MODULE$/images/imported/shared/93ce0099651da3ae.png" alt="image-20250918-180211.png"/>

### **2.3 Bistrôo**

- ***NOMBRE de las CATEGORIAS (API)***
  - 22 caracteres - Helados, Bebidas, Dulces
  - **Valores:** 06 caracteres
- ***NOMBRE ITENS (API)***
  - 25 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versão:**1.0 ***(CONFIG)***
- **Tiempo de transición de las categorias:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:** No tiene
- **Fontes:** Rubik, Futura
- **Categoria:**55px
- **Nombre del Producto:** 34px
- **Precio:** 34px

<img src="$WRS_MODULE$/images/imported/shared/3889ca7c2d711fea.png" alt="image-20250918-180335.png"/>

### **2.4 Kosher**

- ***NOME CATEGORIAS (API)***
  - 16 caracteres - Mediana, Grande etc
  - **Valores:** 06 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versión:**Kosher ***(CONFIG)***
- **Fuente:**
- **Tamaño:**
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos (categoria precisa ter a palavra KOSHER no nome) ***(CONFIG)***
- **Playlist:** No tiene
- **Fuentes:** Oswald, Typold, SinkinSans
- **Frase 1:** DISFRUTA EL SABOR Y LA FRESCURA DE LAS PALOMITAS DE CINEMARK - 5% ou 54px
- **Frase 2:** AHORA CON LA CERTIFICACIÓN KOSHER - 8% o 86px
- **Nombre del producto**: 4% o 43px
- **Precio:** 3.5% o 38px
- **Logo:**  12% o 240px

<img src="$WRS_MODULE$/images/imported/shared/cd4dd19627a97b44.png" alt="image-20250918-180511.png"/>

---

## **3. Regular**

### **3.1 Fonte P**

- ***NOMBRE DE LAS CATEGORIAS (API)***
  - **A:** 08 caracteres - Pipoca
  - **A2:** 21 caracteres (3 TIPOS) | 11 caracteres (5 TIPOS) - Pequeño, mediano, grande
  - **B:**08 caracteres - Bebidas
  - **C-Z:** 20 caracteres
  - **Valores:** 06 caracteres
- ***NOMES ITENS (API)***
  - **A:** 12 caracteres - Salado, Dulces, Mixtas
  - **B CIMA:** 12 caracteres - Mediana, Grande
  - **B LATERAL:**26 caracteres
  - **C-Z:** 36 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **VersIÓN:**2.0 ***(CONFIG)***
- **Tiempo de transición entre categorías:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:**Puede que muestre o no en el player.

### **3.2 Fuente M**

- ***NOMBRES de las CATEGORIAS (API)***
  - **A:**08 caracteres - Pipoca
  - **A2:** 20 caracteres (3 TIPOS) | 10 caracteres (5 TIPOS) - Pequeño, mediano, grande
  - **B:** 08 caracteres - Bebidas
  - **C-Z:** 20 caracteres - Snacks, Extras
- ***NOMBRES de los ITENS (API)***
  - **A:** 10 caracteres - Salado, Dulces, Mixtas
  - **B CIMA:** 11 caracteres - Mediana, Grande
  - **B LATERAL:**25 caracteres
  - **C-Z:** 29 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versión:**2.0 ***(CONFIG)***
- **Tiempo de transición de las categorias:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:**Puede que muestre o no en el player.

### **3.3 Fonte G**

- ***NOMBRES de las CATEGORIAS (API)***
  - **A:** 08 caracteres - Pipoca
  - **A2:** 19 caracteres (3 TIPOS) | 9 caracteres (5 TIPOS) - Pequeño, mediano, grande
  - **B:** 08 caracteres - Bebidas
  - **C-Z:** 20 caracteres
- ***NOMBRES de los ITENS (API)***
  - **A:** 09 caracteres - Salado, Dulces, Mixtas
  - **B CIMA:** 9 caracteres - Mediana, Grande
  - **B LATERAL:**23 caracteres
  - **C-Z:** 24 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versão:**2.0 ***(CONFIG)***
- **Tempo de transição das categorias:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:**Puede que muestre o no en el player.
- **Fuente:** SinkinSans
- **Titulo:** Pequeño 5% - 54px | Mediano 5% - 54px | Grande 5% - 54px
- **Nombre del Producto:** (Pipoca e Bebida) Pequeño 3% o 32px | Medio 3.5% o 38px | Grande 4% o 43px
- **Gramatura del Producto:** Pequeño 1.5% ou 16px | Mediano 2% ou 21px | Grande 2.3% ou 25px
- **Nombre del Producto:** (Bebidas adicionales y otras categorías) Pequeño 2,5 % o 27 px | Mediano 3 % o 32 px | Grande 3,5 % o 38 px
- **Precio Decimal:**Pequeño 3,5 % o 38 px | Mediano 4 % o 43 px | Grande 4,2 % o 45 px
- **Precio Símbolos y Centavos:** Pequeño 2,5 % o 27 px | Mediano 3 % o 32 px | Grande 3,5 % o 38 px

<img src="$WRS_MODULE$/images/imported/shared/40fc369127e7c7c9.png" alt="image-20250918-180847.png"/>

---

## **4. Showtimes**

<img src="$WRS_MODULE$/images/imported/shared/06762cd5a775b4c3.png" alt="image-20250918-181244.png"/>

<img src="$WRS_MODULE$/images/imported/shared/ab7815cec1b85f2f.png" alt="image-20250918-181307.png"/>

- **Nombre de la película:** Hasta 39 caracteres (API)
- **Censura de imagen:** 94 x 107 ***(CONFIG)***
- **Sección de categoría de imagen:**781 x 507 ***(CONFIG)***
- **Horário*****(API)***
- **Audio*****(API)***
- **Sin playlist:** 8 lineas ***(CONFIG)***
- **Con playlist:** 6 lineas ***(CONFIG)***
- **Versión:** 2.0 ***(CONFIG)***
- **Layout:** 1x1 y 2x1 ***(CONFIG)***
- **Ordenación:**Orden alfabético, número de sesiones y prioridad ***(CONFIG)***
- **Período de transición:**Actualmente 3 segundos por línea ***(CONFIG)***
- **URL API*****(CONFIG)***
- http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCartelera (AL)
- http://host_server_cinema/apolo/services/partner/mog/api/v1/BoxOffice?pEstabelecimentoCodigo=**X** (BR)
  - La letra “**X**” equivalente al código interno del cine
- **Quantidad de horários:**5 por linea ***(SOFTWARE)***
  - A partir de 5 horarios de proyección, el plugin crea una línea de tiempo doble para la película, mostrando hasta 10 horarios de proyección. Después de 10 horarios de proyección, se crea otra línea de tiempo.

<img src="$WRS_MODULE$/images/imported/shared/be4edb6ca1d23178.png" alt="image-20250918-181215.png"/>

- **Tamaño de las fuentes*****(SOFTWARE)***
  - **Título:** 35px o 3%
  - **Horário**: 48px o 4.5%
  - **Áudio:** 27px o 2.5%
- **Fuente:** Oswald ***(SOFTWARE)***

---

## **5. Prices**

<img src="$WRS_MODULE$/images/imported/shared/8129de88b620dbca.png" alt="image-20250918-181532.png"/>

- **Texto Topo:**Diecisiete frases de hasta 92 caracteres***(API)***
  - **Día de la semana:** 35px o 3.25%
  - **Fecha:** 30 px o 2,77 %
  - **Mensaje:**Varía según el tamaño del mensaje (base 2,6 % - 28 px)
  - **Hora:** 70 px o 6,5 %
- **Categoria -** Regular/Premier**(*****API) y (SOFTWARE)***
- **Tamaño de las fuentes:**
  - **Pequeño:** 2.96% o 32px
  - **Mediano**: 3.76% o 40px
  - **Grande:** 3.76% o 40px
- **2D/3D*****(SOFTWARE)***
  - **Pequeño**: 2.96% o 32px
  - **Mediano:** 3.66% o 39px
  - **Grande:** 3.66% o 39px
- **Matiné/Noite*****(SOFTWARE)***
  - **Pequeño**: 2.3% ou 25px
  - **Mediano/Grande:** 32px ou 3%
- **Precios:** ***(API)***
  - **Tamaño pequeño normal:**valor - 2,96 % o 32 px | símbolo - 1,85 % o 20 px
  - **Tamaño pequeño dorado**: valor - 3 % o 32 px | símbolo - 21 px
  - **Tamaño mediano/grande normal:**valor - 3,66 % o 40 px | símbolo - 2,55 % o 27 px
  - **Tamaño mediano/grande dorado:**valor - 3,66 % o 40 px | símbolo - 2,7 % o 29 px
- **Poster:**1280x870 -  300Kb ***(CONFIG)***
- **Próxima Sesión:** ***(SOFTWARE)***
  - **Titulo:** 2.5% o 27px
  - **Horário:** 11% o 118px
  - **Áudio:** 3.3% o 35px
  - **3D/2D:** 5% o 54px
- **Nombre del Filme:** hasta 57 caracteres ***(API)***
- **Sala:**3.3% o 35px ***(API)***
- **Clasificación:** **(Upload Communique)**
- **Fuente:**Rubik, Sora y San Francisco Compact

---

## **6. BoxOffice**

<img src="$WRS_MODULE$/images/imported/shared/b556370cfbd85bec.png" alt="image-20250918-181811.png"/>

- **Título de la película: (API)**
- Título de la película con 1 pantalla: 59 caracteres ***(API)***
  - **Tamaños de fuente**:
  - **Título:**4,44 % o 48 px
  - **Hora:** 5 % o 54 px
  - **Audio:**1,5 % o 16 px
- **Nombre de la película con 3 pantallas:**80 caracteres ***(API)***
- **Tamaño de fuente:**
  - **Título:** 3% o 32 píxeles
  - **Hora:** 3% o 32 píxeles
  - **Audio:**1,2% o 12 píxeles
- **Título de película con 4 posters:** 78 caracteres caben en tres líneas. ***(API)***
- **Tamaño de fuente:**
  - **Título:** 3% o 32px
  - **Horário**: 3% o 32px
  - **Áudio:** 1.2% o 12px
- **Título de la película con 8 posters:** 64 caracteres ***(API)***
- **Tamaño de fuente:**
  - **Título:** mayor  | menor
  - **Horário**: mayor  | menor
  - **Áudio:** mayor  | menor
- **Classificação: (*****Upload Communique)***
- **Tamaño de la Imagen**
  - **IMAX:** 150x25
  - **4D:**70x60
  - **2D:** 781x507
  - **3D:** 781x507
  - **D-BOX LARGE:** 313x52
  - **D-BOX:** 150x25
  - **PRIME:** 781x507
  - **XD:**781x507
  - **Classificación :** 94x107
- **XD: (*****Upload Communique)***
- **Horarios:*****(API)***
- **Audio Filme: (*****API)** y**(SOFTWARE)***

---

## **7. Postercase**

- **Título de la película:** Hasta 65 caracteres**. (Fonte\ tamanho )  (*****API*****)**
- **Imagen:**870x1280 POSTER **Upload (*****CONFIG*****)**
- **Sesión : (API) (fuente)**
- **Censura de clasificación de imágenes :**D. 352x180**(*****CONFIG*****)**
- **D-BOX LARGE: 313x52**
- **D-BOX: 150x25 (*****API*****)**
- **CensorshipMessage :**límite de 4 códigos**( fuente)**
- **Logotipo de la sala: (API) (fuente)**
- **Tipo de sala: (API) (fuente)**
- **Horario: (API) (fuente)**
- **Versión del plugin :** 1x1****
- **URL (*****API*****)**
- **Plugin Screen*****(CONFIG)***
- **Tamaño de censura BR:**362x180
- **Tamaño de censura demasiados países:**94x107

- **Fontes:** Oswald, MADE Outer Sans, Rubik
- **Titulo (Variável):** 44px
- **Audio:**4.5% o 48px
- **Tipo de sala:** 5% - 54px
- **Texto (Próxima sesión):** 4.8% o 52px
- **Horário:** 13.3% o 144px
- **Frases Informativas:**20px

<img src="$WRS_MODULE$/images/imported/shared/e0851c5a9aa93d40.png" alt="image-20250918-182222.png"/>

---

## **8. SmartPostercase**

<img src="$WRS_MODULE$/images/imported/shared/4a668663b75939b7.png" alt="image-20250918-182239.png"/>

- **Título de la película:** Hasta 35 caracteres - 60 px (variable) **(API)**
- **Tráiler:**1280x720 o 1920x1080 - hasta 20 MB **(CONFIG)**
- **Póster:**1280x870 - 300 KB **(CONFIG)**
- **Sinopsis (60 px)**: 508 caracteres - 24 px **(variable) (API)**
- **Reparto**: 8 nombres de hasta 23 caracteres cada uno **(API)**
- **Género*****(API)***
- **Director:**2 nombres hasta 23 caracteres cada ***(API)***
- **Duración*****(API)***
- **País*****(API)***
- **Classificación:**94 x 107 ***(CONFIG)***
- **Información adicional sobre la película (reparto, duración, género, etc.):**
  - **Título:**24px
  - **Texto:**28px
- **Tiempo de transición:** 40s ***(CONFIG)***
- **Layout:**1x1 ***(CONFIG)***
- **Versão:**2.1 ***(CONFIG)***
- **Plugin Screen:**Varía dependiendo del número de pantallas/películas en la API.***(CONFIG)***
- **alineación:**Justificado, izquierda y derecha ***(CONFIG)***
- **Orden de visualización:**API o aleatorio ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogProximamente ***(CONFIG)***
- **Tipo de sesión (Presentando):**24px
- **Horário (Presentando):**24px
- **Fuentes:**Rubik, Mobil
