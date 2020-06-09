from django.urls import path
from student import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('index/', views.indexPage, name="index"),
    path('logout/', views.logoutUser, name="logout"),
]