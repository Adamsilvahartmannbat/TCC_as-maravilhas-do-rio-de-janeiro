
opcao = 0
while opcao != 4:
    print("\n----- menu -----")
    print("1. Adicionar um pedido")
    print("2. Cancelar o pedido")
    print("3. Ver total do pedido")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        valor = float(input("Digite o valor do item: "))
    elif opcao == 2:
        valor = float(input("Digite o valor do item a ser cancelado: "))
    elif opcao == 3:
        pass
    elif opcao == 4:
        print("Encerrando o programa...")
    else:
        print("Opção inválida! Tente novamente.")
print("Obrigado por usar o sistema da Lanchonete!")

