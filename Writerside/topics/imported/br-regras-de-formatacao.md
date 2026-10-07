# Regras de Formatação

Última atualização: Set. 18, 2025

---

---

## **1. Combos**

### **1.1 Versão 2.0**

#### **Layout 1x1 (CONFIG)**

- **Línea legal:** 200 caracteres – Base de 35px (3.3%), se reduce a 25px si la cantidad de caracteres supera los 70 (**CONFIG**).
- **Loyalty:** hasta 3 tipos (**API**).
- **Precio Loyalty:** 32px o 3% (**API**).
- **Ícono Loyalty:** altura máxima de 119px o 11% (**CONFIG**).
- **Nombre del combo:** 26 caracteres – 97px o 9% (**API**).
- **Precio del combo:** 32px o 4% (**API**).
- **Lista de productos:** 9 combos con 3 líneas – 30 caracteres – 57px o 5.3% (**CONFIG**).
- **Still:** 692 x 540 (**CONFIG**).
- **Fuente:** Oswald (**SOFTWARE**).

<img src="imported/shared/366be0029520403f.png" alt="image-20250918-175138.png"/>

#### **Layout 2x1 (CONFIG)**

- **Línea legal:** 200 caracteres – Base de 38px (3.5%), se reduce a 27px si la cantidad de caracteres supera los 70 (**CONFIG**).
- **Loyalty:** hasta 3 tipos (**API**).
- **Precio Loyalty:** 32px o 3% (**API**).
- **Ícono Loyalty:** altura máxima de 119px o 11% (**CONFIG**).
- **Nombre del combo:** 38 caracteres – 97px o 9% (**API**).
- **Precio del combo:** 54px o 5% (**API**).
- **Lista de productos:** 9 combos con 2 líneas – 40 caracteres – 57px o 5.3% (**CONFIG**).
- **Still:** 692 x 540 (**CONFIG**).
- **Fuente:** Oswald (**SOFTWARE**).

<img src="imported/shared/48f4601cc3ff2e40.png" alt="image-20250918-175408.png"/>

---

### **1.2 Version 1.0**

**Parte superior:**

- **Playlist:** 2x1 (1920x540) o 4x1 (3840x540) (**CONFIG**).

**Parte inferior:**

- **Cantidad de combos:** sin límite (**API**).
- **Tiempo de transición:** 5s (**CONFIG**).
- **Nombre del combo:** 26 caracteres – Base 60px, disminuye según la cantidad de caracteres (**API**).
- **Precio:** máximo 6 caracteres – Base 60px, disminuye según la cantidad de caracteres (**API**).
- **Loyalty:** máximo 2 tipos – Base 60px, disminuye según la cantidad de caracteres (**API**).
- **Still:** 640 x 441 (**CONFIG**).
- **Fuente:** Sinkin Sans (**SOFTWARE**).

<img src="imported/shared/438a1b59bc2b70d2.png" alt="image-20250918-175541.png"/>

---

## **2. Menus**

### **2.1 PremierMix**

- ***NOMES CATEGORIAS (API)***
  - **A:** 21 caracteres - Pipocas
  - **B:** 15 caracteres - Bebidas
  - **C:** 21 caracteres
  - **D:** 15 caracteres
  - **Valores:** 06 caracteres
- ***NOMES ITENS (API)***
  - **A:** 26 caracteres (Nome da Subcategoria + Nome do Produto)
  - **B:** 22 caracteres (sem Amount ou Nome do Produto + Amount)
  - **C:**27 caracteres
  - **D:** 22 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versão:**1.0 ***(CONFIG)***
- **Tempo de transição das categorias:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:** Não possui
- **Fontes:** GaramondItalic, Garamond
- **Categoria:** 100px
- **Nome Produto:** 48px
- **Preço:** 48px

**NOMBRES DE CATEGORÍAS (API)**

**A:** 21 caracteres – Palomitas
**B:** 15 caracteres – Bebidas
**C:** 21 caracteres
**D:** 15 caracteres
**Valores:** 6 caracteres

---

**NOMBRES DE ÍTEMS (API)**

**A:** 26 caracteres (Nombre de la Subcategoría + Nombre del Producto)
**B:** 22 caracteres (sin *Amount* o Nombre del Producto + *Amount*)
**C:** 27 caracteres
**D:** 22 caracteres

---

**Layout:** 1x1 (**CONFIG**)
**Versión:** 1.0 (**CONFIG**)
**Tiempo de transición de categorías:** 10 s por *card* (**CONFIG**)
**URL API:** `http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos` (**CONFIG**)
**Playlist:** No posee
**Fuentes:** *GaramondItalic*, *Garamond*
**Categoría:** 100 px
**Nombre del producto:** 48 px
**Precio:** 48 px

<img src="imported/shared/7c169c649206ab58.png" alt="image-20250918-175814.png"/>

### **2.2 SelfService**

- **NOMBRES DE CATEGORÍAS (API)**
  - **A:** 17 caracteres – *Palomitas*
  - **A2:** 9 caracteres (nombres en la misma línea del nombre de la categoría) – *Salado*, *Dulce*
  - **B:** 21 caracteres – *Bebidas*
  - **C-Z:** 22 caracteres
  - **Valores:**  06 caracteres
- ***NOMBRES ITENS (API)***
  - **A:** 29 caracteres - Mediano, Grande
  - **B-Z:** 24 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Versão:**1.0 ***(CONFIG)***
- **Tempo de transição das categorias:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:** No tiene.
- **Fuentes:** Norwester, Sinkin Sans
  - **Palomitas**
    - **Categoria:**58px
    - **Subcategoria:** 56px
    - **Nombre del producto:** 41px
    - **Precio:** 41px
  - **Otras categorias**
    - **Categoria:** 48px
    - **Nombre del producto:** 38px
    - **Precio:** 38px

<img src="imported/shared/93ce0099651da3ae.png" alt="image-20250918-180211.png"/>

### **2.3 Bistrô**

- ***NOMBRE CATEGORIAS (API)***
  - 22 caracteres - Helados, Bebidas, Dulces
  - **Valores:** 06 caracteres
- ***NOMBRE ITENS (API)***
  - 25 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Version:**1.0 ***(CONFIG)***
- **Tiempo de transición de categorías:** 10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:** No tiene.
- **Fuentes:** Rubik, Futura
- **Categoria:**55px
- **Nombre del producto:** 34px
- **Precio:** 34px

<img src="imported/shared/3889ca7c2d711fea.png" alt="image-20250918-180335.png"/>

### **2.4 Kosher**

- ***NOMBRES DE CATEGORIAS (API)***
  - 16 caracteres - Mediana, Grande etc
  - **Valores:** 06 caracteres
- **Layout:** 1x1 (CONFIG)
- **Versión:** Kosher (CONFIG)
- **Fuente:** —
- **Tamaño:** —
- **URL API:** `http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos` *(la categoría debe contener la palabra **KOSHER** en su nombre)* (CONFIG)
  **Playlist:** No tiene.
  **Fuentes:** Oswald, Typold, SinkinSans
- **Frase 1:** *DISFRUTA EL SABOR Y LA FRESCURA DE LAS PALOMITAS DE CINEMARK* – 5% o 54px
  **Frase 2:** *AHORA CON LA CERTIFICACIÓN KOSHER* – 8% o 86px
- **Nombre del producto:** 4% o 43px
  **Precio:** 3.5% o 38px
  **Logo:** 12% o 240px

<img src="imported/shared/cd4dd19627a97b44.png" alt="image-20250918-180511.png"/>

---

## **3. Regular**

### **3.1 Fonte P**

- ***NOMBRES  DE CATEGORIAS (API)***
  - **A:** 08 caracteres - Pipoca
  - **A2:** 21 caracteres (3 TIPOS) | 11 caracteres(5 TIPOS) - Pequeno, médio, grande
  - **B:**08 caracteres - Bebidas
  - **C-Z:** 20 caracteres
  - **Valores:** 06 caracteres
- ***NOMBRE ITENS (API)***
  - **A:** 12 caracteres - Salado, Dulces, Mixtas
  - **B CIMA:** 12 caracteres - Mediana, Grande
  - **B LATERAL:**26 caracteres
  - **C-Z:** 36 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Version:**2.0 ***(CONFIG)***
- **Tiempo de transición de categorías:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:**Puede o no mostrarse.

### **3.2 Fonte M**

- ***NOMBRES DE CATEGORIAS (API)***
  - **A:**08 caracteres - Pipoca
  - **A2:** 20 caracteres (3 TIPOS) | 10 caracteres (5 TIPOS) - Pequeno, médio, grande
  - **B:** 08 caracteres - Bebidas
  - **C-Z:** 20 caracteres - Snacks, Extras
- ***NOMBRES ITENS (API)***
  - **A:** 10 caracteres - Salado, Dulces, Mixtas
  - **B CIMA:** 11 caracteres - Mediana, Grande
  - **B LATERAL:**25 caracteres
  - **C-Z:** 29 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Version:**2.0 ***(CONFIG)***
- **Tiempo de transición de categorías:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:**Puede o no mostrarse.

### **3.3 Fonte G**

- ***NOMBRES DE CATEGORIAS (API)***
  - **A:** 08 caracteres - Pipoca
  - **A2:** 19 caracteres (3 TIPOS) | 9 caracteres (5 TIPOS) - Pequeno, médio, grande
  - **B:** 08 caracteres - Bebidas
  - **C-Z:** 20 caracteres
- ***NOMBRES ITENS (API)***
  - **A:** 09 caracteres - Salado, Dulces, Mixtas
  - **B CIMA:** 9 caracteres - Mediana, Grande
  - **B LATERAL:**23 caracteres
  - **C-Z:** 24 caracteres
- **Layout:**1x1 ***(CONFIG)***
- **Version:**2.0 ***(CONFIG)***
- **Tiempo de transición de categorías:**10s por card ***(CONFIG)***
- **URL API:**http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCombos ***(CONFIG)***
- **Playlist:**Puede o no mostrarse.
- **Fuente:** SinkinSans
- **Titulo:** Pequeno 5% - 54px | Medio 5% - 54px | Grande 5% - 54px
- **Nombre del Producto:** (Pipoca e Bebida) Pequeno 3% ou 32px | Medio 3.5% ou 38px | Grande 4% ou 43px
- **Gramatura Producto:** Pequeno 1.5% ou 16px | Medio 2% ou 21px | Grande 2.3% ou 25px
- **Nombre del Producto:** (Bebidas adicionais e demais categorias) Pequeno 2.5% ou 27px | Medio 3% ou 32px | Grande 3.5% ou 38px
- **Precio Decimal:**Pequeno 3.5% ou 38px | Medio 4% ou 43px | Grande 4.2% ou 45px
- **Precio Símbolo e Centavos:** Pequeno 2.5% ou 27px | Medio 3% ou 32px | Grande 3.5% ou 38px

<img src="imported/shared/40fc369127e7c7c9.png" alt="image-20250918-180847.png"/>

---

## **4. Showtimes**

<img src="imported/shared/06762cd5a775b4c3.png" alt="image-20250918-181244.png"/>

<img src="imported/shared/ab7815cec1b85f2f.png" alt="image-20250918-181307.png"/>

- **Nombre de la película:** Hasta 39 caracteres (API)
- **Imagen de censura:** 94 x 107 (CONFIG)
- **Imagen de categoría de sesión:** 781 x 507 (CONFIG)
- **Horario:** (API)
- **Audio:** (API)
- **Sin playlist:** 8 líneas (CONFIG)
- **Con playlist:** 6 líneas (CONFIG)
- **Versión:** 2.0 (CONFIG)
- **Layout:** 1x1 y 2x1 (CONFIG)
- **Ordenación:** Alfabética, número de sesiones y prioridad (CONFIG)
- **Tiempo de transición:** Actualmente 3s por línea (CONFIG)
- **URL API (CONFIG):**
- http://ip_do_cinema/theatermgmt/api/SmartMenu/MogCartelera (AL)
- http://host_server_cinema/apolo/services/partner/mog/api/v1/BoxOffice?pEstabelecimentoCodigo=**X** (BR)
  - A letra “**X**” equivale ao código interno do cinema
- **Cantidad de horarios:** 5 por línea (SOFTWARE)
  - A partir de 5 horarios, el plug-in crea una línea doble para la película, mostrando hasta 10 horarios. A partir de 10 horarios, se genera una nueva línea.

<img src="imported/shared/be4edb6ca1d23178.png" alt="image-20250918-181215.png"/>

- **Tamaño de las fuentes (SOFTWARE)**
  - **Título:** 35px ou 3%
  - **Horario**: 48px ou 4.5%
  - **Áudio:** 27px ou 2.5%
- **Fuente:** Oswald ***(SOFTWARE)***

---

## **5. Prices**

<img src="imported/shared/8129de88b620dbca.png" alt="image-20250918-181532.png"/>

- **Texto Superior:** Diecisiete frases de hasta 92 caracteres (API)
  - **Día de la semana:** 35px o 3.25%
  - **Fecha:** 30px o 2.77%
  - **Mensaje:** varía según la longitud del texto (base 2.6% – 28px)
  - **Horario:** 70px o 6.5%
- **Categoría – Regular/Premier (API) y (SOFTWARE)**
- **Tamaño de fuentes:**
         **Pequeño:** 2.96% o 32px
         **Mediano:** 3.76% o 40px
         **Grande:** 3.76% o 40px
- **2D/3D (SOFTWARE)**
        **Pequeño:** 2.96% o 32px
  **Mediano:**3.66% o 39px
  **Grande**: 3.66% o 39px
- **Matiné/Noche (SOFTWARE)**
          **Pequeño:** 2.3% o 25px
      **Mediano/Grande:** 32px o 3%
- **Precios (API)**
          **Pequeño Regular:** valor – 2.96% o 32px | símbolo – 1.85% o 20px
          **Pequeño Gold:** valor – 3% o 32px | símbolo – 21px
         **Mediano/Grande Regular:** valor – 3.66% o 40px | símbolo – 2.55% o 27px
          **Mediano/Grande Gold:** valor – 3.66% o 40px | símbolo – 2.7% o 29px
- **Póster:** 1280x870 – 300Kb (CONFIG)
- **Próxima Sesión (SOFTWARE)**
         **Título:** 2.5% o 27px
           **Horario:** 11% o 118px
          **Audio:** 3.3% o 35px
          **3D/2D:** 5% o 54px
           **Nombre de la película:** hasta 57 caracteres (API)
           **Sala:** 3.3% o 35px (API)
           **Clasificación:** (Upload Communique)
- **Fuentes:** Rubik, Sora y San Francisco Compact

---

## **6. BoxOffice**

<img src="imported/shared/b556370cfbd85bec.png" alt="image-20250918-181811.png"/>

- **Nombre de la película:** (API)
- **Película con 1 pantalla:** 59 caracteres (API)
- **Tamaño de fuentes:**
  - **Título:** 4.44% o 48px
  - **Horario**: 5% o 54px
  - **Audio:**1.5% o 16px
- **Película con 3 pantallas:** 80 caracteres (API)
- **Tamaño de fuentes:**
  - **Título:**3% o 32px
  - **Horario:** 3% o 32px
  - **Audio:** 1.2% o 12px
- **Película con 4 pósteres:** 78 caracteres distribuidos en tres líneas (API)
- **Tamaño de fuentes:**
  - **Título**: 3% o 32px
  - **Horario:** 3% o 32px
  - **Audio:** 1.2% o 12px
- **Película con 8 pósteres:** 64 caracteres (API)
- **Tamaño de fuentes:**
  - **Título:** mayor | menor
  - **Horario:** mayor | menor
  - **Audio:** mayor | menor
- **Clasificación:** (Upload Communique)
- **Tamaño de imagen:**
  - **IMAX:** 150x25
  - **4D:**70x602D: 781x507
  - **3D:** 781x507D-BOX LARGE: 313x52
  - **D-BOX:** 150x25
  - **PRIME**: 781x507
  - **XD:** 781x507
  - **Clasificación:** 94x107
- **XD:** (Upload Communique)
- **Horarios:** (API)
- **Audio de la película:** (API) y (SOFTWARE)

---

## **7. Postercase**

- **Nombre de la película:**Hasta 65 caracteres (API) **Fuente / tamaño:**(según configuración)
- **Imagen:**870x1280 POSTER **(Upload – CONFIG)**
- **Sesión: (API) (fuente según configuración)**
- **Imagen de clasificación (Censura):**D. 352x180**(*****CONFIG*****)**
- **D-BOX LARGE: 313x52**
- **D-BOX: 150x25 (API)**
- **CensorshipMessage:**Límite de 4 códigos**(fuente configurada)**
- **Logo de la sala: (API) (fuente configurada)**
- **Tipo de sala: (API) (fuente configurada)**
- **Horarios: (API) (fuente configurada)**
- **Versión del plug-in:**1x1
- **URL (API)**
- **Plugin Screen: (CONFIG)**
- **Tamaño de censura BR: 362x180**
- **Tamaño de censura otros países: 94x107**

- **Fuentes:** Oswald, MADE Outer Sans, Rubik
- **Título (variable):**44px
- **Audio:** 4.5% o 48px
- **Tipo de sala:**5% o 54px
- **Texto “Próxima Sesión”:**4.8% o 52px
- **Horario:**13.3% o 144px
- **Frases informativas:**20px

<img src="imported/shared/e0851c5a9aa93d40.png" alt="image-20250918-182222.png"/>

---

## **8. SmartPostercase**

<img src="imported/shared/4a668663b75939b7.png" alt="image-20250918-182239.png"/>

- **Nombre de la película:** Hasta 35 caracteres – 60px variable **(API)**
- **Tráiler:** 1280x720 o 1920x1080 – hasta 20Mb **(CONFIG)**
- **Póster:** 1280x870 – 300Kb **(CONFIG)**
- **Sinopsis (60px):** 508 caracteres – 24px variable**(API)**
- **Elenco:** 8 nombres de hasta 23 caracteres cada uno **(API)**
- **Género (API)**
- **Director:** 2 nombres de hasta 23 caracteres cada uno **(API)**
- **Duración** **(API)**
- **País (API)**
- **Clasificación:** 94x107 **(CONFIG)**
- **Demás informaciones de la película** (elenco, duración, género, etc.):
  - **Título:** 24px
  - **Texto:** 28px
- **Tiempo de transición:** 40s **(CONFIG)**
- **Layout:** 1x1 **(CONFIG)**
- **Versión:** 2.1 **(CONFIG)**
- **Plugin Screen:** Varía según la cantidad de pantallas/películas en la **API (CONFIG)**
- **Alineación:** Justificada, izquierda y derecha **(CONFIG)**
- **Orden de exhibición:** API o aleatoria**(CONFIG)**
- **URL API:** http://ip_do_cinema/theatermgmt/api/SmartMenu/MogProximamente **(CONFIG)**
- **Tipo de Sesión (Presentando):** 24px
- **Horario (Presentando):** 24px
- **Fuentes:** Rubik, Mobil
