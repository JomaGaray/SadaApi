from django.urls import path
from .views import (TipoTramiteListView,TipoTramiteCreateView,TipoTramiteDetailView, TipoTramiteReqDetailView,
                    UserListView, UserCreateView, UserDetailView,
                    RequerimientoCreateView,RequerimientoListView, RequerimientoDetailView,
                    DocumentoListView,DocumentoCreateView,DocumentoDetailView,
                    RolCreateView, NotificacionCreateView,
                    )

urlpatterns = [
    
    #TRAMITES
    path('tramite/create/', TipoTramiteCreateView.as_view(), name = 'tramiteCreate'),
    path('tramite/list/', TipoTramiteListView.as_view(), name = 'tramiteList'),
    path('tramite/detail/<slug:nombre>/', TipoTramiteDetailView.as_view(), name = 'tramiteDetail'),
        #los requerimientos de un tramite en particular
    path('tramite/detail/<slug:nombre>/requerimientos/', TipoTramiteReqDetailView.as_view(), name = 'ReqTramiteList' ),

    #USUARIOS   
    path('usuario/create/', UserCreateView.as_view(), name = 'usuarioCreate' ),
    path('usuario/list/', UserListView.as_view(), name = 'usuaarioList' ),
    path('usuario/detail/<pk>/', UserDetailView.as_view(), name = 'usuarioDetail' ),
    path('usuario/detail/<int:docuemento>/tramitesActivos', UserDetailView.as_view(), name = 'usuarioDetail' ),

    #REQUERIMIENTOS
    path('requerimiento/create/', RequerimientoCreateView.as_view(), name = 'RequerimientoCreate' ),
    path('requerimiento/list/', RequerimientoListView.as_view(), name = 'RequerimientoList' ),
    path('requerimiento/detail/<slug:codigo>/', RequerimientoDetailView.as_view(), name = 'RequerimientoDetail' ),

    #DOCUMENTOS
    path('documento/create/', DocumentoCreateView.as_view(), name = 'DocumentoCreate' ),
    path('documento/list/', DocumentoListView.as_view(), name = 'DocumentoList' ),
    path('documento/detail/<slug:nombre>/', DocumentoDetailView.as_view(), name = 'DocumentoDetail' ),

    #ROLES
    path('rol/create/', RolCreateView.as_view(), name = '' ),
    path('notificacion/create/', NotificacionCreateView.as_view(), name = '' ),

    


]