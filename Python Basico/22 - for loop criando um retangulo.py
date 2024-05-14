# == for loop mested ==
#outer loop
# inner loop

'''
Criar um retangulo de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()    

'''
Claro! Este é um código Python simples que cria um retângulo de 6x6 usando o caractere '@'. Vou explicar linha por linha:

linhas = 6 e colunas = 6: Essas linhas definem duas variáveis, linhas e colunas, com valores 6 cada. Isso define o tamanho do retângulo que queremos criar.

simbolo = '@': Esta linha define uma variável chamada simbolo e atribui o caractere '@' a ela. Este será o caractere usado para desenhar o retângulo.

for l in range(linhas):: Este é um loop externo que percorre cada linha do retângulo. Ele utiliza a função range() para gerar uma sequência de números de 0 a 5 (porque range(6) vai de 0 a 5), que correspondem aos índices das linhas.

for c in range(colunas):: Dentro do loop externo, há um loop interno que percorre cada coluna dentro de uma linha. Ele também usa a função range() para gerar uma sequência de números de 0 a 5, que correspondem aos índices das colunas.

print(simbolo, end=''): Dentro do loop interno, este comando imprime o caractere armazenado na variável simbolo, sem pular para a próxima linha, devido ao parâmetro end=''. Isso significa que todos os caracteres da mesma linha serão impressos na mesma linha na saída.

print(): Após o loop interno, este comando imprime uma nova linha, o que move o cursor para a próxima linha na saída. Isso garante que cada linha do retângulo esteja em uma nova linha na saída.

Então, quando você executa este código, ele itera sobre as linhas e colunas do retângulo, imprimindo o caractere '@' em cada posição, criando assim um retângulo de 6x6.

O parâmetro `end=''` é usado com a função `print()` em Python e é usado para especificar o que deve ser impresso após os elementos que estão sendo impressos pela função `print()`. Por padrão, o valor de `end` é '\n', que significa que após a impressão de todos os elementos, a função `print()` adicionará uma nova linha (ou seja, moverá o cursor para a próxima linha na saída).

Quando `end=''` é especificado, isso indica que nada deve ser adicionado após os elementos impressos. Em outras palavras, isso faz com que a função `print()` não adicione uma nova linha após a impressão dos elementos, mantendo o cursor na mesma linha.

No código que você forneceu:

```python
print(simbolo, end='')
```

Isso significa que após imprimir o caractere `simbolo`, o cursor não avança para uma nova linha. Em vez disso, a próxima impressão começará na mesma linha que a impressão anterior terminou, resultando em todos os caracteres impressos na mesma linha consecutivamente. Isso é útil para construir o retângulo desejado, garantindo que todos os caracteres de uma linha sejam impressos lado a lado.
'''