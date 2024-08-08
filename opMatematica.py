# Função para solicitar um número ao usuário e garantir que a entrada seja válida
def solicitar_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Solicita dois números ao usuário
numero1 = solicitar_numero("Digite o primeiro número: ")
numero2 = solicitar_numero("Digite o segundo número: ")

# Solicita ao usuário que escolha uma operação
print("\nEscolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    operacao = input("Digite o número da operação desejada (1/2/3/4): ")
    if operacao in ['1', '2', '3', '4']:
        break
    print("Escolha inválida. Por favor, insira 1, 2, 3 ou 4.")

# Realiza a operação escolhida
if operacao == '1':
    resultado = numero1 + numero2
    print(f"\nA soma de {numero1} e {numero2} é {resultado}.")
elif operacao == '2':
    resultado = numero1 - numero2
    print(f"\nA subtração de {numero1} e {numero2} é {resultado}.")
elif operacao == '3':
    resultado = numero1 * numero2
    print(f"\nA multiplicação de {numero1} e {numero2} é {resultado}.")
elif operacao == '4':
    # Evita divisão por zero
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"\nA divisão de {numero1} por {numero2} é {resultado}.")
    else:
        print("\nNão é possível dividir por zero.")
