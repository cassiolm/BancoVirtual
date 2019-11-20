from tkinter import *
from PIL import Image, ImageTk
from criarconta2 import CriarConta
from acessarconta import AcessarConta
from contacorrente import ContaCorrente


class MenuPrincipal:
	def __init__(self, janela):

		self.contas = [ContaCorrente("conta1","123","1111-1", "senha")]

		self.janela = janela
		self.janela.geometry("400x300")
		self.fonte = ("Verdana", "12")

		self.apresentacao()
		self.logo()

		self.frame3 = Frame(self.janela)
		self.frame3.pack()

		menubar = Menu(self.frame3)
		self.janela.config(menu = menubar)

		menuBanco = Menu(menubar)
		menubar.add_cascade(label = "Operações do Banco", menu = menuBanco)
		menuBanco.add_command(label = "Acessar Conta", accelerator = "A", command = self.AcessarConta) #accelerator cria um atalho, aqui é label e não teste
		menuBanco.add_command(label = "Criar conta", accelerator = "C", command = self.criarConta) 


	def apresentacao(self):
		self.frame1 = Frame(self.janela)
		self.frame1["pady"] = 10
		self.frame1.pack()

		self.titulo = Label(self.frame1, text = "Bem vindo ao Virtual Bank!", font = ("Verdana", 20, "bold"))
		#self.titulo["font"] = ("Verdana", 20, "bold")
		self.titulo.pack()

	def logo(self):
		self.frame2 = Frame(self.janela)
		self.frame2.pack()

		self.canvas = Canvas(self.frame2, width = 300, height=300)
		self.canvas.pack()
		self.canvas.create_rectangle(50, 50, 250, 150)
		self.canvas.bind("<Double-Button-1>", self.rotacionaImagem) # 1 significa botao esquerdo do mouse (duas vezes)
		self.imagem = Image.open("virtualbank.jpg")
		self.imageframe = ImageTk.PhotoImage(self.imagem)
		self.minhaLogo = self.canvas.create_image(150,100, image = self.imageframe)

	def rotacionaImagem(self, evento): #bind precisa de self de mais o argumento de evento por sintaxe
		self.imagem = self.imagem.rotate(180) #rotaciona 180 graus
		self.imageframe = ImageTk.PhotoImage(self.imagem) #rele a imagem rotacionada
		self.canvas.itemconfig(self.minhaLogo, image = self.imageframe) #setup no canvas para ler a nova imagem


	def criarConta(self):
		CriarConta(self.janela, self.contas)


	def AcessarConta(self):
		print(self.contas[0].nome)
		AcessarConta(self.janela, self.contas)


janela = Tk()
MenuPrincipal(janela)
janela.mainloop()