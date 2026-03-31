def calcularNotas(valor):
    for nota in (100, 50, 20, 10):
        quantidade = valor // nota
        valor = valor % nota
        if quantidade > 0:
            print(f"{quantidade} notas de {nota}")

valor = int(input("Digite o valor: "))
calcularNotas(valor)