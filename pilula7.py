def menu():
    while True:
        op = int(input("MENU\n1 - Soma\n2 - Media\n3 - Sair\nOpção: "))
        if op == 3:
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if op == 1:
            print(f"Soma: {num1} + {num2} = {num1 + num2}")
        elif op == 2:
            print(f"Média de {num1} e {num2} = {(num1 + num2) / 2}")
        else:
            print("Opção inválida")
            
            
menu()