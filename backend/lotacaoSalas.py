import pandas as pd    # biblioteca utilizada para arquivos em dataframe

'''
def preencherLotacaoSalas(dataframe):
    return (dataframe)
'''

# main
if __name__ == '__main__':
 
    # salva dados do arquivo csv em um dataframe dfSigaa
    dfSigaa = pd.read_csv('backend\csvDadosAtualizados.csv', encoding="utf-8",   sep=';')
    # salva dados do arquivo csv em um dataframe dfSigaa
    prediosSalasLotacao = pd.read_csv('backend\csvPrediosSalasLotacao.csv', encoding="utf-8",   sep=';')
    
    # nomes das colunas
    nomesColunas = list(dfSigaa.columns)
    #print(nomesColunas)
    #print("\n")
    
    listaSalaSeparadaSigaa = dfSigaa['salaSeparada'].to_list()
    listaSalaSeparada = prediosSalasLotacao['salaSeparada'].to_list()
    
    #print(prediosSalasLotacao)
    #print(dfSigaa)

    #sala = "I-7"
    i = 0
    j=0
    
    #print(prediosSalasLotacao['salaSeparada'][1])
    #print('\n')
    #print(nomesColunas)
    
    for i in range(len(listaSalaSeparadaSigaa)):
        for j in range(len(listaSalaSeparada)):
            if (dfSigaa['salaSeparada'][i] == prediosSalasLotacao['salaSeparada'][j]):
                dfSigaa['lotacao'][i] = prediosSalasLotacao['lotacao'][j]
                dfSigaa['predio'][i] = prediosSalasLotacao['predio'][j]
    
    print(dfSigaa['lotacao'][2:5])
    print(dfSigaa['salaSeparada'][2:5])
    print(dfSigaa['predio'][2:5])

    print("pronto")

