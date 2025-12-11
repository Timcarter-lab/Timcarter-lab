clientes = [] 
contas = []    

def validar_cpf(cpf: str) -> str:
    """Remove caracteres não numéricos e retorna o CPF tratado."""
    return "".join(filter(str.isdigit, cpf))

def encontrar_cliente_por_cpf(cpf: str):
    cpf = validar_cpf(cpf)
    for c in clientes:
        if c["cpf"] == cpf:

            return c
    return None

def encontrar_conta_por_cpf(cpf: str):
    cpf = validar_cpf(cpf)
    for acc in contas:
        if acc["cpf"] == cpf:
            return acc
    return None

def cadastrar_cliente():
    cpf_raw = input("Informe o CPF (somente números ou com pontos/traço): ")
    cpf = validar_cpf(cpf_raw)

    if not cpf:
        print("\nCPF inválido.\n")
        return

    if encontrar_cliente_por_cpf(cpf):
        print("\nJá existe um cliente cadastrado com esse CPF.\n")
        return

    nome = input("Nome completo: ").strip()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Endereço (logradouro, número, bairro, cidade/UF): ").strip()

    novo_cliente = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    clientes.append(novo_cliente)
    print("\nCliente cadastrado com sucesso!\n")

def criar_conta():
    cpf_raw = input("Informe o CPF do titular da conta: ")
    cpf = validar_cpf(cpf_raw)

    cliente = encontrar_cliente_por_cpf(cpf)
    if not cliente:
        print("\nCliente não encontrado. Cadastre o cliente primeiro.\n")
        return

    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero": numero_conta,
        "cpf": cpf,
        "saldo": 0.0,
        "extrato": []
    }
    contas.append(conta)
    print(f"\nConta criada com sucesso! Agência: {conta['agencia']} | Conta: {conta['numero']}\n")


def deposito(conta, valor, /):
    try:
        valor = float(valor)
    except Exception:
        print("\nValor inválido para depósito.\n")
        return

    if valor <= 0:
        print("\nValor inválido. Deve ser maior que 0.\n")
        return

    conta["saldo"] += valor
    conta["extrato"].append(f"Depósito: +R$ {valor:.2f}")
    print("\nDepósito realizado com sucesso!\n")

def saque(*, conta, valor):
    try:
        valor = float(valor)
    except Exception:
        print("\nValor inválido para saque.\n")
        return

    if valor <= 0:
        print("\nValor inválido. Deve ser maior que 0.\n")
        return

    if valor > conta["saldo"]:
        print("\nSaldo insuficiente.\n")
        return

    conta["saldo"] -= valor
    conta["extrato"].append(f"Saque: -R$ {valor:.2f}")
    print("\nSaque realizado com sucesso!\n")

def extrato(conta, /, *, mostrar_saldo=True):
    print("\n========== EXTRATO ==========")
    if conta["extrato"]:
        for mov in conta["extrato"]:
            print(mov)
    else:
        print("Não há movimentações.")

    if mostrar_saldo:
        print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("============================\n")

def solicitar_cpf():
    return validar_cpf(input("Informe o CPF: "))

def buscar_conta_por_cpf_interativo():
    cpf_raw = input("Informe o CPF da conta: ")
    cpf = validar_cpf(cpf_raw)
    acc = encontrar_conta_por_cpf(cpf)
    if not acc:
        print("\nConta não encontrada.\n")
        return None
    return acc

def exibir_menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [7] Sair

    => """
    return input(menu)

def listar_contas():
    if not contas:
        print("\nNenhuma conta cadastrada.\n")
        return
    print("\n===== LISTA DE CONTAS =====")
    for c in contas:
        cliente = encontrar_cliente_por_cpf(c["cpf"])
        nome = cliente["nome"] if cliente else "—"
        print(f"Agência: {c['agencia']} | Conta: {c['numero']} | CPF: {c['cpf']} | Titular: {nome} | Saldo: R$ {c['saldo']:.2f}")
    print("===========================\n")

def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":  
            conta = buscar_conta_por_cpf_interativo()
            if conta:
                valor = input("Valor do depósito: R$ ")
                deposito(conta, valor)  

        elif opcao == "2":  
            conta = buscar_conta_por_cpf_interativo()
            if conta:
                valor = input("Valor do saque: R$ ")
                saque(conta=conta, valor=valor) 

        elif opcao == "3":  
            conta = buscar_conta_por_cpf_interativo()
            if conta:
                resp = input("Mostrar saldo? [S/n] ").strip().lower()
                mostrar = False if resp == "n" else True
                extrato(conta, mostrar_saldo=mostrar)  

        elif opcao == "4":
            criar_conta()

        elif opcao == "5":
            listar_contas()

        elif opcao == "6":
            cadastrar_cliente()

        elif opcao == "7":
            print("Saindo... até mais!")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
