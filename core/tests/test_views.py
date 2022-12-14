from django.test import TestCase
from django.test import Client

from django.urls import reverse_lazy


# nesta view basicamente carrega o template e gera o formulário
class IndexViewTestCase(TestCase):
    def setUp(self):
        # lista com os campos do formulário
        self.data = {
            'name': 'Elimar Afonso',
            'email': 'elimar_afonso@hotmail.com',
            'subject': 'Vaga de emprego',
            'message': 'esta é uma mensagem válida'
        }

        self.cliente = Client()

    def test_form_valid(self):
        # um post para a rota 'index' com os dados 'data'
        requestValid = self.cliente.post(reverse_lazy('index'), data=self.data)

        # verificando se o codigo de retorno do post é 302
        self.assertEquals(requestValid.status_code, 302)

    def test_form_invalid(self):
        # criando um formulário inválido
        self.dataInvalid = {
            'name': 'elimar',
            'email': 'esta faltando os outros campos'
        }

        requestInvalid = self.cliente.post(reverse_lazy('index'), data=self.dataInvalid)

        self.assertEquals(requestInvalid.status_code, 200)
