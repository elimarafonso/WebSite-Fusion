import uuid
from django.db import models

from stdimage.models import StdImageField
# Create your models here.


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Data Criação', auto_now_add=True)
    modificado = models.DateField('Data Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    biografia = models.TextField('Biografia', max_length=200)
    foto = StdImageField('Foto', upload_to=get_file_path, variations={'thumb': {'width': 300, 'height': 300}})
    facebook = models.CharField('Facebook', max_length=200, default='#')
    twitter = models.CharField('Twitter', max_length=200, default='#')
    instagram = models.CharField('Instagram', max_length=200, default='#')
    linkedin = models.CharField('Linkedin', max_length=200, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome


class Servico(Base):
    ICONE_CHOICES = {
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete')
    }
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)
    nome = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome


class Features(Base):
    ICONE_CHOICES = {
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Pc/Celular'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Multicamada'),
        ('lni-database', 'Banco de dados')
    }
    icon = models.CharField('Icone', max_length=18, choices=ICONE_CHOICES)
    name = models.CharField('Recurso', max_length=50)
    description = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Recurso' # quando vai editar um item específico
        verbose_name_plural = 'Recursos' # Aparece na página ininicial

    def __str__(self):
        return self.name


# avaliações do site (testemunho)
class Avaliacoes(Base):
    ICONE_CHOICES = {
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★')
    }
    nome = models.CharField('Nome', max_length=100)
    profissao = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    comentario = models.TextField('Comentário', max_length=120)
    estrelas = models.IntegerField('Estrelas',  choices=ICONE_CHOICES)
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb': {'width': 75, 'height': 75}})

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return self.nome
