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
    #dataframeSalas = pd.read_csv('./csvPrediosSalasLotacao.csv', encoding="utf-8",   sep=';')
    #dataframeSalas = pd.DataFrame(columns=['salaSeparada','infoSala','predio','lotacao'])
    listaSalaSeparada = []
    listaSalaSeparada = (['I1', 'Sala I1 - AT 49/41 UAC', 'UAC', 45],
        ['I2', 'Sala I2 - AT 42/48 UAC', 'UAC', 60],
        ['I3', 'Sala I3 39/48', 'UAC', 60],
        ['I4', 'Sala I4 32/41', 'UAC', 45],
        ['I5', 'Sala I5 29/41', 'UAC', 45],
        ['I6', 'I6 Lab (laptop)', 'UAC', 40],
        ['I7', 'I7 19/48 lab', 'UAC', 40],
        ['I8', 'I8 12/41', 'UAC', 45],
        ['I9', 'I9 09/41', 'UAC', 130],
        ['I10', 'I10 lab', 'UAC', 80],
        ['S1', 'S1 62/41', 'UAC', 130],
        ['S2', 'S2 59/41', 'UAC', 130],
        ['S3', 'S3 42/41', 'UAC', 130],
        ['S4', 'S4 ', 'UAC', 130],
        ['S5', 'S5 29/41', 'UAC', 45],
        ['S6', 'S6 22/48', 'UAC', 60],
        ['S7', 'S7 19/48', 'UAC', 60],
        ['S8', 'S8 12/41', 'UAC', 45],
        ['S9', 'S9 09/41', 'UAC', 130],
        ['S10', 'S10 09/23 lab', 'UAC', 80],
        ['Anfiteatro', 'Anfiteatro (UAC)', 'UAC', 240],
        ['Ante I-10', 'Ante-sala I10', 'UAC', 20],
        ['Multi.', 'Sala multiuso', 'UAC', 25],
        ['Lab.Quim.', 'Lab quimica UED', 'UED', 20],
        ['Lab.NEI-1', 'Lab NEI 1 UED', 'UED', 20],
        ['Lab.NEI-2', 'Lab NEI 2 UED', 'UED', 20],
        ['Lab.SS', 'Lab SS', 'UED', 45],
        ['Lab.Fis-1', 'Lab Fisica 1', 'UED', 25],
        ['Lab.Ond', 'Lab Fisica 2', 'UED', 25],
        ['Lab.Eletr.', 'Lab Eletr.', 'UED', 20],
        ['Lab.Mater.', 'Lab Materiais', 'UED', 15],
        ['Mocap', 'Lab Mocap', 'UED', 60],
        ['Lab.Termoflui.', 'Lab termofluidos', 'UED', 25],
        ['Lab.Termodin.', 'La termodinamica', 'UED', 25],
        ['Lab.LDS', 'Lab LDS Ued', 'UED', 15],
        ['Cont-4', 'Container nº 4', 'Container', 45],
        ['Cont-8-SHP', 'Container nº 8', 'Container', 16],
        ['Cont-17', 'Container nº 17', 'Container', 30],
        ['LD.Sala-2', 'Sala 2 LDTEA', 'LDTEA', 20],
        ['LD.Sala-3', 'Sala 3 LDTEA', 'LDTEA', 30])

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
    #listaSalaSeparada = dataframeSalas['salaSeparada'].to_list()
    #listaSalaSeparada = dataframeSalas
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
        #for j, rowSalas in dataframeSalas.iterrows():
            if (dataframeSigaa['salaSeparada'][i] == listaSalaSeparada[j][0]):
                row_copy["lotacao"] = int(listaSalaSeparada[j][3])
                row_copy["predio"] = listaSalaSeparada[j][2]
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
    
    #print(new_df.dtypes)

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