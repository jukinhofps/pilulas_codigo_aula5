def ehPrimo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

valor = int(input("Digite o valor: "))
if ehPrimo(valor):
    print("É primo")
else:
    print("Não é primo")