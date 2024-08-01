from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PaisView(View):
    def get(self, request, *args, **kwargs):
        paises= Pais.objects.all()
        return render(request, 'pais.html', {'paises':paises})

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios= Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios':usuarios})

class EmpresaView(View):
    def get(self, request, *args, **kwargs):
        empresas= Empresa.objects.all()
        return render(request, 'empresa.html', {'empresas':empresas})

class HistInfoView(View):
    def get(self, request, *args, **kwargs):
        historiasinfos= HistoriaInformatica.objects.all()
        return render(request, 'historiainformatica.html', {'historiasinfos':historiasinfos})

class DecadaView(View):
    def get(self, request, *args, **kwargs):
        decadas= Decada.objects.all()
        return render(request, 'decada.html', {'decadas':decadas})

class TopicoView(View):
    def get(self, request, *args, **kwargs):
        topicos= Topico.objects.all()
        return render(request, 'topico.html', {'topicos':topicos})

class FiguraImportanteView(View):
    def get(self, request, *args, **kwargs):
        figurasimportantes= FiguraImportante.objects.all()
        return render(request, 'figuraimportante.html', {'figurasimportantes':figurasimportantes})

class ForumView(View):
    def get(self, request, *args, **kwargs):
        foruns= Forum.objects.all()
        return render(request, 'forum.html', {'foruns':foruns})

class QuizView(View):
    def get(self, request, *args, **kwargs):
        quizzes= Quiz.objects.all()
        return render(request, 'quiz.html', {'quizzes':quizzes})

class PesquisaView(View):
    def get(self, request, *args, **kwargs):
        pesquisas= Pesquisa.objects.all()
        return render(request, 'pesquisa.html', {'pesquisas':pesquisas})

class ConfiguracaoView(View):
    def get(self, request, *args, **kwargs):
        configuracoes= Configuracao.objects.all()
        return render(request, 'configuracao.html', {'configuracoes':configuracoes})

class RankingView(View):
    def get(self, request, *args, **kwargs):
        rankings= Ranking.objects.all()
        return render(request, 'ranking.html', {'rankings':rankings})

class ComentarioQuizView(View):
    def get(self, request, *args, **kwargs):
        comentariosforuns= ComentarioForum.objects.all()
        return render(request, 'comentarioforum.html', {'comentariosforuns':comentariosforuns})

class ComentarioForumView(View):
    def get(self, request, *args, **kwargs):
        comentariosquizzes= ComentarioQuiz.objects.all()
        return render(request, 'comentarioquiz.html', {'comentariosquizzes':comentariosquizzes})

class PostagemForumView(View):
    def get(self, request, *args, **kwargs):
        postagensforuns= PostagemForum.objects.all()
        return render(request, 'postagemforum.html', {'postagensforuns':postagensforuns})


















































































