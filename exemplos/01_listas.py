# ============================================================
# Exemplo 01 - Listas em Python
# ============================================================
# Este arquivo demonstra como criar e manipular listas.
# Listas são coleções ordenadas de itens.
# ============================================================

# Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja"]

# Exibindo a lista completa
print("Lista inicial:", frutas)

# ------------------------------------------------------------
# Acessando elementos por índice
# ------------------------------------------------------------
# O primeiro elemento sempre tem índice 0
print("Primeira fruta:", frutas[0])
print("Segunda fruta:", frutas[1])
print("Terceira fruta:", frutas[2])

# ------------------------------------------------------------
# Adicionando um item ao final da lista com append
# ------------------------------------------------------------
frutas.append("uva")
print("Depois de adicionar uva:", frutas)

# Podemos adicionar mais itens
frutas.append("manga")
print("Depois de adicionar manga:", frutas)

# ------------------------------------------------------------
# Removendo um item com remove
# ------------------------------------------------------------
# O remove apaga a primeira ocorrência do valor informado
frutas.remove("banana")
print("Depois de remover banana:", frutas)

# ------------------------------------------------------------
# Descobrindo o tamanho da lista com len
# ------------------------------------------------------------
tamanho = len(frutas)
print("Quantidade de frutas na lista:", tamanho)

# ------------------------------------------------------------
# Percorrendo a lista com for
# ------------------------------------------------------------
print("Frutas disponíveis:")
for fruta in frutas:
    print("-", fruta)

# ------------------------------------------------------------
# Exibição final
# ------------------------------------------------------------
print("Lista final:", frutas)
