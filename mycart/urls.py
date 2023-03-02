from django.urls import path
from .import views

app_name='mycart'
urlpatterns=[

    path('index',views.index),
    path('home',views.home),
    path('face',views.face),
    path('baabtra',views.baabtra,name='baabtraname' ),
    path('about',views.about,name='aboutname'),
    path('contact',views.contact,name='contactname'),
    path('viewpage',views.viewpage,name='toviewpage')

]