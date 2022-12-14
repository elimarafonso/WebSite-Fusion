from django.test import TestCase
from core.forms import ContactForm


class ContactFormTestCase(TestCase):
    def setUp(self):
        self.name = 'Elimar Afonso de Souza'
        self.email = 'elimar_afonso@hotmail.com'
        self.subject = 'Vaga Dev-Junior Python'
        self.message = 'Lorem Ipsum dustrys standardle Ipsum dustrys standardle Ipsum dustrys standardley of t'

        #lista
        self.data = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }

        self.form = ContactForm(data=self.data) # é o mesmo que ContactForm(request.POST)

    def test_send_email(self):
        form1 = ContactForm(data=self.data)
        form1.is_valid()
        resposta1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        resposta2 = form2.send_email()

        self.assertEquals(resposta1, resposta2)
