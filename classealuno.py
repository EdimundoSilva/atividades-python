class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def set_nome(self, nome):
        self.__nome = nome

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def get_nome(self):
        return self.__nome

    def get_nota1(self):
        return self.__nota1

    def get_nota2(self):
        return self.__nota2
    
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2

    def exibir_informacoes(self):
        media = self.calcular_media()
        print(f"Nome do aluno: {self.__nome}")
        print(f"Média das notas: {media:.2f}")


aluno = Aluno("Braga", 8.5, 9.0)
aluno.exibir_informacoes()


aluno.set_nome("Júlia")
aluno.set_nota1(7.0)
aluno.set_nota2(8.5)
aluno.exibir_informacoes()