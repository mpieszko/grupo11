from django.urls import path
from App.comentario.views import Comentar
from . import views
app_name = 'noticias'
urlpatterns = [
    path('noticias/',views.Noticialv.as_view()),
    # path('detalle/<int:pk>/add_comment/', Comentar, name='add_comment'),
    path('detalle/<int:pk>/',views.Detalle_Noticias , name='post_detail'),

]
