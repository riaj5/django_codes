from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'author' : 'Rajon', 'age' : 25}
    return render(request, 'first_app/home.html',d)