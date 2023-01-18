# ==============================================================================================================
# area dos imports - bibliotecas e funcoes
# ==============================================================================================================
import csv  # biblioteca utilizada para ler e escrever arquivos csv
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ==============================================================================================================
# metodo gerarCsv
# ---------------
# funcao que gera os arquivos csv com apenas os nomes das colunas
# ==============================================================================================================
def gerarCsv():
    # ==========================================================================================================
    # criacao dos arquivos csv que receberao os dados coletados e desprezados
    # ==========================================================================================================
    # csv com dados da FGA
    with open('./csvDadosColetados.csv', 'w', newline='', encoding="utf-8") as csvDadosColetados:
        csv.writer(csvDadosColetados, delimiter=';').writerow(
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
        csvDadosColetados.close()
    # ==========================================================================================================
    # csv com dados que nao sao da FGA - so para conferencia
    with open('./csvDadosDesprezados.csv', 'w', newline='', encoding="utf-8") as csvDadosDesprezados:
        csv.writer(csvDadosDesprezados, delimiter=';').writerow(
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
        csvDadosDesprezados.close()
    
# ==============================================================================================================
# fim metodo gerarCsv
# ==============================================================================================================


# ==============================================================================================================
# metodo gerarConsulta
# --------------------------------------------------------------------------------------------------------------
# funcao que preeenche os campos da pagina Sigaa para fazer a consulta
# ==============================================================================================================
def gerarConsulta(nivel, depto, ano, periodo, dados):
    # ==========================================================================================================
    # Configuração do navegador (Chrome)
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # A seguinte funcao acessa a URL do SIGAA, em que será realizado o web scraping
    url = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino'
    navegador.get(url)
    # ==========================================================================================================
    # Seleciona os valores dos campos para as consultas
    navegador.find_element(By.NAME, 'formTurma:inputNivel').send_keys(nivel)
    navegador.find_element(By.NAME, 'formTurma:inputDepto').send_keys(depto)
    navegador.find_element(By.NAME, 'formTurma:inputAno').clear()
    navegador.find_element(By.NAME, 'formTurma:inputAno').send_keys(ano)
    navegador.find_element(By.NAME, 'formTurma:inputPeriodo').send_keys(periodo)
    # Clica no botao buscar para visualizar o resultado da consulta
    navegador.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11').click()
    # ==========================================================================================================
    # espera pagina carregar
    time.sleep(2)
    # captura os dados
    capturarDados(navegador, dados)
    # Fecha o navegador
    navegador.quit()
    # imprime a hora para checar o tempo de coleta
    print(datetime.now())
    return dados
# ==============================================================================================================
# fim metodo gerarConsulta
# ==============================================================================================================


# ==============================================================================================================
# metodo capturarDados
# --------------------------------------------------------------------------------------------------------------
# funcao que captura os dados da pagina Sigaa e armazena em uma lista
# ==============================================================================================================
def capturarDados(navegador, dados):
    # ==========================================================================================================
    # armazena a tabela inteira
    lista = navegador.find_elements(
        By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr')
    # ==========================================================================================================
    # encontra os elementos da pagina e armazena em listas de acordo com o tipo
    # ==========================================================================================================
    # armazena os codigos das turmas
    listaCodigoTurma = navegador.find_elements(By.CLASS_NAME, "turma")
    # armazena os nomes dos professores e a carga horaria das disciplinas
    listaProfCargaHor = navegador.find_elements(By.CLASS_NAME, "nome")
    # armazena os anos e semestres das disciplinas
    listaAnoSemestre = navegador.find_elements(By.CLASS_NAME, "anoPeriodo")
    # armazena os horarios das disciplinas
    listaHorario = (navegador.find_elements(
        By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr//td[4]"))
    # armazena as quantidades de vagas ofertadas
    listaVagasOfertadas = navegador.find_elements(
        By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr/td[6]')
    # armazena as quantidades de vagas ocupadas
    listaVagasOcupadas = navegador.find_elements(
        By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')
    # armazena os locais das disciplinas
    listaLocal = (navegador.find_elements(
        By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr//td[8]"))
    # ==========================================================================================================
    # inicializa os indices das listas que receberao os dados
    indLinhaAcumulada = 0
    indCabecalhoAtual = 0
    # ==========================================================================================================
    # percorre a tabela inteira armazenada procurando os cabecalhos e as linhas de turmas
    for linhaAtual in lista:
        # verifica se eh cabecalho da disciplina
        if linhaAtual.get_attribute("class") == 'agrupador':
            # armazena o codigo e o nome da materia
            linhaCabecalho = linhaAtual.find_elements(
                By.XPATH, "//span[@class='tituloDisciplina']")[indCabecalhoAtual]
            codigoNomeMateria = linhaCabecalho.get_attribute('innerHTML')
            # incrementa o indice que percorre a lista de linhas de cabecalho
            indCabecalhoAtual += 1
        # turmas do mesmo cabecalho estao agrupadas em Linha Par e LinhaImpar
        if linhaAtual.get_attribute("class") == 'linhaPar' or linhaAtual.get_attribute("class") == 'linhaImpar':
            # armazena o local tirando os espacos em branco do inicio e do fim
            local = listaLocal[indLinhaAcumulada].get_attribute(
                'innerText').strip()
            # armazena o nome do professor e a carga horaria
            profCargaHor = listaProfCargaHor[indLinhaAcumulada].get_attribute(
                'innerHTML')
            # separa o nome do professora da carga horaria
            professor, cargahoraria = profCargaHor.split(" (")
            # retira o ultimo parenteses da carga horaria
            cargahoraria, _ = cargahoraria.split(")")
            # aramzena o codigo da turma como string
            codigoTurma = listaCodigoTurma[indLinhaAcumulada].get_attribute(
                'innerHTML')
            # armazena o ano e o semestre como string
            anoSemestre = listaAnoSemestre[indLinhaAcumulada].get_attribute(
                'innerHTML')
            # separa o ano do semestre
            ano, semestre = anoSemestre.split(".")
            # armazena o horario da disciplina
            horario = listaHorario[indLinhaAcumulada].get_attribute(
                'innerText').strip()
            # armazena a quantidade de vagas ofertadas como string
            vagasOfertadas = listaVagasOfertadas[indLinhaAcumulada].get_attribute(
                'innerHTML')
            # armazena a quantidade de vagas ocupadas como string
            vagasOcupadas = listaVagasOcupadas[indLinhaAcumulada].get_attribute(
                'innerHTML')
            # armazena os dados em uma lista
            # dados.append([codigoNomeMateria.encode('utf-8'), codigoTurma, ano, semestre, professor.encode('utf-8'),
            dados.append([codigoNomeMateria, codigoTurma, ano, semestre,
                          professor, cargahoraria, horario, vagasOfertadas, vagasOcupadas, local])
            # print(codigoNomeMateria, codigoTurma, ano, semestre,
            #      professor, cargahoraria, horario, vagasOfertadas, vagasOcupadas, local)
            # incrementa o indice que percorre a lista de elementos coletados
            indLinhaAcumulada += 1
    # ==========================================================================================================
    return dados

# ==============================================================================================================
# fim metodo capturarDados
# ==============================================================================================================
    

# ==============================================================================================================
# metodo salvarDadosCsv
# --------------------------------------------------------------------------------------------------------------
# funcao que salva os dados coletados no arquivo csv
# ==============================================================================================================
def salvarDadosCsv(dados):
    # salva no arquivo csv verificando se sao disciplinas da FGA ou nao
    # ==========================================================================================================
    # salva somente as que tem 'FGA' no campo 'local'
    # campo 'local' = dados[inidice][9]
    with open('./csvDadosColetados.csv', 'a', newline='', encoding="utf-8") as csvDadosColetados:
        for indice, _ in enumerate(dados):
            if 'FGA' in dados[indice][9]:
                csv.writer(csvDadosColetados, delimiter=';').writerow(
                    dados[indice])
    csvDadosColetados.close()
    # ==========================================================================================================
    # salva disciplinas que nao tem 'FGA' no campo 'local' apenas para checar depois
    # campo 'local' = dados[inidice][9]
    with open('./csvDadosDesprezados.csv', 'a', newline='', encoding="utf-8") as csvDadosDesprezados:
        for indice, _ in enumerate(dados):
            if 'FGA' not in dados[indice][9]:
                csv.writer(csvDadosDesprezados, delimiter=';').writerow(
                    dados[indice])
    csvDadosDesprezados.close()

    # ==========================================================================================================
    # le os dados do arquivo csv em um dataframe dfSigaa
    dfSigaa = pd.read_csv('csvDadosColetados.csv', encoding="utf-8",   sep=';')
    # ==========================================================================================================
    # cria um dataframe temporario que vai receber todas as linhas novas
    new_df = pd.DataFrame()
    new_df = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
    for i, row in dfSigaa.iterrows(): 
        row_copy = row.copy()  
        new_df.loc[len(new_df)] = row_copy
    # ==========================================================================================================
    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    new_df.to_csv('csvDadosColetados.csv', encoding="utf-8", sep=';', index = False)
    # ==========================================================================================================
    # teste
    new_df.to_csv('./testesUnitarios/csvTesteUnitDadosColetados.csv', encoding="utf-8", sep=';', index = False)

    print('# ===========================================================================')
    print('total de turmas coletadas: ')
    print(len(new_df))
    print('# ===========================================================================')

# ==============================================================================================================
# fim metodo salvarDadosCsv
# ==============================================================================================================


# ==============================================================================================================
# main
# --------------------------------------------------------------------------------------------------------------
# funcao principal que chama todos os metodos
# ==============================================================================================================
if __name__ == '__main__':
    # ==========================================================================================================
    # imprime a hora de inicio para checar o tempo de coleta
    print(datetime.now())
    # ==========================================================================================================
    # lista que vai receber todos os dados coletados para serem gravados no csv
    dados = []
    # ==========================================================================================================
    # gera os arquivos csv que receberao os dados
    gerarCsv()
    # ==========================================================================================================
    # gera a consulta preeenchendo os campos e clicando em buscar
    # e ja chama a funcao de capturar dados - coleta dados de seis departamentos
    gerarConsulta('GRADUAÇÃO', 'FACULDADE DO GAMA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'DEPTO CIÊNCIAS DA COMPUTAÇÃO - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE FÍSICA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE QUÍMICA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE ENGENHARIA MECANICA - BRASÍLIA', '2022', '2', dados)
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE MATEMÁTICA - BRASÍLIA', '2022', '2', dados)
    # ==========================================================================================================
    # salva os dados coletados no arquivo csv
    salvarDadosCsv(dados)
    # ==========================================================================================================
    # le os dados do arquivo csv em um dataframe dfSigaa
    dfSigaa = pd.read_csv('csvDadosColetados.csv', encoding="utf-8",   sep=';')
    # ==========================================================================================================
    # teste
    dfSigaa.to_csv('./testesUnitarios/csvTesteUnitDadosColetados.csv', encoding="utf-8", sep=';', index = False)
    # ==========================================================================================================
    # imprime a hora de fim para checar o tempo de coleta
    print(datetime.now())

# ==============================================================================================================
# fim main
# ==============================================================================================================