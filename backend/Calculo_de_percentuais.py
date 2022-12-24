import pandas as pd  # biblioteca utilizada para arquivos em dataframe


def calculaPorcentagens(dataframe):
    listaLotacao = dataframe['lotacao'].to_list()
    for i in range(len(listaLotacao)):
        dataframe['percDisciplina'][i] = dataframe['vagasOcupadas'][i] / dataframe['vagasOfertadas'][i]
        dataframe['percOcupacaoReal'][i] = dataframe['vagasOcupadas'][i] / dataframe['lotacao'][i]
        dataframe['percOcupacaoTotal'][i] = dataframe['vagasOfertadas'][i] / dataframe['lotacao'][i]
    
    # retorna para a main
    return (dataframe)


if __name__ == '__main__':

    # salva dados do arquivo csv em um dataframe dfSigaa
    dfSigaa = pd.read_csv('csvDadosColetados.csv', encoding="utf-8",   sep=';')

    dfSigaa  = calculaPorcentagens(dfSigaa)
    
    dfSigaa.to_csv('csvDadosAtualizadosTestePorc.csv', encoding="utf-8",   sep=';')
