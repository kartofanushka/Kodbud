from django.urls import path
from .views import *

urlpatterns = [
    path('', example),
    path('example/', example, name='example'),
    path('topsellers/', top_sellers, name='topsellers'),
    path('profile/', profile, name='profile'),
    path('adv/', adv, name='adv'),
    path('advpost/', advpost, name='advpost'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

]
