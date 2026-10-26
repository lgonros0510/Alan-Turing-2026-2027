from datetime import datetime, timezone

from django.db import migrations


def add_example_articles(apps, schema_editor):
    Article = apps.get_model("blog", "Article")
    database = schema_editor.connection.alias
    examples = [
        {
            "title": "Cómo aprende a mirar un robot móvil",
            "slug": "como-aprende-a-mirar-un-robot-movil",
            "excerpt": "Una introducción a los sensores que ayudan a un robot a orientarse en un espacio desconocido.",
            "content": (
                "Un robot móvil no ve el mundo como una persona. Para orientarse, combina "
                "mediciones parciales y construye una representación útil de su entorno.\n\n"
                "## Sensores que se complementan\n\n"
                "Una cámara aporta color y formas; un sensor de distancia estima qué tan "
                "lejos están los objetos. Ninguno cuenta toda la historia por sí solo.\n\n"
                "## De la medición a la decisión\n\n"
                "El sistema compara las lecturas con su mapa, estima dónde está y elige "
                "un movimiento que pueda realizar con seguridad. Esa estimación se corrige "
                "cada vez que llegan nuevos datos."
            ),
            "author": "Equipo editorial",
            "published_at": datetime(2026, 10, 20, 9, tzinfo=timezone.utc),
            "is_published": True,
        },
        {
            "title": "Probar, medir y volver a diseñar",
            "slug": "probar-medir-y-volver-a-disenar",
            "excerpt": "Por qué los experimentos pequeños son una parte esencial del diseño robótico.",
            "content": (
                "En robótica, una idea solo empieza a responder preguntas cuando se "
                "prueba en el mundo físico. Un prototipo sencillo permite observar lo que "
                "funciona y lo que todavía no entendemos.\n\n"
                "## Una hipótesis concreta\n\n"
                "Antes de cambiar un diseño, conviene definir qué resultado esperamos y "
                "qué vamos a medir. Así, cada prueba aporta información que se puede comparar.\n\n"
                "## Aprender del movimiento\n\n"
                "Las ruedas pueden patinar, una pieza puede flexionarse y una lectura puede "
                "llegar tarde. Registrar esos detalles convierte un fallo en una pista para "
                "la siguiente versión."
            ),
            "author": "Equipo editorial",
            "published_at": datetime(2026, 10, 14, 9, tzinfo=timezone.utc),
            "is_published": True,
        },
    ]
    for example in examples:
        Article.objects.using(database).get_or_create(slug=example["slug"], defaults=example)


class Migration(migrations.Migration):
    dependencies = [("blog", "0001_initial")]

    operations = [migrations.RunPython(add_example_articles, migrations.RunPython.noop)]