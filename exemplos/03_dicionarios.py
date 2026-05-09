# ============================================================
# Exemplo 03 - Dicionários em Python
# ============================================================
# Dicionários guardam dados no formato chave: valor.
# Eles dão SIGNIFICADO a cada informação.
# ============================================================

# Criando um dicionário que representa um aluno
aluno = {
    "nome": "Maria",
    "idade": 20,
    "nota": 8.5
}

print("Dicionário do aluno:", aluno)

# ------------------------------------------------------------
# Acessando valores por chave
# ------------------------------------------------------------
print("Nome do aluno:", aluno["nome"])
print("Idade do aluno:", aluno["idade"])
print("Nota do aluno:", aluno["nota"])

# ------------------------------------------------------------
# Alterando um valor existente
# ------------------------------------------------------------
# A nota da Maria foi corrigida e subiu para 9.0
aluno["nota"] = 9.0
print("Nova nota do aluno:", aluno["nota"])

# ------------------------------------------------------------
# Adicionando uma nova chave ao dicionário
# ------------------------------------------------------------
# Vamos adicionar o campo "aprovado" baseado na nota
if aluno["nota"] >= 7:
    aluno["aprovado"] = True
else:
    aluno["aprovado"] = False

print("Dicionário atualizado:", aluno)

# ------------------------------------------------------------
# Percorrendo apenas as chaves
# ------------------------------------------------------------
print("Chaves do dicionário:")
for chave in aluno.keys():
    print("-", chave)

# ------------------------------------------------------------
# Percorrendo apenas os valores
# ------------------------------------------------------------
print("Valores do dicionário:")
for valor in aluno.values():
    print("-", valor)

# ------------------------------------------------------------
# Percorrendo chaves e valores ao mesmo tempo
# ------------------------------------------------------------
print("Chaves e valores:")
for chave, valor in aluno.items():
    print(chave, "->", valor)
