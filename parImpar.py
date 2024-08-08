# Solicita ao usuário que insira um número inteiro
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
