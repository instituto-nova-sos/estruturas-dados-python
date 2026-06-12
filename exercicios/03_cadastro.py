# ============================================================
# Exercício 03 - Cadastro de Pessoa
# ============================================================
#
# OBJETIVO:
# Criar um dicionário representando uma pessoa, contendo:
#   - nome
#   - idade
#   - cidade
#   - profissão
#
# PASSOS:
#   1. Crie um dicionário chamado "pessoa" com as 4 chaves acima.
#   2. Exiba cada informação separadamente usando print.
#      Exemplo: print("Nome:", pessoa["nome"])
#   3. Altere a idade da pessoa para um novo valor.
#   4. Adicione uma nova chave chamada "email" com um valor.
#   5. Percorra o dicionário com for e mostre chave -> valor.
#
# DICAS:
#   - Dicionários usam pares chave/valor: { "chave": "valor" }
#   - Para percorrer chave e valor, use:
#       for chave, valor in pessoa.items():
# ============================================================


# 1. Crie o dicionário "pessoa" com nome, idade, cidade e profissão
pessoa = {
    "nome": "João da Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "profissão": "Desenvolvedor"
}


# 2. Exiba cada informação
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Profissão:", pessoa["profissão"])


# 3. Altere a idade da pessoa
pessoa["idade"] = 48



# 4. Adicione uma nova chave "email"
pessoa["email"] = "joao.silva@exemplo.com"



# 5. Percorra o dicionário com for e mostre chave -> valor
for chave, valor in pessoa.items():
    print(f"{chave} -> {valor}")

