from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Coordinador, Operador

COORDINADOR_GROUP = 'Coordinador'
OPERADOR_GROUP = 'Operador'

def crear_registro_por_rol(user):

    if user.groups.filter(name=COORDINADOR_GROUP).exists():
        Coordinador.objects.get_or_create(
            user = user,
            defaults={
                'nombre': user.first_name,
                'apellido_paterno': user.last_name,
                'correo': user.email,
            }
        )

    if user.groups.filter(name=OPERADOR_GROUP).exists():
        Operador.objects.get_or_create(
            user = user,
            defaults= {
                'nombre': user.first_name,
                'apellido_paterno': user.last_name,
                'correo': user.email,
            }
        )

@receiver(post_save, sender= User)
def crear_registro_al_crear_usuario(sender, instance, created, **kwargs):
    if created:
        crear_registro_por_rol(instance)

@receiver(m2m_changed, sender=User.groups.through)
def crear_registro_al_asignar_grupo(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        crear_registro_por_rol(instance)