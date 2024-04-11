class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return f"{self.nome} foi aprovadooo!"
        else:
            return f"{self.nome} foi reprovadooo."

notas_luysa = [7.5, 8.0, 6.5, 9.0]
luysa = Estudante("luysa", 17, notas_luysa)
print("Média de", luysa.nome, ":", luysa.calcular_media())
print(luysa.verificar_aprovacao())

notas_raissa = [5.0, 5.5, 4.0, 6.0]
raissa = Estudante("raissa", 17, notas_raissa)
print("Média de",raissa.nome, ":", raissa.calcular_media())
print(raissa.verificar_aprovacao())
