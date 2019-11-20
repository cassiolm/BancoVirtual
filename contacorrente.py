class ContaCorrente:
    def __init__(self, nome, cpf, numConta, senha, saldo=0):
        self.nome= nome
        self.cpf= cpf
        self.numConta=numConta
        self.senha=senha
        self.saldo=0

#     def acessarConta(self):
#         while True:
#             opc=int(input("digite sua conta: "))
#             print(opc)
#             print(self.nunConta)
#             if opc==self.nunConta:
#                 print("Bem-vindo,", self.nome, "!Digite sua senha: ")
#                 opc2=input()
#                 if opc2== self.senha:
#                     print("1.deposito ou 2.saque")
#                     if

#             else:
#                 print("Conta inválida")

#     def deposito(self):
#             deposito=input("Digite o valor: ")
#             self.saldo+=deposito
#             print(self.saldo)

#     def saque(self):
#             saque=input("Digite valor saque: ")
#             self.saldo-=saque
#             print(self.saldo