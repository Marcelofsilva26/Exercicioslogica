print('Crie um algoritmo que leia um numero e diga se ele é par ou ímpar')
print('--------------------------------------------------------------------')

numero = int (input('Por favor, digite um numero: '))

if numero % 2 == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é ímpar')