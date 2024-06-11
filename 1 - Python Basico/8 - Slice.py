'''
Slices em Python

Em Python, um slice é uma forma de acessar partes de uma sequência, como uma string, 
lista ou tupla. É uma técnica muito útil para extrair partes específicas de uma sequência sem modificar a original.

A sintaxe básica de um slice é:

python
Copy code
sequencia[início:fim:passo]

início: O índice onde o slice começa (inclusive).
fim: O índice onde o slice termina (exclusivo).
passo (opcional): O tamanho do passo entre os elementos. O padrão é 1.
Aqui estão alguns exemplos de slices:

python
Copy code
texto = "Olá, mundo!"
parte = texto[2:6]  # Resultado: "á, m"
Neste exemplo, texto[2:6] retorna uma parte de texto que começa no índice 2 (incluindo o caractere 'á') e termina no índice 6 (excluindo o caractere 'm').

python
Copy code
numeros = [1, 2, 3, 4, 5]
sublista = numeros[1:4]  # Resultado: [2, 3, 4]
Neste caso, numeros[1:4] retorna uma parte da lista numeros que começa no índice 1 (incluindo o número 2) e termina no índice 4 (excluindo o número 5).

Os slices são uma maneira poderosa e concisa de manipular sequências em Python. Eles são amplamente usados em operações de manipulação de strings e listas.
'''

'''
frutavalor = 'abacate'
#index   0123456

print(fruta[2:6])
'''

valor = 99.75
valor_str = str(valor)  # Converter valor para uma string
# índices:  01234

print(valor_str[3:5])  # Imprimir os caracteres na posição 3 e 4 da string

