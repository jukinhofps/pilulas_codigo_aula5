def calcularResultado():
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    
    media = (n1 + n2 + n3) / 3
    if media < 6:
        rec = float(input("Digite a nota da recuperação: "))
        media = (media + rec) / 2
        
    return media

m = calcularResultado()
if m >= 6:
    print("Aprovado")
else:
    print("Reprovado")    
    