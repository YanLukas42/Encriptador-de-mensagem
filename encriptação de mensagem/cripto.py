from cryptography.fernet import Fernet

# Gerar e salvar uma chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    print("Chave gerada e salva em 'chave.key'")

# Carregar a chave existente
def carregar_chave():
    with open("chave.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

# Criptografar mensagem
def criptografar_mensagem(mensagem):
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    return mensagem_criptografada

# Descriptografar mensagem
def descriptografar_mensagem(mensagem_criptografada):
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_descriptografada = fernet.decrypt(mensagem_criptografada)
    return mensagem_descriptografada.decode()

# Menu principal
if __name__ == "__main__":
    print("=== Sistema de Criptografia de Mensagens ===")
    print("1. Gerar chave")
    print("2. Criptografar mensagem")
    print("3. Descriptografar mensagem")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        gerar_chave()
    elif escolha == "2":
        mensagem = input("Digite a mensagem para criptografar: ")
        mensagem_criptografada = criptografar_mensagem(mensagem)
        print(f"Mensagem criptografada: {mensagem_criptografada}")
    elif escolha == "3":
        mensagem_criptografada = input("Digite a mensagem criptografada: ").encode()
        try:
            mensagem_original = descriptografar_mensagem(mensagem_criptografada)
            print(f"Mensagem original: {mensagem_original}")
        except Exception as e:
            print(f"Erro ao descriptografar: {e}")
    else:
        print("Opção inválida!")
