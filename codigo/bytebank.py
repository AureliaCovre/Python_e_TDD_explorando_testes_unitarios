from datetime import date #A biblioteca datetime esta sendo utilizada para receber o ano atual

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    """O método idade captura a data de nascimento do funcionário e calcula a idade dele 
    a partir do ano atual."""
    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)


    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]   

    """ Método que identifique quem são os diretores da empresa pelo sobrenome."""
    def _eh_socio(self):   
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)

    """ Método que identifica quais diretores recebem salário igual ou superior a R$100000,00 e faz um decréscimo 
    equivalente a 10% deste valor """
    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo     

    """ Método que calcula o bônus para quem ganha até R$1000, o Exception foi inserido para 
    apresentar a mensagem caso o salario seja acima dos mil. """
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber bônus')
        return valor

    """ Função que retorna as informações completas do objeto."""
    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'

