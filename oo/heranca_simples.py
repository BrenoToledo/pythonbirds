class Pessoa:

    olhos = 2

    def __init__(self, nome=None, idade=35, *filhos):

        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

class Homem(Pessoa):
    pass

class Mulher(Pessoa):
    pass

if __name__ == '__main__':

    #breno é um homem filho de argemiro, que é uma pessoa:

    breno = Homem(nome='Breno')
    argimiro = Pessoa(breno, nome='argimiro')

    # Verificando se breno é um homem e uma pessoa

    print('Verificando se breno é um homem e uma pessoa : ')
    print('É uma pessoa :',isinstance(breno,Pessoa))
    print('É um homem :',isinstance(breno,Homem))
    print('Podemos ver que breno que é um objeto "homem" que herdou de pessoa responde como pessoa e como homem ')

    # Verificando se argimiro é um homem e uma pessoa

    print('Verificando se argimiro é um homem e uma pessoa : ')
    print('É uma pessoa :',isinstance(argimiro,Pessoa))
    print('É um homem :',isinstance(argimiro,Homem))
    print('Podemos ver que argimiro que é um objeto "pessoa" que é pai de homem não herdou de ninguem ele só responde como pessoa, mas não necessariamente é um obj homem')

