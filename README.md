# investimentos é um projeto feito com Django

Sistema para controle de investimentos.
I -A data de criação de um investimento pode ser hoje ou uma data no passado.
II - Um investimento não deve ser ou se tornar negativo.

Cálculo de ganho -->
```bash
O investimento pagará 0,52% todo mês no mesmo dia da criação do investimento.
```

Tributação -->
```bash
Se tiver menos de um ano, o percentual será de 22,5%.
Se tiver entre um e dois anos, o percentual será de 18,5%.
Se tiver mais de dois anos, o percentual será de 15%.
```

Para rodar na sua maquina siga as instruções:

Criação da virtualenv -->
```bash
virtualenv env
cd \env\Scripts
activate
```

Instalação dos requerimentos/bibliotecas -->
```bash
pip install -r requirements.txt
```

Rodar servidor -->
```bash
python manage.py runserver
```
