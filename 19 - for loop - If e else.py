
# Enviar um Email com os Detalhes da Comprar online (Maximo)
# 3 tentantivas para compras confirmas.

compra_confirmada = True
dados_compra = 'Comprar no valor  de R$ 12.50 e ebtraga confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para seu email')
        break
else:
    print('Falha na comprar')

