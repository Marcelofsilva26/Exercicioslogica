print('Ler um valor e dizer se ele é maior ou menor que 10')
print('-----------------------------------------------------')

numero = float (input('Por favor, digite um numero: '))

if numero > 10:
    print(f'{numero} é maior que 10')
elif numero < 10:
    print(f'{numero} é menor que 10')
else:
    print(f'{numero} é igual 10')
    