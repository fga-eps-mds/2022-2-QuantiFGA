import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

dados = []
with open('./teste.csv', 'w', newline='') as csvfile:
    csv.writer(csvfile, delimiter=';').writerow(['codigoMateria', 'nomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
                                                'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local'])
    csvfile.close()


def gerarConsulta(nivel, depto, ano, periodo):
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


def capturarDados(indLinhaAcumulada, codigoMateria, nomeMateria):
    # armazena os resultados de cada linha da consulta
    disciplina = navegador.find_elements(By.CLASS_NAME, "nome")[
        indLinhaAcumulada]
    profCargaHor = disciplina.get_attribute('innerHTML')
    codigoTurma = navegador.find_elements(
        By.CLASS_NAME, "turma")[indLinhaAcumulada].get_attribute('innerHTML')
    anoSemestre = navegador.find_elements(
        By.CLASS_NAME, "anoPeriodo")[indLinhaAcumulada].get_attribute('innerHTML')
    ano, semestre = anoSemestre.split(".")
    professor, cargahoraria = profCargaHor.split(" (")
    cargahoraria, _ = cargahoraria.split(")")
    horario = (navegador.find_elements(
        By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[indLinhaAcumulada].find_elements(By.XPATH, "//td[4]")[indLinhaAcumulada]).get_attribute('innerText').strip()
    vagasOfertadas = navegador.find_elements(
        By.XPATH,
        '//*[@id="turmasAbertas"]/table/tbody/tr/td[6]')[indLinhaAcumulada].get_attribute('innerHTML')
    vagasOcupadas = navegador.find_elements(
        By.XPATH,
        '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')[indLinhaAcumulada].get_attribute('innerHTML')
    local = (navegador.find_elements(
        By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[indLinhaAcumulada].find_elements(By.XPATH, "//td[8]")[indLinhaAcumulada]).get_attribute('innerHTML').strip()
    dados.append([codigoMateria, nomeMateria, codigoTurma, ano, semestre, professor,
                 cargahoraria, horario, vagasOfertadas, vagasOcupadas, local])
    print(dados[indLinhaAcumulada])
    csv.writer(csvfile, delimiter=';').writerow(dados[indLinhaAcumulada])
    return dados


# main
if __name__ == '__main__':

    # Configuração do navegador (Chrome)
    s = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=s)

    # A seguinte funcao acessa a URL do SIGAA, em que será realizado o web scraping
    url = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino'
    navegador.get(url)

    # espera pagina carregar
    # navegador.implicitly_wait(6)
    # gera a consulta preeenchendo os campos e clicando em buscar
    gerarConsulta('GRADUAÇÃO', 'FACULDADE DO GAMA - BRASÍLIA', '2022', '2')
    # espera pagina carregar
    # navegador.implicitly_wait(6)

    # captura os dados linha a linha
    # e um processo demorado
    indLinhaAtual = 0
    indLinhaAcumulada = 0
    indCabecalhoAtual = 0
    lista = navegador.find_elements(
        By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr')

    with open('./teste.csv', 'a', newline='') as csvfile:
        for linhaAtual in lista:
            # cabecalho da disciplina
            if linhaAtual.get_attribute("class") == 'agrupador':
                linhaCabecalho = linhaAtual.find_elements(
                    By.XPATH, "//span[@class='tituloDisciplina']")[indCabecalhoAtual]
                conteudo = linhaCabecalho.get_attribute('innerHTML')
                codigoMateria, nomeMateria = conteudo.split(" - ")
                indCabecalhoAtual += 1
            # turmas do mesmo cabecalho
            if linhaAtual.get_attribute("class") == 'linhaPar' or linhaAtual.get_attribute("class") == 'linhaImpar':
                capturarDados(indLinhaAcumulada, codigoMateria, nomeMateria)
                indLinhaAcumulada += 1
            indLinhaAtual += 1
        csvfile.close()

    # Fecha o navegador
    navegador.quit()
