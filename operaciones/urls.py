from django.urls import path, include
from .views import CustomTokenObtainPairView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .api_views import (
    KitViewSet, LlaveViewSet, RutaViewSet, ProcesoViewSet, 
    EstacionViewSet, MovimientosEstacionViewSet, CoordinadorViewSet, 
    OperadorViewSet, ReporteDiarioViewSet, RegistroDespliegueViewSet,
    UserViewSet
)
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'kits', KitViewSet)
router.register(r'llaves', LlaveViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'procesos', ProcesoViewSet)
router.register(r'estaciones', EstacionViewSet)
router.register(r'movimientos-estacion', MovimientosEstacionViewSet)
router.register(r'coordinadores', CoordinadorViewSet)
router.register(r'operadores', OperadorViewSet)
router.register(r'reportesdiarios', ReporteDiarioViewSet)
router.register(r'registrosdespliegue', RegistroDespliegueViewSet)

urlpatterns = [
    #path('', views.index, name='index'),
    #path para apis
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]