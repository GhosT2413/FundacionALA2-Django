import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20, null=True)),
                ('apellido_materno', models.CharField(max_length=20, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        
        
        migrations.AddField(
            model_name='paciente',
            name='id_genero',
            field=models.ForeignKey(db_column='idGenero', null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.genero'),
        ),
    ]