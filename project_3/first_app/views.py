from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'author' : 'Rajon', 'age' : 25, 'lst' : ['Python','is','best'], 'courses' :[
         
         {
             'id' : 1,
             'name' : 'Python',
             'fee' : 5000
         },

        {
            'id ' : 2,
            'name' : 'django',
            'fee' : 1000     
        },
         {
            'id ' : 3,
            'name' : 'C++',
            'fee' : 1000     
        },
    ]}
         
        
    return render(request, 'first_app/home.html',d)