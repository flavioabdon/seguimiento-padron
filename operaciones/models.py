from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kit(models.Model):
    codigo_kit = models.CharField(max_length=100, unique=True)
    ESCANER_CHOICES = [
        ('Epson 110', 'Epson 110'),
        ('Epson 100', 'Epson 100'),
    ]
    CAMARA_CHOICES = [
        ('Logitech 110', 'Logitech 110'),
        ('Logitech 150', 'Logitech 150'),
    ]
    IMPRESORA_CHOICES = [
        ('HP LPB3000', 'HP LPB3000'),
        ('HP LPB6000', 'HP LPB6000'),
        ('CANON 2700', 'CANON 2700'),
        ('CANON 2900', 'CANON 2900'),
        ('BROTHER 2700', 'BROTHER 2700'),
    ]
    ESTACION_CHOICES = [
        ('LAPTOP', 'LAPTOP'),
        ('DESKTOP', 'DESKTOP'),
    ]
    TIPO_DESKTOP_CHOICES = [
        ('DELL OPTIPLEX 360', 'DELL OPTIPLEX 360'),
        ('DELL OPTIPLEX 390', 'DELL OPTIPLEX 390'),
    ]
    LAPTOP_CHOICES = [
        ('DELL E5500', 'DELL E5500'),
        ('DELL E5520', 'DELL E5520'),
    ]
    tipo_estacion = models.CharField(
        max_length=255, 
        choices=ESTACION_CHOICES,
        blank=True,
        null=True
    )
    modelo_laptop = models.CharField(
        max_length=20,
        choices=LAPTOP_CHOICES,
        blank=True,
        null=True
    )
    modelo_desktop = models.CharField(
        max_length=20,
        choices=TIPO_DESKTOP_CHOICES,
        blank=True,
        null=True
    )
    escaner = models.BooleanField(default=False)
    modelo_escaner = models.CharField(
        max_length=20,
        choices=ESCANER_CHOICES
    )
    camara = models.BooleanField(default=False)
    modelo_camara = models.CharField(
        max_length=20,
        choices=CAMARA_CHOICES
    )
    impresora = models.BooleanField(default=False)
    modelo_impresora = models.CharField(
        max_length=20,
        choices=IMPRESORA_CHOICES
    )
    decadactilar = models.BooleanField(default=False)
    extension = models.BooleanField(default=False)
    estabilizador = models.BooleanField(default=False)
    tripode = models.BooleanField(default=False)
    banner = models.BooleanField(default=False)
    pad_firmas = models.BooleanField(default=False)
    hub_usb = models.BooleanField(default=False)
    adaptador_3a2 = models.BooleanField(default=False)

    def __str__(self):
        return self.codigo_kit

class Llave(models.Model):
    codigo_estacion = models.CharField(max_length=100, unique=True)
    contador_r = models.IntegerField(default=0)
    contador_c = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.codigo_equipo}C{self.contador_c}R{self.contador_r}"

class Ruta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Proceso(models.Model):
    certificacion_pdse = models.IntegerField(default=0)
    fecha_certificado_pdse = models.DateField(blank=True)
    fecha_nota = models.DateField(blank=True)
    cite = models.IntegerField(default=0)
    glosa = models.CharField(max_length=511, blank=True)
    TIPO_PROCESO_CHOICES = [
        ('Operador Urbano', 'Operador Urbano'),
        ('Operador Rural', 'Operador Rural'),
        ('Soporte Urbano', 'Soporte Urbano'),
        ('Soporte Rural', 'Soporte Rural'),
        ('Coordinador', 'Coordinador'),
        ('Auxiliar Tecnico', 'Auxiliar Tecnico'),
        ('Logistica', 'Logistica'),
        ('Asistente Megacentro', 'Asistente Megacentro'),
    ]
    tipo_proceso = models.CharField(
        max_length=20,
        choices=TIPO_PROCESO_CHOICES
    )
    cantidad_de_casos = models.IntegerField(default=0)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monto_literal = models.CharField(max_length=255, blank=True)
    monto_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monto_unitario_literal = models.CharField(max_length=255, blank=True)
    COMISION_1_CHOICES = [
        ('Titular 1', 'Titular 1'),
        ('Titular 2', 'Titular 2'),
        ('Titular 3', 'Titular 3'),
    ]
    comision_1 = models.CharField(
        max_length=55,
        choices=COMISION_1_CHOICES
    )
    COMISION_2_CHOICES = [
        ('Titular 1', 'Titular 1'),
        ('Titular 2', 'Titular 2'),
        ('Titular 3', 'Titular 3'),
    ]
    comision_2 = models.CharField(
        max_length=55,
        choices=COMISION_1_CHOICES
    )
    SEGUIMIENTO_CHOICES = [
        ('TICS', 'TICS'),
        ('JAF', 'JAF'),
        ('Asesoria Legal', 'Asesoria Legal'),
        ('Administracion', 'Administracion'),
    ]
    seguimiento = models.CharField(
        max_length=20,
        choices=SEGUIMIENTO_CHOICES,
        default='TICS'
    )
    nro_grupo = models.IntegerField(default=0)
    nro_preventivo = models.IntegerField(default=0)
    rupe = models.BooleanField(default=False)
    memorandum_comision = models.IntegerField(default=0)
    fecha_memorandum = models.DateField(blank=True)

    def __str__(self):
        return f"{self.certificacion_pdse} - {self.cite}"

class Estacion(models.Model):
    codigo_estacion = models.CharField(max_length=100, unique=True)
    asignada = models.BooleanField(default=False)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    llave = models.ForeignKey(Llave, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ESTADO_CHOICES = [
        ('defectuoso', 'Defectuoso'),
        ('contingencia', 'Contingencia'),
        ('reparacion', 'En Reparacion'),
        ('funcional', 'Funcional'),
        ('nuevo', 'Nuevo'),
    ]
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='funcional'
    )
    observacion = models.TextField(blank=True)

    def __str__(self):
        return self.codigo_estacion
    
class MovimientosEstacion(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"Movimiento de {self.estacion.codigo_estacion} el {self.fecha_movimiento}"
    
class Coordinador(models.Model):
    ESTADO_CHOICES = [
        ('postulante', 'Postulante'),
        ('seleccionado', 'Seleccionado'),
        ('contratado', 'Contratado'),
        ('sin_firmar_contrato', 'Sin Firmar Contrato'),
        ('renuncia', 'Renuncia'),
    ]
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='postulante'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, null=True, blank=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    correo = models.EmailField(unique=True, null=True, blank=True)
    celular = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Operador(models.Model):
    ESTADO_CHOICES = [
        ('postulante', 'Postulante'),
        ('seleccionado', 'Seleccionado'),
        ('contratado', 'Contratado'),
        ('sin_firmar_contrato', 'Sin Firmar Contrato'),
        ('renuncia', 'Renuncia'),
    ]
    TIPO_OPERADOR_CHOICES = [
        ('Operador Urbano', 'Operador Urbano'),
        ('Operador Rural', 'Operador Rural'),
    ]
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='postulante'
    )
    tipo_operador = models.CharField(
        max_length=20,
        choices=TIPO_OPERADOR_CHOICES
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, null=True, blank=True)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, null=True, blank=True)
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE, null=True, blank=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, null=True, blank=True)    
    nro_contrato = models.IntegerField(default=0, unique=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    correo = models.EmailField(unique=True, null=True, blank=True)
    celular = models.CharField(max_length=15, unique=True, null=True, blank=True)
    firmo_contrato = models.BooleanField(default=False)
    firmo_asesoria = models.BooleanField(default=False)
    firmo_direccion = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class ReporteDiario(models.Model):
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    fecha_reporte = models.DateField(auto_now_add=True)
    contador_inicial_c = models.IntegerField(default=0)
    contador_final_c = models.IntegerField(default=0)
    contador_inicial_r = models.IntegerField(default=0)
    contador_final_r = models.IntegerField(default=0)
    incidencias = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)


    def __str__(self):
        return f"{self.operador.user.username} Inicio{self.estacion.codigo_estacion}C{self.contador_inicial_c}R{self.contador_inicial_r} - Fin{self.contador_final_c}R{self.contador_final_r} el {self.fecha_reporte}"

class RegistroDespliegue(models.Model):
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    destino = models.CharField(max_length=255, null=True)
    latitud_despliegue = models.CharField(max_length=255, null=True)
    longitud_despliegue = models.CharField(max_length=255, null=True)
    latitud_llegada = models.CharField(max_length=255, null=True)
    longitud_llegada = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=255, null=True)
    sincronizar = models.BooleanField(default=False)    
    observaciones = models.TextField(blank=True)
    fue_desplegado = models.BooleanField(default=False)
    fecha_hora_salida = models.DateTimeField(blank=True, null=True)
    llego_destino = models.BooleanField(default=False)
    fecha_hora_llegada = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.operador.user.username}-{self.destino}"
