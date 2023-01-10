# ==============================================================================================================
# area dos imports - bibliotecas e funcoes
# ==============================================================================================================
import pandas as pd
import re

# ==============================================================================================================
# metodo separarSalasCompostas
# --------------------------------------------------------------------------------------------------------------
# funcao que gera os arquivos csv com apenas os nomes das colunas
# ==============================================================================================================
def separarSalasCompostas(dfSigaa): 
    # ==========================================================================================================
    # criacao de um dataframe temporario que ira receber as novas linhas criadas pela separacao das salas
    dfSigaa_temporario = pd.DataFrame(columns=    
        ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
        'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local',
        'horarioSeparado','percDisciplina','salaSeparada','predio','lotacao',
        'percOcupacaoReal','percOcupacaoTotal'])
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
    # percorre todas as linhas do dataframe buscando salas compostas
    for i in range(len(dfSigaa)):
        # ==========================================================================================================
        # encontra as variantes dos nomes das salas e armazena em local_separado
        local_separado=re.findall('[SI]\d+|[SI]-\d+|[SI]0\d+|[SI]-0\d+|ANTE SALA I10|LAB NEI 2|LAB NEI|LAB SS|Lab SS|LAB MAT|LAB SHP|LAB ELETR|LAB ELET|MOCAP|LAB OND|LAB FISICA|LAB QUI|LAB QUIMICA|LAB TERMOFLUIDOS|LAB TERMODI\w+|ANFITEATRO|MULTIUSO|CONTEINER \d+\d+|CONTAINER \d+\d+|CONTEINER Nº \d+\d+|CONTAINER Nº \d+\d+|SALA \d+',
            dfSigaa["local"][i])
        # ==========================================================================================================
        # verifica a quantidade de salas ocupadas pela disciplina da linha em questão
        qtde_salas_ocupadas = len(local_separado)
        # ==========================================================================================================
        # seta o flag que verifica se a variante da sala nao esta na matriz de comparacao como false
        encontrou_nome_padrao = False
        # ==========================================================================================================
        # se houver mais de uma sala ocupada, cria novas linhas no dataframe, 
        # uma para cada sala diferente, ja com o nome padrao da sala
        if qtde_salas_ocupadas > 1:
            # repete para cada sala diferente encontrada
            for k in range(qtde_salas_ocupadas):
                # procura o nome padrao da sala na matriz de comparacao
                for j in range(len(matrizComparacaoTroca)):
                    #print(local_separado[k], matrizComparacaoTroca[j][0])
                    if local_separado[k] == matrizComparacaoTroca[j][0]:
                        dfSigaa_temporario.loc[len(dfSigaa_temporario)] = [
                            dfSigaa["codigNomeMateria"][i], dfSigaa["codigoTurma"][i], dfSigaa["ano"][i],
                            dfSigaa["semestre"][i], dfSigaa["professor"][i], dfSigaa["cargahoraria"][i],
                            dfSigaa["horario"][i], dfSigaa["vagasOfertadas"][i], dfSigaa["vagasOcupadas"][i],
                            dfSigaa["local"][i], dfSigaa['horarioSeparado'][i], dfSigaa['percDisciplina'][i],
                            matrizComparacaoTroca[j][1], dfSigaa['predio'][i], dfSigaa['lotacao'][i],
                            dfSigaa['percOcupacaoReal'][i], dfSigaa['percOcupacaoTotal'][i]]
                        encontrou_nome_padrao = True
                        break
                # ==================================================================================================
                # se nao encontrou a variante da sala na matriz de comparacao, escreve no campo
                # uma mensagem para verificacao e futura correcao da matriz de comparacao
                if encontrou_nome_padrao == False:
                    dfSigaa_temporario.loc[len(dfSigaa_temporario)] = [
                        dfSigaa["codigNomeMateria"][i], dfSigaa["codigoTurma"][i], dfSigaa["ano"][i],
                        dfSigaa["semestre"][i], dfSigaa["professor"][i], dfSigaa["cargahoraria"][i],
                        dfSigaa["horario"][i], dfSigaa["vagasOfertadas"][i], dfSigaa["vagasOcupadas"][i],
                        dfSigaa["local"][i], dfSigaa['horarioSeparado'][i], dfSigaa['percDisciplina'][i],
                        'sala nao padronizada na matriz de comparacao - ' + local_separado[k], dfSigaa['predio'][i], dfSigaa['lotacao'][i],
                        dfSigaa['percOcupacaoReal'][i], dfSigaa['percOcupacaoTotal'][i]]    
            # ==========================================================================================================
        # se houver uma sala ocupada somente, apenas copia a linha, preenchendo com o nome padrao da sala
        if  qtde_salas_ocupadas == 1:
            # procura o nome padrao da sala na matriz de comparacao
            for j in range(len(matrizComparacaoTroca)):
                #print(local_separado[0], matrizComparacaoTroca[j][0])
                if local_separado[0] == matrizComparacaoTroca[j][0]:
                    dfSigaa_temporario.loc[len(dfSigaa_temporario)] = [
                        dfSigaa["codigNomeMateria"][i], dfSigaa["codigoTurma"][i], dfSigaa["ano"][i],
                        dfSigaa["semestre"][i], dfSigaa["professor"][i], dfSigaa["cargahoraria"][i],
                        dfSigaa["horario"][i], dfSigaa["vagasOfertadas"][i], dfSigaa["vagasOcupadas"][i],
                        dfSigaa["local"][i], dfSigaa['horarioSeparado'][i], dfSigaa['percDisciplina'][i],
                        matrizComparacaoTroca[j][1], dfSigaa['predio'][i], dfSigaa['lotacao'][i],
                        dfSigaa['percOcupacaoReal'][i], dfSigaa['percOcupacaoTotal'][i]]
                    encontrou_nome_padrao = True
                    break
            # ==========================================================================================================
            # se nao encontrou a variante da sala na matriz de comparacao, escreve no campo
            # uma mensagem para verificacao e futura correcao da matriz de comparacao
            if encontrou_nome_padrao == False:
                dfSigaa_temporario.loc[len(dfSigaa_temporario)] = [
                    dfSigaa["codigNomeMateria"][i], dfSigaa["codigoTurma"][i], dfSigaa["ano"][i],
                    dfSigaa["semestre"][i], dfSigaa["professor"][i], dfSigaa["cargahoraria"][i],
                    dfSigaa["horario"][i], dfSigaa["vagasOfertadas"][i], dfSigaa["vagasOcupadas"][i],
                    dfSigaa["local"][i], dfSigaa['horarioSeparado'][i], dfSigaa['percDisciplina'][i],
                    'sala nao padronizada na matriz de comparacao - ' + local_separado[0], dfSigaa['predio'][i], dfSigaa['lotacao'][i],
                    dfSigaa['percOcupacaoReal'][i], dfSigaa['percOcupacaoTotal'][i]]    
                
    return(dfSigaa_temporario) 


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
    dfSigaa_temporario = separarSalasCompostas(dfSigaa)
    # ==========================================================================================================
    # renomeia a coluna index que o dataframe incluiu 
    dfSigaa_temporario.index.name = 'indexDados'
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa_temporario.to_csv('./testes/csvTesteSalasSeparadas.csv', encoding="utf-8",   sep=';')

# ==============================================================================================================
# fim main
# ==============================================================================================================