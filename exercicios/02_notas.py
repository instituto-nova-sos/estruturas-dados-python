# ============================================================
# Exercício 02 - Notas
# ============================================================
#
# OBJETIVO:
# Criar uma lista de notas e calcular:
#   - a soma de todas as notas
#   - a média
#   - a maior nota
#   - a menor nota
#
# PASSOS:
#   1. Use a lista de notas já fornecida (ou crie a sua).
#   2. Calcule a soma usando um for e um acumulador.
#   3. Calcule a média (soma / quantidade de notas).
#   4. Encontre a maior nota usando for.
#   5. Encontre a menor nota usando for.
#   6. Exiba todos os resultados com print.
#
# DESAFIO EXTRA:
#   - Depois de fazer "na mão", refaça usando sum(), max() e min().
#
# DICAS:
#   - len(notas) retorna o tamanho da lista
#   - Para o maior/menor, comece supondo que o primeiro é o maior/menor
# ============================================================


# Lista inicial de notas (você pode alterar os valores se quiser)
notas = [7, 8, 6, 10, 5, 9, 4]


# 1. Calcule a soma das notas usando um for
soma_notas = 0
for nota in notas:
    soma_notas += nota


# 2. Calcule a média
media_notas = soma_notas / len(notas)



# 3. Encontre a maior nota
maior = notas[0]  # Suponha que a primeira nota é a maior
for nota in notas:
    if nota > maior:
        maior = nota


# 4. Encontre a menor nota
menor = notas[0]  # Suponha que a primeira nota é a menor
for nota in notas:
    if nota < menor:
        menor = nota


# 5. Exiba os resultados (soma, média, maior e menor)
print("Soma das notas:", soma_notas)
print("Média das notas:", media_notas)
print("Maior nota:", maior)
print("Menor nota:", menor)