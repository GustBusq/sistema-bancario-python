# operacoes_bancarias.py
# Importe o que for necessário de outros módulos
from validacoes import formatar_cpf, validar_telefone, validar_cpf_formato
from cliente import Cliente # Para criar novos clientes, se a função cadastrar_cliente estiver aqui
import json
from datetime import datetime
# A lista de clientes será passada ou acessada de forma global (ver main.py)
# Por enquanto, mantemos aqui para exemplificar, mas no main.py ela será global.
# clientes = [] # Não declare aqui se for ser global no main.py

def buscar_cliente_por_cpf(cpf_busca, clientes_list):
    """Busca um cliente na lista pelo CPF."""
    cpf_formatado_busca = formatar_cpf(cpf_busca)
    for cliente in clientes_list:
        if cliente.cpf == cpf_formatado_busca:
            return cliente
    return None

def cadastrar_cliente(clientes_list):
    nome = input("Digite o nome do cliente: ")
    cpf_input = input("Digite o CPF (apenas dígitos ou no formato 000.000.000-00): ").strip()
    cpf_formatado = formatar_cpf(cpf_input)

    if not validar_cpf_formato(cpf_formatado): # Usa a nova função de validação de formato
        print("❌ CPF em formato incorreto. Por favor, verifique.")
        return

    for c in clientes_list:
        if c.cpf == cpf_formatado:
            print("❌ Cliente com esse CPF já está cadastrado.")
            return

    telefone_input = input("Digite o número de telefone: ")
    is_valid_telefone, telefone_final = validar_telefone(telefone_input)

    if not is_valid_telefone:
        return

    novo_cliente = Cliente(nome, cpf_formatado, telefone_final)
    clientes_list.append(novo_cliente)
    print("✅ Cliente cadastrado com sucesso!")

def listar_clientes(clientes_list):
    if not clientes_list:
        print("⚠️ Nenhum cliente cadastrado.")
        return
    for c in clientes_list:
        c.exibir_dados()

def fazer_deposito(clientes_list):
    cpf = input("Informe o CPF do cliente para depósito: ").strip()
    cliente = buscar_cliente_por_cpf(cpf, clientes_list)
    
    if not cliente:
        print("❌ Cliente não encontrado.")
        return
    
    try:
        valor = float(input("Digite o valor a depositar: "))
        cliente.depositar(valor)
    except ValueError:
        print("❌ Valor inválido. Por favor, digite um número.")

def fazer_saque(clientes_list):
    cpf = input("Informe o CPF do cliente para saque: ").strip()
    cliente = buscar_cliente_por_cpf(cpf, clientes_list)
    
    if not cliente:
        print("❌ Cliente não encontrado.")
        return
    
    try:
        valor = float(input("Digite o valor a sacar: "))
        cliente.sacar(valor)
    except ValueError:
        print("❌ Valor inválido. Por favor, digite um número.")

def clientes_com_saldo_negativo(clientes_list):
    print("\n=== Clientes com saldo negativo ===")
    encontrado = False
    for cliente in clientes_list:
        if cliente.saldo < 0:
            cliente.exibir_dados()
            encontrado = True
    if not encontrado:
        print("Nenhum cliente com Saldo negativo.")
            
def consultar_cliente(clientes_list):
    cpf = input("Digite o CPF que deseja consultar: ").strip()
    cliente = buscar_cliente_por_cpf(cpf, clientes_list)
    
    if cliente: 
        cliente.exibir_dados()
    else:
        print("❌ Cliente não encontrado.")

def total_em_caixa(clientes_list):
    total = sum(cliente.saldo for cliente in clientes_list)
    print(f'\n💰 Total de saldo em caixa (soma dos saldos): R$ {total:.2f}')
    
def total_de_clientes(clientes_list):
    print(f"\n👥 Total de clientes cadastrados: {len(clientes_list)}")
    
def consultar_extrato_cliente(clientes_list):
    cpf = input("Digite o CPF do cliente para consultar o extrato: ").strip()
    cliente = buscar_cliente_por_cpf(cpf, clientes_list)
    
    if cliente:
        cliente.exibir_extrato()
    else:
        print("❌ Cliente não encontrado.")

def realizar_transferencia(clientes_list):
    cpf_origem = input("Digite o CPF que deseja debitar o dinheiro: ").strip()
    cpf_destino = input("Digite o CPF que vai ser o destino do dinheiro: ").strip()

    cliente_origem = buscar_cliente_por_cpf(cpf_origem, clientes_list)
    cliente_destino = buscar_cliente_por_cpf(cpf_destino, clientes_list)

    if not cliente_origem:
        print("❌ Cliente de origem não encontrado.")
        return
    if not cliente_destino:
        print("❌ Cliente de destino não encontrado.")
        return

    try:
        valor = float(input("Digite o valor que deseja transferir: "))
    except ValueError:
        print("❌ Valor inválido. Por favor, digite um número.")
        return

    cliente_origem.transferir(cliente_destino, valor)
    
def gerar_relatorio_cliente(clientes_list):
    if not clientes_list:
        print("Nenhum cliente localizado.")
        return
    
    dados = []
    for c in clientes_list:
        dados.append({
            "CPF": c.cpf,
            "Nome": c.nome,
            "Telefone": c.telefone,
            "Saldo": c.saldo,
            "Historico": c.historico         
        })
        
    nome_do_arquivo = f"relatorio_clientes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(nome_do_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        
    print(f"📁 Relatório gerado com sucesso: {nome_do_arquivo}")