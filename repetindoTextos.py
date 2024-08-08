# Solicita ao usuário que insira uma string
texto = input("Digite uma string: ")

# Solicita ao usuário que insira um número inteiro
# O código utiliza um bloco try-except para garantir que a entrada seja um número inteiro válido
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Cria uma lista com a string repetida o número de vezes especificado
# Cada repetição é separada por um espaço
resultado = ' '.join([texto] * numero)

# Exibe o resultado
print("A string repetida é:", resultado)
