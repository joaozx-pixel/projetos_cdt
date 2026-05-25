print("=== SISTEMA DE SEGURANÇA === ")

usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto and senha == senha_correta:

    print("acesso permitido")
    print("bem vindo", usuario)

    print("sistema liberado")
    print("carregando...")
    print("\n=== SISTEMA DO SISTEMA ===")
    print("1 - Ver status ")
    print("2 - Abrir  painel")
    print("3 - Encerrar")

    opcao = input(" Ecolha uma opção")

if opcao == "1":
    
    print("Sistema protegido")
    print("Nenhuma ameaça detectada")

elif opcao == "2":

    print("PAinel aberto")
    print("Carregando informações....")

elif == "3":

    print("Sistema encerrado")
    print("Voltando ao menu")




else:
    print("acesso negado")
    print("opçao invalida")
    print("tente novamente")

    print("usuario bloqueado")
    print("voltando ao menu")

    
