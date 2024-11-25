from tkinter import Tk, Label, Entry, Button, Text, END, filedialog, messagebox
from cryptography.fernet import Fernet

# Função para gerar e salvar chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    messagebox.showinfo("Sucesso", "Chave gerada e salva como 'chave.key'!")

# Função para carregar a chave existente
def carregar_chave():
    try:
        with open("chave.key", "rb") as chave_arquivo:
            return chave_arquivo.read()
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'chave.key' não encontrado. Gere uma chave primeiro.")
        return None

# Função para criptografar
def criptografar():
    chave = carregar_chave()
    if chave:
        fernet = Fernet(chave)
        mensagem = entrada_texto.get("1.0", END).strip()
        if mensagem:
            mensagem_criptografada = fernet.encrypt(mensagem.encode())
            saida_texto.delete("1.0", END)
            saida_texto.insert(END, mensagem_criptografada.decode())
        else:
            messagebox.showwarning("Atenção", "Digite uma mensagem para criptografar!")

# Função para descriptografar
def descriptografar():
    chave = carregar_chave()
    if chave:
        fernet = Fernet(chave)
        mensagem_criptografada = entrada_texto.get("1.0", END).strip()
        if mensagem_criptografada:
            try:
                mensagem_original = fernet.decrypt(mensagem_criptografada.encode()).decode()
                saida_texto.delete("1.0", END)
                saida_texto.insert(END, mensagem_original)
            except Exception:
                messagebox.showerror("Erro", "Mensagem criptografada inválida ou chave incorreta!")
        else:
            messagebox.showwarning("Atenção", "Digite uma mensagem criptografada para descriptografar!")

# Criação da interface
app = Tk()
app.title("Ferramenta de Criptografia")
app.geometry("500x400")

# Botão para gerar chave
botao_gerar_chave = Button(app, text="Gerar Chave", command=gerar_chave)
botao_gerar_chave.pack(pady=10)

# Entrada de texto para mensagem
Label(app, text="Mensagem:").pack()
entrada_texto = Text(app, height=5, width=50)
entrada_texto.pack(pady=5)

# Botões de ação
botao_criptografar = Button(app, text="Criptografar", command=criptografar)
botao_criptografar.pack(pady=5)

botao_descriptografar = Button(app, text="Descriptografar", command=descriptografar)
botao_descriptografar.pack(pady=5)

# Saída de texto para resultado
Label(app, text="Resultado:").pack()
saida_texto = Text(app, height=5, width=50, state="normal")
saida_texto.pack(pady=5)

# Iniciar o loop da interface
app.mainloop()
