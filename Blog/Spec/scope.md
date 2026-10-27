# Alcance del producto: blog de robótica

## Objetivo

Definir qué incluye la primera versión del blog de robótica y qué queda fuera. El producto ofrecerá una experiencia centrada en la lectura y permitirá que una persona editora mantenga el contenido sin modificar las plantillas del sitio.

## Usuarios contemplados

- **Visitante:** consulta los artículos publicados y la sección «Sobre mí». No necesita una cuenta.
- **Editor del sitio:** administra artículos y la presentación del autor mediante el panel administrativo estándar de Django. El acceso está restringido a usuarios autorizados.

## Incluido en la primera versión

### Experiencia pública

- Portada en la ruta `/` con el nombre del blog y los artículos publicados, ordenados del más nuevo al más antiguo.
- Cada artículo de la portada muestra título, fecha, extracto y un enlace al contenido completo.
- Mensaje informativo en la portada cuando no hay artículos publicados.
- Página individual en `/articulos/<slug>/` con título, fecha de publicación, autoría y contenido organizado en párrafos y subtítulos.
- Respuesta 404 para rutas de artículos inexistentes.
- Página «Sobre mí» en `/sobre-mi/`, con una presentación breve y editable del autor.
- Navegación visible entre la portada y «Sobre mí», además de una forma de volver a la portada desde un artículo.
- Navegación básica sin depender de JavaScript.

### Gestión de contenido

- Panel administrativo de Django en `/admin/`, accesible solo a usuarios autorizados.
- Crear, editar y retirar artículos desde el panel.
- Actualizar desde el panel el texto de presentación de «Sobre mí».
- Mantener los artículos no publicados fuera de las páginas públicas.
- Incluir contenido de ejemplo sobre robótica, reemplazable o eliminable desde la gestión de contenido.

### API REST

- `GET /api/articulos/` lista públicamente los artículos publicados que ya están disponibles.
- `GET /api/articulos/<id>/` devuelve un artículo publicado disponible; los borradores y artículos futuros responden con HTTP 404.
- `POST /api/articulos/` crea únicamente borradores y requiere un token de Django REST Framework perteneciente a una persona administradora existente.
- El POST recibe `titulo` y `cuerpo` y responde con `id`, `titulo`, `cuerpo` y `estado` (`borrador` para el artículo creado).
- La API conserva el modelo `Article`: deriva un slug único del título, usa «Equipo editorial» como autoría y deja que el modelo complete la fecha. No introduce usuarios ni modifica el esquema del artículo.

### Datos de los artículos

Cada artículo incluye, como mínimo, título, slug, contenido, autoría, fecha de publicación y estado de publicación. La primera versión contempla una presentación principal del autor.

### Calidad y tecnología

- Sitio adaptable a pantallas pequeñas y grandes, sin desplazamiento horizontal innecesario.
- HTML semántico, encabezados coherentes, enlaces descriptivos y controles utilizables con teclado.
- Tipografía, contraste, espaciado y longitud de línea adecuados para la lectura prolongada.
- Renderizado en el servidor mediante Django, con plantillas HTML y CSS adaptable.
- Modelos y migraciones de Django; SQLite para el desarrollo inicial.
- JavaScript solo si una necesidad concreta lo justifica.

## Fuera de alcance

- Cuentas, perfiles o registro para lectores.
- Comentarios o interacción social.
- Suscripciones o boletines.
- Buscador.
- Flujos editoriales avanzados, como revisión, programación de publicaciones o múltiples roles.
- Edición de contenido por visitantes o acceso anónimo a operaciones administrativas.
- Creación de usuarios para la API, publicación de artículos desde la API y métodos de autenticación distintos del token integrado para administradores existentes.

## Rutas de referencia

- `/`: portada y artículos recientes.
- `/sobre-mi/`: presentación del autor.
- `/articulos/<slug>/`: página de un artículo.
- `/api/articulos/`: lista de artículos y creación autenticada de borradores.
- `/api/articulos/<id>/`: detalle JSON de un artículo publicado.
- `/admin/`: administración restringida de Django.

## Supuestos y decisiones pendientes

- El idioma inicial será el español y el tema será la robótica.
- La primera versión tendrá una persona editora y una única presentación principal del autor.
- El nombre definitivo del blog, la identidad visual, el contenido final, el dominio y el entorno de despliegue todavía no están definidos.
- SQLite se utilizará durante el desarrollo; la base de datos de producción dependerá del entorno de despliegue.
- La estructura exacta de aplicaciones, las versiones de Django y la configuración de despliegue se decidirán durante la implementación.

## Documento relacionado

- [Visión del producto](vision.md)
