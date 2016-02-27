from . import app
from .calculadora import soma, subtracao, divisao, multiplicacao

def exemplo():

    # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
    result = soma.chunks(zip(range(10), range(10)), 3).apply_async()

    print "Todas as subtasks concluidas ?"
    print result.ready()

    while result.waiting():

        print "Quantas subtasks concluidas ?"
        print result.successful()
        print result.completed_count()

    print "Resultado do job"
    print result.get()