import csv  # biblioteca utilizada para ler e escrever arquivos csv
import pandas as pd  # biblioteca utilizada para arquivos em dataframe
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# lista que vai receber todos os dados coletados para serem gravados no csv
dados = []

# csv com dados da FGA
with open('./csvDadosColetados.csv', 'w', newline='', encoding="utf-8") as csvDadosColetados:
    csv.writer(csvDadosColetados, delimiter=';').writerow(['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
                                                           'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local'])
    csvDadosColetados.close()
# csv com dados que nao sao da FGA - so para conferencia
with open('./csvDadosDesprezados.csv', 'w', newline='', encoding="utf-8") as csvDadosDesprezados:
    csv.writer(csvDadosDesprezados, delimiter=';').writerow(['codigoNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
                                                             'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local'])
    csvDadosDesprezados.close()


def gerarConsulta(nivel, depto, ano, periodo):

    # Configuração do navegador (Chrome)
    navegador = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    # A seguinte funcao acessa a URL do SIGAA, em que será realizado o web scraping
    url = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino'
    navegador.get(url)
    # Seleciona os valores dos campos para as consultas
    navegador.find_element(
        By.NAME, 'formTurma:inputNivel').send_keys(nivel)
    navegador.find_element(
        By.NAME, 'formTurma:inputDepto').send_keys(depto)
    navegador.find_element(
        By.NAME, 'formTurma:inputAno').send_keys(ano)
    navegador.find_element(
        By.NAME, 'formTurma:inputPeriodo').send_keys(periodo)
    # Clica no botao buscar para visualizar o resultado da consulta
    navegador.find_element(
        By.NAME, 'formTurma:j_id_jsp_1370969402_11').click()
    # espera pagina carregar
    time.sleep(10)
    # captura os dados
    capturarDados(navegador)
    # Fecha o navegador
    navegador.quit()
    # imprime a hora para checar o tempo de coleta
    print(datetime.now())


def capturarDados(navegador):

    # encontra os elementos da pagina e
    # armazena em listas de acordo com o tipo

    # armazena a tabela inteira
    lista = navegador.find_elements(
        By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr')

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

   # inicializa os indices das listas que receberao os dados
    indLinhaAcumulada = 0
    indCabecalhoAtual = 0

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

    return dados

def separaSalasCompostas(dfSigaa):
	# comandos
	# retorna para a main
    return(dfSigaa)

def preencheLotacaoSalas(dfSigaa):
	# comandos
	# retorna para a main
    return (dfSigaa)

def separaHorario(dfSigaa):
	# comandos
	# retorna para a main
    return (dfSigaa)

def calculaPorcentagens(dfSigaa):
	# comandos
	# retorna para a main
    return (dfSigaa)


# main
if __name__ == '__main__':

    # imprime a hora de inicio para checar o tempo de coleta
    print(datetime.now())
    
    # gera a consulta preeenchendo os campos e clicando em buscar
    # e ja chama a funcao de capturar dados
    # coleta dados de seis departamentos
    gerarConsulta('GRADUAÇÃO', 'FACULDADE DO GAMA - BRASÍLIA', '2022', '2')
    gerarConsulta(
        'GRADUAÇÃO', 'DEPTO CIÊNCIAS DA COMPUTAÇÃO - BRASÍLIA', '2022', '2')
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE FÍSICA - BRASÍLIA', '2022', '2')
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE QUÍMICA - BRASÍLIA', '2022', '2')
    gerarConsulta(
        'GRADUAÇÃO', 'DEPARTAMENTO DE ENGENHARIA MECANICA - BRASÍLIA', '2022', '2')
    gerarConsulta(
        'GRADUAÇÃO', 'DEPARTAMENTO DE MATEMÁTICA - BRASÍLIA', '2022', '2')

    # salva no arquivo csv verificando se sao disciplinas da FGA ou nao
    # salva somente as que tem 'FGA' no campo 'local'
    with open('./csvDadosColetados.csv', 'a', newline='', encoding="utf-8") as csvDadosColetados:
        for indice, _ in enumerate(dados):
            if 'FGA' in dados[indice][9]:
                csv.writer(csvDadosColetados, delimiter=';').writerow(
                    dados[indice])
    csvDadosColetados.close()

    # salva disciplinas que nao tem 'FGA' no campo 'local' apenas para checar depois
    with open('./csvDadosDesprezados.csv', 'a', newline='', encoding="utf-8") as csvDadosDesprezados:
        for indice, _ in enumerate(dados):
            if 'FGA' not in dados[indice][9]:
                csv.writer(csvDadosDesprezados, delimiter=';').writerow(
                    dados[indice])
    csvDadosDesprezados.close()
    
    # salva dados do arquivo csv em um dataframe dfSigaa
    dfSigaa = pd.read_csv('csvDadosColetados.csv', encoding="utf-8",   sep=';')
    # Cria novas colunas em um dataframe:
    dfSigaa['horarioSeparado'] = ''
    dfSigaa['percDisciplina'] = 0
    dfSigaa['salaSeparada'] = ''
    dfSigaa['predio'] = ''
    dfSigaa['lotacao'] = 0
    dfSigaa['percOcupacaoReal'] = 0
    dfSigaa['percOcupacaoTotal'] = 0
    # renomeia a coluna index que o dataframe incluiu
    dfSigaa.index.name = 'indexDados'

    # chama as funcoes para preencher os dados dessas novas colunas
    separaSalasCompostas(dfSigaa)
    preencheLotacaoSalas(dfSigaa)
    separaHorario(dfSigaa)
    calculaPorcentagens(dfSigaa)

    # cria um novo csv com o dataframe preenchido e atualizado com as novas informacoes
    dfSigaa.to_csv('csvDadosAtualizados.csv', encoding="utf-8",   sep=';')

    # imprime a hora de fim para checar o tempo de coleta
    print(datetime.now())
    
