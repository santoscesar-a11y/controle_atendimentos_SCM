from atendimentos import registrar_atendimento, listar_atendimentos, encerrar_atendimento

def menu():
    while True:
        print("\n=== SISTEMA DE ATENDIMENTOS ===")
        print("1 - Registrar atendimento")
        print("2 - Listar atendimentos")
        print("3 - Encerrar atendimento")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = input("Nome do cliente: ")
            problema = input("Descrição do problema: ")
            registrar_atendimento(cliente, problema)

        elif opcao == "2":
            listar_atendimentos()

        elif opcao == "3":
            listar_atendimentos()
            indice = int(input("Número do atendimento para encerrar: "))
            encerrar_atendimento(indice)

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()