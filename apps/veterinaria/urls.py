from django.urls import path
from apps.veterinaria.views import ClienteCreateView, ClienteUpdateView, HistoriaClinicaCreateView, HistoriaClinicaListView, HistoriaUpdateView, MacotaUpdateView, ClienteDeleteView, MascotaCreateView, HistoriaDeleteView, MascotaDeleteView, MascotaListView, filter_cliente, homeView, salir

app_name = "apps.veterinaria"

urlpatterns = [
    path('', homeView , name='home'),
    path('salir/', salir , name='salir'),
    path('cliente', filter_cliente, name='listado_clientes'),
    path('nuevo', ClienteCreateView.as_view(), name='crear_clientes'),
    path('editar/<int:pk>', ClienteUpdateView.as_view(), name='editar_clientes'),
    path('eliminar/<int:pk>', ClienteDeleteView.as_view(), name='eliminar_clientes'),
    path('mascota', MascotaListView.as_view(), name='listado_mascota'),
    path('mascota/nuevo', MascotaCreateView.as_view(), name='crear_mascota'),
    path('mascota/eliminar/<int:pk>', MascotaDeleteView.as_view(), name='eliminar_mascota'),
    path('mascota/editar/<int:pk>', MacotaUpdateView.as_view(), name='editar_mascota'),
    path('historia', HistoriaClinicaListView.as_view(), name='listado_historia'),
    path('historia/nuevo', HistoriaClinicaCreateView.as_view(), name='crear_historia'),
    path('historia/editar/<int:pk>', HistoriaUpdateView.as_view(), name='editar_historia'),
    path('historia/eliminar/<int:pk>', HistoriaDeleteView.as_view(), name='eliminar_historia'),
]
