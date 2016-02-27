from . import app
from .calculadora import soma, subtracao, divisao, multiplicacao
from celery import group


def exemplo():

    tasks = group([
                soma.s(4, 4),
                soma.s(8, 8),
                soma.s(16, 16),
                soma.s(32, 32),
    ])

    result = tasks.apply_async()

    print "Todas as subtasks concluidas ?"
    print result.ready()

    while result.waiting():

        print "Quantas subtasks concluidas ?"
        print result.successful()
        print result.completed_count()

    print "Resultado do job"
    print result.join()