from django.db import models

# Create your models here.
class Pais(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Pais")
    continente = models.CharField(max_length=100, verbose_name="Nome do Continente")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural="Paises"

class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do usuario")
    perfil = models.CharField(max_length=100, verbose_name="Tipo de Perfil")
    cpf = models.CharField(max_length=100, verbose_name="Cpf")
    telefone = models.CharField(max_length=100, verbose_name="Telefone")
    cidade = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="Nome do pais")
    endereco = models.CharField(max_length=100, verbose_name="Endereco")
    email = models.CharField(max_length=100, verbose_name="Email")
    senha = models.CharField(max_length=8, verbose_name="Senha")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural="usuarios"
class Decada(models.Model):
    decada = models.CharField(max_length=100, verbose_name="Decada")
    def __str__(self):
        return self.decada
    class Meta:
        verbose_name = "Decada"
        verbose_name_plural="Decadas"

class Empresa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da empresa")
    fundador = models.CharField(max_length=100, verbose_name="Nome do Fundador")
    datafund = models.DateField("Data de fundacao da empresa")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="Pais em que foi fundada")
    decada = models.ForeignKey(Decada, on_delete=models.CASCADE, verbose_name="Decada")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural="Empresas"

class FiguraImportante(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Figura")
    datanascimento = models.DateField("Data de nascimento")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Nome da Empresa")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "FiguraImportante"
        verbose_name_plural="FigurasImportantes"

class Topico(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Tópico")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Topico"
        verbose_name_plural="Topicos"

class Pesquisa(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name="Nome do Topico ")
    empresa= models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Nome da Empresa")
    figuraimportante= models.ForeignKey(FiguraImportante, on_delete=models.CASCADE, verbose_name="Nome da figura")
    decada= models.ForeignKey(Decada, on_delete=models.CASCADE, verbose_name="Decada")
    def __str__(self):
        return f'{self.topico},{self.empresa},{self.figuraimportante},{self.decada}'
    class Meta:
        verbose_name = "Pesquisa"
        verbose_name_plural="Pesquisas"

class Forum(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Figura")
    topico= models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name="Topico")
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    datainicio = models.DateField("Data de inicio")
    datatermino = models.DateField("Data de termino")
    def __str__(self):
        return f'{self.nome},{self.topico}'
        
    class Meta:
        verbose_name = "Forum"
        verbose_name_plural="Foruns"

class Quiz(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do quiz")
    pontuacao = models.CharField(max_length=100, verbose_name="pontuacao")
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    topico= models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name="Topico")
    def __str__(self):
        return f'{self.nome},{self.topico}'
    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural="Quizzes"

class Ranking(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name="Topico")
    quiz= models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Quiz")
    # pontuacao= models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="pontuacao")
    def __str__(self):
        return f'{self.usuario},{self.quiz},{self.topico}'
    class Meta:
        verbose_name = "Ranking"
        verbose_name_plural="Rankings"

class Configuracao(models.Model):    
    tamanhofonte = models.CharField(max_length=100, verbose_name="Fonte")
    idioma = models.CharField(max_length=100, verbose_name="Idioma")
    def __str__(self):
        return self.tamanhofonte 
    class Meta:
        verbose_name = "Configuracao"
        verbose_name_plural="Configuracoes"

class ComentarioQuiz(models.Model):
    comentario = models.CharField(max_length=100, verbose_name="Comentario")
    data = models.DateField("Data de postagem")  
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    quiz= models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Quiz")
    def __str__(self):
        return f'{self.usuario},{self.comentario},{self.data},{self.quiz}'
    class Meta:
        verbose_name = "ComentarioQuiz"
        verbose_name_plural="ComentariosQuizzes"

class ComentarioForum(models.Model):
    comentario = models.CharField(max_length=100, verbose_name="Comentario")
    data = models.DateField("Data de postagem")  
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    forum= models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Forum")
    def __str__(self):
        return f'{self.usuario},{self.comentario},{self.data},{self.forum}'
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural="Comentarios"

class HistoriaInformatica(models.Model):
    contexto = models.CharField(max_length=100, verbose_name="Contexto")
    tipotecnologia = models.CharField(max_length=100, verbose_name="Tipo da Tecnologia")
    empresa= models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")
    Topico= models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name="Topico")    
    figuraimportante= models.ForeignKey(FiguraImportante, on_delete=models.CASCADE, verbose_name="FiguraImportante")
    def __str__(self):
        return self.contexto
    class Meta:
        verbose_name = "Historia"
        verbose_name_plural="Historias"

class PostagemForum(models.Model):
    postagem = models.CharField(max_length=100, verbose_name="Nome da Figura")
    data = models.DateField("Data de postagem")  
    forum= models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name="Forum")
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return f'{self.usuario},{self.postagem},{self.data},{self.forum}'  
    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural="Postagens"
























