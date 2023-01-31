import pandas as pd # biblioteca utilizada para dataframe
import re           # biblioteca utilizada para expressoes regulares

def adicionarLinhasPorHorarioComSalasSeparadas(dataframe):
# funcao que chama os metodos que separam os horarios por credito e as salas compostas em salas simples
 
    dfTempLinhasNovas = pd.DataFrame()
    dfTempLinhasNovas = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])

    for indiceDataframe, linhaDataframe in dataframe.iterrows():
        horariosSeparados = separarHorarios(linhaDataframe["horario"])
        locaisSeparados = separarSalas(linhaDataframe["local"])
        qtdeSalasOcupadas = len(locaisSeparados)
        qtdeHorariosSeparados = len(horariosSeparados)
        
        if qtdeSalasOcupadas == 1:
            for horario in horariosSeparados:
                linhaDfCopia = linhaDataframe.copy()
                linhaDfCopia["horarioSeparado"] = horario
                linhaDfCopia["salaSeparada"] = locaisSeparados[0]
                dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia

        # para turmas com duas salas e 4 creditos, pressupoe-se que as salas 
        # estejam na ordem dos dias da semana do horario
        # exemplo: 24T23 - I9 e S7 -> 2T2 e 2T3 na I9 e
        #                             4T2 e 4T3 na S7
        if qtdeSalasOcupadas == 2 and qtdeHorariosSeparados == 4:
            linhaDfCopia = linhaDataframe.copy()
            linhaDfCopia["horarioSeparado"] = horariosSeparados[0]
            linhaDfCopia["salaSeparada"] = locaisSeparados[0]
            dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia
            linhaDfCopia = linhaDataframe.copy()
            linhaDfCopia["horarioSeparado"] = horariosSeparados[1]
            linhaDfCopia["salaSeparada"] = locaisSeparados[0]
            dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia
            linhaDfCopia = linhaDataframe.copy()
            linhaDfCopia["horarioSeparado"] = horariosSeparados[2]
            linhaDfCopia["salaSeparada"] = locaisSeparados[1]
            dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia
            linhaDfCopia = linhaDataframe.copy()
            linhaDfCopia["horarioSeparado"] = horariosSeparados[3]
            linhaDfCopia["salaSeparada"] = locaisSeparados[1]
            dfTempLinhasNovas.loc[len(dfTempLinhasNovas)] = linhaDfCopia
                      
    return dfTempLinhasNovas
# fim metodo adicionarLinhasPorHorario

def separarHorarios(horario):
# Dado uma string horario no padrao [DIAS_DA_SEMANA][PERIODO][HORARIOS] 
# é retornado uma lista do horario separado por hora 
# [DIAS_DA_SEMANA] 2-7
# [PERIODO] manha = M, tarde = T, e noite = N
# [HORARIO] 1 a 5
# exemplo horario = 26T23 
#         retorno = ['2T2 - Segunda 14h', '2T3 - Segunda 15h', '6T2 - Sexta 14h', '6T3 - Sexta 15h']

    horariosDecompostos = horario.split() 
    horariosSeparados = []
    for indiceH in horariosDecompostos:
        horarioContemTurno = re.search("^(\d+)([M|T|N])(\d+)", indiceH) # encontra o M ou T ou N
        if horarioContemTurno:
            dias = [int(horarioContemTurno) for horarioContemTurno in horarioContemTurno.group(1)]
            turno = horarioContemTurno.group(2)
            horas = [int(horarioContemTurno) for horarioContemTurno in horarioContemTurno.group(3)]
            for cadaDia in dias:
                if cadaDia == 2:
                    cadaDiaTraduzido = 'Segunda'
                elif cadaDia == 3:
                    cadaDiaTraduzido = 'Terça'
                elif cadaDia == 4:
                    cadaDiaTraduzido = 'Quarta'
                elif cadaDia == 5:
                    cadaDiaTraduzido = 'Quinta'
                elif cadaDia == 6:
                    cadaDiaTraduzido = 'Sexta'
                elif cadaDia == 7:
                    cadaDiaTraduzido = 'Sábado' 
                else:
                    cadaDiaTraduzido = 'dia'
                for cadaHora in horas:
                    if (turno == 'M' and cadaHora == 1):
                        cadaHoraTraduzida = '08h'
                    elif (turno == 'M' and cadaHora == 2):
                        cadaHoraTraduzida = '09h'
                    elif (turno == 'M' and cadaHora == 3):
                        cadaHoraTraduzida = '10h'
                    elif (turno == 'M' and cadaHora == 4):
                        cadaHoraTraduzida = '11h'
                    elif (turno == 'M' and cadaHora == 5):
                        cadaHoraTraduzida = '12h'
                    elif (turno == 'T' and cadaHora == 1):
                        cadaHoraTraduzida = '13h'
                    elif (turno == 'T' and cadaHora == 2):
                        cadaHoraTraduzida = '14h'
                    elif (turno == 'T' and cadaHora == 3):
                        cadaHoraTraduzida = '15h'
                    elif (turno == 'T' and cadaHora == 4):
                        cadaHoraTraduzida = '16h'
                    elif (turno == 'T' and cadaHora == 5):
                        cadaHoraTraduzida = '17h'
                    elif (turno == 'T' and cadaHora == 6):
                        cadaHoraTraduzida = '18h'
                    elif (turno == 'N' and cadaHora == 1):
                        cadaHoraTraduzida = '19h'
                    elif (turno == 'N' and cadaHora == 2):
                        cadaHoraTraduzida = '20h'
                    elif (turno == 'N' and cadaHora == 3):
                        cadaHoraTraduzida = '21h'
                    elif (turno == 'N' and cadaHora == 4):
                        cadaHoraTraduzida = '22h'
                    else:
                        cadaHoraTraduzida = 'hora'
                    horariosSeparados.append(f'{cadaDia}{turno}{cadaHora} - {cadaDiaTraduzido} {cadaHoraTraduzida}')
        
    return horariosSeparados
# fim metodo separarHorario

def separarSalas(local): 
# funcao que troca o nome da sala coletado pelo nome tabelado (padronizado) e
# separa as salas quando houver mais de uma sala na mesma turma (salas compostas)

    matrizDeEquivalenciaNomeSalaPadronizado = (
        ['I-2','I01'], ['I-2','I02'], ['I-3','I03'], ['I-4','I04'], ['I-5','I05'], ['I-6','I06'], ['I-7','I07'], ['I-8','I08'], ['I-9','I09'], ['I-10','I10'],
        ['I1','I01'], ['I2','I02'], ['I3','I03'], ['I4','I04'], ['I5','I05'], ['I6','I06'], ['I7','I07'], ['I8','I08'], ['I9','I09'], ['I10','I10'],
        ['I01','I01'], ['I02','I02'], ['I03','I03'], ['I04','I04'], ['I05','I05'], ['I06','I06'], ['I07','I07'], ['I08','I08'], ['I09','I09'], ['I010','I10'],
        ['I-01','I01'], ['I-02','I02'], ['I-03','I03'], ['I-04','I04'], ['I-05','I05'], ['I-06','I06'], ['I-07','I07'], ['I-08','I08'], ['I-09','I09'], ['I-010','I10'],
        ['S-1','S01'], ['S-2','S02'], ['S-3','S03'], ['S-4','S04'], ['S-5','S05'], ['S-6','S06'], ['S-7','S07'], ['S-8','S08'], ['S-9','S09'], ['S-10','S10'],
        ['S1','S01'], ['S2','S02'], ['S3','S03'], ['S4','S04'], ['S5','S05'], ['S6','S06'], ['S7','S07'], ['S8','S08'], ['S9','S09'], ['S10','S10'], 
        ['S01','S01'], ['S02','S02'], ['S03','S03'], ['S04','S04'], ['S05','S05'], ['S06','S06'], ['S07','S07'], ['S08','S08'], ['S09','S09'], ['S010','S10'], 
        ['S-01','S01'], ['S-02','S02'], ['S-03','S03'], ['S-04','S04'], ['S-05','S05'], ['S-06','S06'], ['S-07','S07'], ['S-08','S08'], ['S-09','S09'], ['S-010','S10'], 
        ['ANFITEATRO','Anfiteatro'], ['ANTE SALA I10','Ante I-10'], ['MULTIUSO','Multi.'], ['LAB NEI 2','Lab.NEI-2'], ['LAB NEI','Lab.NEI-1'], 
        ['LAB QUI','Lab.Quim.'], ['LAB QUIM','Lab.Quim.'], ['LAB QUIMICA','Lab.Quim.'], 
        ['LAB SS','Lab.SS'], ['Lab SS','Lab.SS'], ['LAB FIS','Lab.Fis-1'], ['LAB FISICA','Lab.Fis-1'], ['LAB OND','Lab.Ond'], ['LAB ELET','Lab.Eletr.'], 
        ['LAB ELETR','Lab.Eletr.'], ['LAB MAT','Lab.Mater.'], ['MOCAP','Mocap'], ['LAB TERMOFLUIDOS','Lab.Termoflui.'], 
        ['LAB TERMODINÂMICA','Lab.Termodin.'], ['LAB LDS','Lab.LDS'], ['CONTEINER 4','Cont-4'], ['CONTEINER 04','Cont-4'], 
        ['LAB SHP','Cont-8-SHP'], ['CONTAINER Nº 17','Cont-17'], ['LDTEA SALA 2','LD.Sala-2'], ['SALA 2','LD.Sala-2'], 
        ['LDTEA SALA 3','LD.Sala-3'], ['SALA 3','LD.Sala-3']) 
    
    locaisContemSala = re.findall('[SI]\d+|[SI]-\d+|[SI]0\d+|[SI]-0\d+|ANTE SALA I10|LAB NEI 2|LAB NEI|LAB SS|Lab SS|LAB MAT|LAB SHP|LAB ELETR|LAB ELET|MOCAP|LAB OND|LAB FISICA|LAB QUI|LAB QUIMICA|LAB TERMOFLUIDOS|LAB TERMODI\w+|ANFITEATRO|MULTIUSO|CONTEINER \d+\d+|CONTAINER \d+\d+|CONTEINER Nº \d+\d+|CONTAINER Nº \d+\d+|SALA \d+',local)
    qtdeSalasOcupadas = len(locaisContemSala)
    
    encontrouNomePadraoSala = False
    
    for indiceQtdeSalas in range(qtdeSalasOcupadas):
        for indiceLinhaMatriz in range(len(matrizDeEquivalenciaNomeSalaPadronizado)):
            if locaisContemSala[indiceQtdeSalas] == matrizDeEquivalenciaNomeSalaPadronizado[indiceLinhaMatriz][0]:
                locaisContemSala[indiceQtdeSalas] = matrizDeEquivalenciaNomeSalaPadronizado[indiceLinhaMatriz][1]                    
                encontrouNomePadraoSala = True
                break
 
        if encontrouNomePadraoSala == False:
            locaisContemSala[indiceQtdeSalas] = 'sala nao padronizada na matriz de comparacao - ' + locaisContemSala 

    return locaisContemSala
# fim metodo separarSala


if __name__ == '__main__':
# main - para testes isolados de cada metodo
    
    dfTurmasColetadasFGA = pd.read_csv('./testesUnitarios/csvTurmasColetadasFGA.csv', encoding="utf-8",  sep=';') 
    
    dfTurmasColetadasFGA = adicionarLinhasPorHorarioComSalasSeparadas(dfTurmasColetadasFGA)
    
    dfTurmasColetadasFGA.to_csv('./testesUnitarios/csvTesteSalasHorariosSeparadas.csv', encoding="utf-8", sep=';', index = False)
# fim main