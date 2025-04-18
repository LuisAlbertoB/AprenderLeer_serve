from alembic import op
import sqlalchemy as sa

# Identificadores de revisión (¡OBLIGATORIOS!)
revision = '0c7c0756f42c'  # Debe coincidir con el inicio del nombre del archivo
down_revision = None  # Será el primer seeder
branch_labels = None
depends_on = None

def upgrade():
    # Datos a insertar
    lecturas_data = [
        {
            "nombre_libro": "El Principito",
            "autor": "Antoine de Saint-Exupéry",
            "capitulo": 1,
            "contenido": """Cuando yo tenía seis años vi en un libro sobre la selva virgen que se titulaba "Historias vividas", una magnífica lámina. Representaba una serpiente boa que se tragaba a una fiera. En el libro se afirmaba: La serpiente boa se traga su presa entera, sin masticarla. Luego ya no puede moverse y duerme durante los seis meses que dura su digestión. Reflexioné mucho en ese momento sobre las aventuras de la jungla y a mi vez logré trazar con un lápiz de colores mi primer dibujo. Mi dibujo número 1 era de esta manera: Enseñé mi obra de arte a las personas mayores y les pregunté si mi dibujo les daba miedo. —¿Por qué habría de asustar un sombrero? —me respondieron. Mi dibujo no representaba un sombrero. Representaba una serpiente boa que digiere un elefante. Dibujé entonces el interior de la serpiente boa a fin de que las personas mayores pudieran comprender. Siempre estas personas tienen necesidad de explicaciones. Mi dibujo número 2 era así: Las personas mayores me aconsejaron abandonar el dibujo de serpientes boas, ya fueran abiertas o cerradas, y poner más interés en la geografía, la historia, el cálculo y la gramática. De esta manera a la edad de seis años abandoné una magnífica carrera de pintor. Había quedado desilusionado por el fracaso de mis dibujos número 1 y número 2. Las personas mayores nunca pueden comprender algo por sí solas y es muy aburrido para los niños tener que darles una y otra vez explicaciones. Un poco por todo el mundo y la geografía, en efecto, me ha servido de mucho; al primer vistazo podía distinguir perfectamente la China de Arizona. Esto es muy útil, sobre todo si se pierde uno durante la noche. A lo largo de mi vida he tenido multitud de contactos con multitud de gente seria. Viví mucho con personas mayores y las he conocido muy de cerca; pero esto no ha mejorado demasiado mi opinión sobre ellas. Cuando me he encontrado con alguien que me parecía un poco lúcido, lo he sometido a la experiencia de mi dibujo número 1 que he conservado siempre. Quería saber si verdaderamente era un ser comprensivo. E invariablemente me contestaban siempre: "Es un sombrero". Me abstenía de hablarles de la serpiente boa, de la selva virgen y de las estrellas. Poniéndome a su altura, les hablaba del bridge, del golf, de política y de corbatas. Y mi interlocutor se quedaba muy contento de conocer a un hombre tan razonable."""
        },
    ]

    # Insertar datos
    op.bulk_insert(
        sa.Table(
            'lecturas',
            sa.MetaData(),
            sa.Column('nombre_libro', sa.String(100)),
            sa.Column('autor', sa.String(100)),
            sa.Column('capitulo', sa.Integer),
            sa.Column('contenido', sa.Text)
        ),
        lecturas_data
    )

def downgrade():
    op.execute("DELETE FROM lecturas WHERE nombre_libro = 'El Principito' AND capitulo = 1")
