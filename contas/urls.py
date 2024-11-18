from django.urls import path
from . import views
from app.views import *

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('cadastro/', cadastro, name='cadastro'),
]