atendimentos = []

def registrar_atendimento(cliente, problema):
    atendimento = {
        "cliente": cliente,
        "problema": problema,
        "status": "Aberto"
    }
    atendimentos.append(atendimento)
    print("Atendimento registrado com sucesso!")

def listar_atendimentos():
    if not atendimentos:
        print("Nenhum atendimento registrado.")
    else:
        print("\nLista de Atendimentos:")
        for i, atendimento in enumerate(atendimentos):
            print(f"{i} - Cliente: {atendimento['cliente']} | Problema: {atendimento['problema']} | Status: {atendimento['status']}")

def encerrar_atendimento(indice):
    if 0 <= indice < len(atendimentos):
        atendimentos[indice]["status"] = "Encerrado"
        print("Atendimento encerrado com sucesso!")
    else:
        print("Índice inválido.")