import os
from time import sleep


def titulo():
    print('-' * 30)
    print('   CALCULADORA   ')
    print('-' * 30)
    print("[+ soma ]\n[- subtração]\n[* Multiplicação]\n[/ Divisão]\n[** Exponenciação]")


def soma(x, y):
    return (x + y)


def subracao(x, y):
    return (x - y)


def multiplicacao(x, y):
    return (x * y)


def divisao(x, y):
    return (x / y)


def exponenciacao(x, y):
    return (x ** y)


while True:
    titulo()
    print("Escolha a operação que deseja realizar:")
    while True:
        opc = str(input(':> '))
        if opc in '+-/**':
            break
        else:
            print('Erro digite o operador correto!!!')
    print('\033[1;93m-\033[m' * 25)
    print('{} Escolhida'.format(opc))
    x = float(input('->:  '))
    y = float(input('->:  '))
    print('\033[1;93m-\033[m' * 25)
    if opc in '+':
        print(f'{x} + {y} =', soma(x, y))
    if opc in '-':
        print(f'{x} - {y} = {subracao(x, y)}')
    if opc in '*':
        print(f'{x} x {y} = {multiplicacao(x, y)}')
    if opc in '/':
        print(f'{x} / {y} = {divisao(x, y)}')
    if opc == '**':
        print(f'{x} ** {y} = {exponenciacao(x, y)}')
    print('\033[1;93m-\033[m' * 25)
    print('Deseja fazer outro calculo :')
    print('[S] ou [N]')
    pergunta = str(input()).upper().strip()[0]
    if pergunta in 'S':
        os.system('cls')
    elif pergunta in 'N':
        print('Finalizando programa...')
        sleep(1)
        print('Volte sempre!!!')
        break
