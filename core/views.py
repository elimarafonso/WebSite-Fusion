from django.shortcuts import render
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Features
from .forms import ContactForm
# Create your views here.


class IndexView(FormView):
    # informando qual é o tamplate
    template_name = 'index.html'
    # qual é a classe do formulário
    form_class = ContactForm
    # se o formulário for válido envia a página pro index
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['serviços'] = Servico.objects.order_by('?').all()
        total_recursos = int(Features.objects.count() / 2)
        features = Features.objects.all()
        context['Feature_esquerdo'] = features[:total_recursos]
        context['Feature_direito'] = features[total_recursos:]

        return context

    # caso formuláro válido: envia o email e coloca uma msg de sucesso
    def form_valid(self, form, *args, **kwargs):
        print('Entrou do valid')
        form.send_email()

        messages.success(self.request, 'E-mail enviado com sucesso!!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # caso formuláro INválido: coloca uma msg de erro e retorna o formulário
    def form_invalid(self, form, *args, **kwargs):
        print('Entrou do INvalid')
        print(dir(messages))
        messages.error(self.request, 'Erro ao enviar E-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class Formulario(FormView):
    template_name = 'teste.html'
    form_class = ContactForm
    success_url = 'teste'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
