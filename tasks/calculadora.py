from . import app

#  callbacks/errback/expires/hostname
#  default_retry_delay


@app.task(retries=3)
def soma(x, y):
    return int(x + y)


@app.task
def subtracao(x, y):
    return int(x - y)


@app.task
def divisao(x, y):
    return int(x / y)


@app.task
def multiplicacao(x, y):
    return float(x * y)