# ==============================================================================================================
# area dos imports - bibliotecas e funcoes
# ==============================================================================================================
import pandas as pd
import re



# ==============================================================================================================
# metodo adicionarLinhasPorHorario
# --------------------------------------------------------------------------------------------------------------
# funcao que separa os horarios por credito
# ==============================================================================================================
def adicionarLinhasPorHorarioSalasSeparadas(dataframe):
    # ==========================================================================================================
    # Percorre o dataframe e adiciona linhas de materias que tem mais de 1 horario, 
    # especificando cada horario por linha.
    # ==========================================================================================================
    # cria um dataframe temporario que vai receber todas as linhas novas
    new_df = pd.DataFrame()
    new_df = pd.DataFrame(columns=    
             ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
    # tratamento para salas compostas que sera feito em versoes posteriores
    qtdd_disciplinas_ignoradas = 0
    qtdd_disciplinas_uma_sala = 0
    qtdd_disciplinas_duas_salas_quatro_creditos = 0
    # percorre todas as linhas do dataframe
    for index, row in dataframe.iterrows():
        # chama o metodo que separa os horarios por credito
        horarios = separaHorario(row["horario"])
        localSeparado = separaSala(row["local"])
        # verifica a quantidade de salas ocupadas pela disciplina da linha em questão
        qtde_salas_ocupadas = len(localSeparado)
        # verifica a quantidade de horarios apos a separacao
        qtde_horarios = len(horarios)
        # salva novas linhas no dataframe temporario

        if qtde_salas_ocupadas == 1:
            qtdd_disciplinas_uma_sala = qtdd_disciplinas_uma_sala + 1
            for horario in horarios:
                row_copy = row.copy()
                row_copy["horarioSeparado"] = horario
                row_copy["salaSeparada"] = localSeparado[0]
                new_df.loc[len(new_df)] = row_copy

        if qtde_salas_ocupadas == 2 and qtde_horarios == 4:
            qtdd_disciplinas_duas_salas_quatro_creditos = qtdd_disciplinas_duas_salas_quatro_creditos + 1
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[0]
            row_copy["salaSeparada"] = localSeparado[0]
            new_df.loc[len(new_df)] = row_copy
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[1]
            row_copy["salaSeparada"] = localSeparado[0]
            new_df.loc[len(new_df)] = row_copy
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[2]
            row_copy["salaSeparada"] = localSeparado[1]
            new_df.loc[len(new_df)] = row_copy
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[3]
            row_copy["salaSeparada"] = localSeparado[1]
            new_df.loc[len(new_df)] = row_copy
            
        # ===================================================================================
        if qtde_salas_ocupadas == 2 and qtde_horarios != 4:
            # tratamento para salas compostas que sera feito em versoes posteriores
            qtdd_disciplinas_ignoradas = qtdd_disciplinas_ignoradas + 1
            #print(' | ', qtdd_disciplinas_ignoradas, ' | ',row["codigNomeMateria"], ' | ',row["codigoTurma"], 
            #    ' | ',row["local"], ' | ',row["horario"], ' | duas salas - diferente de 4 creditos | IGNORADA |')
            '''
            for horario in horarios:
                for sala in localSeparado:
                    row_copy = row.copy()
                    row_copy["horarioSeparado"] = horario
                    row_copy["salaSeparada"] = 'teste - duas salas - mais de 4 creditos'
                    new_df = new_df.append(row_copy, ignore_index=True)
            '''
        # ===================================================================================
        if qtde_salas_ocupadas == 3 and qtde_horarios == 6:
            # tratamento para salas compostas que sera feito em versoes posteriores
            qtdd_disciplinas_ignoradas = qtdd_disciplinas_ignoradas + 1
            #print(' | ', qtdd_disciplinas_ignoradas, ' | ',row["codigNomeMateria"], ' | ',row["codigoTurma"], 
            #    ' | ',row["local"], ' | ',row["horario"], ' | tres salas - 6 creditos | IGNORADA |')
            '''
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[0]
            row_copy["salaSeparada"] = localSeparado[0]
            new_df = new_df.append(row_copy, ignore_index=True)
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[1]
            row_copy["salaSeparada"] = localSeparado[0]
            new_df = new_df.append(row_copy, ignore_index=True)
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[2]
            row_copy["salaSeparada"] = localSeparado[1]
            new_df = new_df.append(row_copy, ignore_index=True)
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[3]
            row_copy["salaSeparada"] = localSeparado[1]
            new_df = new_df.append(row_copy, ignore_index=True)
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[4]
            row_copy["salaSeparada"] = localSeparado[2]
            new_df = new_df.append(row_copy, ignore_index=True)
            row_copy = row.copy()
            row_copy["horarioSeparado"] = horarios[5]
            row_copy["salaSeparada"] = localSeparado[2]
            new_df = new_df.append(row_copy, ignore_index=True)
            '''
        # ===================================================================================
        if qtde_salas_ocupadas == 3 and qtde_horarios != 6:
            # tratamento para salas compostas que sera feito em versoes posteriores
            qtdd_disciplinas_ignoradas = qtdd_disciplinas_ignoradas + 1
            #print(' | ', qtdd_disciplinas_ignoradas, ' | ',row["codigNomeMateria"], ' | ',row["codigoTurma"], 
            #    ' | ',row["local"], ' | ',row["horario"], ' | tres salas - diferente de 6 creditos | IGNORADA |')
            '''
            for horario in horarios:
                for sala in localSeparado:
                    row_copy = row.copy()
                    row_copy["horarioSeparado"] = horario
                    row_copy["salaSeparada"] = 'teste - tres salas ' + str(len(horarios)) + ' creditos'
                    new_df = new_df.append(row_copy, ignore_index=True)
            '''
        # ===================================================================================
        if qtde_salas_ocupadas > 3:
            # tratamento para salas compostas que sera feito em versoes posteriores
            qtdd_disciplinas_ignoradas = qtdd_disciplinas_ignoradas + 1
            #print(' | ', qtdd_disciplinas_ignoradas, ' | ',row["codigNomeMateria"], ' | ',row["codigoTurma"], 
            #    ' | ',row["local"], ' | ',row["horario"], ' | mais de tres salas | IGNORADA |')
            '''
            for horario in horarios:
                for sala in localSeparado:
                    row_copy = row.copy()
                    row_copy["horarioSeparado"] = horario
                    row_copy["salaSeparada"] = 'teste - quatro ou mais salas'
                    new_df = new_df.append(row_copy, ignore_index=True)
            '''
        # ===================================================================================
          
    print('# ===========================================================================')
    print('total de turmas e horarios separados - uma linha por credito: ')
    print(len(new_df))
    print('# ===========================================================================')
    '''
    print('turmas tratadas e separadas - total: ')
    print(qtdd_disciplinas_uma_sala + qtdd_disciplinas_duas_salas_quatro_creditos)
    print('# ============================================')
    print('-> turmas com so uma sala: ')
    print(qtdd_disciplinas_uma_sala)
    print('-> turmas com duas salas e quatro creditos: ')
    print(qtdd_disciplinas_duas_salas_quatro_creditos)
    print('# ===========================================================================')
    print('turmas ignoradas - duas salas (diferente de 4 creditos) ou mais salas: ')
    print(qtdd_disciplinas_ignoradas)
    print('tratamento para salas compostas ignoradas sera feito em versoes posteriores')
    print('# ===========================================================================')
    '''
    # ===================================================================================
    # teste
    new_df.to_csv('./testesUnitarios/csvTesteUnitSalasHorariosSeparadas.csv', encoding="utf-8", sep=';', index = False)
       

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
            #for d in days:
            #    print(days)
            # M - T - N
            turno = x.group(2)
            #print(turno)
            # depois do M - T - N estao as horas
            hours = [int(x) for x in x.group(3)]
            #for ho in hours:
            #    print(hours)
            # para cada dia e hora cria uma nova linha no dataframe temporario
            for d in days:
                for ho in hours:
                    resultado.append(f'{d}{turno}{ho}')
        # se nao encontrar M - T - N imprime valores com mensagem para checagem
        else:
            print("No match", h)
    return resultado
# ==============================================================================================================
# fim metodo separaHorario
# ==============================================================================================================


# ==============================================================================================================
# metodo separaSala
# --------------------------------------------------------------------------------------------------------------
# 
# ==============================================================================================================
def separaSala(local): 
    # ==========================================================================================================
    # criacao de uma matriz para padronizar os nomes das salas da FGA 
    # primeira coluna - diversos nomes que cada sala aparece no Sigaa
    # segunda coluna - nome padrão de cada sala que constara nos dados finais
    matrizComparacaoTroca = (
        ['I-2','I1'], ['I-2','I2'], ['I-3','I3'], ['I-4','I4'], ['I-5','I5'], ['I-6','I6'], ['I-7','I7'], ['I-8','I8'], ['I-9','I9'], ['I-10','I10'],
        ['I1','I1'], ['I2','I2'], ['I3','I3'], ['I4','I4'], ['I5','I5'], ['I6','I6'], ['I7','I7'], ['I8','I8'], ['I9','I9'], ['I10','I10'],
        ['I01','I1'], ['I02','I2'], ['I03','I3'], ['I04','I4'], ['I05','I5'], ['I06','I6'], ['I07','I7'], ['I08','I8'], ['I09','I9'], ['I010','I10'],
        ['I-01','I1'], ['I-02','I2'], ['I-03','I3'], ['I-04','I4'], ['I-05','I5'], ['I-06','I6'], ['I-07','I7'], ['I-08','I8'], ['I-09','I9'], ['I-010','I10'],
        ['S-1','S1'], ['S-2','S2'], ['S-3','S3'], ['S-4','S4'], ['S-5','S5'], ['S-6','S6'], ['S-7','S7'], ['S-8','S8'], ['S-9','S9'], ['S-10','S10'],
        ['S1','S1'], ['S2','S2'], ['S3','S3'], ['S4','S4'], ['S5','S5'], ['S6','S6'], ['S7','S7'], ['S8','S8'], ['S9','S9'], ['S10','S10'], 
        ['S01','S1'], ['S02','S2'], ['S03','S3'], ['S04','S4'], ['S05','S5'], ['S06','S6'], ['S07','S7'], ['S08','S8'], ['S09','S9'], ['S010','S10'], 
        ['S-01','S1'], ['S-02','S2'], ['S-03','S3'], ['S-04','S4'], ['S-05','S5'], ['S-06','S6'], ['S-07','S7'], ['S-08','S8'], ['S-09','S9'], ['S-010','S10'], 
        ['ANFITEATRO','Anfiteatro'], ['ANTE SALA I10','Ante I-10'], ['MULTIUSO','Multi.'], ['LAB NEI 2','Lab.NEI-2'], ['LAB NEI','Lab.NEI-1'], 
        ['LAB QUI','Lab.Quim.'], ['LAB QUIM','Lab.Quim.'], ['LAB QUIMICA','Lab.Quim.'], 
        ['LAB SS','Lab.SS'], ['LAB FIS','Lab.Fis-1'], ['LAB FISICA','Lab.Fis-1'], ['LAB OND','Lab.Ond'], ['LAB ELET','Lab.Eletr.'], 
        ['LAB ELETR','Lab.Eletr.'], ['LAB MAT','Lab.Mater.'], ['MOCAP','Mocap'], ['LAB TERMOFLUIDOS','Lab.Termoflui.'], 
        ['LAB TERMODINÂMICA','Lab.Termodin.'], ['LAB LDS','Lab.LDS'], ['CONTEINER 4','Cont-4'], ['CONTEINER 04','Cont-4'], 
        ['LAB SHP','Cont-8-SHP'], ['CONTAINER Nº 17','Cont-17'], ['LDTEA SALA 2','LD.Sala-2'], ['SALA 2','LD.Sala-2'], 
        ['LDTEA SALA 3','LD.Sala-3'], ['SALA 3','LD.Sala-3']) 
    # ==========================================================================================================
    # encontra as variantes dos nomes das salas e armazena em local_separado
    local_separado=re.findall('[SI]\d+|[SI]-\d+|[SI]0\d+|[SI]-0\d+|ANTE SALA I10|LAB NEI 2|LAB NEI|LAB SS|Lab SS|LAB MAT|LAB SHP|LAB ELETR|LAB ELET|MOCAP|LAB OND|LAB FISICA|LAB QUI|LAB QUIMICA|LAB TERMOFLUIDOS|LAB TERMODI\w+|ANFITEATRO|MULTIUSO|CONTEINER \d+\d+|CONTAINER \d+\d+|CONTEINER Nº \d+\d+|CONTAINER Nº \d+\d+|SALA \d+',
        local)
    # ==========================================================================================================
    # verifica a quantidade de salas ocupadas pela disciplina da linha em questão
    qtde_salas_ocupadas = len(local_separado)
    # ==========================================================================================================
    # seta o flag que verifica se a variante da sala nao esta na matriz de comparacao como false
    encontrou_nome_padrao = False
    
    for i in range(qtde_salas_ocupadas):
        for j in range(len(matrizComparacaoTroca)):
            if local_separado[i] == matrizComparacaoTroca[j][0]:
                local_separado[i] = matrizComparacaoTroca[j][1]                    
                encontrou_nome_padrao = True
                break
        # ==================================================================================================
        # se nao encontrou a variante da sala na matriz de comparacao, escreve no campo
        # uma mensagem para verificacao e futura correcao da matriz de comparacao
        if encontrou_nome_padrao == False:
            local_separado[i] = 'sala nao padronizada na matriz de comparacao - ' + local_separado 

    return local_separado
# ==============================================================================================================
# fim metodo separaSala
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
    # chama o metodo que separa as salas compostas
    dfSigaa = adicionarLinhasPorHorarioSalasSeparadas(dfSigaa)
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('./testes/csvTesteSalasHorariosSeparadas.csv', encoding="utf-8", sep=';', index = False)
    
# ==============================================================================================================
# fim main
# ==============================================================================================================