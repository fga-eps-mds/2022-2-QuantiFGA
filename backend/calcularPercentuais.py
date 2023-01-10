# ==============================================================================================================
# area dos imports - bibliotecas e funcoes
# ==============================================================================================================
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
from separarSalasCompostas import separarSalasCompostas
from preencherLotacaoSalas import preencherLotacaoPredio
from separarHorarios import adicionarLinhasPorHorario

# ==============================================================================================================
# metodo calcularPorcentagens
# --------------------------------------------------------------------------------------------------------------
# funcao que calcula os percentuais de ocupacao das salas e preenche a informacao no dataframe
# ==============================================================================================================
def calcularPorcentagens(dataframe):
    # ==========================================================================================================
    # gera uma lista com a coluna lotacao
    listaLotacao = dataframe['lotacao'].to_list()
    # percorre toda a lista calculando e preenchendo as porcentagens
    for i in range(len(listaLotacao)):
        dataframe['percDisciplina'][i] = dataframe['vagasOcupadas'][i] / dataframe['vagasOfertadas'][i]
        dataframe['percOcupacaoReal'][i] = dataframe['vagasOcupadas'][i] / dataframe['lotacao'][i]
        dataframe['percOcupacaoTotal'][i] = dataframe['vagasOfertadas'][i] / dataframe['lotacao'][i]

    return dataframe
# ==============================================================================================================
# fim metodo calcularPorcentagens
# ==============================================================================================================


# ==============================================================================================================
# main
# --------------------------------------------------------------------------------------------------------------
# funcao principal que chama todos os metodos
# ==============================================================================================================
if __name__ == '__main__':
    # ==========================================================================================================
    # le os dados do arquivo csv em um dataframe dfSigaa 
    dfSigaa = pd.read_csv('csvDadosColetados.csv', encoding="utf-8",  sep=';') 
    # ==========================================================================================================
    # renomeia a coluna index que o dataframe incluiu 
    dfSigaa.index.name = 'indexDados'
    # ==========================================================================================================
    # chama o metodo que separa as salas compostas
    dfSigaa = separarSalasCompostas(dfSigaa)
    # ==========================================================================================================
    # chama o metodo que separa as salas compostas
    dfSigaa = preencherLotacaoPredio(dfSigaa)
    # ==========================================================================================================
    # chama o metodo que separa os horarios por credito
    dfSigaa = adicionarLinhasPorHorario(dfSigaa)
    # ==========================================================================================================
    # chama o metodo que separa os horarios por credito
    dfSigaa  = calcularPorcentagens(dfSigaa)
    # ==========================================================================================================
    # renomeia a coluna index que o dataframe incluiu 
    dfSigaa.index.name = 'indexDados'
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('./testes/csvTestePorcentagens.csv', encoding="utf-8",   sep=';')

# ==============================================================================================================
# fim main
# ==============================================================================================================