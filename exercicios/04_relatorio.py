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
print("=" * 50)
print("RELATÓRIO DE PRODUTOS")
print("=" * 50)

produtos = [
    {"nome": "Caderno", "preco": 15.0, "quantidade": 10},
    {"nome": "Agenda", "preco": 19.9, "quantidade": 5},
    {"nome": "Caneta", "preco": 4.50, "quantidade":38}
] 


# 2. Crie uma variável "total" iniciando em 0
total = 0


# 3. Percorra a lista de produtos e calcule o subtotal de cada um.
#    Some os subtotais na variável "total".
for produto in produtos:
    print("Produto:", produto["nome"])
    print("Preço: R$", produto["preco"])
    print("Quant.:", produto["quantidade"])
    valor_produto = produto["preco"] * produto["quantidade"]
    print(f"Subtotal: R$ {valor_produto:.2f}")
    print("---------------------")
    
    total += valor_produto


# 4. Exiba o valor total em estoque
print(f"O valor total em estoque é de R$ {total:.2f}")



