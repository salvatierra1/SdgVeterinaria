from django.contrib.auth import logout
from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.veterinaria.forms import ClienteForm,MascotaForm, HistoriaClinicaForm
from apps.veterinaria.models import Cliente, HistoriaClinica, Mascota
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


# HOME
@login_required
def homeView(request):
    return render(request,'home.html')

def salir(request):
    logout(request)
    return redirect('apps.veterinaria:home')
    

#  CLIENTE
'''class ClienteListView(ListView):
    model = Cliente
    queryset = model.objects.filter(estado = True)
    template_name ='cliente/lista.html'''

@login_required
def filter_cliente(request):
    clientes = Cliente.objects.filter(estado = True)
    busqueda = request.GET.get('buscar')
    if busqueda :
        clientes = Cliente.objects.filter(
            Q (nombre__iexact  = busqueda) & Q(estado=True) | Q(apellido__iexact = busqueda) & Q(estado=True)
        ).distinct()
        print(clientes.query)
        print(clientes.exists())
    return render(request, 'cliente/lista.html', {'clientes': clientes})

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name ='cliente/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_clientes')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear Cliente"
        context["btn"] = "Crear"
        return context
    

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name ='cliente/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_clientes')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Actualizar cliente"
        context["btn"] = "Guardar"
        return context

"""clienteDeleteView(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.estado = False
        cliente.save()
        return redirect('apps.veterinaria:listado_clientes')
    context = {'cliente': cliente}
    return render(request, 'cliente/cliente_confirm_delete.html', context)"""

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    def post(self, request, pk, *args, **kwargs):
        cliente = Cliente.objects.get(id=pk)
        cliente.estado = False
        cliente.save()
        return redirect('apps.veterinaria:listado_clientes')    

# MASCOTA
class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name ='mascota/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_mascota')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear Mascota"
        context["btn"] = "Crear"
        return context

class MascotaListView(ListView):
    model = Mascota
    queryset = model.objects.filter(estado = True)
    template_name ='mascota/lista.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear Mascota"
        return context
    
'''def filter_mascota(request):
    mascota = Mascota.objects.filter(estado = True)
    busqueda = request.GET.get('buscar')
    if busqueda :
        mascota = Mascota.objects.filter(
            Q(nombre_mascota__icontains  = busqueda) & Q(estado=True) or
            Q(observaciones__icontains  = busqueda) & Q(estado=True)
        ).distinct()
    return render(request, 'mascota/lista.html', {'mascota': mascota})'''
    
'''def mascotaDeleteView(request, id):
    mascota = Mascota.objects.get(id=id)
    if request.method == 'POST':
        mascota.estado = False
        mascota.save()
        return redirect('apps.veterinaria:listado_mascota')
    context = {'mascota': mascota}
    return render(request,'mascota/mascota_confirm_delete.html', context)'''

class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name ='mascota/mascota_confirm_delete.html'
    def post(self, request, pk, *args, **kwargs):
        mascota = Mascota.objects.get(id=pk)
        mascota.estado = False
        mascota.save()
        return redirect('apps.veterinaria:listado_mascota')

class MacotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name ='mascota/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_mascota')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Actualizar mascota"
        context["btn"] = "Guardar"
        return context
    

# Historia Clinica
class HistoriaClinicaListView(ListView):
    model = HistoriaClinica
    queryset = model.objects.filter(estado = True)
    template_name = 'historia/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear Historia"
        return context

'''def filter_historia(request):
    historias = HistoriaClinica.objects.filter(estado = True)
    busqueda = request.GET.get('buscar')
    if busqueda:
        historias = historias.filter(
          Q(fecha_consulta__icontains = busqueda) and Q(estado = True)
         ).distinct()
    return render(request, 'historia/lista.html', {'historia': historias})'''
  
class HistoriaClinicaCreateView(CreateView):
    model = HistoriaClinicaForm
    form_class = HistoriaClinicaForm
    template_name ='historia/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_historia')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear historia"
        context["btn"] = "Crear"
        return context

'''def historiaDeleteView(request, id):
    historia = HistoriaClinica.objects.get(id=id)
    if request.method == 'POST':
        historia.estado = False
        historia.save()
        return redirect('apps.veterinaria:listado_historia')
    context = {'historia': historia}
    return render(request, 'historia/historia_confirm_delete.html', context)'''


class HistoriaDeleteView(DeleteView):
    model = HistoriaClinica
    template_name = 'historia/historia_confirm_delete.html'
    def post(self, request, pk, *args, **kwargs):
        historia = HistoriaClinica.objects.get(id=pk)
        historia.estado = False
        historia.save()
        return redirect('apps.veterinaria:listado_historia')


class HistoriaUpdateView(UpdateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name ='mascota/create.html'
    success_url = reverse_lazy('apps.veterinaria:listado_historia')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Actualizar historia"
        context["btn"] = "Guardar"
        return context