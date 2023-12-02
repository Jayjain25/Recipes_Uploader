"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import *
from add_receipes.views import *
from home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from search.views import *
from log_reg.views import *
from login_home.views import *


urlpatterns = [
    path('',home, name = "home"),
    path('landpage/',Landpage, name='landpage'),
    path('delete-receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('update-receipe/<id>/',update_receipe, name = "update_receipe"),
    path('addreceipe/',addreceipe, name="addreceipe"),
    path('search/', Search, name="search"),
    path('login/',Login_page, name="login" ),
    path('logout/',Logout_page, name="logout" ),
    path('register/',Register_page, name="register_page" ),
    path('admin/', admin.site.urls),
    path('api/',api),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns = urlpatterns+staticfiles_urlpatterns()

