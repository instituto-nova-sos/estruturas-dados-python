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
    {"nome": "Caneta", "preco": 2.5, "quantidade": 50},
    {"nome": "Mochila", "preco": 120.0, "quantidade": 5},
    {"nome": "Lápis", "preco": 1.0, "quantidade": 100},
    {"nome": "Borracha", "preco": 0.5, "quantidade": 200},
    {"nome": "Apontador", "preco": 3.0, "quantidade": 30},
    {"nome": "Estojo", "preco": 25.0, "quantidade": 15},
    {"nome": "Régua", "preco": 4.0, "quantidade": 20},
    {"nome": "Marcador", "preco": 5.0, "quantidade": 10},
    {"nome": "Livro de Matemática - Ensino Fundamental", "preco": 50.0, "quantidade": 8},
    {"nome": "Livro de Português - Ensino Fundamental", "preco": 45.0, "quantidade": 12},
    {"nome": "Livro de Ciências - Ensino Fundamental", "preco": 60.0, "quantidade": 6},
    {"nome": "Livro de História - Ensino Fundamental", "preco": 55.0, "quantidade": 10},
    {"nome": "Livro de Geografia - Ensino Fundamental", "preco": 40.0, "quantidade": 9},
    {"nome": "Livro de Inglês - Ensino Fundamental", "preco": 65.0, "quantidade": 7},
    {"nome": "Livro de Espanhol - Ensino Fundamental", "preco": 55.0, "quantidade": 5},
    {"nome": "Livro de Artes - Ensino Fundamental", "preco": 70.0, "quantidade": 4},
    {"nome": "Livro de Física - Ensino Médio", "preco": 30.0, "quantidade": 10},
    {"nome": "Livro de Química - Ensino Médio", "preco": 35.0, "quantidade": 8},
    {"nome": "Livro de Biologia - Ensino Médio", "preco": 40.0, "quantidade": 6},
    {"nome": "Livro de Literatura - Ensino Médio", "preco": 45.0, "quantidade": 12},
    {"nome": "Livro de Filosofia - Ensino Médio", "preco": 50.0, "quantidade": 5},
    {"nome": "Livro de Sociologia - Ensino Médio", "preco": 55.0, "quantidade": 7}
]


# 2. Crie uma variável "total" iniciando em 0
total = 0


# Formata um número no padrão brasileiro: R$1.234,56
def formata_brl(valor):
    return f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# 3. Percorra a lista de produtos e calcule o subtotal de cada um.
#    Some os subtotais na variável "total".
# extra: saida formatada em R$ com 2 casas decimais usanddo notação brasileira
for produto in produtos:
    subtotal = produto["preco"] * produto["quantidade"]
    total += subtotal
    print(f"Produto: {produto['nome']}, Preço: {formata_brl(produto['preco'])}, Quantidade: {produto['quantidade']}, Subtotal: {formata_brl(subtotal)}")


# 4. Exiba o valor total em estoque
print(f"Valor total em estoque: {formata_brl(total)}")
