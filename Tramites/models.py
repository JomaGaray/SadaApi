from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver
#https://docs.djangoproject.com/en/3.1/topics/db/models/#field-options
#https://docs.djangoproject.com/en/3.1/topics/db/models/#relationships
#https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#extending-the-existing-user-model

    
class Documento(models.Model):
    nombre = models.CharField(max_length=50, null = True)
    descripcion = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=50, null = True)
    departamento = models.CharField(max_length=50, null = True)

    def __str__(self):
        return self.nombre

class Notificacion(models.Model):
    descripcion = models.CharField(max_length=100, null = True)
    #pas = models.OneToOneField(Pass, on_delete=models.CASCADE) #one to one to pass, genera conflicto, lo pongo en pass


class Requerimiento(models.Model):
    nombre = models.CharField(max_length=50, null = True)
    codigo = models.CharField(max_length=100, null = True)
    descripcion = models.CharField(max_length=100, null = True)
    inicio = models.DateField(  null = True)
    fecha_limite = models.DateField( null = True)
    #usuario = models.ForeignKey(User, on_delete = models.CASCADE, null = True) #usuario que completa el requerimiento
    documento = models.ForeignKey(Documento, blank=True, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50, null = True)
    descripcion = models.CharField(max_length=100, null = True)
    creador = models.ForeignKey (User, on_delete=models.CASCADE, null = True) #usuario creador
    a_cargo = models.ForeignKey (Rol, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.nombre

class Tramite(models.Model): 
    nombre = models.CharField(max_length=50, null = True)
    codigo = models.CharField(max_length=100, null = True)
    descripcion = models.CharField(max_length=100, null = True)
    creado = models.DateField( null = True)
    requerimientos = models.ManyToManyField(Requerimiento) #muchos requerimientos
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    estados = models.ManyToManyField(Estado)

    def __str__(self):
        return self.nombre

#related name especifica que es tu modelo con respecto al referenciado
#https://docs.djangoproject.com/en/3.1/topics/db/queries/#following-relationships-backward
#https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name
#https://docs.djangoproject.com/en/3.1/topics/db/models/#extra-fields-on-many-to-many-relationships
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null = True)
    documento = models.IntegerField(null = True)
    tramites_solicitados = models.ManyToManyField(Tramite, through='TramiteSolicitado')
    #roles = models.ManyToManyField(Rol) #un usuario con muchos roles 
    #notificaciones = models.ManyToManyField(Notificacion) #un usuario con muchas notificaciones
"""
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


tabla para registrar las solicitudes, una sol. pertenece univocamente a un usuario, un
usuario puede tener varias solicitudes, en esta tabla se registra tambien el tramite,
un tramite puede ser solicitado muchas veces 
"""
class TramiteSolicitado(models.Model):
    iniciado = models.DateField(null = True)
    terminado = models.DateField(blank=True, null=True)
    en_proceso =  models.BooleanField(null = True) #para saber los tramites activos
    finalizado = models.BooleanField(null = True) # para tener un historial
    alumno = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True) 
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE, null = True)
    

class Peticion (models.Model):
    inicio = models.DateField( null = True)
    peticionario = models.ForeignKey (User, on_delete=models.CASCADE, related_name = 'alumno_peticionante', null = True) #peticionario
    a_cargo = models.ForeignKey (User, on_delete=models.CASCADE, related_name = 'rol_a_cargo', null = True)
    tramite = models.ForeignKey (Tramite, on_delete=models.CASCADE, null = True) #tramite

class Pase(models.Model): 
    inicio = models.DateField( null = True)
    fin = models.DateField(  null = True)
    user = models.ForeignKey (User, on_delete=models.CASCADE, null = True) #usuario que realiza la peticion
    proximo_estado = models.OneToOneField (Estado, on_delete=models.CASCADE, null = True)
    peticion = models.OneToOneField (Peticion, on_delete=models.CASCADE, null = True) #peticion
    requerimientos = models.ManyToManyField (Requerimiento, blank=True)
    notificacion = models.OneToOneField(Notificacion, on_delete=models.CASCADE, null = True)