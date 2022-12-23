import pandas as pd    # biblioteca utilizada para arquivos em dataframe


def preencherLotacaoPredio(dataframeSigaa, dataframeSalas):
    listaSalaSeparadaSigaa = dataframeSigaa['salaSeparada'].to_list()
    listaSalaSeparada = dataframeSalas['salaSeparada'].to_list()
    i=0
    j=0
    for i in range(len(listaSalaSeparadaSigaa)):
        for j in range(len(listaSalaSeparada)):
            if (dataframeSigaa['salaSeparada'][i] == dataframeSalas['salaSeparada'][j]):
                dataframeSigaa['lotacao'][i] = dataframeSalas['lotacao'][j]
                dataframeSigaa['predio'][i] = dataframeSalas['predio'][j]
    dataframeSigaa.to_csv('csvDadosAtualizadosLotacao.csv', encoding="utf-8",   sep=';')

""" if __name__ == '__main__':
 
    # salva dados do arquivo csv em um dataframe dfSigaa
    dfSigaa = pd.read_csv('backend\csvDadosAtualizados.csv', encoding="utf-8",   sep=';')
    # salva dados do arquivo csv em um dataframe dfSigaa
    prediosSalasLotacao = pd.read_csv('backend\csvPrediosSalasLotacao.csv', encoding="utf-8",   sep=';')
    
    # cria uma lista com as salas separadas do dfSigaa
    listaSalaSeparadaSigaa = dfSigaa['salaSeparada'].to_list()
    # cria uma lista com as salas separadas de prediosSalasLotacao
    listaSalaSeparada = prediosSalasLotacao['salaSeparada'].to_list()
    
    # TESTE ----------------
    #nomesColunas = list(dfSigaa.columns)
    #print(prediosSalasLotacao['salaSeparada'][1])
    #print('\n')
    #print(nomesColunas)
    # TESTE ----------------
    
    i=0
    j=0
    for i in range(len(listaSalaSeparadaSigaa)):
        for j in range(len(listaSalaSeparada)):
            if (dfSigaa['salaSeparada'][i] == prediosSalasLotacao['salaSeparada'][j]):
                dfSigaa['lotacao'][i] = prediosSalasLotacao['lotacao'][j]
                dfSigaa['predio'][i] = prediosSalasLotacao['predio'][j]
    
    dfSigaa.to_csv('csvDadosAtualizadosLotacao.csv', encoding="utf-8",   sep=';')

    
    # TESTE -------------------
    # inseri I7 na sala separada do dfSigaa na linha 4 e vi se modificava
    #print(dfSigaa['lotacao'][2:5])
    #print(dfSigaa['salaSeparada'][2:5])
    #print(dfSigaa['predio'][2:5])
    # TESTE ---------------------- """

