# ==============================================================================================================
# area dos imports - bibliotecas e funcoes
# ==============================================================================================================
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
from separarSalasCompostasEHorarios import adicionarLinhasPorHorarioSalasSeparadas
from preencherLotacaoSalas import preencherLotacaoPredio

# ==============================================================================================================
# metodo calcularPorcentagens
# --------------------------------------------------------------------------------------------------------------
# funcao que calcula os percentuais de ocupacao das salas e preenche a informacao no dataframe
# ==============================================================================================================
def calcularPorcentagens(dataframe):
    # ==========================================================================================================
    # cria um dataframe temporario que vai receber todas as linhas novas
    new_df = pd.DataFrame()
    new_df = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
    # ==========================================================================================================
    # percorre toda a lista calculando e preenchendo as porcentagens
    for i, row in dataframe.iterrows():
        row_copy = row.copy()  
        row_copy["percDisciplina"] = (dataframe['vagasOcupadas'][i] / dataframe['vagasOfertadas'][i])*100
        row_copy["percOcupacaoReal"] = (dataframe['vagasOcupadas'][i] / dataframe['lotacao'][i])*100
        row_copy["percOcupacaoTotal"] = (dataframe['vagasOfertadas'][i] / dataframe['lotacao'][i])*100
        new_df.loc[len(new_df)] = row_copy

    print('# ===========================================================================')
    print('total de turmas com o percentual calculado')
    print(len(new_df))
    print('# ===========================================================================')

    # ==========================================================================================================
    # teste
    new_df.to_csv('./testesUnitarios/csvTesteUnitPorcentagens.csv', encoding="utf-8", sep=';', index = False)
    
    return new_df

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
    # chama o metodo que separa os horarios por credito
    dfSigaa = adicionarLinhasPorHorarioSalasSeparadas(dfSigaa)
    # ==========================================================================================================
    # chama o metodo que separa as salas compostas
    dfSigaa = preencherLotacaoPredio(dfSigaa)
    # ==========================================================================================================
    # chama o metodo que separa os horarios por credito
    dfSigaa  = calcularPorcentagens(dfSigaa)
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('./testes/csvTestePorcentagens.csv', encoding="utf-8", sep=';', index = False)
    
# ==============================================================================================================
# fim main
# ==============================================================================================================