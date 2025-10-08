from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarea

class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'  
    context_object_name = 'tareas' 

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detail.html'
    context_object_name = 'tarea'

class TareaCreateView(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:lista')

class TareaUpdateView(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:lista')

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tareas:lista')

