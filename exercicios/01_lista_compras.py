# ============================================================
# Exercício 01 - Lista de Compras
# ============================================================
#
# OBJETIVO:
# Criar uma lista de compras, adicionar itens, remover um item
# e exibir a lista final.
#
# PASSOS:
#   1. Crie uma lista chamada "compras" com pelo menos 3 itens.
#   2. Adicione mais 2 itens usando append.
#   3. Remova 1 item usando remove.
#   4. Mostre o tamanho final da lista usando len.
#   5. Percorra a lista usando for e exiba todos os itens.
#
# DICAS:
#   - Use aspas para textos: "arroz", "feijão", "leite"
#   - Lembre-se: append adiciona no final, remove tira pelo nome
# ============================================================


# 1. Crie aqui a lista inicial de compras
compras = ["arroz", "feijaõ", "açucar"]


# 2. Adicione mais 2 itens com append
compras.append("macarrão")
compras.append("açúcar")


# 3. Remova 1 item com remove
compras.remove("feijão")


# 4. Mostre o tamanho da lista
print("Tamanho da lista de compras: ", len(compras))


# 5. Percorra a lista e exiba cada item
for item in compras:
    print("- " + item)
