
import time

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

# Captura a entrada do usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Mede o tempo de execução
inicio = time.time()
resultado = fatorial(numero)
fim = time.time()

# Exibe o resultado e o tempo de execução
print(f"{numero}! = {resultado}")
print(f"Tempo de execução: {fim - inicio:.10f} segundos")



