from rest_framework import serializers
from Tramites.models import *
from django.contrib.auth.models import User



# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer


class TipoTramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTramite
        fields = '__all__'

class TipoTramiteReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTramite
        fields = ['nombre','requerimientos']

"""
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                 'last_name', 'email', 'password','documento','roles','notificaciones']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = '__all__'

class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(source = 'userprofile')
    Profile = ProfileSerializer ()

    class ProfileSerializer(serializers.ModelSerializer):
    documento = serializers.IntegerField(source='userprofile.documento')
    class Meta:
        model =  User
        fields = ['username', 'first_name', 'last_name', 'email', 'password','documento']
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'first_name',
                 'last_name', 'email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    userdetails = UserSerializer(many =True)

    class Meta:
        model =  Profile
        fields = ['userdetails','documento', 'roles', 'notificaciones']
      
    def create(self, validated_data):
        profile = Profile( nombre = validated_data.get("documento") )
        profile.save()        
        userdetails_data = validated_data.get('userdetails')
        profile = Profile.objects.create (**validated_data)

        for userdetail in userdetails_data:
            Profile.objects.create(user = user, **userdetail)
        return validated_data
    
"""

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = ['documento','roles', 'notificaciones']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
   
    class Meta: 
        model = User
        fields = ['username', 'first_name',
                 'last_name', 'email', 'password', 'profile']
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        #for data in profile_data:
        #    Profile.objects.create(user=user, **profile_data)
        return user
    

    
class RolSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rol
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Notificacion
        fields = '__all__'













        
class TramiteSolicitadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TramiteSolicitado
        fields = '__all__'


class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class PaseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Pase
        fields = '__all__'

class PeticionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Peticion
        fields = '__all__'

class RequerimientoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Requerimiento
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Estado
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Documento
        fields = '__all__'
    


