def validarSenha(senha):
    if len(senha) < 8:
        return "Senha inválida, mínimo 8 caracteres"
    
    temNumero = False
    temMaiuscula = False
    
    for letra in senha:
        if letra == " ":
            return "Senha inválida, espaços não são permitidos"
        
        if letra >= "0" and letra <= "9":
            temNumero = True
            
        if letra >= "A" and letra <= "Z":
            temMaiuscula = True
            
    if not temNumero:
        return "Senha inválida, mínimo 1 número"
    
    if not temMaiuscula:
        return "Senha inválida, mínimo 1 letra maiúscula"
    
    return "Senha válida"
                

senha = input("Digite sua senha: ")
print(validarSenha(senha))