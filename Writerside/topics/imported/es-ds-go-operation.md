# DS - GO Operation

Última actualización: Abril. 23, 2026.

---

---

## **Descripción**

Sesión destinada a los **Gerentes Operativos** para la gestión y eliminación de medios promocionales (combos/ofertas) programados en los cines bajo su responsabilidad.

A través de esta pantalla, el usuario puede seleccionar todos los cines asociados, visualizar todos los **medios promocionales** programados y eliminarlos de la exhibición.

Además, la pantalla proporciona un historial de eliminaciones, lo que permite rastrear cuándo se eliminó un medio, qué usuario realizó la acción y en qué reproductor.

<img src="$WRS_MODULE$/images/imported/shared/81e9d3394ebb5bb8.png" alt="image-20260423-164158.png"/>

## 1. Descripción de los campos

<img src="$WRS_MODULE$/images/imported/shared/9cdf19dc4503a647.png" alt="image-20260423-154732.png"/>

### **1.1 Botón “Seleccionar Cine”**

Abre la ventana para seleccionar el cine deseado. En esta pantalla aparecerán los cines asignados a su usuario.

<img src="$WRS_MODULE$/images/imported/shared/834786eab89ca3d5.png" alt="image-20260423-154819.png"/>

### **1.2 Campo de búsqueda (pesquisa)**

Después de seleccionar los cines en la pantalla anterior, se cargará la lista de contenidos de dichos cines

<img src="$WRS_MODULE$/images/imported/shared/a1a2ba8945455628.png" alt="image-20260423-155234.png"/>

El **campo de búsqueda** permite buscar medios específicos dentro del cine seleccionado, utilizando palabras clave como el nombre del medio.

<img src="$WRS_MODULE$/images/imported/shared/9f84dbd8e9bc1741.png" alt="image-20260423-155442.png"/>

### **1.3 Tabla - Medios Programados**

<img src="$WRS_MODULE$/images/imported/shared/cfdd4ae28581c2a2.png" alt="image-20260423-170607.png"/>

Lista los **medios promocionales** vinculados al cine seleccionado, con las siguientes columnas:

| Columna | Función |
| --- | --- |
| Nombre del Medio | Muestra el nombre del combo/medio promocional. |
| Formato | Formato del medio (Ej.: 2x1, 4x1) |
| Duración | Tiempo de exhibición del contenido en segundos |
| Fecha de Inicio | Cuándo comienza la exhibición del medio. |
| Fecha Final | Cuándo deja de exhibirse el medio. |
| Vista previa | Opción para visualizar el contenido del medio. |

### 1.4 Eliminar

<img src="$WRS_MODULE$/images/imported/shared/237d84044bc7294a.png" alt="image-20260423-171816.png"/>

Después de seleccionar los medios, haz clic en el botón “**Eliminar**” para realizar la operación de exclusión.

Se abrirá una ventana con la información sobre en qué cines se realizará la exclusión.

<img src="$WRS_MODULE$/images/imported/shared/54b7443823e225b2.png" alt="image-20260423-171638.png"/>

Confirma la información y haz clic en “**Eliminar**”, si deseas realizar modificaciones, haz clic en “**Cancelar**”.

### **1.5 Historial de Eliminaciones**

Una vez eliminados los medios, se mostrará la siguiente tabla con el **historial de eliminación**.

<img src="$WRS_MODULE$/images/imported/shared/73eac2af3335caca.png" alt="image-20260423-172205.png"/>

La tabla contiene las siguientes columnas:

| Columna | Función |
| --- | --- |
| Nombre del Medio | Nombre del medio eliminado. |
| Cinema | Cine donde fue eliminado. |
| PlayerName | Nombre del player. |
| Hostname | Identificación del player. |
| Fecha de Eliminación | Fecha y hora de la acción. |
| Eliminado por | Usuario responsable de la eliminación. |
| Status | Estado de la operación. |

## 2. Validación de la versión

Para verificar la versión de Communique antes de utilizar la funcionalidad, siga los pasos que se indican a continuación:

1. Primero, ve a la pantalla de inicio y comprueba si la versión actual es la más reciente:

<img src="$WRS_MODULE$/images/imported/shared/db448e7a6a7b8b14.png" alt="image-20260423-153217.png"/>

1. Si no es el caso, tendremos que borrar la caché de la página. Primero, presiona las teclas Ctrl+Shift+i:

<img src="$WRS_MODULE$/images/imported/shared/9580839f05777218.png" alt="image-20260423-153605.png"/>

1. Navega por los menús superiores hasta la opción “Network”:

<img src="$WRS_MODULE$/images/imported/shared/bfad38eabf8084ee.png" alt="image-20260423-153734.png"/>

1. Clic en la opción “Disable cache”:

<img src="$WRS_MODULE$/images/imported/shared/4b472fd3455d5d42.png" alt="image-20260423-153933.png"/>

1. Actualiza la página (Ctrl+R) para borrar la caché.
2. Si el problema persiste, ponte en contacto con el equipo de soporte de MOG para que te proporcionen una mejor asistencia.
