# Visión del producto: blog de robótica

## Visión

Crear un espacio digital sencillo y accesible para compartir ideas y artículos sobre robótica. El sitio debe ayudar a las personas interesadas a descubrir las publicaciones recientes, leer cada artículo con comodidad y conocer a quien escribe.

## Usuarios y necesidades

- **Visitantes:** quieren encontrar artículos de robótica, leerlos sin distracciones y consultar una presentación breve del autor.
- **Editor del sitio:** quiere publicar, actualizar o retirar artículos y modificar la presentación del autor sin editar plantillas ni código.

## Propuesta de valor

El blog reúne artículos de robótica en una experiencia clara, adaptable a móviles y ordenadores, centrada en el contenido. La portada facilita descubrir publicaciones recientes; cada artículo ofrece una lectura completa y estructurada; la sección «Sobre mí» aporta contexto sobre su autor.

## Experiencia principal

1. La persona visitante llega a la portada y ve los artículos publicados más recientes, con título, fecha y extracto.
2. Abre un artículo para leer su contenido, autoría y fecha de publicación.
3. Puede volver a la portada o visitar «Sobre mí» desde la navegación principal.
4. El editor gestiona el contenido desde el panel administrativo estándar de Django; los borradores no aparecen en el sitio público.

## Principios del producto

- **Lectura primero:** priorizar una jerarquía clara, tipografía legible, buen contraste y contenido organizado en párrafos y subtítulos.
- **Navegación sencilla:** ofrecer enlaces descriptivos entre la portada, los artículos y «Sobre mí», utilizables sin JavaScript.
- **Accesibilidad y adaptación:** emplear HTML semántico y permitir el uso con teclado, en pantallas pequeñas y grandes.
- **Edición práctica:** permitir que el editor mantenga artículos y presentación desde Django Admin, sin ofrecer registro público.
- **Simplicidad:** evitar funciones que no contribuyen a descubrir, leer o mantener el contenido.

## Alcance de la primera versión

Incluye una portada con publicaciones recientes, páginas individuales de artículos, una sección «Sobre mí», navegación común, contenido de ejemplo reemplazable y gestión editorial con Django Admin. La interfaz se renderiza en el servidor y utiliza JavaScript solo si una necesidad concreta lo justifica.

Quedan fuera las cuentas de lectores, comentarios, suscripciones, boletines, buscador, interacción social y flujos editoriales avanzados o con múltiples roles.

## Criterios de éxito

- Las personas visitantes pueden descubrir una publicación desde la portada y leerla completa.
- «Sobre mí» es fácil de encontrar desde la navegación.
- El contenido y la navegación siguen siendo legibles y utilizables en móvil y escritorio.
- El editor puede actualizar publicaciones y presentación sin modificar plantillas.

## Decisiones conocidas y pendientes

La primera versión estará en español, tratará sobre robótica y contará con una persona editora y una presentación principal del autor. Además de las páginas web, expondrá una API REST para leer artículos publicados y permitir que administradores existentes creen borradores mediante un token. Se implementará con Django, Django REST Framework, el modelo de artículos existente, plantillas del servidor y SQLite en desarrollo. La identidad visual, el contenido definitivo, el dominio, el despliegue y la base de datos de producción se definirán más adelante.
