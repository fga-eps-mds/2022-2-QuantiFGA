import pandas as pd    # biblioteca utilizada para dataframe
from separarSalasCompostasEHorarios import *

def preencherLotacaoPredio(dataframe):
# funcao que preenche a lotacao das salas e o nome do predio ao qual ela pertence

    listaPredioLotacaoDeCadaSala = []
    listaPredioLotacaoDeCadaSala = (
        ['I01', 'Sala I1 - AT 49/41 UAC', 'UAC', 45],
        ['I02', 'Sala I2 - AT 42/48 UAC', 'UAC', 60], 
        ['I03', 'Sala I3 39/48', 'UAC', 60],
        ['I04', 'Sala I4 32/41', 'UAC', 45],
        ['I05', 'Sala I5 29/41', 'UAC', 45],
        ['I06', 'I6 Lab (laptop)', 'UAC', 40],
        ['I07', 'I7 19/48 lab', 'UAC', 40],
        ['I08', 'I8 12/41', 'UAC', 45],
        ['I09', 'I9 09/41', 'UAC', 130],
        ['I10', 'I10 lab', 'UAC', 80],
        ['S01', 'S1 62/41', 'UAC', 130],
        ['S02', 'S2 59/41', 'UAC', 130],
        ['S03', 'S3 42/41', 'UAC', 130],
        ['S04', 'S4 ', 'UAC', 130],
        ['S05', 'S5 29/41', 'UAC', 45],
        ['S06', 'S6 22/48', 'UAC', 60],
        ['S07', 'S7 19/48', 'UAC', 60],
        ['S08', 'S8 12/41', 'UAC', 45],
        ['S09', 'S9 09/41', 'UAC', 130],
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

    dfTempLinhasNovas = pd.DataFrame()
    dfTempLinhasNovas = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio', 'lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])

    indiceDataframe=0 
    indiceLista=0 

    for indiceDataframe, linhaDataframe in dataframe.iterrows(): 
        linhaDfCopia = linhaDataframe.copy()  
        encontrou_info_sala = False
        for indiceLista in range(len(listaPredioLotacaoDeCadaSala)):
            if (dataframe['salaSeparada'][indiceDataframe] == listaPredioLotacaoDeCadaSala[indiceLista][0]):
                linhaDfCopia["lotacao"] = int(listaPredioLotacaoDeCadaSala[indiceLista][3])
                linhaDfCopia["predio"] = listaPredioLotacaoDeCadaSala[indiceLista][2]
                dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia
                encontrou_info_sala = True
                break

        if encontrou_info_sala == False:
            linhaDfCopia["lotacao"] = 1
            linhaDfCopia["predio"] = 'sala nao encontrada - ' + dataframe['salaSeparada'][indiceDataframe]
            dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia
        
    return dfTempLinhasNovas
# fim do metodo preencherLotacaoPredio
''' 
if __name__ == '__main__':
# main - para testes isolados de cada metodo

    dfTurmasColetadasFGA = pd.read_csv('./testesUnitarios/csvTurmasColetadasFGA.csv', encoding="utf-8",  sep=';') 
    
    dfTurmasColetadasFGA = adicionarLinhasPorHorarioComSalasSeparadas(dfTurmasColetadasFGA)
    dfTurmasColetadasFGA = preencherLotacaoPredio(dfTurmasColetadasFGA)

    dfTurmasColetadasFGA.to_csv('./testesUnitarios/csvTesteLotacaoPredio.csv', encoding="utf-8", sep=';', index = False)
# fim main
'''