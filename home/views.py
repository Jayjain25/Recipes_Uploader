from django.shortcuts import *
from add_receipes.views import *
from add_receipes.models import *
from django.http import *
from first import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login
# Create your views here.
def home(request):
    context = {'page' : 'Home'}
    queryset = Receipe.objects.all()

    # Search Function
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))


    
    context = {'home': queryset}
    
    return render(request,'home1.html', context)

# def update_receipe(request , id):
#     queryset = Receipe.objects.get(id = id)
    

#     if request.method == "POST":
#         data = request.POST
#         receipe_name = data.get('receipe_name')
#         receipe_description = data.get('receipe_description')
#         receipe_image = request.FILES.get('receipe_image')

#         queryset.receipe_name = receipe_name
#         queryset.receipe_description = receipe_description
#         if receipe_image:
#             queryset.receipe_image = receipe_image
#         queryset.save()
#         return redirect('/')

#     context = {'update_receipe':queryset}
#     return render(request,'update_receipe.html', context)

# def delete_receipe(request , id):
#     queryset = Receipe.objects.get(id = id)
#     queryset.delete()
#     return redirect('/')
    


