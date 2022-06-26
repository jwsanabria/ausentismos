from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pais'
        verbose_name_plural = 'paises'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Pais, self).save(*args, **kwargs)

class Departamento(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Departamento, self).save(*args, **kwargs)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ciudad'
        verbose_name_plural = 'ciudades'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Ciudad, self).save(*args, **kwargs)

class Sede(models.Model):
    descripcion = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'sede'
        verbose_name_plural = 'sedes'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Sede, self).save(*args, **kwargs)

class Seccion(models.Model):
    descripcion = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'seccion'
        verbose_name_plural = 'secciones'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Seccion, self).save(*args, **kwargs)

class Area(models.Model):
    descripcion = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Area, self).save(*args, **kwargs)

class Cargo(models.Model):
    descripcion = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Cargo, self).save(*args, **kwargs)

class Afp(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'afp'
        verbose_name_plural = 'afp'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Afp, self).save(*args, **kwargs)


class Arl(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'arl'
        verbose_name_plural = 'arl'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Arl, self).save(*args, **kwargs)

class Eps(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'eps'
        verbose_name_plural = 'eps'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Eps, self).save(*args, **kwargs)

class CajaCompensacion(models.Model):
    nombre = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'caja compensación'
        verbose_name_plural = 'cajas compensación'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CajaCompensacion, self).save(*args, **kwargs)

class Persona(models.Model):
    TIPO_DOCUMENTO = (
        ('CC', 'Cedula de ciudadania'),
        ('CE', 'Cedula de extranjeria'),
        ('P', 'Pasaporte'),
        ('TI', 'Tarjeta de identidad'),
    )

    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('B', 'No binario')
    )
    ESTADO_CIVIL = (
        ('C', "Casado (a)"),
        ('V', "Viudo (a)"),
        ('S', "Soltero (a)"),
        ('L', "Unión Libre")
    )
    RH = (
        ('+', 'Positivo'),
        ('-', 'Negativo')
    )
    ESTADO = (
        ('0', 'INACTIVO'),
        ('1', 'ACTIVO')
    )
    GRUPO_RH = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    )
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO)
    documento = models.CharField(max_length=20)
    nombre=models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=GENERO)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE)
    libreta_militar = models.BooleanField()
    distrito_militar = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)], blank=True, null=True)
    numero_libreta = models.PositiveIntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL)
    direccion_residencia = models.CharField(max_length=200)
    estrato = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    telefono = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)], blank=True, null=True)
    celular = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)])
    correo = models.EmailField()
    foto = models.ImageField(blank=True, null=True)
    fecha_ingreso = models.DateField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    estado = models.CharField(max_length=1, choices=ESTADO)
    eps = models.ForeignKey(Eps, on_delete=models.CASCADE)
    afp = models.ForeignKey(Afp, on_delete=models.CASCADE)
    arl = models.ForeignKey(Arl, on_delete=models.CASCADE)
    caja = models.ForeignKey(CajaCompensacion, on_delete=models.CASCADE)
    rh = models.CharField(max_length=1, choices=RH)
    grupo_rh = models.CharField(max_length=2, choices=GRUPO_RH)
    persona_contacto = models.CharField(max_length=100, blank=True, null=True)
    celuar_contacto = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)], blank=True, null=True)
    coreeo_contacto = models.EmailField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

    def __str__(self):
        return self.tipo_documento + "-" + self.documento + " " + self.nombre

    def display_salario(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        #return ', '.join([genre.name for genre in self.genre.all()[:3]])
        return '${:,.2f}'.format(self.salario)

    display_salario.short_description = 'Salario'

    def get_absolute_url(self):
        return reverse("persona_view", kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Persona, self).save(*args, **kwargs)


class InfoAcademica(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    anio = models.PositiveIntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2050)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'información académica'
        verbose_name_plural = 'información académica'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(InfoAcademica, self).save(*args, **kwargs)


class ExperienciaLaboral(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    anio_inicio = models.PositiveIntegerField( validators=[MinValueValidator(1950), MaxValueValidator(2050)])
    anio_fin = models.PositiveIntegerField( validators=[MinValueValidator(1950), MaxValueValidator(2050)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'experiencia laboral'
        verbose_name_plural = 'experiencia laboral'

    def __str__(self):
        return self.cargo

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ExperienciaLaboral, self).save(*args, **kwargs)


class MotivoAusentismo(models.Model):
    descripcion = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'motivo'
        verbose_name_plural = 'motivos'

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(MotivoAusentismo, self).save(*args, **kwargs)


class Ausentismo(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    motivo = models.ForeignKey(MotivoAusentismo, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    fecha_ausentismo = models.DateField()
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    tiempo_ausentismo = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ausentismo'
        verbose_name_plural = 'ausentismos'

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Ausentismo, self).save(*args, **kwargs)

