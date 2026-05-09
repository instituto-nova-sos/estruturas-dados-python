# ============================================================
# Exemplo 04 - Lista de Dicionários
# ============================================================
# Uma lista pode guardar vários dicionários.
# Esse formato é muito parecido com dados reais usados em
# APIs, JSON e bancos de dados.
# ============================================================

# Lista com vários alunos, onde cada aluno é um dicionário
alunos = [
    {"nome": "Ana",   "idade": 19, "nota": 8.0},
    {"nome": "Bruno", "idade": 21, "nota": 6.5},
    {"nome": "Carla", "idade": 20, "nota": 9.2},
]

# ------------------------------------------------------------
# Mostrando todos os alunos
# ------------------------------------------------------------
print("Lista completa de alunos:")
for aluno in alunos:
    print(aluno)

# ------------------------------------------------------------
# Mostrando apenas o nome e a nota de cada aluno
# ------------------------------------------------------------
print("\nNome e nota de cada aluno:")
for aluno in alunos:
    print(aluno["nome"], "-", aluno["nota"])

# ------------------------------------------------------------
# Verificando aprovação (nota >= 7)
# ------------------------------------------------------------
print("\nSituação de cada aluno:")
for aluno in alunos:
    if aluno["nota"] >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(aluno["nome"], "->", situacao)

# ------------------------------------------------------------
# Observação importante:
# ------------------------------------------------------------
# Esse formato (lista de dicionários) é praticamente igual ao
# que você vai encontrar em:
#   - Respostas de APIs (JSON)
#   - Tabelas de bancos de dados
#   - Datasets usados em IA e Machine Learning
# ------------------------------------------------------------
