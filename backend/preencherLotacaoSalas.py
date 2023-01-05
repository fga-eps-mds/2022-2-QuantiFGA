# ==============================================================================================================
# area dos imports - bibliotecas e funcoes
# ==============================================================================================================
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
from separarSalasCompostas import separarSalasCompostas

# ==============================================================================================================
# metodo preencherLotacaoPredio
# --------------------------------------------------------------------------------------------------------------
# funcao que preenche a lotacao das salas e o nome do predio ao qual ela pertence
# ==============================================================================================================
def preencherLotacaoPredio(dataframeSigaa):
    # ==========================================================================================================
    # salva informacoes de lotacao e predio de cada sala do csv especifico em um dataframe prediosSalasLotacao
    dataframeSalas = pd.read_csv('./csvPrediosSalasLotacao.csv', encoding="utf-8",   sep=';')
    # ==========================================================================================================
    # cria listas com os valores dos campos salaSeparada para comparacao
    listaSalaSeparadaSigaa = dataframeSigaa['salaSeparada'].to_list()
    listaSalaSeparada = dataframeSalas['salaSeparada'].to_list()
    # ==========================================================================================================
    # inicializa os contadores que percorrem as duas listas
    i=0 # listaSalaSeparadaSigaa
    j=0 # listaSalaSeparada
    # ==========================================================================================================
    # seta o flag que verifica se a variante da sala nao esta na matriz de comparacao como false
    encontrou_info_sala = False
    # ==========================================================================================================
    # percorre a lista das salas de todas as disciplinas procurando a sala na lista que contem 
    # as informacoes de lotacao e predio
    for i in range(len(listaSalaSeparadaSigaa)):
        for j in range(len(listaSalaSeparada)):
            if (dataframeSigaa['salaSeparada'][i] == dataframeSalas['salaSeparada'][j]):
                dataframeSigaa['lotacao'][i] = dataframeSalas['lotacao'][j]
                dataframeSigaa['predio'][i] = dataframeSalas['predio'][j]
                encontrou_info_sala = True
                break
        # ======================================================================================================
        # se nao encontrou a sala na lista de informacoes de lotacao e predio, preeenche
        # uma mensagem para verificacao e futura correcao do arquivo csv
        if encontrou_info_sala == False:
            dataframeSigaa['lotacao'][i] = 0
            dataframeSigaa['predio'][i] = 'sala nao encontrada' + dataframeSigaa['salaSeparada'][i]
    
    return dataframeSigaa


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
    # chama a funcao que preenche a lotacao e o predio de cada sala
    dfSigaa = preencherLotacaoPredio(dfSigaa)
    # ==========================================================================================================
    # renomeia a coluna index que o dataframe incluiu 
    dfSigaa.index.name = 'indexDados'
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('./testes/csvTesteLotacaoPredio.csv', encoding="utf-8",   sep=';')

# ==============================================================================================================
# fim main
# ==============================================================================================================