def F(n):
    if n == 1:
        return 2
    return 2 * F(n - 1) + n**2

# Solicita ao usuário um valor para n
n = int(input("Digite um valor para n: "))
resultado = F(n)
print(f"F({n}) = {resultado}")
