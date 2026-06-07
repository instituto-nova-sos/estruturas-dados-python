# ============================================================
# Exercício 04 - Relatório de Produtos
# ============================================================
#
# OBJETIVO:
# Criar uma lista de dicionários representando produtos.
# Cada produto deve ter:
#   - nome
#   - preço
#   - quantidade
#
# Depois, calcular o VALOR TOTAL EM ESTOQUE.
#
# Cálculo do valor total:
#   Para cada produto: preço * quantidade
#   Some todos esses valores para obter o total geral.
#
# PASSOS:
#   1. Complete a lista "produtos" com pelo menos 3 dicionários.
#   2. Percorra a lista e calcule o valor total em estoque.
#   3. Exiba cada produto com seu nome, preço, quantidade
#      e o subtotal (preço * quantidade).
#   4. No final, exiba o valor total em estoque.
#
# DICAS:
#   - Para acessar um campo: produto["preco"]
#   - Use uma variável "total" começando em 0 para acumular
# ============================================================


# 1. Estrutura inicial sugerida — adicione mais produtos
produtos = [
    {"nome": "Caderno", "preco": 15.0, "quantidade": 10},
    # adicione mais produtos aqui
    {"nome": "livro", "preco": 50.0, "quantidade": 10},
    {"nome": "lapis", "preco": 2.0, "quantidade": 20},
] 

# 2. Crie uma variável "total" iniciando em 0
total = 0


# 3. Percorra a lista de produtos e calcule o subtotal de cada um.
#    Some os subtotais na variável "total".
print('-----ESTOQUE-----')

for item in produtos:
    nome = item["nome"]
    preco = item["preco"]
    quantidade = item["quantidade"]
    total_em_material = preco * quantidade

    total += total_em_material
# 4. Exiba o valor total em estoque
    print(f"Produto: {nome} | Preço: R${preco:.2f} | Qtd: {quantidade} | Subtotal: R${total_em_material:.2f}")

print("-" * 40)

print(f"VALOR TOTAL EM ESTOQUE: R${total:.2f}")

print("." * 40)