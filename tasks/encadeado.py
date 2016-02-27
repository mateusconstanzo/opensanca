from . import app
from .calculadora import soma, subtracao, divisao, multiplicacao
from celery import chain


def exemplo():

    result = chain(soma.s(4, 4),  # 8
                soma.s(8),  # 8+8
                soma.s(16),  # 16+16
                soma.s(32),  # 32+32
    )()

    print "Resultado do chain"
    print result.get()