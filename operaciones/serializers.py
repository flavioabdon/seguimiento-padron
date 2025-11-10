from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    Kit, Llave, Ruta, Proceso, Estacion, 
    MovimientosEstacion, Coordinador, Operador,
    ReporteDiario, RegistroDespliegue)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        if user.groups.exists():
            token['group'] = user.groups.first().name
        else:
            token['group'] = None
        
        return token

    def validate(self, atrrs):
        data = super().validate(atrrs)
        user = self.user

        data['user'] = {
            'id' : user.id,
            'username' : user.username,
            'email' : user.email,
            'groups' : [g.name for g in user.groups.all()],
        }
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'groups']

class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = '__all__'
    
class LlaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llave
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = '__all__'

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class MovimientosEstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientosEstacion
        fields = '__all__'     

class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = '__all__'

class ReporteDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteDiario
        fields = '__all__'

class RegistroDespliegueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDespliegue
        fields = '__all__'

class ListarOperadoresSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source = 'operador.nombre', read_only=True)
    apellido_paterno = serializers.CharField(source = 'operador.apellido_paterno', read_only = True)
    apellido_materno = serializers.CharField(source = 'operador.apellido_materno', read_only = True)

    class Meta:
        model = RegistroDespliegue
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fue_desplegado', 'llego_destino']



