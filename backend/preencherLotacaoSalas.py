# ==============================================================================================================
# area dos imports - bibliotecas e funcoes
# ==============================================================================================================
import pandas as pd    # biblioteca utilizada para arquivos em dataframe
from separarSalasCompostasEHorarios import adicionarLinhasPorHorarioSalasSeparadas

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
    # cria um dataframe temporario que vai receber todas as linhas novas
    new_df = pd.DataFrame()
    new_df = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
    # ==========================================================================================================
    # cria listas com os valores dos campos salaSeparada para comparacao
    #listaSalaSeparadaSigaa = dataframeSigaa['salaSeparada'].to_list()
    listaSalaSeparada = dataframeSalas['salaSeparada'].to_list()
    # ==========================================================================================================
    # inicializa os contadores que percorrem as duas listas
    i=0 # listaSalaSeparadaSigaa
    j=0 # listaSalaSeparada
    # ==========================================================================================================
    # ==========================================================================================================
    # percorre a lista das salas de todas as disciplinas procurando a sala na lista que contem 
    # as informacoes de lotacao e predio
    for i, row in dataframeSigaa.iterrows(): 
        row_copy = row.copy()  
        # seta o flag que verifica se a variante da sala nao esta na matriz de comparacao como false
        encontrou_info_sala = False
        for j in range(len(listaSalaSeparada)):
            if (dataframeSigaa['salaSeparada'][i] == dataframeSalas['salaSeparada'][j]):
                row_copy["lotacao"] = dataframeSalas['lotacao'][j]
                row_copy["predio"] = dataframeSalas['predio'][j]
                new_df.loc[len(new_df)] = row_copy
                encontrou_info_sala = True
                break
        # ======================================================================================================
        # se nao encontrou a sala na lista de informacoes de lotacao e predio, preeenche
        # uma mensagem para verificacao e futura correcao do arquivo csv
        if encontrou_info_sala == False:
            row_copy["lotacao"] = 1
            row_copy["predio"] = 'sala nao encontrada' + dataframeSigaa['salaSeparada'][i]
            new_df.loc[len(new_df)] = row_copy
    
    print('# ===========================================================================')
    print('total de turmas com lotacao e predio preenchidos - uma linha por credito: ')
    print(len(new_df))
    print('# ===========================================================================')
    
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    new_df.to_csv('./testesUnitarios/csvTesteUnitLotacaoPredio.csv', encoding="utf-8", sep=';', index = False)
    
    return new_df


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
    dfSigaa = adicionarLinhasPorHorarioSalasSeparadas(dfSigaa)
    # ==========================================================================================================
    # chama a funcao que preenche a lotacao e o predio de cada sala
    dfSigaa = preencherLotacaoPredio(dfSigaa)
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('./testes/csvTesteLotacaoPredio.csv', encoding="utf-8", sep=';', index = False)
    
# ==============================================================================================================
# fim main
# ==============================================================================================================