import email
from django.contrib import admin
from.models import Registro, Proveedor, RegistroReparacion,Producto,Marca,CategoriaProducto, Contacto
# Register your models here.



class RegistroAdmin(admin.ModelAdmin):
    list_display=["run","nombre","apellido","dia","fecha_nacimiento"] # se lista por las columnas seleccionadas
    search_fields = ["dia","nombre"] # se crea barra de busqueda por las columnas seleccionadas
    list_filter=["dia"]  #se crea el filtro 




class ProveedorAdmin(admin.ModelAdmin):
    list_display=["run", "nombre","telefono","email", "representante"]
    search_fields=["nombre"]


class RegistroReparacionAdmin(admin.ModelAdmin):
    list_display=["nombre_cliente", "telefono","email","descripcion","precio", "fecha_entrega"]
    search_fields=["nombre_cliente"]
    list_filter = ["fecha_entrega"]


class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre_producto", "precio_compra","precio_venta","cantidad","marca", "categoria"]
    search_fields=["codigo","nombre"]
    list_filter=["marca","categoria"]
    list_per_page = 5 #resgistro por pagina




admin.site.register(Registro, RegistroAdmin)
admin.site.register(Proveedor,ProveedorAdmin) #listar proveedor
admin.site.register(RegistroReparacion,RegistroReparacionAdmin) ##listar proveedor
admin.site.register(Marca)
admin.site.register(CategoriaProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Contacto)











