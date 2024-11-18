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
from app import views
from app.views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('pais/',PaisView.as_view(),name='pais'),
    path('decada/',DecadaView.as_view(),name='decada'),
    path('empresa/',EmpresaView.as_view(),name='empresa'),
    path('historiainformatica/',HistInfoView.as_view(),name='historiainformatica'),
    path('forum/',ForumView.as_view(),name='forum_list'),
    path('', forum_list, name='forum_list'),
    path('criar/', criar_forum, name='criar_forum'),
    path('<int:forum_id>/comentar/', comentar_forum, name='comentar_forum'),
    path('<int:forum_id>/responder/', responder_forum, name='responder_forum'),
    path('forum/editar/<int:id>/', editar_forum, name='editar_forum'),
    path('comentario/editar/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('resposta/editar/<int:resposta_id>/', views.editar_resposta, name='editar_resposta'),
    path('figuraimportante/',FiguraImportanteView.as_view(),name='figuraimportante'),
    path('forum/apagar/<int:id>/', views.apagar_forum, name='apagar_forum'),
    path('comentario/apagar/<int:id>/', views.apagar_comentario, name='apagar_comentario'),
    path('resposta/apagar/<int:id>/', views.apagar_resposta, name='apagar_resposta'),
    path('contas/', include('contas.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
