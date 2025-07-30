# main.py
from cliente import Cliente
from data_manager import salvar_dados, carregar_dados
from operacoes_bancarias import (
    cadastrar_cliente, listar_clientes, fazer_deposito, fazer_saque,
    consultar_cliente, clientes_com_saldo_negativo, total_em_caixa,
    total_de_clientes, consultar_extrato_cliente, realizar_transferencia,
    gerar_relatorio_cliente, buscar_cliente_por_cpf
)

# A lista de clientes é global aqui e será passada para as funções
clientes = []

# Carrega os dados ao iniciar o programa
clientes = carregar_dados()

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar novo cliente")
        print("2 - Listar todos os clientes")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Consultar cliente por CPF")
        print("6 - Clientes com saldo negativo")
        print("7 - Total em caixa")
        print("8 - Total de clientes")
        print("9 - Consultar extrato")
        print("10 - Transferencia entre contas")
        print("11 - Relatorio de clientes")
        print("12 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente(clientes) # Passa a lista de clientes
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            fazer_deposito(clientes)
        elif opcao == "4":
            fazer_saque(clientes)
        elif opcao == "5":
            consultar_cliente(clientes)
        elif opcao == "6":
            clientes_com_saldo_negativo(clientes)
        elif opcao == "7":
            total_em_caixa(clientes)
        elif opcao == "8":
            total_de_clientes(clientes)
        elif opcao == '9':
            consultar_extrato_cliente(clientes)
        elif opcao == "10":
            realizar_transferencia(clientes)
        elif opcao == "11":
            gerar_relatorio_cliente(clientes)
        elif opcao == "12":
            print("Encerrando o sistema. Até logo!")
            salvar_dados(clientes) # Salva os dados antes de sair
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Inicia o menu quando o script é executado
if __name__ == "__main__":
    menu()