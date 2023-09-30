print('Crie um algoritmo que recebe três números e informe qual o maior entre eles')
print('-----------------------------------------------------------------------------')

n1 = float (input('Digite o primeiro numero: '))
n2 = float (input('Digite o segundo numero: '))
n3 = float (input('Digite o terceiro numero: '))


if n1 > n2 or n1 > n3:
    print(f'{n1} é o maior numero.')
elif n2 > n3:
    print(f'{n2} é o maior numero.')
else:
    print(f'{n3} é o maior numero.')