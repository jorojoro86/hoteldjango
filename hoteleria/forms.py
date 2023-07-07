from django import forms
from .models import Habitacionm
from .models import Pasajerom


class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacionm
        fields = '__all__'


class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajerom
        fields = '__all__'




