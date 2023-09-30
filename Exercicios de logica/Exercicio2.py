print('Crie um código que leia um numero diferente de zero e diga se este número é positivo ou negativo')
print('----------------------------------------------------------------------------------------------------')

numero = float (input('Digite um número para saber se ele é positivo ou negativo: '))

if numero > 0:
    print(f'{numero} é postivo')
elif numero < 0:
    print(f'{numero} é negativo')
else:
    print(f'O numero é zero')