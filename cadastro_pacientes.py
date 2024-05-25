import tkinter as tk
from tkinter import messagebox

# Função para salvar os dados do paciente!
def salvar_paciente():
    nome = entry_nome.get()
    idade = entry_idade.get()
    endereco = entry_endereco.get()

    if not nome or not idade or not endereco:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        return

    if not idade.isdigit():
        messagebox.showerror("Erro", "Por favor, insira uma idade válida.")
        return

    idade = int(idade)
    paciente_info = f"Nome do Paciente: {nome}, Idade do Paciente: {idade}, Endereço do Paciente: {endereco}"
    listbox_pacientes.insert(tk.END, paciente_info)
    limpar_campos()

# Função para limpar os campos de entrada!
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Função para deletar um paciente selecionado
def deletar_paciente():
    selecionado = listbox_pacientes.curselection()
    if not selecionado:
        messagebox.showerror("Erro", "Nenhum paciente selecionado.")
        return
    listbox_pacientes.delete(selecionado)

# Função para carregar os dados de um paciente selecionado nos campos de entrada
def carregar_paciente():
    selecionado = listbox_pacientes.curselection()
    if not selecionado:
        messagebox.showerror("Erro", "Nenhum paciente selecionado.")
        return
    paciente_info = listbox_pacientes.get(selecionado)
    nome, idade, endereco = paciente_info.split(", ")
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, nome.split(": ")[1])
    entry_idade.delete(0, tk.END)
    entry_idade.insert(0, idade.split(": ")[1])
    entry_endereco.delete(0, tk.END)
    entry_endereco.insert(0, endereco.split(": ")[1])

# Função para atualizar os dados de um paciente selecionado
def atualizar_paciente():
    selecionado = listbox_pacientes.curselection()
    if not selecionado:
        messagebox.showerror("Erro", "Nenhum paciente selecionado.")
        return

    nome = entry_nome.get()
    idade = entry_idade.get()
    endereco = entry_endereco.get()

    if not nome or not idade or not endereco:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        return

    if not idade.isdigit():
        messagebox.showerror("Erro", "Por favor, insira uma idade válida.")
        return

    idade = int(idade)
    paciente_info = f"Nome: {nome}, Idade: {idade}, Endereço: {endereco}"
    listbox_pacientes.delete(selecionado)
    listbox_pacientes.insert(selecionado, paciente_info)
    limpar_campos()

# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Pacientes")

# Criar e posicionar os componentes
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_idade = tk.Label(janela, text="Idade:")
label_idade.grid(row=1, column=0, padx=5, pady=5)

entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

label_endereco = tk.Label(janela, text="Endereço:")
label_endereco.grid(row=2, column=0, padx=5, pady=5)

entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=2, column=1, padx=5, pady=5)

button_salvar = tk.Button(janela, text="Salvar", command=salvar_paciente)
button_salvar.grid(row=3, column=0, padx=5, pady=5)

button_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_paciente)
button_atualizar.grid(row=3, column=1, padx=5, pady=5)

button_deletar = tk.Button(janela, text="Deletar", command=deletar_paciente)
button_deletar.grid(row=4, column=0, padx=5, pady=5)

button_carregar = tk.Button(janela, text="Carregar", command=carregar_paciente)
button_carregar.grid(row=4, column=1, padx=5, pady=5)

listbox_pacientes = tk.Listbox(janela)
listbox_pacientes.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Iniciar o loop principal da interface
janela.mainloop()
