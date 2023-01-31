import pandas as pd             # biblioteca utilizada para arquivos em dataframe
import urllib                   # biblioteca utilizada para aceitar caracteres especiais (@) no nome do usuario
from datetime import datetime   # biblioteca utilizada para calcular o tempo do processo
from pymongo import MongoClient # biblioteca utilizada para criar conexao com o banco de dados
from carregarDados import *
from separarSalasCompostasEHorarios import *
from preencherLotacaoSalas import *
from calcularPercentuais import *

def obterBancoDeDados():
# Funçao para conectar o banco de dados mongodb atlas e gerar o database Quanti_FGA_DB
 
    # se desejar a conexao com o servidor na nuvem
    # substituir <username> pelo nome do usuario e <password> pela senha para a conexao
    CONNECTION_STRING = 'mongodb+srv://<username>:<password>@cluster-quantifga.b6tob2c.mongodb.net/Quanti_FGA_DB'
    # se desejar a conexao local, basta comentar a linha anterior e descomentar a linha seguinte
    #CONNECTION_STRING = 'mongodb://localhost:27017'

    client = MongoClient(CONNECTION_STRING, tlsInsecure=True)
    
    return client['Quanti_FGA_DB']
# fim do metodo obterBancoDeDados

def salvarTurmasNoBancoDeDados(dataset):
# funçao para salvar as turmas coletadas na tabela Disciplinas do banco de dados 
    
    data_dict = dataset.to_dict("records")
    mongo_client = obterBancoDeDados()
    m = mongo_client["Disciplinas"]
    m.drop()
    m.insert_many(data_dict)
# fim do metodo salvarTurmasNoBancoDeDados

if __name__ == '__main__':
# funcao principal que chama todos os metodos

    dataHoraInicioDoProcesso = datetime.now()
    
    gerarCsv()
    
    listaTurmasColetadas = []
    gerarConsulta('GRADUAÇÃO', 'FACULDADE DO GAMA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    gerarConsulta('GRADUAÇÃO', 'DEPTO CIÊNCIAS DA COMPUTAÇÃO - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE FÍSICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE QUÍMICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE ENGENHARIA MECANICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE MATEMÁTICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    
    # salvando dados em um arquivo .csv para uso em testes unitarios e em testes de metodos isolados
    salvarTurmasColetadasNoCsvFiltrandoFGA(listaTurmasColetadas)
    dfTurmasColetadasFGA = pd.read_csv('./testesUnitarios/csvTurmasColetadasFGA.csv', encoding="utf-8",  sep=';') 
    
    # obtendo informacoes adicionais
    dfTurmasColetadasFGA = adicionarLinhasPorHorarioComSalasSeparadas(dfTurmasColetadasFGA)
    dfTurmasColetadasFGA = preencherLotacaoPredio(dfTurmasColetadasFGA)
    dfTurmasColetadasFGA = calcularPercentuais(dfTurmasColetadasFGA)

    salvarTurmasNoBancoDeDados(dfTurmasColetadasFGA)
    # salvando dados em um arquivo .csv para uso em testes unitarios e em testes de metodos isolados
    dfTurmasColetadasFGA.to_csv('./testesUnitarios/csvTurmasAtualizadasFGA.csv', encoding="utf-8", sep=';', index = False)
    
    dataHoraFimDoProcesso = datetime.now()
    print(f'\nDuração do processo de coleta e carregamento das turmas:  {dataHoraFimDoProcesso - dataHoraInicioDoProcesso}\n')
# fim main