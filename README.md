# Estruturas de Dados Essenciais em Python

> **SOS Capacita – Programação com IA**
> **Módulo 3 — Estruturas de Dados Essenciais**

> _"Dados são a matéria-prima do software moderno."_

Bem-vindo(a) ao terceiro módulo do curso! Aqui você vai aprender a organizar e manipular conjuntos de dados em Python — uma habilidade fundamental para qualquer pessoa que queira programar, trabalhar com APIs, bancos de dados, ciência de dados ou Inteligência Artificial.

---

## Sumário

1. [Introdução](#1-introdução)
2. [Listas](#2-listas)
3. [Percorrendo listas](#3-percorrendo-listas)
4. [Dicionários](#4-dicionários)
5. [Lista de dicionários](#5-lista-de-dicionários)
6. [Mini-projeto: Sistema de Controle de Alunos](#6-mini-projeto-sistema-de-controle-de-alunos)
7. [Exercícios](#7-exercícios)
8. [Conclusão](#8-conclusão)

---

## 1. Introdução

No **módulo anterior**, você aprendeu os blocos básicos da programação:

- **Variáveis** para guardar valores;
- **Condicionais** (`if`, `else`) para tomar decisões;
- **Laços de repetição** (`for`, `while`) para repetir tarefas;
- **Funções** para organizar o código.

Agora chegou o momento de dar um passo importante: **aprender a organizar muitos dados ao mesmo tempo**.

### Por que estruturas de dados são tão importantes?

Quase todo software moderno **manipula dados**. Pense nos exemplos do dia a dia:

- 🛒 Uma loja online tem **listas de produtos**;
- 📱 Uma rede social tem **listas de amigos** e **postagens**;
- 🏦 Um banco tem **cadastros de clientes** e **transações**;
- 🤖 Modelos de **IA e LLMs** são treinados a partir de gigantescos conjuntos de dados;
- 🌐 **APIs** entregam dados em formatos como JSON;
- 🗄️ **Bancos de dados** guardam tabelas com milhões de registros.

Para trabalhar com tudo isso, precisamos de **estruturas de dados** — formas organizadas de guardar e acessar informações.

Neste módulo, você vai aprender as duas estruturas mais usadas em Python:

- **Listas** → coleções ordenadas de itens;
- **Dicionários** → coleções de pares chave/valor;
- E também a **combinação das duas**, que é base de praticamente todo sistema real.

---

## 2. Listas

Uma **lista** é uma coleção ordenada de elementos. Pense nela como uma "fila de itens" guardados em uma única variável.

### Quando usar listas?

Sempre que você precisar guardar **vários valores do mesmo tipo** ou **vários itens relacionados**:

- Uma lista de alunos;
- Uma lista de notas;
- Uma lista de produtos;
- Uma lista de tarefas a fazer.

### Como criar uma lista

```python
frutas = ["maçã", "banana", "laranja"]
numeros = [10, 20, 30, 40]
vazia = []
```

### Acessando elementos por índice

Em Python, o **primeiro elemento** tem o índice `0`:

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # maçã
print(frutas[1])  # banana
print(frutas[2])  # laranja
```

### Operações comuns

| Operação | Exemplo | O que faz |
|----------|---------|-----------|
| `append` | `frutas.append("uva")` | Adiciona um item ao final |
| `remove` | `frutas.remove("banana")` | Remove o primeiro item igual |
| `len`    | `len(frutas)` | Retorna o tamanho da lista |

### Percorrendo uma lista com `for`

```python
for fruta in frutas:
    print(fruta)
```

📁 **Arquivo de exemplo:** [`exemplos/01_listas.py`](exemplos/01_listas.py)

Para executar:

```bash
python3 exemplos/01_listas.py
```

---

## 3. Percorrendo listas

Saber percorrer uma lista é uma das habilidades mais usadas em programação. Com isso conseguimos:

- **Somar** todos os valores;
- Calcular a **média**;
- Encontrar o **maior** e o **menor** valor;
- **Filtrar** itens segundo uma condição;
- **Transformar** os dados em outras estruturas.

### Acumuladores

Um **acumulador** é uma variável que vai "acumulando" valores enquanto o `for` roda:

```python
notas = [7, 8, 6, 10, 5]

soma = 0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print("Média:", media)
```

### Encontrando o maior e o menor manualmente

```python
notas = [7, 8, 6, 10, 5]

maior = notas[0]
menor = notas[0]

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
```

### Usando funções prontas

O Python já oferece funções que fazem isso de forma direta:

```python
print(sum(notas))   # soma total
print(min(notas))   # menor valor
print(max(notas))   # maior valor
```

> 💡 **Por que aprender o jeito manual também?**
> Porque entender a **lógica por trás** das funções é o que vai permitir você resolver problemas novos no futuro, especialmente em IA e algoritmos.

📁 **Arquivo de exemplo:** [`exemplos/02_percorrendo_listas.py`](exemplos/02_percorrendo_listas.py)

Para executar:

```bash
python3 exemplos/02_percorrendo_listas.py
```

---

## 4. Dicionários

Os **dicionários** guardam dados no formato **chave: valor**. Eles dão **significado** aos dados, diferente das listas que apenas guardam valores em sequência.

### Diferença entre lista e dicionário

```python
# Lista — apenas valores em sequência
aluno_lista = ["Maria", 20, 8.5]

# Dicionário — cada valor tem um nome (chave)
aluno_dict = {
    "nome": "Maria",
    "idade": 20,
    "nota": 8.5
}
```

No dicionário, fica **muito mais claro** o que cada valor representa.

### Acessando valores por chave

```python
print(aluno_dict["nome"])   # Maria
print(aluno_dict["idade"])  # 20
```

### Alterando valores e adicionando novas chaves

```python
aluno_dict["nota"] = 9.0           # altera a nota
aluno_dict["aprovado"] = True      # adiciona nova chave
```

### Percorrendo chaves e valores

```python
for chave, valor in aluno_dict.items():
    print(chave, "->", valor)
```

📁 **Arquivo de exemplo:** [`exemplos/03_dicionarios.py`](exemplos/03_dicionarios.py)

Para executar:

```bash
python3 exemplos/03_dicionarios.py
```

---

## 5. Lista de dicionários

Aqui é onde o conteúdo do módulo **se conecta com o mundo real**. Quase todo sistema real usa **listas de dicionários** para representar conjuntos de registros:

- Uma lista de alunos, onde cada aluno é um dicionário;
- Uma lista de produtos, onde cada produto é um dicionário;
- Uma lista de pedidos, onde cada pedido é um dicionário.

### Exemplo

```python
alunos = [
    {"nome": "Ana",   "idade": 19, "nota": 8.0},
    {"nome": "Bruno", "idade": 21, "nota": 6.5},
    {"nome": "Carla", "idade": 20, "nota": 9.2},
]

for aluno in alunos:
    print(aluno["nome"], "-", aluno["nota"])
```

### Conexão com o mundo real

Esse formato é praticamente idêntico ao que aparece em:

- 📦 **JSON** (formato usado por APIs);
- 🌐 **Respostas de APIs REST**;
- 🗃️ **Tabelas de bancos de dados**;
- 🤖 **Datasets** usados em IA e Machine Learning.

Quando você dominar **listas de dicionários**, já estará trabalhando com a mesma estrutura de dados que sistemas profissionais usam todos os dias.

📁 **Arquivo de exemplo:** [`exemplos/04_lista_de_dicionarios.py`](exemplos/04_lista_de_dicionarios.py)

Para executar:

```bash
python3 exemplos/04_lista_de_dicionarios.py
```

---

## 6. Mini-projeto: Sistema de Controle de Alunos

Para fechar a parte teórica, vamos juntar tudo em um **mini-sistema** real.

### O que o programa faz

- Cadastra alunos em uma **lista de dicionários**;
- Guarda **nome**, **idade** e **nota**;
- Lista todos os alunos;
- Calcula a **média da turma**;
- Mostra os **aprovados**;
- Mostra os **reprovados**.

### Critério

| Nota | Situação |
|------|----------|
| `>= 7` | Aprovado ✅ |
| `< 7`  | Reprovado ❌ |

📁 **Arquivo de exemplo:** [`exemplos/05_mini_sistema_alunos.py`](exemplos/05_mini_sistema_alunos.py)

Para executar:

```bash
python3 exemplos/05_mini_sistema_alunos.py
```

---

## 7. Exercícios

Agora é a sua vez! Os exercícios estão na pasta `exercicios/`. Cada arquivo já tem o **enunciado em comentários** e uma **estrutura inicial** para você completar.

### 🛒 Exercício 1 — Lista de compras

📁 [`exercicios/01_lista_compras.py`](exercicios/01_lista_compras.py)

**Objetivo:** Criar uma lista de compras, adicionar itens, remover um item e exibir a lista final.

### 📊 Exercício 2 — Notas

📁 [`exercicios/02_notas.py`](exercicios/02_notas.py)

**Objetivo:** Criar uma lista de notas e calcular **soma**, **média**, **maior nota** e **menor nota**.

### 👤 Exercício 3 — Cadastro

📁 [`exercicios/03_cadastro.py`](exercicios/03_cadastro.py)

**Objetivo:** Criar um dicionário representando uma pessoa com **nome**, **idade**, **cidade** e **profissão**.

### 📦 Exercício 4 — Relatório de produtos

📁 [`exercicios/04_relatorio.py`](exercicios/04_relatorio.py)

**Objetivo:** Criar uma lista de dicionários representando produtos, cada um com **nome**, **preço** e **quantidade**. Depois calcular o **valor total em estoque**.

### Como executar um exercício

```bash
python3 exercicios/01_lista_compras.py
```

> 💡 **Dica:** tente resolver sem olhar a internet primeiro. Errar faz parte do aprendizado!

---

## 8. Conclusão

Parabéns! 🎉 Você completou o **Módulo 3** e agora entende as estruturas de dados mais importantes da programação.

### O que você aprendeu

- **Listas** organizam coleções de dados em sequência;
- **Dicionários** dão significado aos dados, com pares chave/valor;
- **Listas de dicionários** se aproximam de dados reais usados em sistemas profissionais;
- Como **percorrer**, **somar**, **filtrar** e **calcular** estatísticas de uma coleção.

### O que vem pela frente

Este módulo é a **base** para tudo o que vem depois:

- 📈 **Análise de dados** e estatística;
- 🌐 Consumo de **APIs** e formatos como **JSON**;
- 🗄️ **Bancos de dados** e SQL;
- 🤖 **Inteligência Artificial** e **Machine Learning**;
- 💬 Trabalho com **LLMs** (modelos de linguagem) que recebem e devolvem dados estruturados.

> _"Quem domina dados, domina o software moderno."_

**Bons estudos e até o próximo módulo! 🚀**
