
import time
import random

def quick_sort(arr):
    """
    Implementação do algoritmo Quick Sort.
    """
    if len(arr) <= 1:
        return arr  # Retorna se a lista tiver 1 ou nenhum elemento
    
    pivot = arr[len(arr) // 2]  # Escolhe o elemento do meio como pivô
    left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
    middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
    right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
    
    return quick_sort(left) + middle + quick_sort(right)  # Recursão

def measure_time(n):
    """
    Mede o tempo de execução do Quick Sort para uma lista de tamanho n.
    """
    arr = [random.randint(0, 1000000) for _ in range(n)]  # Gera lista aleatória
    
    start_time = time.time()  # Inicia o cronômetro
    sorted_arr = quick_sort(arr)  # Executa a ordenação
    end_time = time.time()  # Para o cronômetro
    
    return end_time - start_time  # Retorna o tempo decorrido

# Testando para diferentes tamanhos de entrada
test_sizes = [100, 1000, 10000, 100000]
results = {}

for size in test_sizes:
    exec_time = measure_time(size)
    results[size] = exec_time
    print(f"Tempo para ordenar {size} elementos: {exec_time:.6f} segundos")

# Teste
# Tempo para ordenar 100 elementos: 0.000283 segundos
# Tempo para ordenar 1000 elementos: 0.003068 segundos
# Tempo para ordenar 10000 elementos: 0.036175 segundos
# Tempo para ordenar 100000 elementos: 0.455572 segundos
