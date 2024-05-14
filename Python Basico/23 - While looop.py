# == While Loop ==
# Excelente para loops Depedentes de um condição
# Criar uma Promoção para um produto no valor de R$100.


valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f' no dia {dia} o produto vai ser vendido por R${valor}')
    valor -= 5