print('Bem-vindo a Loja do Ytalo Gabriel') #Mensagem de Boas-Vindas
valorDoPedido = float(input('Qual o valor do pedido: ')) #Solicita o valor total do pedido
quantidadeParcelas = int(input('Qual a quantidade de parcelas: ')) #Solicita a quantidade de parcelas

juros = 0

if quantidadeParcelas < 4 and quantidadeParcelas >= 1:
    juros = 0                    #Até 3 parcelas = Sem juros
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4 / 100              #Entre 4 e 5 parcelas = 4% de juros
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100              #Entre 6 e 8 parcelas = 8% de juros
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16 / 100             #Entre 9 e 12 parcelas = 16% de juros
elif quantidadeParcelas >= 13:
    juros = 32 / 100             #Entre 13 parcelas ou mais = 32% de juros
else:
    print('Valor de parcelas inválida. Digite outro valor. ')   #Se o valor de parcelas for menor que 1 é invalidado

valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas
print(f'O valor das parcelas é de: R${valorDaParcela:.2f}')          #Mostra na tela o valor das parcelas
print(f'O valor Total Parcelado é de:R${valorTotalParcelado:.2f}')  #Mostra na tela o valor total parcelado