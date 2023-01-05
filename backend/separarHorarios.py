# ==========================================================================================
# area dos import - bibliotecas e funcoes
# ==========================================================================================
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
import re
from separarSalasCompostas import separarSalasCompostas
from preencherLotacaoSalas import preencherLotacaoPredio

# ==============================================================================================================
# metodo adicionarLinhasPorHorario
# --------------------------------------------------------------------------------------------------------------
# funcao que separa os horarios por credito
# ==============================================================================================================
def adicionarLinhasPorHorario(dataframe):
    # ==========================================================================================================
    # Percorre o dataframe e adiciona linhas de materias que tem mais de 1 horario, 
    # especificando cada horario por linha.
    # ==========================================================================================================
    # cria um dataframe temporario que vai receber todas as linhas novas
    new_df = pd.DataFrame()
    # percorre todas as linhas do dataframe
    for index, row in dataframe.iterrows():
        # chama o metodo que separa os horarios por credito
        horarios = separaHorario(row["horario"])
        # salva novas linhas no dataframe temporario
        for horario in horarios:
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horario
            new_df = new_df.append(row_copy, ignore_index=True)

    return new_df
# ==============================================================================================================
# fim metodo adicionarLinhasPorHorario
# ==============================================================================================================


# ==============================================================================================================
# metodo separaHorario
# --------------------------------------------------------------------------------------------------------------
# funcao que separa os horarios por credito
# ==============================================================================================================
def separaHorario(horario):
    # ==========================================================================================================
    # Dado uma string horario no padrão [DIAS_DA_SEMANA][PERIODO][HORARIO] é retornado uma lista do horario 
    # separado por hora 
    # [DIAS_DA_SEMANA] 2-7
    # [PERIODO] manha = M, tarde = T, e noite = N
    # [HORARIO] to do
    # exemplo Horario = 26T12 retorno = [[2, "tarde", 1 ], [2, "tarde", 2 ], [6, "tarde", 1 ], [6, "tarde", 2 ]]
    # ==========================================================================================================
    # separa os horarios se for composto
    horarios = horario.split() 
    resultado = []
    for h in horarios:
        # encontra o M ou T ou N
        x = re.search("^(\d+)([M|T|N])(\d+)", h)
        if x:
            # antes do M - T - N estao os dias
            days = [int(x) for x in x.group(1)]
            # M - T - N
            turno = x.group(2)
            # depois do M - T - N estao as horas
            hours = [int(x) for x in x.group(3)]
            # para cada dia e hora cria uma nova linha no dataframe temporario
            for d in days:
                for ho in hours:
                    resultado.append(f'{d}{turno}{ho}')
        # se nao encontrar M - T - N imprime valores com mensagem para checagem
        else:
            print("No match", h)
    return resultado


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
    # chama o metodo que separa as salas compostas
    dfSigaa = preencherLotacaoPredio(dfSigaa)
    # ==========================================================================================================
    # chama o metodo que separa os horarios por credito
    dfSigaa = adicionarLinhasPorHorario(dfSigaa)
    # ==========================================================================================================
    # renomeia a coluna index que o dataframe incluiu 
    dfSigaa.index.name = 'indexDados'
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('./testes/csvTesteHorariosSeparados.csv', encoding="utf-8",   sep=';')

# ==============================================================================================================
# fim main
# ==============================================================================================================