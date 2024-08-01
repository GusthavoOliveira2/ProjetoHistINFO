"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('pais/',PaisView.as_view(),name='pais'),
    path('decada/',DecadaView.as_view(),name='decada'),
    path('empresa/',EmpresaView.as_view(),name='empresa'),
    path('topico/',TopicoView.as_view(),name='topico'),
    path('usuario/',UsuarioView.as_view(),name='usuario'),
    path('historiainformatica/',HistInfoView.as_view(),name='historiainformatica'),
    path('quiz/',QuizView.as_view(),name='quiz'),
    path('forum/',ForumView.as_view(),name='forum'),
    path('ranking/',RankingView.as_view(),name='ranking'),
    path('figuraimportante/',FiguraImportanteView.as_view(),name='figuraimportante'),
    path('configuracao/',ConfiguracaoView.as_view(),name='configuracao'),
    path('postagemforum/',PostagemForumView.as_view(),name='postagemforum'),
    path('comentarioforum/',ComentarioForumView.as_view(),name='comentarioforum'),
    path('comentarioquiz/',ComentarioQuizView.as_view(),name='comentarioquiz'),
    path('pesquisa/',PesquisaView.as_view(),name='pesquisa'),
   
]
