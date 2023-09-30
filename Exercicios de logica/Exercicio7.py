print('Faça um código que receba o valor da base e da altura de um triangulo e calcule sua area.')
print('--------------------------------------------------------------------------------------------')
base = float (input('Digite o valor da base do triangulo: '))
altura = float (input('Digite o valor da altura do triangulo: '))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    print(f'A area do triangulo é {area}')
else:
    print('Por favor, digite um número positivo!')


