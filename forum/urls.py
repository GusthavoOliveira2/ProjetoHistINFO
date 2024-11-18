from django.contrib import admin 
from django.urls import include, path 
from django.views.generic import TemplateView 
from app.views import *
from django.urls import path 
from django.urls import path 
from . import views
from app.views import *
from forum.views import *


urlpatterns = [
    path('forum/',ForumView.as_view(),name='forum'),
    path('forum_list/', forum_list, name='forum_list'),
    path('criar/', criar_forum, name='criar_forum'),
    path('<int:forum_id>/comentar/', comentar_forum, name='comentar_forum'),



]