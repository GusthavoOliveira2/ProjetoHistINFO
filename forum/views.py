# from app.models import Forum, Comentario
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from django.views import View
# from django.contrib.auth.decorators import login_required
# from app.forms import ComentarioForm

# @login_required
# def forum_list(request):
#     foruns = Forum.objects.all()
#     return render(request, 'forum/forum_list.html', {'foruns': foruns})

# @login_required
# def criar_forum(request):
#     if request.method == 'POST':
#         nome = request.POST['nome']
#         topico = request.POST['topico']
#         forum = Forum(nome=nome, topico=topico, usuario=request.user)
#         forum.save()
#         return redirect('forum_list')
#     return render(request, 'forum/criar_forum.html')

# @login_required
# def comentar_forum(request, forum_id):
#     forum = get_object_or_404(Forum, id=forum_id)
#     if request.method == 'POST':
#         form = ComentarioForm(request.POST)
#         if form.is_valid():
#             comentario = form.save(commit=False)
#             comentario.forum = forum
#             comentario.usuario = request.user
#             comentario.save()
#             return redirect('forum_list')
#     else:
#         form = ComentarioForm()
#     return render(request, 'forum/comentar_forum.html', {'form': form, 'forum': forum})
# @login_required
# def criar_forum(request):
#     if request.user.is_staff:
#         if request.method == 'POST':
#             nome = request.POST.get('nome')
#             topico = request.POST.get('topico')
#             forum = Forum(nome=nome, topico=topico, usuario=request.user)
#             forum.save()
#             return redirect('forum_list')
#         return render(request, 'forum/criar_forum.html')
#     else:
#         return redirect('forum_list')
from django.shortcuts import get_object_or_404, redirect # type: ignore
from .models import Forum, Comentario

def apagar_forum(request, id):
    if request.method == 'POST':
        forum = get_object_or_404(Forum, id=id)
        forum.delete()
        return redirect('home')  # Redirecione para a página inicial ou outra página que você desejar

def apagar_comentario(request, id):
    if request.method == 'POST':
        comentario = get_object_or_404(Comentario, id=id)
        comentario.delete()
        return redirect('home')  # Redirecione para a página inicial ou outra página que você desejar