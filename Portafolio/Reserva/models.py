
from distutils.command.upload import upload
from django.db import models

# Create your models here.


opciones_dia = [
    ["Jueves", "Jueves"],
    ["Viernes", "Viernes"]
]

opciones_lateralidad =[
    ["Diestro", "DIESTRO"],
    ["Zurdo", "ZURDO"]
]


class Registro(models.Model):

    run = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono =models.IntegerField()
    dia = models.CharField(choices=opciones_dia, max_length=50)
    fecha_nacimiento = models.DateField()
    comuna = models.CharField(max_length=50)
    lateralidad = models.CharField(choices=opciones_lateralidad,max_length=50)

    def __str__(self):
        return self.run   #se devuelve el nombre que mas represente la tabla
    class Meta:
        verbose_name_plural="Solicitudes clases de golf"
        verbose_name="Solicitud de clase"


class Proveedor(models.Model):
    run = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    telefono =models.IntegerField()
    email = models.CharField(max_length=50)
    representante = models.CharField(max_length=50)
    def __str__(self):
        return self.run

    class Meta:
        verbose_name_plural="Proveedores"
        verbose_name="Proveedor"


class RegistroReparacion(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    telefono =models.CharField(max_length=15,verbose_name="Teléfono")
    email = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200, verbose_name="Descripción") #CAMBIAR  A textfield PARA DESCRIPCIÓN
    precio = models.IntegerField(verbose_name="Costo reparación")
    fecha_recepcion = models.DateField(verbose_name="Fecha recepción")
    fecha_entrega = models.DateField()

    def __str__(self):
        return self.nombre_cliente
    class Meta:
        verbose_name_plural="Registro de reparaciones"
        verbose_name="Registro de reparación"


class Marca(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.categoria


class Producto(models.Model):
    codigo= models.IntegerField()
    nombre_producto = models.CharField(max_length=50)
    precio_compra = models.IntegerField(verbose_name="Precio unidad")
    precio_venta = models.IntegerField()
    fecha_recepcion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)
    cantidad = models.IntegerField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria=models.ForeignKey(CategoriaProducto, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_producto



consultas=[
["consulta","consulta"],
["reclamo","reclamo"],
["sugerencia","sugerencia"],
["felicitaciones","felicitaciones"]
]


class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta= models.CharField(choices=consultas, max_length=20)
    mensaje=models.TextField()
    aviso= models.BooleanField

    def __str__(self):
        return self.nombre


















