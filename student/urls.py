from django.urls import path
from student import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('index/', views.indexPage, name="index"),
    path('logout/', views.logoutUser, name="logout"),
    path('change_password/', views.change_password, name='change_password'),
    path('excel_2018_2019', views.export_users_xls_2018_2019, name='export_users_xls_2018_2019'),
    path('excel_2019', views.export_users_xls_2019, name='export_users_xls_2019'),
]
