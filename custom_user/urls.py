from django.urls import path
from data_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
]
