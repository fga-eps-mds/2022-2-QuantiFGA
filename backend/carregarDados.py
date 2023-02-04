import csv                      # biblioteca utilizada para ler e escrever arquivos csv
import pandas as pd             # biblioteca utilizada para arquivos em dataframe
from datetime import datetime   # biblioteca utilizada para calcular o tempo do processo
import time                     # biblioteca utilizada para impor delay para carregamento do site
from selenium import webdriver  # configuracoes para abrir o navegador e capturar os dados
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def gerarCsv():
# funcao que gera os arquivos csv vazios apenas com os nomes das colunas

    with open('./testesUnitarios/csvTurmasColetadasFGA.csv', 'w', newline='', encoding="utf-8") as csvTurmasColetadasFGA:
        csv.writer(csvTurmasColetadasFGA, delimiter=';').writerow(['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        csvTurmasColetadasFGA.close()
    
    with open('./testesUnitarios/csvTurmasColetadasQueNaoSaoFGA.csv', 'w', newline='', encoding="utf-8") as csvTurmasColetadasQueNaoSaoDaFGA:
        csv.writer(csvTurmasColetadasQueNaoSaoDaFGA, delimiter=';').writerow(['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        csvTurmasColetadasQueNaoSaoDaFGA.close()
    # fim metodo gerarCsv

def gerarConsulta(nivel, depto, ano, periodo, listaTurmasColetadas):
# funcao que preeenche os campos da pagina Sigaa para fazer a consulta e chama a funcao para coletar os dados

    servico = Service(ChromeDriverManager().install())
    opcoes = webdriver.ChromeOptions()
    opcoes.add_experimental_option('excludeSwitches', ['enable-logging'])
    navegador = webdriver.Chrome(service=servico, options=opcoes)
    url = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino'
    navegador.get(url)
 
    navegador.find_element(By.NAME, 'formTurma:inputNivel').send_keys(nivel)
    navegador.find_element(By.NAME, 'formTurma:inputDepto').send_keys(depto)
    navegador.find_element(By.NAME, 'formTurma:inputAno').clear()
    navegador.find_element(By.NAME, 'formTurma:inputAno').send_keys(ano)
    navegador.find_element(By.NAME, 'formTurma:inputPeriodo').send_keys(periodo)
    navegador.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11').click()

    time.sleep(2)
    coletarTurmas(navegador, listaTurmasColetadas)
    navegador.quit()
    return listaTurmasColetadas
# fim metodo gerarConsulta

def coletarTurmas(navegador, listaTurmasColetadas):
# funcao que captura os dados da pagina Sigaa e armazena em uma lista

    # armazena a tabela inteira
    listaTodosElementosDaPagina = navegador.find_elements(By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr')
    # encontra os elementos da pagina e armazena em listas de acordo com o tipo
    listaCodigoTurma = navegador.find_elements(By.CLASS_NAME, "turma")
    listaProfCargaHor = navegador.find_elements(By.CLASS_NAME, "nome")
    listaAnoSemestre = navegador.find_elements(By.CLASS_NAME, "anoPeriodo")
    listaHorario = (navegador.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr//td[4]"))
    listaVagasOfertadas = navegador.find_elements(By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr/td[6]')
    listaVagasOcupadas = navegador.find_elements(By.XPATH, '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')
    listaLocal = (navegador.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr//td[8]"))

    indLinhaAcumulada = 0
    indCabecalhoAtual = 0

    for linhaAtual in listaTodosElementosDaPagina:
        # verifica se eh cabecalho da disciplina
        if linhaAtual.get_attribute("class") == 'agrupador':
            linhaCabecalho = linhaAtual.find_elements(By.XPATH, "//span[@class='tituloDisciplina']")[indCabecalhoAtual]
            codigoNomeMateria = linhaCabecalho.get_attribute('innerHTML')
            indCabecalhoAtual += 1
        # turmas do mesmo cabecalho estao agrupadas em Linha Par e LinhaImpar
        if linhaAtual.get_attribute("class") == 'linhaPar' or linhaAtual.get_attribute("class") == 'linhaImpar':
            local = listaLocal[indLinhaAcumulada].get_attribute('innerText').strip()
            profCargaHor = listaProfCargaHor[indLinhaAcumulada].get_attribute('innerHTML')
            professor, cargahoraria = profCargaHor.split(" (")
            cargahoraria, _ = cargahoraria.split(")")
            codigoTurma = listaCodigoTurma[indLinhaAcumulada].get_attribute('innerHTML')
            anoSemestre = listaAnoSemestre[indLinhaAcumulada].get_attribute('innerHTML')
            ano, semestre = anoSemestre.split(".")
            horario = listaHorario[indLinhaAcumulada].get_attribute('innerText').strip()
            vagasOfertadas = listaVagasOfertadas[indLinhaAcumulada].get_attribute('innerHTML')
            vagasOcupadas = listaVagasOcupadas[indLinhaAcumulada].get_attribute('innerHTML')
            listaTurmasColetadas.append([codigoNomeMateria, codigoTurma, ano, semestre, professor, cargahoraria, horario, vagasOfertadas, vagasOcupadas, local])
            indLinhaAcumulada += 1
            
    return listaTurmasColetadas
# fim metodo coletarTurmas
    
def salvarTurmasColetadasNoCsvFiltrandoFGA(listaTurmasColetadas):
# funcao que salva as turmas coletadas no arquivo csv verificando se sao disciplinas da FGA ou nao

    # salva somente as que tem 'FGA' no campo 'local' - dados[inidice][9]
    with open('./testesUnitarios/csvTurmasColetadasFGA.csv', 'a', newline='', encoding="utf-8") as csvTurmasColetadasFGA:
        for indice, _ in enumerate(listaTurmasColetadas):
            if 'FGA' in listaTurmasColetadas[indice][9]:   
                csv.writer(csvTurmasColetadasFGA, delimiter=';').writerow(listaTurmasColetadas[indice])
    csvTurmasColetadasFGA.close()

    # salva disciplinas que nao tem 'FGA' no campo 'local' - dados[indice][9] - para teste unitario
    with open('./testesUnitarios/csvTurmasColetadasQueNaoSaoFGA.csv', 'a', newline='', encoding="utf-8") as csvTurmasColetadasQueNaoSaoDaFGA:
        for indice, _ in enumerate(listaTurmasColetadas):
            if 'FGA' not in listaTurmasColetadas[indice][9]:
                csv.writer(csvTurmasColetadasQueNaoSaoDaFGA, delimiter=';').writerow(
                    listaTurmasColetadas[indice])
    csvTurmasColetadasQueNaoSaoDaFGA.close()
# fim metodo salvarTurmasColetadasNoCsvFiltrandoFGA
'''
if __name__ == '__main__':
# main - para testes isolados de cada metodo

    dataHoraInicioDoProcesso = datetime.now()
    
    gerarCsv()
    
    listaTurmasColetadas = []
    gerarConsulta('GRADUAÇÃO', 'FACULDADE DO GAMA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    print('Coleta do departamento FACULDADE DO GAMA - BRASÍLIA ok')
    
    gerarConsulta('GRADUAÇÃO', 'DEPTO CIÊNCIAS DA COMPUTAÇÃO - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    print('Coleta do departamento DEPTO CIÊNCIAS DA COMPUTAÇÃO - BRASÍLIA ok')
    
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE FÍSICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    print('Coleta do departamento INSTITUTO DE FÍSICA - BRASÍLIA ok')
    
    gerarConsulta('GRADUAÇÃO', 'INSTITUTO DE QUÍMICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    print('Coleta do departamento INSTITUTO DE QUÍMICA - BRASÍLIA ok')
    
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE ENGENHARIA MECANICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    print('Coleta do departamento DEPARTAMENTO DE ENGENHARIA MECANICA - BRASÍLIA ok')
    
    gerarConsulta('GRADUAÇÃO', 'DEPARTAMENTO DE MATEMÁTICA - BRASÍLIA', '2022', '2', listaTurmasColetadas)
    print('Coleta do departamento DEPARTAMENTO DE MATEMÁTICA - BRASÍLIA ok')
    
    # salvando dados em um arquivo .csv para uso em testes unitarios e em testes de metodos isolados
    salvarTurmasColetadasNoCsvFiltrandoFGA(listaTurmasColetadas)
    
    dataHoraFimDoProcesso = datetime.now()
    print(f'\nDuração do processo de coleta e carregamento das turmas:  {dataHoraFimDoProcesso - dataHoraInicioDoProcesso}\n')
# fim main
'''