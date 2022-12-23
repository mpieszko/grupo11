from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Comentarios
from .forms import  ComentarioForm
from django.views.generic import DeleteView
from App.usuario.models import Usuario
from django.urls import reverse_lazy
# Create your views here.

# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')


def Comentar(request):
    comentarios = Comentarios.objects.all()
    # usuario = request.user.id

    context={
        'comentarios' : comentarios,
        'usuario': Usuario,
    }
    return render(request,'comentario/listadoComentario.html', context)


def agregarComentario(request):
    usuario = Usuario(usuario = request.user)
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ComentarioForm()


    context={
        'form': form,
        'usuario': usuario,
    }
    return render(request,'comentario/agregarComentario.html', context)


class DeleteComentario(DeleteView):
    model = Comentarios
    template_name = 'comentario/eliminarComentario.html'
    success_url = reverse_lazy('App.noticia:noticias')