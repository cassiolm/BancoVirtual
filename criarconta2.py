from tkinter import *
from contacorrente import ContaCorrente

class CriarConta:
	def __init__(self, janela, contas):
		self.contas = contas

		self.janela = Toplevel(janela) #para criar outra janela acima
		self.fonte = ("Verdana", 12)

		#CAMPO NOME
		frame1 = Frame(self.janela)
		frame1["pady"] = 5
		frame1["padx"] = 5
		frame1.pack(side = TOP)

		lbNome = Label(frame1, text = "Nome", font = self.fonte)
		lbNome.pack(side = LEFT)
		self.txtNome = Entry(frame1)
		self.txtNome["font"] = self.fonte
		self.txtNome["width"] = 10
		self.txtNome.pack(side = LEFT)

		#CAMPO CPF

		frame2 = Frame(self.janela)
		frame2["pady"] = 5
		frame2["padx"] = 5
		frame2.pack()

		lbCPF = Label(frame2, text = "CPF", font = self.fonte)
		lbCPF.pack(side = LEFT)
		self.txtCPF = Entry(frame2)
		self.txtCPF["font"] = self.fonte
		self.txtCPF["width"] = 10
		self.txtCPF.pack(side = LEFT)

		#CAMPO SENHA

		frame3 = Frame(self.janela)
		frame3["pady"] = 5
		frame3["padx"] = 5
		frame3.pack()

		lbSenha = Label(frame3, text = "Senha", font = self.fonte)
		lbSenha.pack(side = LEFT)
		self.txtSenha = Entry(frame3)
		self.txtSenha["font"] = self.fonte
		self.txtSenha["width"] = 10
		self.txtSenha.pack(side = LEFT)

		#Numero de Conta

		frame5 = Frame(self.janela)
		frame5["pady"] = 5
		frame5["padx"] = 5
		lbNconta = Label(frame5, text = "N Conta", font = self.fonte)
		lbNconta.pack(side = LEFT)
		self.txtNconta = Entry(frame5)
		self.txtNconta["font"] = self.fonte
		self.txtNconta["width"] = 10
		self.txtNconta.pack(side = LEFT)
		frame5.pack()

		#COMANDO CRIAR CONTA

		frame4 = Frame(self.janela)
		frame4["pady"] = 5
		frame4["padx"] = 5
		frame4.pack()

		lbBotao = Label(frame4, font = self.fonte)
		lbBotao.pack()

		btn = Button(frame4, text = "Criar Conta", background="green", font = self.fonte, command = self.criarConta)
		btn.pack()



	def criarConta(self):
		novaConta = ContaCorrente(self.txtNome.get(), self.txtCPF.get(),self.txtSenha.get(),self.txtNconta.get())
		self.contas.append(novaConta)

		#Conta criada com Sucesso

		frame6 = Frame(self.janela)
		frame6["pady"] = 5
		frame6["padx"] = 5
		lbsucesso = Label(frame6, text = "Conta "+self.txtNconta.get()+"criada com sucesso", font = self.fonte, fg = "green")
		lbsucesso.pack()
		frame6.pack()
