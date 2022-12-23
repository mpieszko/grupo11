from django.shortcuts import render,redirect
from App.noticias.forms import ContactoForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages



# Create your views here.
def Index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def password(request):
    return render(request, 'password.html')

def donaciones(request):
    return render(request, 'donaciones.html')

#-----View de la pág con el formulario para contactos:
def Contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
#-----

# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, " La Cuenta se creo con Exito")
#             return redirect('login')
#     context = {'form':form}
#     return render(request,'log/register.html',context)

# def loginPage(request):

#     if request.method == 'POST':
#         username1 = request.POST.get('username')
#         password1 = request.POST.get('password')
#         # nombre_usuario = form.cleaned_data.get('username')
#         # contra = form.cleaned_data.get('password')

#         user = authenticate(request, username=username1,password=password1)

#         if user is not None:
#             login(request, user)
#             return redirect('inicio')
#         else:
#          messages.info(request, 'Usuario o contraseña es incorrecto')   
#     context = {}
#     return render(request,'log/login.html',context)

# def logoutUser(request):
#     logout(request)
#     return redirect('inicio')
