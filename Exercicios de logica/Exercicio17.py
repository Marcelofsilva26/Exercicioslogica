print('As maçãs custam R$1,30 cada se forem compradas menos de uma duzia\n'
      'e R$1,00 se forem compradas pelo menos 12. Escreva um codigo que leia e calcule\n'
      'o valor total de maçãs compradas.')
print('-------------------------------------------------------------------------')

quantidadedemaca = int(input("Digite o número de maçãs compradas: "))

if quantidadedemaca < 12:
    custounidade = 1.30
else:
    custounidade = 1.00


total = custounidade * quantidadedemaca


print(f"O custo total da compra é R$ {total:.2f}")
