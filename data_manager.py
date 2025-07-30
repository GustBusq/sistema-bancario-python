# data_manager.py
import json
from cliente import Cliente # Importa a classe Cliente para recriar objetos ao carregar

def salvar_dados(clientes_list): # Renomeie 'clientes' para 'clientes_list' para evitar conflito com a lista global
    dados = []
    for cliente in clientes_list:
        dados.append({
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "telefone": cliente.telefone,
            "saldo": cliente.saldo,
            "historico": cliente.historico
        })

    with open("clientes.json", "w", encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False) # ensure_ascii=False para caracteres especiais
    print("💾 Dados salvos com sucesso.")

def carregar_dados():
    try:
        with open("clientes.json", "r", encoding='utf-8') as f:
            dados = json.load(f)
            clientes_carregados = []
            for d in dados:
                cliente = Cliente(d["nome"], d["cpf"], d["telefone"])
                cliente.saldo = d["saldo"]
                cliente.historico = d["historico"]
                clientes_carregados.append(cliente)
            return clientes_carregados
    except FileNotFoundError:
        print("⚠️ Arquivo 'clientes.json' não encontrado. Iniciando com dados vazios.")
        return []
    except json.JSONDecodeError:
        print("❌ Erro ao ler 'clientes.json'. Arquivo corrompido ou formato inválido. Iniciando com dados vazios.")
        return []
    except Exception as e:
        print(f"❌ Erro inesperado ao carregar dados: {e}. Iniciando com dados vazios.")
        return []