from django.urls import path
from .import views
app_name='gadgets'


urlpatterns=[

    path('gadget',views.gadgets, name='gadgets'),

     path('gadget',views.gadgets, name='baabtra'),

      path('gadget',views.gadgets, name='about'),

       path('gadget',views.gadgets, name='baabtra')



    
 
]