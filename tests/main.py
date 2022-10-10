# Para criar o ambiente virtual: python3 -m venv venv
# Para ativar o ambiente virtual: souce venv/bin/activate

from codigo.bytebank import Funcionario

#lucas = Funcionario("Lucas Carvalho", "13/03/2000", 1000)
#print(lucas.idade())

# Teste unitario
#def teste_idade():
 #   funcionario_teste = Funcionario("teste", "13/03/2000", 1111)
  #  print(f"Teste = {funcionario_teste.idade()}")
   # 
    #funcionario_teste1 = Funcionario("teste", "13/03/1999", 1111)
    #print(f"Teste = {funcionario_teste1.idade()}")
  
#teste_idade()

#------------------------------------------------------

ana = Funcionario('Ana', '12/03/1997',100000)
print(ana.calcular_bonus())

# ---------------------------------------------------

# Instalação Pytest: pip3 install pytest==7.1.2
# Lista de todos os pacotes instalados no ambiente virtual: pip freeze 

""" É uma boa prática criarmos um arquivo .txt para reunir as informações de tudo que estamos
instalando, para manter a organização do nosso projeto. Posteriormente, se outra pessoa 
quiser reproduzi-lo, basta consultar esse documento."""
# Criando txt para salvar o que foi instalado na maquina virtual: pip freeze > requeriments.txt
