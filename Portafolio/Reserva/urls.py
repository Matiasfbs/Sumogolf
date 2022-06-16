from django.urls import path
from django.contrib.auth.decorators import login_required
from Reserva.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, checkout_carrito
from django.contrib.auth import views as auth_views
from . import views 
from .views import RegistroPdf

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('somos/', views.somos, name='somos'),
    path('registrar_hora/', login_required(views.registrar_hora),
         name='registrar_hora'),
    path('clases/', views.infoclases, name='clases'),
    path('registro/', views.registro, name="registro"),
    path('contacto/', views.contacto, name="contacto"),
    path('clases_golf/', views.clases_golf, name="clases_golf"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/restablecer_contraseña.html"), name="reset_password"),

    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/restablecer_contraseña_enviada.html"), name="password_reset_done"),

    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/restablecer_contraseña_form.html"), name="password_reset_confirm"),

    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/restablecer_contraseña_hecho.html"), name="password_reset_complete"),

        
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('checkout/', checkout_carrito, name="Checkout"),

    
    path('reparacion/', views.reparacion, name="reparacion"),
    path('list_reparacion/', views.list_reparacion, name="list_reparacion"),
    path('mod_registro/<id>/', views.mod_registro, name="mod_registro"),
    path('eliminar_registro/<id>/', views.eliminar_registro, name="eliminar_registro"),
    path('list_solicitud/', views.list_solicitud, name="list_solicitud"),
    path('list_contacto/', views.list_contacto, name="list_contacto"),
    path('registropdf/', RegistroPdf.as_view() , name="registros_all"),
    path('eliminar_solicitud/<id>/', views.eliminar_solicitud, name="eliminar_solicitud"),

]
