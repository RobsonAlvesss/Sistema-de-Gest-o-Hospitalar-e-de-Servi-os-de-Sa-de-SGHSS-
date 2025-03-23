# Importa a biblioteca de criptografia
from cryptography.fernet import Fernet

# Função para gerar e salvar a chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Função para carregar a chave armazenada
def carregar_chave():
    try:
        with open("chave.key", "rb") as chave_file:
            return chave_file.read()
    except FileNotFoundError:
        gerar_chave()
        return carregar_chave()

# Carregar ou gerar chave
chave = carregar_chave()

# Criar suíte de criptografia
cipher_suite = Fernet(chave)

# Função para criptografar
def criptografar(texto):
    return cipher_suite.encrypt(texto.encode())

# Função para descriptografar
def descriptografar(texto_criptografado):
    return cipher_suite.decrypt(texto_criptografado).decode()

# Teste do código
try:
    texto = "Dado sensível do SGHSS"
    print(f"Texto original: {texto}")

    # Criptografar
    texto_criptografado = criptografar(texto)
    print(f"Texto criptografado: {texto_criptografado.decode()}")

    # Descriptografar
    texto_descriptografado = descriptografar(texto_criptografado)
    print(f"Texto descriptografado: {texto_descriptografado}")

except Exception as e:
    print(f"Erro durante a criptografia/descriptografia: {e}")
