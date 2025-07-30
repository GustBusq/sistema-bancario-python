from datetime import datetime # Importa a classe datetime diretamente

class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome.title()
        self.cpf = cpf  # CPF já virá formatado ou será formatado aqui
        self.telefone = telefone
        self.saldo = 0.0
        self.historico = [] # Lista para armazenar o histórico de transações
        
    def registrar_transacao(self, tipo, valor): # Renomeado para o que você usa
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.historico.append(f"{data_hora} - {tipo}: R$ {valor:.2f}") # Formata o valor no histórico
        
    def exibir_dados(self):
        print(f"--- Cliente ---")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("-------------------")
    
    def depositar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido. Depósito deve ser maior que zero.")
            return
        self.saldo += valor
        self.registrar_transacao("Depósito", valor) # Nome correto do método
        print(f"✅ Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("❌ O valor do saque deve ser maior que zero.")
            return
        if valor > self.saldo:
            print(f"❌ Saldo insuficiente. Seu saldo é R${self.saldo:.2f}")
            return
        self.saldo -= valor
        self.registrar_transacao("Saque", valor) # Nome correto do método
        print(f"✅ Saque de R${valor:.2f} realizado com sucesso.")

    def exibir_extrato(self): # Tornando exibir_extrato um método da classe Cliente
        print(f"\n=== Extrato da conta de {self.nome} (CPF: {self.cpf}) ===")
        
        if not self.historico:
            print("Sem histórico de transações.")
        else:
            for registro in self.historico:
                print(registro)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("================================")
        
    def transferir(self, destino_cliente, valor):
        if valor <= 0:
            print("❌ O valor da transferência deve ser maior que zero.")
            return
        if valor > self.saldo:
            print(f"❌ O valor (R${valor:.2f}) é maior que o saldo disponível (R${self.saldo:.2f}).")
            return

        self.saldo -= valor
        destino_cliente.saldo += valor # Adiciona diretamente ao saldo do cliente de destino

        self.registrar_transacao(f"Transferência para {destino_cliente.nome}", valor)
        destino_cliente.registrar_transacao(f"Transferência recebida de {self.nome}", valor)
        print(f"✅ Transferência de R${valor:.2f} realizada com sucesso.")
