# Função para solicitar uma nota ao usuário e garantir que a entrada seja válida
def solicitar_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:  # Assumindo que a nota deve estar entre 0 e 10
                return nota
            else:
                print("A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Solicita três notas ao usuário
nota1 = solicitar_nota("Digite a primeira nota: ")
nota2 = solicitar_nota("Digite a segunda nota: ")
nota3 = solicitar_nota("Digite a terceira nota: ")

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print(f"A média das três notas é: {media:.2f}")