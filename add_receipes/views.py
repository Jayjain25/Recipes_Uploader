from django.shortcuts import *
from django.http import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url = "/login/")
def addreceipe(request):
    context = {'page' : 'Add Receipe'}
    if request.method == 'POST':
        data = request.POST


        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,

            receipe_image = receipe_image
        )

    queryset = Receipe.objects.all()


    context = {'addreceipe': queryset}
        
    return render(request,'receipe.html', context)

# Create your views here.
