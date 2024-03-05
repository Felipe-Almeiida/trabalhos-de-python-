# programa que calcula o preco de um produto
# a partir de um desconto percentual 

v_compra = float(input('informe o preço do produto: '))
desconto_p = float(input('informe o valor do desconto: '))

desconto_m = v_compra * desconto_p / 100 
preco_final = v_compra - desconto_p 

print(f'Preço do produto: R${v_compra}')
print(f'valor do desconto: {desconto_p}')
print(f'preço com desconto: R${preco_final}')