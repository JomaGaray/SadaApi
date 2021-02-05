from django.urls import path
from .views import (TipoTramiteListView,TipoTramiteCreateView,TipoTramiteDetailView, TipoTramiteReqDetailView,
                    UserListView, UserCreateView, UserDetailView,
                    RequerimientoCreateView,RequerimientoListView, RequerimientoDetailView,
                    DocumentoListView,DocumentoCreateView,DocumentoDetailView,
                    RolCreateView, NotificacionCreateView,
                    )

urlpatterns = [
    
    path('api/tramite/create/', TipoTramiteCreateView.as_view(), name = 'tramiteCreate'),
    path('api/tramite/list/', TipoTramiteListView.as_view(), name = 'tramiteList'),
    path('api/tramite/detail/<slug:nombre>/', TipoTramiteDetailView.as_view(), name = 'tramiteDetail'),
    #los requerimientos de un tramite en particular
    path('api/tramite/detail/<slug:nombre>/requerimientos/', TipoTramiteReqDetailView.as_view(), name = 'ReqTramiteList' ),

    path('api/usuario/create/', UserCreateView.as_view(), name = 'usuarioCreate' ),
    path('api/usuario/list/', UserListView.as_view(), name = 'usuaarioList' ),
    path('api/usuario/detail/<pk>/', UserDetailView.as_view(), name = 'usuarioDetail' ),
    path('api/usuario/detail/<int:docuemento>/tramitesActivos', UserDetailView.as_view(), name = 'usuarioDetail' ),


    path('api/requerimiento/create/', RequerimientoCreateView.as_view(), name = 'RequerimientoCreate' ),
    path('api/requerimiento/list/', RequerimientoListView.as_view(), name = 'RequerimientoList' ),
    path('api/requerimiento/detail/<slug:codigo>/', RequerimientoDetailView.as_view(), name = 'RequerimientoDetail' ),

    path('api/documento/create/', DocumentoCreateView.as_view(), name = 'DocumentoCreate' ),
    path('api/documento/list/', DocumentoListView.as_view(), name = 'DocumentoList' ),
    path('api/documento/detail/<slug:nombre>/', DocumentoDetailView.as_view(), name = 'DocumentoDetail' ),


    path('api/rol/create/', RolCreateView.as_view(), name = '' ),
    path('api/notificacion/create/', NotificacionCreateView.as_view(), name = '' ),


]