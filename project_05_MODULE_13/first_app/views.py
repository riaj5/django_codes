from django.shortcuts import render
from .forms import contactform
def home(request):
    return render(request, './first_app/home.html')


def about(request):
    return render(request, './first_app/about.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, './first_app/form.html', {'name' : name, 'email' : email})
    
    else:
        return render(request, './first_app/form.html')


def DjangoForm(request):
    form = contactform()
    return render(request, './first_app/django_form.html', {'form' : form})