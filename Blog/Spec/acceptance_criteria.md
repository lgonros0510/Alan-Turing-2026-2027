# Criterios de aceptación: blog de robótica

Estos criterios definen las condiciones observables para aceptar la primera versión del producto y se derivan de los requisitos funcionales y no funcionales del PRD. «Editor autorizado» se refiere a una persona autenticada con permisos para gestionar el contenido en Django Admin.

## CA-01: Portada y artículos recientes (RF-01)

- **Dado** que una persona visita la ruta raíz `/`, **cuando** hay artículos publicados, **entonces** ve el nombre del blog y una lista de artículos ordenada del más nuevo al más antiguo.
- **Dado** que la lista de artículos está visible, **entonces** cada artículo incluye título, fecha de publicación, extracto y un enlace a su página individual.
- **Dado** que no hay artículos publicados, **cuando** se visita la portada, **entonces** se muestra un mensaje informativo en lugar de una lista vacía sin contexto.
- **Dado** que existen borradores, **cuando** una persona visitante consulta la portada, **entonces** esos borradores no aparecen en la lista.

## CA-02: Lectura de un artículo (RF-02)

- **Dado** que una persona selecciona un artículo publicado, **cuando** se abre su ruta `/articulos/<slug>/`, **entonces** se muestran su título, fecha de publicación, autoría y contenido.
- **Dado** que el contenido incluye párrafos y subtítulos, **entonces** se conserva esa estructura de forma legible.
- **Dado** que se solicita un slug inexistente o no publicado, **cuando** se abre su ruta pública, **entonces** el sitio responde con una página de no encontrado y estado HTTP 404.
- **Dado** que una persona está leyendo un artículo, **entonces** dispone de un enlace para volver a la portada.

## CA-03: Página «Sobre mí» (RF-03)

- **Dado** que una persona visita `/sobre-mi/`, **cuando** la página carga, **entonces** encuentra una presentación breve identificada como «Sobre mí».
- **Dado** que una persona está en cualquier página pública, **entonces** la navegación principal ofrece un enlace descriptivo a «Sobre mí» y otro a la portada.
- **Dado** que el editor actualiza la presentación, **cuando** guarda el cambio, **entonces** el nuevo texto aparece en la página pública sin modificar plantillas.

## CA-04: Navegación (RF-04)

- **Dado** que una persona recorre las páginas públicas, **cuando** utiliza los enlaces principales, **entonces** puede navegar entre la portada y «Sobre mí» y volver a la portada desde un artículo.
- **Dado** que una persona utiliza navegación básica con JavaScript desactivado, **entonces** los enlaces principales siguen funcionando.
- **Entonces** los enlaces tienen nombres claros y comprensibles, pueden recibir el foco con el teclado y activarse sin ratón.

## CA-05: Gestión de contenido (RF-05)

- **Dado** que un editor autorizado accede a `/admin/`, **cuando** utiliza el panel, **entonces** puede crear, editar y retirar artículos y actualizar la presentación del autor.
- **Dado** que una persona anónima intenta acceder a una función administrativa, **entonces** no puede ejecutar operaciones de edición; para gestionarlas se requiere autenticación y autorización.
- **Dado** que un artículo está en estado no publicado, **cuando** se consultan las páginas públicas, **entonces** el artículo no aparece en la portada ni se puede leer desde una ruta pública.
- **Dado** que el proyecto incluye contenido inicial de ejemplo sobre robótica, **entonces** el editor puede sustituirlo o eliminarlo desde la gestión de contenido.
- **Entonces** el sitio no ofrece registro público, cuentas o perfiles para lectores.

## CA-06: Adaptabilidad, legibilidad y accesibilidad

- **Dado** que se visita el sitio desde una pantalla pequeña o grande, **cuando** se muestran sus páginas, **entonces** el contenido y la navegación siguen siendo utilizables sin desplazamiento horizontal innecesario.
- **Dado** que una persona lee un artículo, **entonces** la tipografía, el contraste, el espaciado y la longitud de línea favorecen la lectura prolongada.
- **Entonces** las páginas utilizan HTML semántico, una estructura de encabezados coherente, enlaces descriptivos y controles utilizables con teclado.

## CA-07: Renderizado del servidor y JavaScript

- **Dado** que una persona solicita la portada, «Sobre mí» o un artículo, **entonces** Django entrega el contenido de la página renderizado en la respuesta del servidor.
- **Dado** que JavaScript está desactivado, **cuando** se consultan las páginas y se utiliza la navegación básica, **entonces** el contenido y los enlaces principales siguen disponibles.
- **Entonces** JavaScript y sus dependencias solo se incluyen si una necesidad concreta del producto los justifica.

## CA-08: Seguridad para producción

- **Dado** que se prepara una configuración para producción, **cuando** se revisa antes del despliegue, **entonces** se siguen las prácticas de seguridad recomendadas por Django y las operaciones administrativas permanecen restringidas a usuarios autorizados.

## CA-09: Contenido y datos mínimos

- **Dado** que se crea o edita un artículo, **entonces** se pueden mantener su título, slug, contenido, autoría, fecha de publicación y estado de publicación.
- **Dado** que se configura la presentación del autor, **entonces** se puede mantener un texto breve y editable para la presentación principal del sitio.

## Documentos relacionados

- [PRD](../PRD.md)
- [Visión del producto](vision.md)
- [Alcance del producto](scope.md)