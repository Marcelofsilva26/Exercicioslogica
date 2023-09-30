print('Faça um código que recaba 4 numeros e realize a soma deles e a media entre eles e mostre os resultados')
print('-------------------------------------------------------------------------------------------------------')
soma = 0

for i in range(4):
    numeros = float (input('Digite um numero:'))
    soma = soma + numeros

media = soma / 4
print(f'A soma dos quatro numeros foi {soma} e a media deles {media}')


