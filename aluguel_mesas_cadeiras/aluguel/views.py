from django.shortcuts import render, redirect
from .forms import MesasForm, CadeirasForm, TransacaoForm, CadastrarMesasCadeirasForm
from .models import Mesas, Cadeiras, Transação

def cadastrar_aluguel(request):
    if request.method == 'POST':
        form_transacao = TransacaoForm(request.POST)
        form_mesas = MesasForm(request.POST)
        form_cadeiras = CadeirasForm(request.POST)
        if form_transacao.is_valid() and form_mesas.is_valid() and form_cadeiras.is_valid():
            transacao = form_transacao.save()
            form_mesas.instance.transacao = transacao
            form_mesas.save()
            form_cadeiras.instance.transacao = transacao
            form_cadeiras.save()
            return redirect('lista_alugueis')
    else:
        form_transacao = TransacaoForm()
        form_mesas = MesasForm()
        form_cadeiras = CadeirasForm()

    return render(request, 'aluguel/cadastrar_aluguel.html', {
        'form_transacao': form_transacao,
        'form_mesas': form_mesas,
        'form_cadeiras': form_cadeiras
    })

def lista_alugueis(request):
    alugueis = Transação.objects.all()
    return render(request, 'aluguel/lista_alugueis.html', {'alugueis': alugueis})

def cadastrar_mesas_cadeiras_disponiveis(request):
    if request.method == 'POST':
        form_mesas_cadeiras = CadastrarMesasCadeirasForm(request.POST)
        if form_mesas_cadeiras.is_valid():
            quantidade_mesas = form_mesas_cadeiras.cleaned_data['quantidade_mesas']
            quantidade_cadeiras = form_mesas_cadeiras.cleaned_data['quantidade_cadeiras']

            Mesas.objects.create(estoque=quantidade_mesas)

            Cadeiras.objects.create(estoque=quantidade_cadeiras)

            return redirect('lista_mesas_cadeiras')

    else:
        form_mesas_cadeiras = CadastrarMesasCadeirasForm()

    return render(request, 'aluguel/cadastrar_mesas_cadeiras_disponiveis.html', {'form_mesas_cadeiras': form_mesas_cadeiras})
