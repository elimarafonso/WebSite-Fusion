from django import forms
from django.core.mail.message import EmailMessage

# adicionando formularios

# nome , email, assunto e mensagem


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):

        print(f' entrou no send')
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}\n'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='elimar_afonso@hotmail.com',
            to=['elimar_afonso@hotmail.com', ],
            headers={'Reply-To': email}
        )

        mail.send()


