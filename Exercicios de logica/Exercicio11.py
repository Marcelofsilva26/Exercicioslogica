print('Faça um algoritmo que leia exatamente a idade de uma pessoa e expresse em dias ')
print('-----------------------------------------------------------------------------------')

anos = int (input('Digite sua idade em anos: '))
meses = int (input('Digite sua idade em meses: '))
dias = int (input('Digite o dia que você nasceu: '))

idadedias = (anos * 365) + (meses * 30) + dias

print(f'A sua idade em dias é {idadedias} dias')