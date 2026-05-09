# ============================================================
# Exemplo 02 - Percorrendo Listas
# ============================================================
# Aqui aprendemos a usar o laço for para somar, calcular média,
# encontrar o maior e o menor valor de uma lista.
# Primeiro fazemos tudo "na mão" para entender a lógica.
# Depois usamos as funções prontas do Python.
# ============================================================

# Lista de notas dos alunos
notas = [7, 8, 6, 10, 5]

print("Notas:", notas)

# ------------------------------------------------------------
# 1) Soma manual usando um acumulador
# ------------------------------------------------------------
# Começamos com 0 e vamos somando cada nota
soma = 0
for nota in notas:
    soma = soma + nota

print("Soma das notas (manual):", soma)

# ------------------------------------------------------------
# 2) Cálculo da média
# ------------------------------------------------------------
# A média é a soma dividida pela quantidade de notas
quantidade = len(notas)
media = soma / quantidade

print("Quantidade de notas:", quantidade)
print("Média da turma:", media)

# ------------------------------------------------------------
# 3) Encontrando o maior valor manualmente
# ------------------------------------------------------------
# Começamos supondo que o primeiro é o maior.
# Depois comparamos com cada item da lista.
maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota

print("Maior nota (manual):", maior)

# ------------------------------------------------------------
# 4) Encontrando o menor valor manualmente
# ------------------------------------------------------------
menor = notas[0]
for nota in notas:
    if nota < menor:
        menor = nota

print("Menor nota (manual):", menor)

# ------------------------------------------------------------
# 5) Funções prontas do Python: sum, min e max
# ------------------------------------------------------------
# Agora veja como o Python facilita usando funções prontas:
print("Soma com sum():", sum(notas))
print("Maior com max():", max(notas))
print("Menor com min():", min(notas))

# Média usando sum e len
media_pronta = sum(notas) / len(notas)
print("Média com sum/len:", media_pronta)
