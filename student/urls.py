from django.urls import path
from student import views


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('index/', views.indexPage, name="index"),
    path('logout/', views.logoutUser, name="logout"),
    path(r'^password/$', views.change_password, name='change_password'),
    path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]