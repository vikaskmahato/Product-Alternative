from django.urls import path
from accounts import views

urlpatterns = [
    
    path('profile/', views.profileupdate, name="profileupdate"),
    path('search/', views.searching, name="search"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('view/', views.viewprofile, name="viewprofile"),
    path('visit/<int:id>/', views.visit, name="visitprofile"),
    path('business/', views.business, name="business"),
    

]