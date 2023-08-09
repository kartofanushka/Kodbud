"""
URL configuration for adv project.

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
from django.urls import include, path
from app_lesson_4 import views
from app_adv.views import example
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('app_lesson_4.urls')),
    path('', include('app_adv.urls')),
    # path('lesson_4/', views.lesson_4, name='lesson_4'),
    # path('example/', example, name='lesson_4 example'),

]
