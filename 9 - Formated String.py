'''
Uma string formatada em Python é uma maneira conveniente de criar strings que contêm valores de variáveis ou expressões formatadas de uma maneira específica. Isso é feito usando uma sintaxe especial que permite inserir valores de variáveis diretamente na string.

A partir do Python 3.6, você pode usar f-strings (ou strings formatadas) para fazer isso. A sintaxe básica de uma f-string é colocar um "f" antes das aspas que delimitam a string e, em seguida, incluir expressões ou variáveis entre chaves {} dentro da string. Essas expressões ou variáveis serão substituídas pelos seus valores reais quando a string for criada.

Aqui está um exemplo simples de uma f-string:

python
Copy code
nome = "João"
idade = 30
altura = 1.75

frase = f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros."
Neste exemplo, as variáveis nome, idade e altura são substituídas pelos seus valores correspondentes quando a string frase é criada. O resultado será:

arduino
Copy code
'Meu nome é João, tenho 30 anos e minha altura é 1.75 metros.'
As f-strings são uma maneira simples e legível de criar strings formatadas em Python, tornando o código mais fácil de entender e manter. Elas são amplamente utilizadas em operações de formatação de texto em Python.
'''

nome = 'Marcos'
sobrenome = 'Silva'
profisaao = 'Programador'

texto = 'O ' + nome + ' '+ sobrenome + ' E um excelente ' + '[' + profisaao + ']'

texto2 = f' O {nome} {sobrenome} e um Excelente [{profisaao}]'

print(texto)
print(texto2)


# O marcos silva e um excelente Programador 