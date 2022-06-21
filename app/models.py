from django.db import models
import datetime
from django.core.exceptions import ValidationError


class Proprietarios(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.CharField('Email', max_length=100)
    context_object_name = 'proprietarios'


def validate_date(date):
    if date > datetime.date.today():
        raise ValidationError("Data não pode ser maior que hoje!")


class Investimento(models.Model):
    nome = models.CharField('Nome', max_length=100)
    valor = models.PositiveIntegerField('Valor Investido')
    data_entrada = models.DateField('Data de Entrada', default=datetime.date.today, null=True, blank=True,
                                    validators=[validate_date])
    data_saida = models.DateField('Data de Saida', default=datetime.date.today, null=True, blank=True,
                                  validators=[validate_date])
    proprietario_id = models.IntegerField('Proprietario ID')
    context_object_name = 'investimento'
