
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



# 1) O código implementa uma função recursiva para calcular o fatorial de um número. A função fatorial(n) chama a si mesma até atingir o caso base (n == 0 ou n == 1). O tempo de execução do cálculo é medido para avaliar o desempenho. A complexidade assintótica do algoritmo é O(n), pois a função realiza n chamadas recursivas, cada uma executando uma multiplicação. Isso significa que o tempo de execução cresce linearmente com o tamanho da entrada n.
# 2) Os resultados mostram que o tempo de execução cresce linearmente à medida que n aumenta. Isso confirma a complexidade O(n) do algoritmo, pois a função faz exatamente n chamadas recursivas, cada uma realizando uma multiplicação. Para valores muito grandes de n, o algoritmo pode sofrer com estouro de pilha


#3)n	Tempo de execução
  #10 0.00000357
# 100 0.0000167
# 500 0.0008507
#1000 0.0023546
