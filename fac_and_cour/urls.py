"""fac_and_cour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from start.views import home,fac_view,all_fac,all_cour


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('all_faculty/',all_fac, name="all_faculty"),
    path('all_course/',all_cour, name="all_course"),
    path('<a>',fac_view, name="fac_view"),
]
