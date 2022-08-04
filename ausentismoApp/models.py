from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
from .validators import validador_fecha_futura
import datetime
from decimal import Decimal


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
    celular_contacto = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)], blank=True, null=True)
    correo_contacto = models.EmailField(blank=True, null=True)
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

    def personaToDictionary(self):
        if self == None:
            return None

        dictionary = {}
        dictionary["nombre"] = self.nombre
        dictionary["documento"] = self.documento
        dictionary["tipo_documento"] = self.tipo_documento
        dictionary["id"] = self.id

        return dictionary


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
    PERIODO_AUSENTISMO = (
        ('D', 'Día'),
        ('H', 'Hora')
    )
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    motivo = models.ForeignKey(MotivoAusentismo, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    fecha_ausentismo = models.DateField()
    tiempo_ausentismo = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    periodo_ausentismo = models.CharField(max_length=2, choices=PERIODO_AUSENTISMO)
    horas_ausentismo = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    salario_ausentismo = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    valor_ausentismo = models.DecimalField(decimal_places=2, max_digits=18, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    seccion = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    sede = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ausentismo'
        verbose_name_plural = 'ausentismos'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Ausentismo, self).save(*args, **kwargs)



class Cie10(models.Model):
    MODALIDAD = (
        ('Pri', 'Privada'),
        ('Pub', 'Publica')
    )
    codigo = models.CharField(unique=True, max_length=4)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, default="")
    habilitado = models.BooleanField(default=True)
    aplicacion = models.CharField(max_length=255, blank=True, null=True)
    estandar_gel = models.BooleanField(default=False,blank=True, null=True)
    estandar_msps = models.BooleanField(default=False,blank=True, null=True)
    aplica_sexo = models.BooleanField(default=False,blank=True, null=True)
    edad_minima = models.IntegerField(default=0,blank=True, null=True)
    edad_maxima = models.IntegerField(default=0,blank=True, null=True)
    grupo_mortalidad = models.IntegerField(default=0,blank=True, null=True)
    extra_v = models.CharField(max_length=100,blank=True, null=True)
    capitulo = models.CharField(max_length=100,blank=True, null=True)
    grupo = models.IntegerField(default=0,blank=True, null=True)
    subgrupo = models.IntegerField(default=0,blank=True, null=True)
    categoria = models.IntegerField(default=0,blank=True, null=True)
    subcategoria = models.IntegerField(default=0,blank=True, null=True)
    valor_registro = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,blank=True, null=True)
    usuario_responsable = models.CharField(max_length=200,blank=True, null=True)
    fecha_actualizacion = models.DateField(default=datetime.date.today,blank=True, null=True)
    publico_privado = models.CharField(max_length=3, choices=MODALIDAD,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'CIE 10'
        verbose_name_plural = 'CIE 10'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nombre)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Cie10, self).save(*args, **kwargs)



class Csst_ba_personal(models.Model):
    codigo = models.CharField(max_length=4, unique=True)
    descripcion = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Condición Básica Personal'
        verbose_name_plural = 'Condiciones Básicas Personales'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.descripcion)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Csst_ba_personal, self).save(*args, **kwargs)


class Csst_ba_laboral(models.Model):
    codigo = models.CharField(max_length=4, unique=True)
    descripcion = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Condición Básica Laborel'
        verbose_name_plural = 'Condiciones Básicas Laborales'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.descripcion)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Csst_ba_laboral, self).save(*args, **kwargs)

class Csst_inm_subestandar(models.Model):
    codigo = models.CharField(max_length=4, unique=True)
    descripcion = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Condición Inmediata Subestandar'
        verbose_name_plural = 'Condiciones Inmediatas Subestandar'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.descripcion)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Csst_inm_subestandar, self).save(*args, **kwargs)


class Csst_inm_amb_subestandar(models.Model):
    codigo = models.CharField(max_length=4, unique=True)
    descripcion = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Condición Inmediata Ambiental Subestandar'
        verbose_name_plural = 'Condiciones Inmediatas Ambientales Subestandar'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.descripcion)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Csst_inm_amb_subestandar, self).save(*args, **kwargs)


class Accidente(models.Model):
    JORNADA = (
        ('O', 'ORDINARIA'),
        ('A', 'ADICIONAL'),
        ('T', 'TURNOS')
    )
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha_accidente = models.DateField(validators=[validador_fecha_futura])
    hora_accidente = models.TimeField()
    tipo_jornada = models.CharField(max_length=1, choices=JORNADA)
    inicio_jornada = models.TimeField()
    final_jornada = models.TimeField()
    fallecido = models.BooleanField(default=False,blank=True, null=True)
    incapacidad = models.BooleanField(default=False,blank=True, null=True)
    invalidez = models.BooleanField(default=False,blank=True, null=True)
    dias_incapacidad = models.PositiveIntegerField(blank=True, null=True)
    grado_invalidez = models.PositiveIntegerField(blank=True, null=True)
    descripcion_accidente = models.TextField()
    codigo_cie10 = models.ForeignKey(Cie10, on_delete=models.CASCADE)
    factor_personal = models.ForeignKey(Csst_ba_personal, on_delete=models.CASCADE)
    factor_laboral = models.ForeignKey(Csst_ba_laboral, on_delete=models.CASCADE)
    acto_subestandar = models.ForeignKey(Csst_inm_subestandar, on_delete=models.CASCADE)
    cond_ambientales_subestandar = models.ForeignKey(Csst_inm_amb_subestandar, on_delete=models.CASCADE)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    lucro_consolidado = models.DecimalField(decimal_places=2, max_digits=18, blank=True, null=True)
    lucro_futuro = models.DecimalField(decimal_places=2, max_digits=18, blank=True, null=True)
    ipc_inicial = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    ipc_final = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    num_mes_lcc = models.PositiveIntegerField(blank=True, null=True)
    salario_accidentado = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    salario_minimo = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    factor_moral_n1 = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    factor_moral_n2 = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    factor_moral_n3 = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    factor_moral_n4 = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True,
                                                  null=True)
    factor_moral_n5 = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True,
                                                  null=True)
    valor_moral_n1 = models.DecimalField(decimal_places=2, max_digits=6, validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    valor_moral_n2 = models.DecimalField(decimal_places=2, max_digits=6,
                                         validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    valor_moral_n3 = models.DecimalField(decimal_places=2, max_digits=6,
                                         validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    valor_moral_n4 = models.DecimalField(decimal_places=2, max_digits=6,
                                         validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    valor_moral_n5 = models.DecimalField(decimal_places=2, max_digits=6,
                                         validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    valor_dano_moral = models.DecimalField(decimal_places=2, max_digits=18, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'accidente'
        verbose_name_plural = 'accidentes'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        if self.fecha_accidente > datetime.date.today():
            raise ValidationError("La fecha del accidente no puede ser mayor a hoy!")
        return super(Accidente, self).save(*args, **kwargs)

    def get_documentar_url(self):
        return reverse("costos_list", kwargs={'pk': self.id})

    def get_lucro_url(self):
        return reverse("lucro_cesante", kwargs={'pk': self.id})

    def get_nomina_url(self):
        return reverse("apropiaciones_nomina", kwargs={'pk': self.id})

    def get_cambio_url(self):
        return reverse("adaptacion_cambio", kwargs={'pk': self.id})

    def get_balance_url(self):
        return reverse("balance", kwargs={'pk': self.id})

    def get_detalle_url(self):
        return reverse("detalle_accidente", kwargs={'pk': self.id})


class CostosAccInsumosMedicos(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    insumo = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])


    class Meta:
        verbose_name = 'Costos Accidente Insumo Médico'
        verbose_name_plural = 'Costos Accidnte Insumos Médicos'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccInsumosMedicos, self).save(*args, **kwargs)



class CostosAccTransporte(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    elemento = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Costo de transporte'
        verbose_name_plural = 'Costos de transporte'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccTransporte, self).save(*args, **kwargs)


class CostosAccOtros(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    elemento = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Otro costo'
        verbose_name_plural = 'Otros costos'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccOtros, self).save(*args, **kwargs)


class CostosAccMaquinaria(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    elemento = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Maquinaria requerida'
        verbose_name_plural = 'Lista de maquinaria requerida'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccMaquinaria, self).save(*args, **kwargs)


class CostosAccRepuestos(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    elemento = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Repuesto requerido'
        verbose_name_plural = 'Lista de repuestos requeridos'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccRepuestos, self).save(*args, **kwargs)


class CostosAccManoObra(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mano de obra requerida'
        verbose_name_plural = 'Lista de mano de obra requerida'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccManoObra, self).save(*args, **kwargs)


class FactorIPC(models.Model):
    anio = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    mes = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    factor = models.DecimalField(decimal_places=2, max_digits=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Factor IPC'
        verbose_name_plural = 'Lista de factores IPC'

    def __str__(self):
        return '%s - %s => %s' % (self.anio, self.mes, self.factor)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(FactorIPC, self).save(*args, **kwargs)


class ExpectativaVida(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('B', 'No binario')
    )
    edad = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(150)])
    tipo = models.CharField(max_length=1, choices=GENERO)
    expectativa = models.DecimalField(decimal_places=2, max_digits=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Expectativa de vida'
        verbose_name_plural = 'Expectativas de vida'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ExpectativaVida, self).save(*args, **kwargs)


class CostosAccDanoEmergente(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Daño emergente'
        verbose_name_plural = 'Lista de daños emergentes'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccDanoEmergente, self).save(*args, **kwargs)


class FactorTiemposAcompanamiento(models.Model):
    tipo_acompanamiento = models.CharField(max_length=5, unique=True)
    descripción = models.CharField(max_length=50)
    factor = models.DecimalField(decimal_places=2, max_digits=4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Factor tiempo acompañamiento'
        verbose_name_plural = 'Lista de factores'

    def __str__(self):
        return str(self.tipo_acompanamiento)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(FactorTiemposAcompanamiento, self).save(*args, **kwargs)



class TipoAcompanamiento(models.Model):
    descripcion = models.CharField(max_length=80, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tipo acompañamiento'
        verbose_name_plural = 'Lista de tipos de acompañamiento'

    def __str__(self):
        return str(self.descripcion)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TipoAcompanamiento, self).save(*args, **kwargs)

class TiemposAccAcompanamiento(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_acompanamiento = models.ForeignKey(TipoAcompanamiento, on_delete=models.CASCADE)
    tiempo = models.TimeField()
    factor = models.ForeignKey(FactorTiemposAcompanamiento, on_delete=models.CASCADE)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    valor_diario = models.DecimalField(decimal_places=2, max_digits=10)
    valor_factor = models.DecimalField(decimal_places=2, max_digits=10)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Acompañaieno en el accidente'
        verbose_name_plural = 'Acompañamientos en el accidente'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TiemposAccAcompanamiento, self).save(*args, **kwargs)

class ReemplazoAccidente(models.Model):
    TIPO_REEMPLAZO=(
        ('INTERNO', 'Interno'),
        ('EXTERNO', 'Externo')
    )
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    reemplazo = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_reemplazo = models.CharField(max_length=7, choices=TIPO_REEMPLAZO)
    dias = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Remplazo del accideentado'
        verbose_name_plural = 'Reemplazo del accidentado'

    def __str__(self):
        return str(self.reemplazo)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ReemplazoAccidente, self).save(*args, **kwargs)


class CapacitadorAccidente(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    capacitador = models.ForeignKey(Persona, on_delete=models.CASCADE)
    dias = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Capacitación para el reemplazo'
        verbose_name_plural = 'Capacitación para el reemplazo'

    def __str__(self):
        return str(self.capacitador)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CapacitadorAccidente, self).save(*args, **kwargs)


class FactorAccParafiscales(models.Model):
    descripcion = models.CharField(max_length=80, unique=True)
    factor = models.DecimalField(decimal_places=2, max_digits=4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Factor de accidentalidad por Parafiscales'
        verbose_name_plural = 'Factores de accidentalidad por parafiscales'

    def __str__(self):
        return '%s - %s' % (self.descripcion, self.factor)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(FactorAccParafiscales, self).save(*args, **kwargs)


class CostosAccAdicionales(models.Model):
    accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    actividad = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Costos adicionales'
        verbose_name_plural = 'Lista de costos adicionales'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CostosAccAdicionales, self).save(*args, **kwargs)



class NivDanoMoral(models.Model):
    TIPO_DANO = (
        ('M', 'Muerte'),
        ('I', 'Invalidez')
    )
    tipo_dano = models.CharField(max_length=1, choices=TIPO_DANO)
    rango_inf = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    rango_sup = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    nivel = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    valor = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Niveles de daño moral'
        verbose_name_plural = 'Lista de niveles de daño moral'

    def __str__(self):
        return '%s (%s : %s) - %s => %s' % (self.tipo_dano, self.rango_inf, self.rango_sup, self.nivel, self.valor)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(NivDanoMoral, self).save(*args, **kwargs)

class ParametrosApp(models.Model):
    parametro = models.CharField(max_length=100)
    valor = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Parámetro de la aplicación'
        verbose_name_plural = 'Lista de parametros'

    def __str__(self):
        return '%s => %s' % (self.parametro, self.valor)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ParametrosApp, self).save(*args, **kwargs)



