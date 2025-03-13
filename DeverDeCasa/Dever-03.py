def palindrome(arr):
    # se o array tiver 0 ou 1 elementos, é palíndromo
    if len(arr) <= 1:
        return True
    # Verifica se o primeiro e o último elemento são iguais
    if arr[0] != arr[-1]:
        return False
    # Chama recursivamente a função removendo o primeiro e o último elemento
    return palindrome(arr[1:-1])

# Exemplos
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

# Testando
print(palindrome(array1))  # True
print(palindrome(array2))  # True
print(palindrome(array3))  # True
print(palindrome(array4))  # False