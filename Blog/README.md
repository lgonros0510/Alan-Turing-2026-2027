# Blog de robótica

Blog en español para compartir artículos sobre robótica en una experiencia sencilla, accesible y centrada en la lectura. Las personas visitantes pueden descubrir publicaciones recientes, leer cada artículo completo y conocer al autor en la sección «Sobre mí».

## Funcionalidades

- Portada con artículos publicados, ordenados del más reciente al más antiguo.
- Páginas individuales con título, fecha, autoría y contenido estructurado.
- Página «Sobre mí» con una presentación editable del autor.
- Navegación simple entre las secciones principales.
- Panel administrativo para que el editor gestione artículos y presentación, sin modificar las plantillas.
- Diseño adaptable a móviles y ordenadores, con criterios de legibilidad y accesibilidad.

Los borradores solo están disponibles para el editor autorizado. El sitio no contempla cuentas públicas, comentarios, suscripciones ni buscador.

## Tecnología

- Django para el backend y el renderizado en el servidor.
- Modelos y migraciones de Django para el contenido.
- Django Admin para la gestión editorial.
- Plantillas HTML semánticas y CSS adaptable.
- SQLite para el desarrollo inicial; la base de datos de producción está pendiente de definirse.

## Inicio local

Abre PowerShell en la carpeta del proyecto. Si todavía no existe el entorno virtual `.venv`, créalo:

```powershell
py -m venv .venv
```

Activa el entorno virtual e instala las dependencias:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
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

## Documentación

- [Briefing](briefing.md)
- [Requisitos del producto (PRD)](PRD.md)
- [Visión del producto](Spec/vision.md)
- [Alcance](Spec/scope.md)
- [Criterios de aceptación](Spec/acceptance_criteria.md)
