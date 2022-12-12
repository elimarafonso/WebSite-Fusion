import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path


# criando minha classe de teste


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'qualquerNome.png')
        self.assertTrue(len(self.filename), len(arquivo))


class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    # testando a funçao __str__ do model Cargo
    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcinario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcinario), self.funcinario.nome)


class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.nome)


class FeaturesTestCase(TestCase):
    def setUp(self):
        self.features = mommy.make('Features')

    def test_str(self):
        self.assertEquals(str(self.features), self.features.name)


class AcaliacoesTestCase(TestCase):
    def setUp(self):
        self.avaliacoes = mommy.make('Avaliacoes')

    def test_str(self):
        self.assertEquals(str(self.avaliacoes), self.avaliacoes.nome)

