# Blog de robótica

Blog en español para compartir artículos sobre robótica en una experiencia sencilla, accesible y centrada en la lectura. Las personas visitantes pueden descubrir publicaciones recientes, leer cada artículo completo y conocer al autor en la sección «Sobre mí».

## Funcionalidades

- Portada con artículos publicados, ordenados del más reciente al más antiguo.
- Páginas individuales con título, fecha, autoría y contenido estructurado.
- Página «Sobre mí» con una presentación editable del autor.
- Navegación simple entre las secciones principales.
- Panel administrativo para que el editor gestione artículos y presentación, sin modificar las plantillas.
- API REST para consultar artículos publicados y crear borradores con el token de una persona administradora existente.
- Diseño adaptable a móviles y ordenadores, con criterios de legibilidad y accesibilidad.

Los borradores no aparecen en las páginas públicas ni en las lecturas de la API. El sitio no contempla cuentas públicas, comentarios, suscripciones ni buscador.

## Tecnología

- Django para el backend y el renderizado en el servidor.
- Modelos y migraciones de Django para el contenido.
- Django Admin para la gestión editorial.
- Django REST Framework para la API de artículos y la autenticación por token.
- Plantillas HTML semánticas y CSS adaptable.
- SQLite para el desarrollo inicial; la base de datos de producción está pendiente de definirse.

## Inicio local

Abre PowerShell en la carpeta del proyecto. Si todavía no existe el entorno virtual `.venv`, créalo con Python 3.13:

```powershell
uv venv --python 3.13 .venv
```

Activa el entorno virtual e instala las dependencias:

```powershell
.\.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
```

Si PowerShell impide ejecutar el script de activación, permite su ejecución solo en la sesión actual y vuelve a activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Prepara la base de datos y arranca el servidor de desarrollo:

```powershell
python manage.py migrate
python manage.py runserver
```

El sitio estará disponible en <http://127.0.0.1:8000/>. Para detener el servidor, pulsa `Ctrl+C`. Para salir del entorno virtual, ejecuta `deactivate`.

### Crear o cambiar la clave del administrador

Para crear una cuenta con acceso al panel administrativo, ejecuta:

```powershell
python manage.py createsuperuser
```

Django solicitará un nombre de usuario, un correo electrónico (si está configurado como obligatorio) y una contraseña. Al escribir la contraseña no aparecerán caracteres en la consola; escríbela y pulsa `Enter`. Después, confírmala cuando se solicite. La cuenta podrá iniciar sesión en <http://127.0.0.1:8000/admin/>.

Si la cuenta ya existe y quieres asignarle o cambiarle la contraseña, ejecuta el comando con su nombre de usuario:

```powershell
python manage.py changepassword NOMBRE_DE_USUARIO
```

Introduce y confirma la nueva contraseña cuando Django lo solicite.

## API de artículos

- `GET /api/articulos/`: lista los artículos publicados y disponibles. No requiere autenticación.
- `GET /api/articulos/{id}/`: devuelve un artículo publicado y disponible. Los borradores, artículos futuros y artículos inexistentes responden con HTTP 404. No requiere autenticación.
- `POST /api/articulos/`: crea un borrador y requiere un token de una cuenta administradora (`is_staff`) existente. El JSON de entrada contiene `titulo` y `cuerpo`; la respuesta incluye `id`, `titulo`, `cuerpo` y `estado`.

Después de aplicar las migraciones, genera un token para una cuenta administradora existente:

```powershell
python manage.py migrate
python manage.py drf_create_token NOMBRE_DE_USUARIO
```

Guarda el token de forma segura y envíalo en la cabecera `Authorization`. La API genera un slug único a partir del título, asigna la autoría «Equipo editorial» y siempre guarda el artículo como borrador.

Ejemplos con `curl.exe` en PowerShell:

```powershell
curl.exe http://127.0.0.1:8000/api/articulos/
curl.exe http://127.0.0.1:8000/api/articulos/1/
curl.exe -X POST http://127.0.0.1:8000/api/articulos/ -H "Authorization: Token <TOKEN>" -H "Content-Type: application/json" --data-raw '{"titulo":"Robótica en el aula","cuerpo":"Un borrador sobre robots educativos."}'
```

## Documentación

- [Briefing](briefing.md)
- [Requisitos del producto (PRD)](PRD.md)
- [Visión del producto](Spec/vision.md)
- [Alcance](Spec/scope.md)
- [Criterios de aceptación](Spec/acceptance_criteria.md)
