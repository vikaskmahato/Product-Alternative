from django.urls import path
from posts import views

urlpatterns = [
    
    path('mainposts/', views.createpost, name="posts"),
   
    

]