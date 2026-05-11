print("=== SISTEMA DE SEGURANÇA === ")

usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("acesso permitido")
    print("bem vindo", usuario)

else:
    print("acesso negado")
    print("opçao invalida")
    print("tente novamente")
    
