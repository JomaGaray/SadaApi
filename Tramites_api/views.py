from .models import * 
from .serializers import *
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,)
from rest_framework.pagination import PageNumberPagination #https://www.django-rest-framework.org/api-guide/pagination/#api-reference


# https://www.django-rest-framework.org/api-guide/generic-views/#api-reference
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
# https://www.django-rest-framework.org/api-guide/generic-views/#attributes

#USUARIOS
"""
class UserCreateView (CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UserListView (ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = PageNumberPagination

class UserDetailView (RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    #lookup_field = 'first_name'
    #lookup_url_kwarg = 'first_name'

"""

class UserCreateView (CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer

class UserListView (ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    pagination_class = PageNumberPagination

class UserDetailView (RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer
    lookup_field = 'user_id'
  
   
"""
    lookup_url_kwarg = 'username'
    def get_queryset(self):
    profile = self.request.profile
    return user.

     def get_object(self):
        object.queryset = queryset.filter(pk=self.request.user.pk)
        return object

"""


#ROL 
class RolCreateView (CreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

#NOTIFICACIONES 
class NotificacionCreateView (CreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

#TRAMITES
class TramiteCreateView (CreateAPIView):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer

class TramiteListView (ListAPIView):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer
    pagination_class = PageNumberPagination
    # authentication_classes =
    # permissions_clasess = 

class TramiteDetailView (RetrieveAPIView):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer
    lookup_field = 'nombre'
    lookup_url_kwarg = 'nombre'


class TramiteReqDetailView (RetrieveAPIView):
    queryset = Tramite.objects.all()
    serializer_class = TramiteReqSerializer
    lookup_field = 'nombre'
    lookup_url_kwarg = 'nombre'




#REQUERIMIENTOS
class RequerimientoCreateView (CreateAPIView):
    queryset = Requerimiento.objects.all()
    serializer_class = RequerimientoSerializer

class RequerimientoListView (ListAPIView):
    queryset = Requerimiento.objects.all()
    serializer_class = RequerimientoSerializer
    pagination_class = PageNumberPagination

class RequerimientoDetailView (RetrieveAPIView):
    queryset = Requerimiento.objects.all()
    serializer_class = RequerimientoSerializer
    lookup_field = 'codigo'
    lookup_url_kwarg = 'codigo'
    

#DOCUMENTOS
class DocumentoCreateView (CreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class DocumentoListView (ListAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    pagination_class = PageNumberPagination

class DocumentoDetailView (RetrieveAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    lookup_field = 'nombre'
    lookup_url_kwarg = 'nombre'

