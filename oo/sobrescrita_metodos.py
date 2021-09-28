"""
 A nossa classe Pessoa tem um método para comprimentar as pessoas, mas nem todos
 comprimentam as pessoas da mesma forma, quando herdamos em nossa classe homem
 e mulher da nossa classe pessoa, mantemos a mesma forma de comprimentarmos.
"""

from heranca_simples import *

breno = Homem(nome='breno')
barbara = Mulher(nome='Barbara')

if __name__ == '__main__':

    print(breno.cumprimentar())
    print(barbara.cumprimentar())

"""
Podemos substituir esse metodo quando criamos uma classe, veja o exemplo
"""

class Homem_sub(Pessoa):

    def cumprimentar(self):
        return f'Im Breno ! '

breno = Homem_sub(nome='breno')

if __name__ == '__main__':

    print('Exemplo 2')
    print(breno.cumprimentar())
    print(barbara.cumprimentar())

"""
Ou nos podemos executar o metodo pai e unir com o metodo local
"""


class Homem_super(Pessoa):

    def cumprimentar(self):
        cumprimentar_met_pai = super().cumprimentar()
        return f'{cumprimentar_met_pai} Im Breno ! '


breno = Homem_super(nome='breno')

if __name__ == '__main__':
    print('Exemplo 3')
    print(breno.cumprimentar())
    print(barbara.cumprimentar())