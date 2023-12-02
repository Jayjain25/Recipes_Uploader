from django.shortcuts import *
from django.http import *
from add_receipes.models import *
from home.views import *


# Create your views here.

def Search(request):
    context = {'page' : 'Search'}
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
        

    context = {'search':queryset}

    return render(request , 'search.html',context)
