# -----------------------------
# ----- CADASTRO DE USUÁRIO ---
# -----------------------------

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    # Verifica se já existe usuário com este CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário com esse CPF!")
            return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (rua, número, bairro, cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("✔ Usuário cadastrado com sucesso!")


# -----------------------------
# -------- CRIAR CONTA --------
# -----------------------------

def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    # Busca o usuário
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break

    if usuario is None:
        print("Nenhum usuário encontrado com esse CPF. Cadastre o usuário primeiro.")
        return

    numero_conta = len(contas) + 1

    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "saques_realizados": 0
    })

    print("✔ Conta criada com sucesso!")
    print(f"Agência: {agencia} | Conta: {numero_conta} | Cliente: {usuario['nome']}")


# -----------------------------
# ----------- DEPÓSITO --------
# -----------------------------

def depositar(conta):
    valor = float(input("Valor do depósito: "))

    if valor <= 0:
        print("Valor inválido!")
        return

    conta["saldo"] += valor
    conta["extrato"] += f"Depósito: + R$ {valor:.2f}\n"

    print("✔ Depósito realizado!")


# -----------------------------
# ------------ SAQUE ----------
# -----------------------------

def sacar(*, conta, limite=500, limite_saques=3):
    valor = float(input("Valor do saque: "))

    if valor > conta["saldo"]:
        print("Saldo insuficiente!")
    elif valor > limite:
        print(f"Seu limite de saque é R$ {limite:.2f}!")
    elif conta["saques_realizados"] >= limite_saques:
        print("Você atingiu o limite de saques diários!")
    elif valor <= 0:
        print("Valor inválido!")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: - R$ {valor:.2f}\n"
        conta["saques_realizados"] += 1
        print("✔ Saque realizado!")


# -----------------------------
# ------------ EXTRATO --------
# -----------------------------

def exibir_extrato(conta):
    print("\n========== EXTRATO ==========")
    print(conta["extrato"] if conta["extrato"] else "Nenhuma movimentação.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("==============================\n")


# -----------------------------
# --------- LISTAR CONTAS -----
# -----------------------------

def listar_contas(contas):
    for conta in contas:
        print(f"""
Agência: {conta['agencia']}
Conta: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
        """)


# -----------------------------
# --------- MENU PRINCIPAL ----
# -----------------------------

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


# -----------------------------
# ----------- PROGRAMA --------
# -----------------------------

def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            if not contas:
                print("Nenhuma conta criada!")
                continue

            num = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c["numero_conta"] == num), None)

            if conta:
                depositar(conta)
            else:
                print("Conta não encontrada!")

        elif opcao == "2":
            num = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c["numero_conta"] == num), None)

            if conta:
                sacar(conta)
            else:
                print("Conta não encontrada!")

        elif opcao == "3":
            num = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c["numero_conta"] == num), None)

            if conta:
                exibir_extrato(conta)
            else:
                print("Conta não encontrada!")

        elif opcao == "4":
            criar_conta(AGENCIA, contas, usuarios)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            cadastrar_usuario(usuarios)

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


# Executa o programa

main()
