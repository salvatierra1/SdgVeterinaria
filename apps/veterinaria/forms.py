from django import forms
from apps.veterinaria.models import Cliente, HistoriaClinica, Mascota

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        # Todos los campos
        fields = '__all__'
        
    '''dni = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fecha_alta = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))'''
   

class MascotaForm(forms.ModelForm):
    class Meta:
        model= Mascota
        # Todos los campos
        fields = '__all__'
    cliente_id= forms.ModelChoiceField(queryset=Cliente.objects.filter(estado=True), widget=forms.Select(attrs={'class': 'form-control'}))
    '''numero_chip=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    nombre_mascota=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_mascota = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))'''
       

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model= HistoriaClinica
        # Todos los campos
        fields = ['fecha_consulta', 'observaciones']
    mascota_id= forms.ModelChoiceField(queryset=Mascota.objects.filter(estado=True), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_consulta = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    '''observaciones = forms.CharField(widget=forms.Textarea(attrs={"rows":"4"}))'''