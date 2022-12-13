# Documento de Arquitetura de Software

## Histórico de revisão

| Data       | Versão | Descrição| Autor(es)|
| :----------: | :------: | :------: | :------: |
| 09/12/2022 | 0.1    | Abertura do documento de Arquitetura | [Pedro](https://github.com/pedrobarbosaocb) e [ Vera ](https://github.com/verabelucia)



# Sumário

   O documento de arquitetura está organizado em informações da seguinte maneira:
   
   1. [Finalidade](#Finalidade)
   2. [Escopo](#Escopo)
   4. [Representação da arquitetura](#Representação)
   6. [Diagrama de Classes](#Classes)
   7. [Diagrama de Pacotes](#Pacotes)

<div id='Finalidade'/>

# Finalidade

   - QuantiFGA tem como intuito ser uma ferramenta para ajudar a cordenação da FGA em relação a distribuição de alunos as disciplinas, podendo por meio do QuantiFGA observar as salas com maior porcentagem de vagas e cadeiras vazias, de acordo com o horário e sala. Ademais, o software contém uma ferramenta de simulação da alteração das quantidades da disciplina escolhida.

<div id='Escopo'/>

# Escopo
- Já imaginou um software com a funcionalidade de mostrar as salas cadastradas no SIGAA e mostrar os dados da sua taxa de ocupação, professor da turma, quantidade de alunos cadastrados na matéria e o horário e por essas informações e colocar em um gráfico? O software proposto é uma página web que possui um robozinho que pega essas informações no portal do SIGAA e gera um gráfico para facilitar a coordenação na análise de locação de turmas no semestre.

<div id='Representação'/>

# Representação da arquitetura

![Reperesentação da arquitetura](https://github.com/pedrobarbosaocb/RepositorioTeste/blob/main/Arquitetura3.png)



## Front-end
### Flask
 - o Flask é um micro-framework destinado principalmente a pequenas aplicações com requisitos mais simples, como por exemplo, a criação de um site básico. Possuir apenas o necessário para o desenvolvimento de uma aplicação,os projetos escritos em Flask tendem a ser menores e mais leves se comparados a frameworks maiores.

## Back-end

### Mongodb 
- O MongoDB é um banco de dados orientado a documentos que possui código aberto (open source) e foi projetado para armazenar uma grande escala de dados, além de permitir que se trabalhe de forma eficiente com grandes volumes.

### Metabase
- A ferramenta de business intelligence é capaz de transformar os dados e suas estruturas em algo palpável através de filtros orgânicos e uma estética confortável para a visualização.

### Selenium 
- Selenium é um conjunto de ferramentas de código aberto multiplataforma, usado para testar aplicações web pelo browser de forma automatizada. Ele executa testes de funcionalidades da aplicação web e testes de compatibilidade entre browser e plataformas diferentes. O Selenium suporta diversas linguagens de programação. A linguagem escolhida para utilizar foi o python e também será utilizado o selenium webdriver que usa o próprio driver do navegador para a automação.

<div id='Classes'/>

## Diagrama de Classes

![Diagrama de classes](https://github.com/pedrobarbosaocb/RepositorioTeste/blob/main/Diagrama%20de%20classes.jpeg)


<div id='Pacotes'/>

## Diagrama de Pacotes

![Diagrama de Pacotes](https://github.com/pedrobarbosaocb/RepositorioTeste/blob/main/Diagrama%20de%20Pacotes.jpeg)

