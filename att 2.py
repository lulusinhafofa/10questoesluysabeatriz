class Animal:
    def __init__ (self,nome,idade,espécie):
        self.nome = nome
        self.idade = idade
        self.espécie = espécie
        
    def emitir_som (self):
        pass
    def informações (self):
       return f"Nome: {self.nome}, Idade: {self.idade}, Espécie: {self.espécie}"
    
class Cachorro(Animal):
    def emitir_som (self):
      return "au-au!"
    
class Cachorro(Animal):
    def emitir_som (self):
      return "miau!"
    
o_cachorro = Animal("dora","2","vira-lata")
o_gato = Animal("nino","5 meses","perturbado")

print(o_cachorro.emitir_som())
print(o_cachorro.informações())
print(o_gato.emitir_som())
print(o_gato.informações())





    
    