from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

def home(request):
    return render(request, 'voluntarios/home.html')

def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'voluntarios/lista_voluntarios.html', {'voluntarios': voluntarios})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Voluntario creado exitosamente.')
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm()
    return render(request, 'voluntarios/form_voluntario.html', {'form': form, 'accion': 'Crear'})

def editar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Voluntario actualizado exitosamente.')
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'voluntarios/form_voluntario.html', {'form': form, 'accion': 'Editar'})

def eliminar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        voluntario.delete()
        messages.success(request, 'Voluntario eliminado exitosamente.')
        return redirect('lista_voluntarios')
    return render(request, 'voluntarios/confirmar_eliminar.html', {
        'objeto': voluntario,
        'tipo': 'voluntario'
    })

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'voluntarios/lista_eventos.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento creado exitosamente.')
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'voluntarios/form_evento.html', {'form': form, 'accion': 'Crear'})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento actualizado exitosamente.')
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'voluntarios/form_evento.html', {'form': form, 'accion': 'Editar'})

def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado exitosamente.')
        return redirect('lista_eventos')
    return render(request, 'voluntarios/confirmar_eliminar.html', {
        'objeto': evento,
        'tipo': 'evento'
    })

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'voluntarios/detalle_evento.html', {'evento': evento})