from rest_framework import serializers
from Tramites.models import *
from django.contrib.auth.models import User



# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer


class TramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tramite
        fields = '__all__'

class TramiteReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tramite
        fields = ['nombre','requerimientos']

"""
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                 'last_name', 'email', 'password','documento','roles','notificaciones']



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
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        #for data in profile_data:
        #    Profile.objects.create(user=user, **profile_data)
        return user
"""

class RolSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rol
        fields = ['nombre', 'departamento']



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'first_name',
                 'last_name', 'email', 'password']

#https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
class ProfileCreateSerializer(serializers.ModelSerializer):
    user =  UserCreateSerializer()
    class Meta: 
        model = Profile
        fields = ['user','documento']
    
    def create(self, validated_data):
       profile_data = validated_data.pop('documento') #valido los datos del perfil
       user_data = validated_data.pop('user') #valido los datos de user 
       usuario=User.objects.create(**user_data) #creo un usuario con los datos validados
       profile = Profile.objects.create(user=usuario,documento=profile_data) #creo el perfil con el usuario y los datos
       return profile
""" 
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile = Profile.objects.create(**validated_data)
        for data in user_data:
            User.objects.create(**data, profile=profile) #hay un error en esta linea
        return profile
"""


class UserListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'first_name',
                 'last_name', 'email']

class ProfileListSerializer(serializers.ModelSerializer):
    user =  UserListSerializer()
    class Meta: 
        model = Profile
        fields = ['user','documento']




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
    


