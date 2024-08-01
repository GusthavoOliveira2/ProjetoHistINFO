# Generated by Django 5.0.7 on 2024-07-29 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanhofonte', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('idioma', models.CharField(max_length=100, verbose_name='Nome da Figura')),
            ],
            options={
                'verbose_name': 'Configuracao',
                'verbose_name_plural': 'Configuracoes',
            },
        ),
        migrations.CreateModel(
            name='Decada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decada', models.CharField(max_length=100, verbose_name='Nome do Pais')),
            ],
            options={
                'verbose_name': 'Decada',
                'verbose_name_plural': 'Decadas',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Pais')),
                ('continente', models.CharField(max_length=100, verbose_name='Nome do Continente')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Tópico')),
            ],
            options={
                'verbose_name': 'Topico',
                'verbose_name_plural': 'Topicos',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Pais')),
                ('fundador', models.CharField(max_length=100, verbose_name='Nome do Pais')),
                ('datafund', models.DateField(verbose_name='Data de fundacao da empresa')),
                ('decada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.decada', verbose_name='Nome do pais')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais', verbose_name='Nome do pais')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='FiguraImportante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('datanascimento', models.DateField(verbose_name='Data de nascimento')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa', verbose_name='Nome da Empresa')),
            ],
            options={
                'verbose_name': 'FiguraImportante',
                'verbose_name_plural': 'FigurasImportantes',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('pontuacao', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico', verbose_name='Topico')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.decada', verbose_name='Decada')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa', verbose_name='Nome da Empresa')),
                ('figuraimportante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.figuraimportante', verbose_name='Nome da figura')),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico', verbose_name='Nome do Topico ')),
            ],
            options={
                'verbose_name': 'Pesquisa',
                'verbose_name_plural': 'Pesquisas',
            },
        ),
        migrations.CreateModel(
            name='HistoriaInformatica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contexto', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('tipotecnologia', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa', verbose_name='Empresa')),
                ('figuraimportante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.figuraimportante', verbose_name='FiguraImportante')),
                ('Topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico', verbose_name='Topico')),
            ],
            options={
                'verbose_name': 'Historia',
                'verbose_name_plural': 'Historias',
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('datainicio', models.DateField(verbose_name='Data de inicio')),
                ('datatermino', models.DateField(verbose_name='Data de termino')),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico', verbose_name='Topico')),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Foruns',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Pais')),
                ('perfil', models.CharField(max_length=100, verbose_name='Tipo de Perfil')),
                ('cpf', models.CharField(max_length=100, verbose_name='Cpf')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('cidade', models.CharField(max_length=100, verbose_name='Nome da Cidade')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereco')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('senha', models.CharField(max_length=8, verbose_name='Senha')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais', verbose_name='Nome do pais')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz', verbose_name='Quiz')),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico', verbose_name='Topico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Ranking',
                'verbose_name_plural': 'Rankings',
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario'),
        ),
        migrations.CreateModel(
            name='PostagemForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postagem', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('data', models.DateField(verbose_name='Data de postagem')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.forum', verbose_name='Forum')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
            },
        ),
        migrations.AddField(
            model_name='forum',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario'),
        ),
        migrations.CreateModel(
            name='ComentarioQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('data', models.DateField(verbose_name='Data de postagem')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz', verbose_name='Quiz')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'ComentarioQuiz',
                'verbose_name_plural': 'ComentariosQuizzes',
            },
        ),
        migrations.CreateModel(
            name='ComentarioForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=100, verbose_name='Nome da Figura')),
                ('data', models.DateField(verbose_name='Data de postagem')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.forum', verbose_name='Forum')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
