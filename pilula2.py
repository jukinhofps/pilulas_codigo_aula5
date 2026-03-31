def simularCrescimento(pupulacao, taxa, limite):
    anos = 0
    while pupulacao < limite:
        anos += 1
        pupulacao = pupulacao * (1 + taxa)
    return anos

populacao = float(input("Digite a população inicial: "))
taxa = (float(input("Digite a taxa de crescimento: (%) ")) / 100)
limite = float(input("Digite o limite de crescimento: "))

print(f"Anos = {simularCrescimento(populacao, taxa, limite)}")