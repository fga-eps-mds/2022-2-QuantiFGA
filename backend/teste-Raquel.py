
from datetime import datetime
from separarSalasCompostasEHorarios import *
from preencherLotacaoSalas import preencherLotacaoPredio
from calcularPercentuais import calcularPorcentagens
import pandas as pd


if __name__ == '__main__':
    # dfSigaaDadosColetados = []
    # dfSigaaDadosColetados = pd.DataFrame(columns=    
    #             ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
    #             'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
    #             'predio','lotacao', 'horarioSeparado', 'percDisciplina',
    #             'percOcupacaoReal','percOcupacaoTotal'])
    # dfSigaaDadosColetados.loc[len(dfSigaaDadosColetados)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', '-', '-', 0, '-', 0, 0, 0]
    # # print(datetime.now())
    # print(dfSigaaDadosColetados["horario"]) 
    # horarioSeparado = separaHorario(dfSigaaDadosColetados["horario"][0])
    # print(horarioSeparado)

    dfSigaaDadosColetados = []
    dfSigaaDadosColetados = pd.DataFrame(columns=    
                ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
                'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
                'predio','lotacao', 'horarioSeparado', 'percDisciplina',
                'percOcupacaoReal','percOcupacaoTotal'])
    dfSigaaDadosColetados.loc[len(dfSigaaDadosColetados)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', '-', '-', 0, '-', 0, 0, 0]


    listaSigaaDadosColetadosHoraio = dfSigaaDadosColetados['horario'].to_list()
    listaSigaaHorario = [
                [[2, "tarde", 2 ], [2, "tarde", 3 ], [6, "tarde", 2 ], [6, "tarde", 3 ]],
                [[2, "manha", 1 ], [2, "manha", 2 ], [4, "manha", 1 ], [4, "manha", 2 ]],
                [[3, "manha", 3 ], [3, "manha", 4 ], [5, "manha", 3 ], [5, "manha", 4 ]],
                [[3, "tarde", 4 ], [3, "tarde", 5 ], [5, "tarde", 4 ], [6, "tarde", 5 ]]
                ]

    #dfSigaaDadosColetados.loc[len(dfSigaaDadosColetados)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', '-', '-', 0, '-', 0, 0, 0]
    # print(datetime.now())
    print(listaSigaaDadosColetadosHoraio)
    print(listaSigaaHorario[0]) 

    separaHorario(listaSigaaDadosColetadosHoraio[0])