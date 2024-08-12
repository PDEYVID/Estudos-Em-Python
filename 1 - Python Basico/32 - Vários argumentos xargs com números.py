# Fuctions (Funções)
    # Dry - Don´t repeat yourself.

# Criar uma Função que Soma Vários Números


def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num  #soma =0+2=2+3=5+4=9+7=16
    return resultado

x = soma(2,3,4,7)
print(x)


