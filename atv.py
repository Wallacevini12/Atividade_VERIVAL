def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Programa principal
if __name__ == "__main__":
    while True:
        entrada = input("Digite um número inteiro (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            print("Programa finalizado.")
            break
        
        try:
            numero = int(entrada)
            if is_prime(numero):
                print(f"{numero} é primo!")
            else:
                print(f"{numero} não é primo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")