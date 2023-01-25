# ==========================================================================================
# area dos import - bibliotecas e funcoes
# ==========================================================================================
from datetime import datetime
from carregarDados import gerarCsv
from carregarDados import gerarConsulta
from carregarDados import salvarDadosCsv
from separarSalasCompostasEHorarios import adicionarLinhasPorHorarioSalasSeparadas
from preencherLotacaoSalas import preencherLotacaoPredio
from calcularPercentuais import calcularPorcentagens
from pymongo import MongoClient
import pandas as pd

# Função para gerar o database 
def get_database():
    #  URL do mongodb atlas para conectar ao banco pela string de conexão
    CONNECTION_STRING = 'mongodb+srv://<username>:<password>@cluster-quantifga.b6tob2c.mongodb.net/test' 
    # Cria uma conexão usando o MongoClient 
    client = MongoClient(CONNECTION_STRING, tlsInsecure=True)
    # Cria o bando de dados Quanti_FGA_DB
    return client['Quanti_FGA_DB']


# função para savar os daods no banco de dados 
def save_dataset_to_database(dataset):
    data_dict = dataset.to_dict("records")
    mongo_client = get_database()
    m = mongo_client["Disciplinas"]
    m.drop()
    m.insert_many(data_dict)

# ==============================================================================================================
# main
# --------------------------------------------------------------------------------------------------------------
# funcao principal que chama todos os metodos
# ==============================================================================================================
if __name__ == '__main__':
    # ==========================================================================================================
    # imprime a hora de inicio para checar o tempo de coleta
    print(datetime.now())
    
    # ==========================================================================================================
    # lista que vai receber todos os dados coletados para serem gravados no csv
    dados = []
    # ==========================================================================================================
    # gera os arquivos csv que receberao os dados
    gerarCsv()
    # ==========================================================================================================
    # gera a consulta preeenchendo os campos e clicando em buscar
    # e ja chama a funcao de capturar dados - coleta dados de seis departamentos
    gerarConsulta('GRADUAÇÃO', 'FACULDADE DO GAMA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'DEPTO CIÊNCIAS DA COMPUTAÇÃO - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE FÍSICA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE QUÍMICA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE ENGENHARIA MECANICA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE MATEMÁTICA - BRASÍLIA', '2022', '2', dados)
    # ==========================================================================================================
    # salva os dados coletados no arquivo csv
    salvarDadosCsv(dados)
    # ==========================================================================================================
    # le os dados do arquivo csv em um dataframe dfSigaa
    dfSigaa = pd.read_csv('csvDadosColetados.csv', encoding="utf-8",   sep=';')
    # ==========================================================================================================
    # chama as funcoes para preencher os dados dessas novas colunas
    # ==========================================================================================================
    dfSigaa = adicionarLinhasPorHorarioSalasSeparadas(dfSigaa)
    # ==========================================================================================================
    dfSigaa = preencherLotacaoPredio(dfSigaa)
    # ==========================================================================================================
    dfSigaa = calcularPorcentagens(dfSigaa)
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('csvDadosAtualizados.csv', encoding="utf-8", sep=';', index = False)
    # ==========================================================================================================
    # imprime a hora de fim para checar o tempo de coleta
    print(datetime.now())
    # ==========================================================================================================
    # Salvando  os dados  na base de dados 
    save_dataset_to_database(dfSigaa)
# ==============================================================================================================
# fim main
# ==============================================================================================================