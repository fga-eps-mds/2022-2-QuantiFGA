# ==========================================================================================
# area dos import - bibliotecas e funcoes
# ==========================================================================================
from datetime import datetime
from carregarDados import gerarCsv
from carregarDados import gerarConsulta
from carregarDados import salvarDadosCsv
from separarSalasCompostas import separarSalasCompostas
from preencherLotacaoSalas import preencherLotacaoPredio
from separarHorarios import adicionarLinhasPorHorario
from calcularPercentuais import calcularPorcentagens
import pandas as pd

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
    # renomeia a coluna index que o dataframe incluiu
    dfSigaa.index.name = 'indexDados'
    # ==========================================================================================================
    # chama as funcoes para preencher os dados dessas novas colunas
    # ==========================================================================================================
    dfSigaa = separarSalasCompostas(dfSigaa)
    # ==========================================================================================================
    dfSigaa = preencherLotacaoPredio(dfSigaa)
    # ==========================================================================================================
    dfSigaa = adicionarLinhasPorHorario(dfSigaa)
    # ==========================================================================================================
    dfSigaa = calcularPorcentagens(dfSigaa)
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('csvDadosAtualizados.csv', encoding="utf-8",   sep=';')
    # ==========================================================================================================
    # imprime a hora de fim para checar o tempo de coleta
    print(datetime.now())

# ==============================================================================================================
# fim main
# ==============================================================================================================