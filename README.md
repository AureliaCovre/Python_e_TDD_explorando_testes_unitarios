
# PROJETO PYTHON E TTD: EXPLORANDO TESTES UNITÁRIOS
Curso de Python focado em testes e em TDD oferecido pela Alura.

* Anotações interessantes sobre o curso que quis guardar: 

Ao longo desse curso, trabalhamos com um projeto que utiliza classes, métodos dentro de classes e instanciação de objetos. 
Esse treinamento é sobre o que são e para que servem os testes, bem como de que se trata a metodologia TDD (Test-driven Development),como utilizar metodologias e boas práticas direcionadas à utilização de testes no desenvolvimento de projetos em Python. 

No início do desenvolvimento, enquanto o projeto ainda está pequeno, é fácil julgar se o código respeita ou não as regras de negócio. Porém, conforme o projeto crescer, a hierarquia do projeto aumentar, existir mais módulos, classes e métodos, e surgir mais regras de negócio, logo cada funcionalidade terá que respeitar inúmeras regras! É neste ponto que entra o processo de testes.

O teste verifica se cada funcionalidade está se comportando como deveria, garantindo um desempenho de maior qualidade dos códigos. O teste manual apresenta algumas desvantagens em relação ao automático. Primeiramente, ele é um processo mais lento e trabalhoso, visto que é uma pessoa quem o realizará. Ela precisa visualizar e interpretar o código, analisar as regras de negócio e elaborar algoritmos que testarão a funcionalidade específica. Por conta desse fator humano, os testes manuais também estão sujeitos a falhas. Por outro lado, um tester é capaz de observar a especificidade de cada projeto em particular. Este é o grande mérito dos testes manuais: uma pessoa encarregada exclusivamente de testes examinará minuciosamente os processos envolvidos no código.

Em contrapartida, o teste automatizado possui várias características interessantes. A primeira vantagem é ser automatizado. Uma vez desenvolvido, é necessário apenas informar o valor que a função receberá e o valor esperado como retorno. O restante do processo é automático, não será preciso alocar tanta atenção a ele.

Além disso, o feedback é rápido. Com a execução dos testes, obtemos rapidamente o retorno com os pontos de melhorias do código.

Outra vantagem é a segurança na alteração do código. Como os testes automatizados definem as regras de negócio que o projeto deve obedecer, há maior segurança ao trabalhar com um código que nunca vimos antes e modificá-lo (fazendo uma migração de um padrão de projeto para outro, por exemplo). Contanto que o novo código continue obedecendo às mesmas regras do código antigo, temos maior liberdade para alterá-lo sem problemas.

Dessa forma, os testes automatizados influenciam a cultura da refatoração (refactoring), incentivando a melhoria contínua de código.

A seguir, vamos comentar sobre os tipos de testes.

Os testes unitários são responsáveis por averiguar o funcionamento de pequenas partes da aplicação (as menores unidades de um código), como um método ou uma classe.

Os testes de integração, como o nome sugere, verificam a integração entre essas unidades menores que compõem o projeto, isto é, os trechos que testamos individualmente nos testes unitários.

Os testes de ponta a ponta (End-to-End — E2E) aferem o bom funcionamento da aplicação inteira, desde o início até o final. Muitas vezes, esse teste simula o usuário da aplicação e o ambiente de produção em que o produto será colocado. Trata-se de um teste mais abrangente, que compreende todo o processo da aplicação.

Esses são os tipos de testes mais relevantes. Teremos mais conteúdos sobre esse tema no decorrer do curso e poderemos tirar dúvidas relacionadas aos tipos de testes. No caso, focaremos nos testes unitários.

-- -------------------------------------------------------------------------------
### FRAMEWORK
Pytest: É um framework especializado em testes;
Vantagens:
    * Ele possui Múltiplos plugins, extensões.
            Temos um pacote de ferramentas inclusas no Pytest para realizar testes dos mais variados tipos e personalizar nossa interação com o código.
    * Altamente escalável.
            Comportando desde aplicações pequenas até projetos maiores, com hierarquias complexas, diversos módulos e muitos diretórios.
    * Utilização simples.     

O Pytest é o framework de testes mais utilizado do mercado de desenvolvimento de software com Python. Ele facilita a construção de testes unitários, sendo altamente escalável e detentor de múltiplas ferramentas para facilitar o uso de metodologias de desenvolvimento de software voltadas a testes.    

Os nomes dos testes devem ser construídos da forma mais verbosa possível.
A escrita verbosa de nomes para teste é um padrão que ultrapassa o próprio Python. Muitas linguagens de programação seguem essa boa prática, que diz que o nome do teste deve explicar da forma mais clara possível para que ele serve.

Uma boa prática na utilização do Pytest é a criação de um módulo específico para testes, ou seja, um diretório denominado tests contendo um arquivo __init__.py.
Esse diretório irá conter todos os arquivos referentes aos testes da aplicação, sendo que a nomenclatura dos arquivos sempre deverá conter o prefixo test_.


Parte da razão pela qual o Pytest é conhecido como framework de testes, não uma simples biblioteca, está no fato do Pytest possuir uma vasta gama de ferramentas direcionadas a melhorar a eficiência e organização dos testes desenvolvidos.

Os markers ou marcadores são uma dessas ferramentas incríveis do Pytest e oferecem não somente uma forma de organizar melhor os testes com tags personalizadas, mas colaboram para definir como determinados testes irão funcionar ou ser executados.

Documentação oficial do do Pytest: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark

-- ---------------------------------------------------------------------------------------------
### METODOLOGIA ÁGIL 
A Given-When-Then é uma metodologia ágil para desenvolvimento de testes. Given pode ser traduzido como "dado" (o verbo "dar" no particípio), no sentido de "Dado determinado contexto...". When significa "quando" e definirá a ação a ser testada. Then significa "então" e indicará o desfecho.

Em resumo: dado determinado contexto, quando uma ação específica ocorrer, então acontecerá certo desfecho. Para elucidar esses conceitos.

    GIVEN — Contexto: entrada da data de nascimento
    WHEN — Ação: chamada do método idade
    THEN — Desfecho: verificação se resultado é igual ao esperado
    
-- ---------------------------------------------------------------------------------------------
### TEST-DRIVEN DEVELOPMENT: 
É uma metodologia para desenvolvimento de software utilizando testes e possui 3 etapas cíclicas: Construção de Testes, Implementação de Código e Refatoração;
