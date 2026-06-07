def validador_de_numero(mensagem): # 1. O valor entra aqui
    while True:
        # 2. E você usa ele aqui dentro do input
        numero = input(mensagem) 
        try:
            variavel = int(numero)
            # 3. Importante: use o return para mandar o valor para a variável 'idade'
            return variavel 
        except:
            print(f'Você tem "{numero}" de idade? DIGITE UM NÚMERO VÁLIDO NEANDERTAL!')

# Agora sim a frase "Digite sua idade: " vai aparecer na tela!
idade = validador_de_numero("Digite sua idade: ")
print(f"Idade confirmada: {idade}. Obrigado pelo seu tempo!")