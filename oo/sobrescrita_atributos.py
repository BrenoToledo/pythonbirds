"""
Quando eu chamo um atributo  a classe que eu estou trabalhando irá buscar localmente
um atributo em __dict__ da classe que estou trabalhando ( EX : Homem), se não encontrar o atributo
localmente ele ira para a classe PAI caso tenha ( EX: Pessoa ) e assim se repete até a classe
não ter mais nenhuma classe PAI - então ele vai buscar na classe objects que é comum a todas
as classes do python.

"""

from heranca_simples import *

# Os dois herdam de Pessoa
# Pessoa utiliza um valor estatico para os olhos que são comum a todos
# Mas uma pessoa pode ter sofrido um acidente e perdido um olho

breno = Homem(nome='breno')
barbara = Mulher(nome='Barbara')

# Aqui nós mudamos um atributo herdado por barbara:
barbara.olhos = 1



if __name__ == '__main__':

    print('Breno numero de Olhos : ',breno.olhos )
    print('Barbara numero de Olhos : ',barbara.olhos )