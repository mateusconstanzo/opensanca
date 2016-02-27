from . import app
from celery import Task


class Soma(Task):

    def run(self, x, y, **kwargs):
        return int(x + y)


class Subtracao(Task):

    def run(self, x, y, **kwargs):
        return int(x - y)


class Divisao(Task):

    def run(self, x, y, **kwargs):
        return int(x / y)


class Multiplicacao(Task):

    def run(self, x, y, **kwargs):
        return int(x * y)
