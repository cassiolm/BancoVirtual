from tkinter import *
from contacorrente import ContaCorrente

class AcessarConta:
	def __init__(self, janela, contas):
		self.contas = contas
		self.janela = Toplevel(janela) #para criar outra janela acima
		self.fonte = ("Verdana", 12)

		#CAMPO USER
		self.frame1 = Frame(self.janela)
		self.frame1["pady"] = 5
		self.frame1["padx"] = 5
		self.frame1.pack(side = TOP)

		lbUser = Label(self.frame1, text = "CPF", font = self.fonte)
		lbUser.pack(side = LEFT)
		self.txtUser = Entry(self.frame1)
		self.txtUser["font"] = self.fonte
		self.txtUser["width"] = 10
		self.txtUser.pack(side = LEFT)

		#CAMPO SENHA
		self.frame2 = Frame(self.janela)
		self.frame2["pady"] = 5
		self.frame2["padx"] = 5
		self.frame2.pack()

		lbUser = Label(self.frame2, text = "Senha", font = self.fonte)
		lbUser.pack(side = LEFT)
		self.txtSenha = Entry(self.frame2)
		self.txtSenha["font"] = self.fonte
		self.txtSenha["width"] = 10
		self.txtSenha.pack(side = LEFT)

		#COMANDO CRIAR CONTA

		self.frame3 = Frame(self.janela)
		self.frame3["pady"] = 5
		self.frame3["padx"] = 5
		self.frame3.pack()

		lbBotao = Label(self.frame3, font = self.fonte)
		lbBotao.pack()

		btn = Button(self.frame3, text = "Confirmar", background="green", font = self.fonte, command = self.AcessarConta)
		btn.pack()

	def AcessarConta(self):
		naoEncontrada = True
		for conta in self.contas:
			if conta.cpf == self.txtUser.get() and conta.senha == self.txtSenha.get():
				self.frame1.pack_forget()
				self.frame2.pack_forget()
				self.frame3.pack_forget()
				self.verConta(conta)
				naoEncontrada = False
				break
		if naoEncontrada:
			frame = Frame(self.janela)
			frame.pack()
			lbFalha = Label(frame, text= 'Usuario/senha inválidos', fg = 'red')
			lbFalha.pack()

	def verConta(self, conta):
		self.frame4 = Frame(self.janela)
		self.frame4.pack()
		self.frame5 = Frame(self.janela)
		self.frame5.pack()

		lbNome = Label(self.frame4, text = conta.nome)
		lbNome.pack()
		lbConta = Label(self.frame4, text = conta.numConta)
		lbConta.pack()
		self.lbSaldo = Label(self.frame4, text = conta.saldo)
		self.lbSaldo.pack()

		indice = self.contas.index(conta)

		btnMais5 = Button(self.frame5, text = "+5", command = lambda: self.alteraSaldo(5, indice) )
		btnMais5.grid(row = 0, column = 0)
		btnMenos5 = Button(self.frame5, text = "-5", command = lambda: self.alteraSaldo(-5, indice))
		btnMenos5.grid(row = 0, column = 2)

		btnMais10 = Button(self.frame5, text = "+10", command = lambda: self.alteraSaldo(10,indice))
		btnMais10.grid(row = 2, column = 0)
		btnMais10 = Button(self.frame5, text = "-10", command = lambda: self.alteraSaldo(-10, indice))
		btnMais10.grid(row = 2, column = 2)

	def alteraSaldo(self,valor,indice):
		if valor <0:
			diferenca = self.contas[indice].saldo + valor
			if diferenca >=0:
				self.contas[indice].saldo += valor
		else:
			self.contas[indice].saldo+= valor
		self.lbSaldo['text'] = self.contas[indice].saldo
		# print(self.contas[indice].saldo)	
		