from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,
                              redirect)
from django.core.paginator import Paginator
from app.forms import InvestimentoForm
from .models import Investimento, Proprietarios


def investimento(request, id):
    investimentos = Investimento.objects.filter(proprietario_id=id).order_by('id')

    investimento_paginator = Paginator(investimentos, 5)
    page_num = request.GET.get('page')
    page = investimento_paginator.get_page(page_num)

    contexto = {
        'page': page,
        'id': id,
    }

    return render(request, 'investimento.html', contexto)


def view_investimento(request, id):
    global imposto
    investimentos = Investimento.objects.get(id=id)

    d1 = investimentos.data_entrada
    d2 = investimentos.data_saida

    valor = investimentos.valor

    dias = abs((d2 - d1).days)

    print(dias)

    if dias < 365:
        imposto = 22.5
    elif 365 < dias < 730:
        imposto = 18.5
    elif dias > 730:
        imposto = 15.0

    impostodecimal = imposto / 100
    quantidade_meses = dias / 30

    rentabilidade = 0.52 / 100

    rendimento = round(valor * (1 + rentabilidade) ** quantidade_meses, 2)  # Calculo juros composto

    lucrobruto = round(rendimento - valor, 2)

    valorimposto = round(lucrobruto * impostodecimal, 2)

    lucroliquido = round(lucrobruto - valorimposto, 2)

    valorfinal = valor + lucroliquido

    contexto = {
        'investimentos': investimentos,
        'id': id,
        'imposto': imposto,
        'rendimento': rendimento,
        'valorfinal': valorfinal,
        'lucroliquido': lucroliquido,
        'lucrobruto': lucrobruto,
        'valorimposto': valorimposto,
    }

    return render(request, 'view_investimento.html', contexto)


def create_investimento(request, id):
    form = InvestimentoForm(request.POST or None, initial={"proprietario_id": id})

    if form.is_valid():
        form.save()
        return redirect('/investimento/' + id)

    context = {
        'form': form
    }

    return render(request, 'create_investimento.html', context)


def update_investimento(request, id):
    obj = get_object_or_404(Investimento, id=id)

    form = InvestimentoForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'create_investimento.html', context)


def delete_investimento(request, id):
    obj = get_object_or_404(Investimento, id=id)
    obj.delete()

    return redirect('/')


def proprietarios(request):
    proprietarios = Proprietarios.objects.all()

    contexto = {
        'proprietarios': proprietarios
    }

    return render(request, 'proprietarios.html', contexto)
