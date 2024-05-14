# == while loops == 

# excelente para loops dependentes de uma condição.
# publica um produto com comissão de 10% se for acima de r$20


valor = int(input('Digite o Valor do Produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f' O valor final do seu produtor será de R${valor}')
    break