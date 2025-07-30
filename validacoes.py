# validacoes.py
import re

def formatar_cpf(cpf_raw):
    """Formata o CPF para o padrão 000.000.000-00, se for apenas dígitos."""
    cpf_digits = re.sub(r'\D', '', cpf_raw)
    if len(cpf_digits) == 11:
        return f"{cpf_digits[0:3]}.{cpf_digits[3:6]}.{cpf_digits[6:9]}-{cpf_digits[9:11]}"
    return cpf_raw

def validar_cpf_formato(cpf_formatado):
    """Valida se o CPF está no formato 000.000.000-00."""
    padrao_cpf_regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(padrao_cpf_regex, cpf_formatado) is not None

def validar_telefone(telefone_raw):
    """Valida e formata o telefone para um padrão comum."""
    telefone_digits = re.sub(r'\D', '', telefone_raw)

    if not (len(telefone_digits) == 10 or len(telefone_digits) == 11):
        print("❌ Telefone deve conter 10 ou 11 dígitos (apenas números).")
        return False, None

    if len(telefone_digits) == 11:
        telefone_formatado = f"({telefone_digits[0:2]}) {telefone_digits[2:7]}-{telefone_digits[7:11]}"
    elif len(telefone_digits) == 10:
        telefone_formatado = f"({telefone_digits[0:2]}) {telefone_digits[2:6]}-{telefone_digits[6:10]}"
    else:
        print("❌ Formato de telefone inválido após processamento.")
        return False, None

    print(f"✅ Telefone validado: {telefone_formatado}")
    return True, telefone_formatado