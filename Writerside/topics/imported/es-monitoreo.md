# Monitoreo

Última atualização: Nov. 3, 2025

---

---

## Descripción

La sección de **Monitoreo**es responsable del seguimiento en tiempo real del funcionamiento y la conectividad de los componentes del sistema. A través de ella, es posible monitorear el estado de las ***APIs***, la actividad de los ***players***, los períodos ***offline*******y la **salud general del sistema**. Esta sección ofrece una visión centralizada del rendimiento operativo, permitiendo la identificación rápida de fallas y la adopción de acciones correctivas para garantizar la estabilidad y la continuidad de los servicios.

<img src="$WRS_MODULE$/images/imported/shared/d842b9d44fad5a26.png" alt="image-20251103-233634.png"/>

Dividido en:

- **API**
- **Players**
- **Offline**
- **Salud del sistema**

---

## 1. API

En la pantalla de **Monitoreo de*****API***, cada ícono circular representa el estado de la *API* de un *cinema*. El ícono verde indica que la comunicación está estable y funcionando correctamente, mientras que el ícono rojo señala inestabilidad o la ocurrencia de errores de conexión.

Al hacer clic en cualquiera de estos íconos, se mostrará una *card* que presenta una vista detallada de las *APIs* configuradas para el *cinema* seleccionado. En esta visualización, es posible identificar cuáles *APIs* están activas, consultar los registros de solicitudes recientes, visualizar el código de retorno de la *API* y, si es necesario, cambiar la dirección de la *API* haciendo clic en el ícono de engranaje.

---

## 2. **Players**

La pantalla de **Monitoreo –*****Players*** permite seguir en tiempo real el estado de conexión y la información técnica de los *players* instalados en los *cinemas*.

Cada círculo mostrado en la pantalla principal representa un ***cinema***, y el color del ícono indica el estado de conectividad de los *players* vinculados:

- **Azul** – todos los *players* del *cinema* están conectados y funcionando normalmente
- **Naranja** – uno o más *players* del *cinema* están desconectados.
- **Rojo** – todos los *players* del *cinema* están desconectados.

En la parte superior, los indicadores generales muestran los porcentajes de sincronización de los *players* en diferentes intervalos de tiempo **(*****Synced*****,*****Synced 3H*****,*****Synced 1D*****,*****Synced 1W*****)**, así como el número total de ***cinemas*****(*****Theaters*****) y*****players*****(*****Players*****)** monitoreados.

Al hacer clic en un *cinema*, el sistema muestra, en el panel lateral derecho**, los detalles del lugar seleccionado**, incluyendo:

- **Código del*****cinema*****(*****Code*****)**
- **Nombre del*****cinema***
- **Horario de operación (*****Operations*****)**
- **Cantidad de*****players*****asociados (*****Players*****)**

Debajo de esta información, se muestra una lista lateral de *players* pertenecientes a ese *cinema*. Cada *player* está identificado por un ícono de color que representa su estado:

- **Azul** – *player* conectado.
- **Rojo** – *player* desconectado.

Al seleccionar un ***player*****específico**, se presentan sus **informaciones técnicas detalladas,** incluyendo:

- **Ubicación (*****Locate*****)**
- **Estado de conexión y hora de la última actualización**
- ***Hostname*****y dirección*****MAC***
- **Sistema operativo (*****OS*****)**
- **Procesador (*****Processor*****)**
- **Memoria (*****Memory*****)**
- **Almacenamiento (*****Storage*****)**
- **Tarjeta gráfica (*****Graphics*****)**
- **Resolución de pantalla (*****Resolution*****)**

Esta visualización ofrece un diagnóstico completo del estado operativo de cada *player*, permitiendo identificar fallas, monitorear el desempeño y garantizar el correcto funcionamiento de la infraestructura de exhibición en los *cinemas*.

---

## 3. Offline

<img src="$WRS_MODULE$/images/imported/shared/004ff2b48679f870.png" alt="image-20251103-233846.png"/>

La pantalla de **Monitoreo –*****Offline*** muestra un informe detallado generado a partir del *cinema* seleccionado y de los *players* asociados a él. El informe presenta información sobre el estado de **sincronización (*****Sync*****), descargas (*****Downloads*****)**y **conexiones de*****API***, permitiendo seguir el funcionamiento y la disponibilidad de cada *player*.

Para cada *player* listado, se muestran los siguientes datos:

- **Sync (Sincronización)** – indica la fecha y hora de la última sincronización de las configuraciones (***Config***) y *playlists* (***Playlist***) del *player*.
- **Download**– muestra el estado de descarga de los diferentes tipos de *media* vinculados al *player*, como ***Posters*****,*****Trailers*** y*******Videos***.
- **API**– presenta el estado de comunicación de las *APIs* integradas al sistema, incluyendo ***BoxOffice*****,*****Smartprice*****,*****Menu*******y*******Próximamente***, señalando si están **sincronizadas (*****Synched*****)**o con fallas.

Los íconos de marca verde indican que el componente está funcionando correctamente, mientras que las alertas o la ausencia de marca señalan posibles fallas de sincronización o conectividad.

Esta pantalla permite al usuario monitorear, de forma consolidada, el estado operativo de los *players* de un *cinema* específico, garantizando el control y la rápida identificación de posibles indisponibilidades.
