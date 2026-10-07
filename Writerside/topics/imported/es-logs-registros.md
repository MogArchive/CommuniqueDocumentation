# Logs - Registros

Última atualização: Nov. 3, 2025

---

---

## Descripción

La pantalla de ***Logs*******presenta el registro detallado de eventos, alertas y mensajes del sistema, permitiendo el seguimiento y diagnóstico en tiempo real de las operaciones realizadas por los *players* y los servicios integrados.

---

## 1. Logs - Pantalla de inicio

<img src="$WRS_MODULE$/images/imported/shared/d4ee762e3f050e6e.png" alt="image-20251103-234118.png"/>

En la parte superior, hay un campo de **búsqueda (*****“Search for”*****)**, que permite filtrar registros específicos por palabra clave, facilitando la identificación de ocurrencias relacionadas con un *player*, servicio o evento determinado.

Debajo, están disponibles los **filtros de refinamiento** organizados en tres categorías principales:

- **Host** – lista todos los *players* o dispositivos identificados por el código de *hostname* (ej.: BR0682ROD10), permitiendo seleccionar uno o más para un análisis específico.
- **Service** – presenta los servicios del sistema relacionados con los *logs*, como ***mog-player*** (servicio del *player* local) y ***cinemark-api*** (servicio de integración con el sistema de la red).
- **Status** – clasifica los registros de acuerdo con el tipo de evento, pudiendo ser:
  - **Error** – errores críticos de operación.
  - **Warning** – alertas de comportamiento anómalo o inestabilidad.
  - **Info** – informaciones generales de estado y rutina del sistema.
  - **Debug** – *logs* de depuración técnica para análisis avanzado.

En la parte superior derecha, el **filtro de tiempo (*****“Last 15 Minutes”*****)**permite definir el intervalo de tiempo para la visualización de los registros (por ejemplo: últimos 15 minutos, 1 hora, 24 horas, etc.), con un botón de **actualización automática (*****refresh*****)** para actualizar los datos en tiempo real.

El cuerpo principal de la tabla presenta las siguientes columnas:

- **Date** – fecha y hora de la ocurrencia del *log*.
- **Host** – *player* o dispositivo en el que se registró el evento.
- **Service** – servicio responsable del evento (ej.: *mog-player*, *cinemark-api*).
- **Content** – descripción detallada del evento o error, incluyendo mensajes específicos, códigos de *mídia*, fallas de conexión o ausencia de archivos (*Posters Missing*, *Playlist Empty*, *Player Offline*, etc.).

Cada evento está identificado por un **ícono de color** a la izquierda, que indica su nivel de severidad:

- **Rojo**– error crítico.
- **Naranja**– alerta.
- **Azul**– información.
- **Gris**– *log* de depuración.

En la parte superior de la tabla, se encuentran los botones *“**Show Table”*** y ***“Show Chart”***, que permiten alternar entre la visualización tabular de los *logs* y una representación gráfica (estadística) de los eventos registrados. También está la opción ***“Export”*****,** que permite exportar los registros filtrados en formato de informe para análisis externo.

Esta pantalla ofrece una visión completa y estructurada de los eventos del sistema, permitiendo que los administradores y los equipos técnicos monitoreen el comportamiento de los *players*, detecten errores, validen comunicaciones y tomen decisiones correctivas basadas en evidencias precisas y en tiempo real.
