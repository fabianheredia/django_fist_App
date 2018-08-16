from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from frontend.forms import SignUpForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Evento

def index(reqest):
    return HttpResponse("Hola Fabian")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')



class EventosL(generic.ListView):
    model = Evento
    def get_Evento(self):
            return Evento.objects.filter(usuario=self.request.user).order_by('-e_fechaIni')


class newEvento(LoginRequiredMixin,CreateView):
    model = Evento
    success_url = reverse_lazy('eventos:home')
    fields = ['e_nombre', 'e_categoria', 'e_lugar', 'e_direccion', 'e_fechaIni', 'e_fechaFin', 'e_tipo']

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class detalleEvento(DetailView):
    model = Evento

class modificacionEvento(LoginRequiredMixin,UpdateView):
    model = Evento
    success_url = reverse_lazy('eventos:listaEventos')
    fields = ['e_nombre', 'e_categoria', 'e_lugar', 'e_direccion', 'e_fechaIni', 'e_fechaFin', 'e_tipo']

class borrarEvento(LoginRequiredMixin,DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos:listaEventos')