def verificar_palindromo(palavra):
    # Remove espaços e converte a palavra para minúsculas
    palavra = palavra.replace(" ", "").lower()
    
    # Compara a palavra com sua versão invertida
    return palavra == palavra[::-1]

# Solicita ao usuário que insira uma palavra
entrada = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if verificar_palindromo(entrada):
    print(f"A palavra '{entrada}' é um palíndromo.")
else:
    print(f"A palavra '{entrada}' não é um palíndromo.")