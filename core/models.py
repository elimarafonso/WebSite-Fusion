from django.db import models
from stdimage.models import StdImageField
# Create your models here.


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
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb': {'width': 300, 'height': 300}})
    facebook = models.CharField('Facebook', max_length=200, default='#')
    twitter = models.CharField('twitter', max_length=200, default='#')
    instagram = models.CharField('instagram', max_length=200, default='#')

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
