from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('habitacion', views.habitacion, name='habitacion'),
    path('crearhab', views.crearhab, name='crearhab'),
    path('editarhab/<int:id>', views.editarhab, name='editarhab'),
    path('eliminarhab/<int:id>', views.eliminarhab, name='eliminarhab'),
    path('pasajeroindex', views.pasajeroindex, name='pasajeroindex'),
    path('crearpas', views.crearpas, name='crearpas'),
    path('editarpas/<int:id>', views.editarpas, name='editarpas'),
    path('eliminarpas/<int:id>', views.eliminarpas, name='eliminarpas'),
    path('habpas', views.habpas, name='habpas'),

]