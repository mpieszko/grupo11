from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Noticia

# Create your views here.

class Noticialv(ListView):
    model = Noticia
    template_name = 'noticia/nview.html'

# def post_detail(request, pk):
#     post = get_object_or_404(Noticia, pk=pk)
#     return render(request, 'post_detail.html', {'post': post})   

def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) 
	contexto['noticia'] = n

	return render(request, 'noticias/detalle.html',contexto)