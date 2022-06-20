# Generated by Django 4.0.5 on 2022-06-20 01:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'afp',
                'verbose_name_plural': 'afp',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Arl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'arl',
                'verbose_name_plural': 'arl',
            },
        ),
        migrations.CreateModel(
            name='CajaCompensacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'caja compensación',
                'verbose_name_plural': 'cajas compensación',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'cargo',
                'verbose_name_plural': 'cargos',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'eps',
                'verbose_name_plural': 'eps',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'pais',
                'verbose_name_plural': 'paises',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'seccion',
                'verbose_name_plural': 'secciones',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'sede',
                'verbose_name_plural': 'sedes',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('CE', 'Cedula de extranjeria'), ('P', 'Pasaporte'), ('TI', 'Tarjeta de identidad')], max_length=2)),
                ('documento', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=255)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('B', 'No binario')], max_length=1)),
                ('libreta_militar', models.BooleanField()),
                ('distrito_militar', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('numero_libreta', models.PositiveIntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('estado_civil', models.CharField(choices=[('C', 'Casado (a)'), ('V', 'Viudo (a)'), ('S', 'Soltero (a)'), ('L', 'Unión Libre')], max_length=1)),
                ('direccion_residencia', models.CharField(max_length=200)),
                ('estrato', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)])),
                ('telefono', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)])),
                ('celular', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)])),
                ('correo', models.EmailField(max_length=254)),
                ('foto', models.ImageField(upload_to='')),
                ('fecha_ingreso', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('0', 'INACTIVO'), ('1', 'ACTIVO')], max_length=1)),
                ('rh', models.CharField(choices=[('+', 'Positivo'), ('-', 'Negativo')], max_length=1)),
                ('grupo_rh', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('persona_contacto', models.CharField(max_length=100)),
                ('celuar_contacto', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)])),
                ('coreeo_contacto', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('afp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.afp')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.area')),
                ('arl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.arl')),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.cajacompensacion')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.cargo')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.ciudad')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.departamento')),
                ('eps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.eps')),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.pais')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.seccion')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.sede')),
            ],
            options={
                'verbose_name': 'persona',
                'verbose_name_plural': 'personas',
            },
        ),
        migrations.CreateModel(
            name='InfoAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('anio', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2050)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.persona')),
            ],
            options={
                'verbose_name': 'información académica',
                'verbose_name_plural': 'información académica',
            },
        ),
        migrations.CreateModel(
            name='ExperienciaLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=200)),
                ('anio_inicio', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2050)])),
                ('anio_fin', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2050)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ausentismoApp.persona')),
            ],
            options={
                'verbose_name': 'experiencia laboral',
                'verbose_name_plural': 'experiencia laboral',
            },
        ),
    ]