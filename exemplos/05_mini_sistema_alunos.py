# ============================================================
# Exemplo 05 - Mini Sistema de Controle de Alunos
# ============================================================
# Este é um mini-projeto que junta tudo o que aprendemos:
# listas, dicionários, laços e condicionais.
#
# O programa:
#   1. Cadastra alunos em uma lista de dicionários
#   2. Lista todos os alunos
#   3. Calcula a média da turma
#   4. Mostra os aprovados (nota >= 7)
#   5. Mostra os reprovados (nota < 7)
# ============================================================

# Criamos a lista vazia de alunos
alunos = []

# ------------------------------------------------------------
# Cadastrando alunos com append
# ------------------------------------------------------------
# Cada aluno é um dicionário com nome, idade e nota
alunos.append({"nome": "Ana",     "idade": 19, "nota": 8.0})
alunos.append({"nome": "Bruno",   "idade": 21, "nota": 6.5})
alunos.append({"nome": "Carla",   "idade": 20, "nota": 9.2})
alunos.append({"nome": "Daniel",  "idade": 22, "nota": 5.5})
alunos.append({"nome": "Eduarda", "idade": 18, "nota": 7.0})

# ------------------------------------------------------------
# 1) Listar todos os alunos
# ------------------------------------------------------------
print("=" * 50)
print("LISTA DE ALUNOS CADASTRADOS")
print("=" * 50)

for aluno in alunos:
    print("Nome:", aluno["nome"], "| Idade:", aluno["idade"], "| Nota:", aluno["nota"])

# ------------------------------------------------------------
# 2) Calcular a média da turma
# ------------------------------------------------------------
soma_notas = 0
for aluno in alunos:
    soma_notas = soma_notas + aluno["nota"]

media_turma = soma_notas / len(alunos)

print("\n" + "=" * 50)
print("MÉDIA DA TURMA")
print("=" * 50)
print("Total de alunos:", len(alunos))
print("Soma das notas:", soma_notas)
print("Média da turma:", media_turma)

# ------------------------------------------------------------
# 3) Separar aprovados e reprovados
# ------------------------------------------------------------
aprovados = []
reprovados = []

for aluno in alunos:
    if aluno["nota"] >= 7:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

# ------------------------------------------------------------
# 4) Relatório final
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("ALUNOS APROVADOS")
print("=" * 50)
for aluno in aprovados:
    print("-", aluno["nome"], "(nota:", aluno["nota"], ")")

print("\n" + "=" * 50)
print("ALUNOS REPROVADOS")
print("=" * 50)
for aluno in reprovados:
    print("-", aluno["nome"], "(nota:", aluno["nota"], ")")

print("\n" + "=" * 50)
print("RESUMO")
print("=" * 50)
print("Aprovados:", len(aprovados))
print("Reprovados:", len(reprovados))
print("Média da turma:", media_turma)
