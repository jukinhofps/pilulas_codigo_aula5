def calcularMedia(prod, qual, pont):
    return (prod + qual + pont) / 3

def classificar(media):
    if media >= 8:
        return "Excelente"
    elif media >= 6:
        return "Bom"
    else:
        return "Crítico"
    
    
def avaliarFuncionarios():
    total = 0
    exc = 0
    bom = 0
    crit = 0
    melhorNome = ""
    melhorMedia = -1
    while True:
        nome = input("Digite o nome do funcionário: ")
        if nome == "fim":
            break
        
        prod = float(input("Digite a nota de produção: "))
        qual = float(input("Digite a nota de qualidade: "))
        pont = float(input("Digite a nota de pontualidade: "))
        
        media = calcularMedia(prod, qual, pont)
        categoria = classificar(media)
        print(f"{nome}, Media: {media}, Categoria: {categoria}")
        
        total += 1
        
        if categoria == "Excelente":
            exc += 1
        elif categoria == "Bom":
            bom += 1
        else:
            crit += 1
            
        if media > melhorMedia:
            melhorMedia = media
            melhorNome = nome
            
    if total == 0:
        print("Nada para calcular")
        return
    
    print("-" * 50)
    print("Relatório")
    print("-" * 50)
    print(f"Total de funcionários: {total}")
    print(f"Quantidade de funcionários Excelentes: {exc}")
    print(f"Quantidade de funcionários Bom: {bom}")
    print(f"Quantidade de funcionários Críticos: {crit}")
    print(f"Melhor Funcionário: {melhorNome} - {melhorMedia}")
    
avaliarFuncionarios()