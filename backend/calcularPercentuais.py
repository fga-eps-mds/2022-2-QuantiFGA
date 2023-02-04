import pandas as pd  # biblioteca utilizada para dataframe
from separarSalasCompostasEHorarios import *
from preencherLotacaoSalas import *

def calcularPercentuais(dataframe):
# funcao que calcula os percentuais de ocupacao das salas e preenche a informacao no dataframe
    
    dfTempLinhasNovas = pd.DataFrame()
    dfTempLinhasNovas = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
 
    for i, row in dataframe.iterrows():
        linhaDfCopia = row.copy()  
        linhaDfCopia["percDisciplina"] = (dataframe['vagasOcupadas'][i] / dataframe['vagasOfertadas'][i])*100
        linhaDfCopia["percOcupacaoReal"] = (dataframe['vagasOcupadas'][i] / dataframe['lotacao'][i])*100
        linhaDfCopia["percOcupacaoTotal"] = (dataframe['vagasOfertadas'][i] / dataframe['lotacao'][i])*100
        dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia

    return dfTempLinhasNovas
# fim metodo calcularPercentuais
'''
if __name__ == '__main__':
# main - para testes isolados de cada metodo

    dfTurmasColetadasFGA = pd.read_csv('./testesUnitarios/csvTurmasColetadasFGA.csv', encoding="utf-8",  sep=';') 
    
    dfTurmasColetadasFGA = adicionarLinhasPorHorarioComSalasSeparadas(dfTurmasColetadasFGA)
    dfTurmasColetadasFGA = preencherLotacaoPredio(dfTurmasColetadasFGA)
    dfTurmasColetadasFGA  = calcularPercentuais(dfTurmasColetadasFGA)
    
    dfTurmasColetadasFGA.to_csv('./testesUnitarios/csvTestePorcentagens.csv', encoding="utf-8", sep=';', index = False)
# fim main
'''