class Conta_bancária:
    def __init__ (self,num_conta,saldo,nome_titular):
        self.num_conta = num_conta
        self.saldo = saldo
        self.nome_titular = nome_titular

    def depositar (self,valor):
        if valor > 0:
         self.saldo += valor 
         print (f"depósito de {valor} realizado com sucesso!. novo saldo: {self.saldo}")
        else:
         print ("o valor do depósito deve ser maior que zero!!")
     
    def sacar (self,valor):
       if valor > 0:
        if valor <= self.saldo:
         self.saldo -= valor
         print (f"saque de {valor} realizado com sucesso!. novo saldo: {self.saldo}")
        else:
            print ("saldo insuficiente para fazer o depósito!")
       else:
         print ("o valor do depósito deve ser maior que zero!!")
    def mostrar_saldo (self):
       print("mostrar saldo atual:{saldo}")

#uso das classes
conta_dalulu=Conta_bancária("1234567",10000,"luysa beatriz gama")
conta_dalulu.depositar(125)
conta_dalulu.sacar(400)
conta_dalulu.mostrar_saldo()




       

