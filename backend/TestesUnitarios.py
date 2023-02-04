import unittest
import pandas as pd
import os
from pandas.testing import assert_frame_equal
from preencherLotacaoSalas import preencherLotacaoPredio
from calcularPercentuais import calcularPercentuais
from separarSalasCompostasEHorarios import *
from carregarDados import *

class TesteColetaSigaa(unittest.TestCase):

    def testeCalcularPercentuais(self):
    # teste da funcao que calcula os percentuais de ocupacao das salas e preenche a informacao no dataframe

        dfExemploEntrada = pd.DataFrame()
        dfExemploEntrada = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', 'UAC', 130, '4T2 - Quarta 14h', 0, 0, 0]
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', 'UAC', 130, '4T3 - Quarta 15h', 0, 0, 0]
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', 'UAC', 60, '6T2 - Sexta 14h', 0, 0, 0]
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', 'UAC', 60, '6T3 - Sexta 15h', 0, 0, 0]
 
        dfExemploSaida = pd.DataFrame()
        dfExemploSaida = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', 'UAC', 130, '4T2 - Quarta 14h', 98.82352941176471, 64.61538461538461, 65.38461538461539]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', 'UAC', 130, '4T3 - Quarta 15h', 98.82352941176471, 64.61538461538461, 65.38461538461539]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', 'UAC', 60, '6T2 - Sexta 14h', 98.82352941176471, 140.0, 141.66666666666669]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', 'UAC', 60, '6T3 - Sexta 15h', 98.82352941176471, 140.0, 141.66666666666669]

        dfTesteResultado = calcularPercentuais(dfExemploEntrada)

        dfTesteResultado.to_csv('./testesUnitarios/csvTeste03Percentuais.csv', encoding="utf-8", sep=';', index = False)
        dfTesteResultado = pd.read_csv('./testesUnitarios/csvTeste03Percentuais.csv', encoding="utf-8",   sep=';')
        
        self.assertIsNone(assert_frame_equal(dfTesteResultado, dfExemploSaida))
    # fim do metodo testeCalcularPercentuais

    def testePreencherLotacaoPredio(self):
    # teste da funcao que preenche a lotacao das salas e o nome do predio ao qual ela pertence
    
        dfExemploEntrada = pd.DataFrame()
        dfExemploEntrada = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', '-', 0, '4T2 - Quarta 14h', 0, 0, 0]
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', '-', 0, '4T3 - Quarta 15h', 0, 0, 0]
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', '-', 0, '6T2 - Sexta 14h', 0, 0, 0]
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', '-', 0, '6T3 - Sexta 15h', 0, 0, 0]
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '6T3', 85, 84, 'FGA - SALA S-43', 'S43', '-', 0, '6T3 - Sexta 15h', 0, 0, 0]
        
        dfExemploSaida = pd.DataFrame()
        dfExemploSaida = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', 'UAC', 130, '4T2 - Quarta 14h', 0, 0, 0]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', 'UAC', 130, '4T3 - Quarta 15h', 0, 0, 0]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', 'UAC', 60, '6T2 - Sexta 14h', 0, 0, 0]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', 'UAC', 60, '6T3 - Sexta 15h', 0, 0, 0]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '6T3', 85, 84, 'FGA - SALA S-43', 'S43', 'sala nao encontrada - S43', 1, '6T3 - Sexta 15h', 0, 0, 0]
        
        dfTesteResultado = preencherLotacaoPredio(dfExemploEntrada)

        dfTesteResultado.to_csv('./testesUnitarios/csvTeste02LotacaoPredio.csv', encoding="utf-8", sep=';', index = False)
        dfTesteResultado = pd.read_csv('./testesUnitarios/csvTeste02LotacaoPredio.csv', encoding="utf-8",   sep=';')
        
        self.assertIsNone(assert_frame_equal(dfTesteResultado, dfExemploSaida))
    # fim do metodo testePreencherLotacaoPredio
    
    def testeSepararSalas(self):
    # teste da funcao que troca o nome da sala coletado pelo nome tabelado (padronizado) e
    # separa as salas quando houver mais de uma sala na mesma turma (salas compostas)

        listaExemploEntrada = ['FGA - SALA TESTE', 'FGA - SALA LAB SS', 'FGA - SALA S-4 e I-3','FGA - SALAS S7 e I7','FGA - SALA I6 E I7', 'FGA - SALA S1 E S4']

        listaExemploSaida = [['sala nao padronizada na matriz de comparacao - TESTE'],
                             ['Lab.SS'], ['S04','I03'], ['S07','I07'], ['I06','I07'], ['S01','S04']]
        
        listaTesteResultado0 = separarSalas(listaExemploEntrada[0])
        listaTesteResultado1 = separarSalas(listaExemploEntrada[1])
        listaTesteResultado2 = separarSalas(listaExemploEntrada[2])
        listaTesteResultado3 = separarSalas(listaExemploEntrada[3])
        listaTesteResultado4 = separarSalas(listaExemploEntrada[4])
        listaTesteResultado5 = separarSalas(listaExemploEntrada[5])
        listaTesteResultado = [listaTesteResultado0, listaTesteResultado1, listaTesteResultado2, 
                               listaTesteResultado3, listaTesteResultado4, listaTesteResultado5]
        
        self.assertEqual(listaTesteResultado, listaExemploSaida)
    # fim do metodo testeSepararSalas
    
    
    def testeSepararHorarios(self):
    # teste da funcao que separa os horarios por credito

        listaExemploEntrada = ['46T23','24M12','35M34','7M1234', '2N12', '28M51', '4T1', '2T45', '6N34','5T8']
        
        listaExemploSaida = [['4T2 - Quarta 14h','4T3 - Quarta 15h','6T2 - Sexta 14h','6T3 - Sexta 15h'],
                            ['2M1 - Segunda 08h','2M2 - Segunda 09h','4M1 - Quarta 08h','4M2 - Quarta 09h'] ,
                            ['3M3 - Terça 10h','3M4 - Terça 11h','5M3 - Quinta 10h','5M4 - Quinta 11h'] ,
                            ['7M1 - Sábado 08h','7M2 - Sábado 09h','7M3 - Sábado 10h','7M4 - Sábado 11h'],
                            ['2N1 - Segunda 19h','2N2 - Segunda 20h'],
                            ['2M5 - Segunda 12h', '2M1 - Segunda 08h', '8M5 - dia 12h', '8M1 - dia 08h'],
                            ['4T1 - Quarta 13h'],
                            ['2T4 - Segunda 16h','2T5 - Segunda 17h'],
                            ['6N3 - Sexta 21h','6N4 - Sexta 22h'],
                            ['5T8 - Quinta hora']]
        
        listaTesteResultado0 = separarHorarios(listaExemploEntrada[0])
        listaTesteResultado1 = separarHorarios(listaExemploEntrada[1])
        listaTesteResultado2 = separarHorarios(listaExemploEntrada[2])
        listaTesteResultado3 = separarHorarios(listaExemploEntrada[3])
        listaTesteResultado4 = separarHorarios(listaExemploEntrada[4])
        listaTesteResultado5 = separarHorarios(listaExemploEntrada[5])
        listaTesteResultado6 = separarHorarios(listaExemploEntrada[6])
        listaTesteResultado7 = separarHorarios(listaExemploEntrada[7])
        listaTesteResultado8 = separarHorarios(listaExemploEntrada[8])
        listaTesteResultado9 = separarHorarios(listaExemploEntrada[9])
        listaTesteResultado = [listaTesteResultado0, listaTesteResultado1, listaTesteResultado2, 
                                listaTesteResultado3, listaTesteResultado4, listaTesteResultado5,
                                listaTesteResultado6, listaTesteResultado7, listaTesteResultado8, listaTesteResultado9]

        self.assertEqual(listaTesteResultado, listaExemploSaida)
    # fim do metodo testeSepararHorarios

    def testeAdicionarLinhasPorHorarioComSalasSeparadas(self):
    # teste da funcao que chama os metodos que separam os horarios por credito e as salas compostas em salas simples

        dfExemploEntrada = pd.DataFrame()
        dfExemploEntrada = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        dfExemploEntrada.loc[len(dfExemploEntrada)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', '-', '-', 0, '-', 0, 0, 0]
        
        dfExemploSaida = pd.DataFrame()
        dfExemploSaida = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', '-', 0, '4T2 - Quarta 14h', 0, 0, 0]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S04', '-', 0, '4T3 - Quarta 15h', 0, 0, 0]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', '-', 0, '6T2 - Sexta 14h', 0, 0, 0]
        dfExemploSaida.loc[len(dfExemploSaida)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I03', '-', 0, '6T3 - Sexta 15h', 0, 0, 0]
        
        dfTesteResultado = adicionarLinhasPorHorarioComSalasSeparadas(dfExemploEntrada)

        dfTesteResultado.to_csv('./testesUnitarios/csvTeste01HorariosSalas.csv', encoding="utf-8", sep=';', index = False)
        dfTesteResultado = pd.read_csv('./testesUnitarios/csvTeste01HorariosSalas.csv', encoding="utf-8",   sep=';')

        self.assertIsNone(assert_frame_equal(dfTesteResultado, dfExemploSaida))
    # fim do metodo testeAdicionarLinhasPorHorarioComSalasSeparadas

    def testeSalvarTurmasColetadasNoCsvFiltrandoFGA(self):
    # teste da funcao que salva as turmas coletadas no arquivo csv verificando se sao disciplinas da FGA ou nao

        listaExemploEntrada = []
        listaExemploEntrada.append(['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', '-', '-', 0, '-', 0, 0, 0])
        listaExemploEntrada.append(['CDT1101 - TECNOLOGIA SOCIAL E INOVAÇÃO', 1, 2022, 2,'TANIA CRISTINA DA SILVA CRUZ','30h','6T1234 (25/10/2022 - 18/02/2023)', 40, 16,'CDT - Sala Interação', '-', '-', 0, '-', 0, 0, 0])

        listaExemploSaidaColetados = pd.DataFrame()
        listaExemploSaidaColetados = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        listaExemploSaidaColetados.loc[len(listaExemploSaidaColetados)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', '-', '-', 0, '-', 0, 0, 0]

        listaExemploSaidaDesprezados = pd.DataFrame()
        listaExemploSaidaDesprezados = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        listaExemploSaidaDesprezados.loc[len(listaExemploSaidaDesprezados)] = ['CDT1101 - TECNOLOGIA SOCIAL E INOVAÇÃO', 1,2022, 2,'TANIA CRISTINA DA SILVA CRUZ', '30h','6T1234 (25/10/2022 - 18/02/2023)',40,16,'CDT - Sala Interação', '-', '-', 0, '-', 0, 0, 0]
        
        salvarTurmasColetadasNoCsvFiltrandoFGA(listaExemploEntrada)
        
        listaTesteResultadoColetados = pd.read_csv('./testesUnitarios/csvTurmasColetadasFGA.csv', encoding="utf-8",   sep=';')
        listaTesteResultadoDesprezados = pd.read_csv('./testesUnitarios/csvTurmasColetadasQueNaoSaoFGA.csv', encoding="utf-8",   sep=';')

        self.assertIsNone(assert_frame_equal(listaTesteResultadoColetados, listaExemploSaidaColetados))
        self.assertIsNone(assert_frame_equal(listaTesteResultadoDesprezados, listaExemploSaidaDesprezados))
        self.assertEqual(all('FGA' in listaTesteResultadoColetados['local'].iloc[i] for i in range(len(listaTesteResultadoColetados))), True)
        self.assertEqual(all('FGA' not in listaTesteResultadoDesprezados['local'].iloc[i] for i in range(len(listaTesteResultadoDesprezados))), True)
    # fim do metodo testeSalvarTurmasColetadasNoCsvFiltrandoFGA

    def testeColetarTurmas(self):
    # teste da funcao que captura os dados da pagina Sigaa e armazena em uma lista

        servico = Service(ChromeDriverManager().install())
        opcoes = webdriver.ChromeOptions()
        opcoes.add_experimental_option('excludeSwitches', ['enable-logging'])
        navegador = webdriver.Chrome(service=servico, options=opcoes)
        url = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino'
        navegador.get(url)


        navegador.find_element(By.NAME, 'formTurma:inputNivel').send_keys('GRADUAÇÃO')
        navegador.find_element(By.NAME, 'formTurma:inputDepto').send_keys('CENTRO DE APOIO AO DESENVOLVIMENTO TECNOLÓGICO - BRASÍLIA')
        navegador.find_element(By.NAME, 'formTurma:inputAno').clear()
        navegador.find_element(By.NAME, 'formTurma:inputAno').send_keys('2022')
        navegador.find_element(By.NAME, 'formTurma:inputPeriodo').send_keys('2')
        navegador.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11').click()
        
        listaExemploSaida = []
        listaExemploSaida.append (['CDT1101 - TECNOLOGIA SOCIAL E INOVAÇÃO',' 01','2022','2','TANIA CRISTINA DA SILVA CRUZ','30h','6T1234 (25/10/2022 - 18/02/2023)','40','16','CDT - Sala Interação'])
        listaExemploSaida.append (['CDT1101 - TECNOLOGIA SOCIAL E INOVAÇÃO',' 01','2022','2','JONATHAS FELIPE AIRES FERREIRA','30h','6T1234 (25/10/2022 - 18/02/2023)','40','16','CDT - Sala Interação'])
        
        listaTesteResultado = []
        time.sleep(2)
        listaTesteResultado = coletarTurmas(navegador, listaTesteResultado)
        navegador.quit()
    
        self.assertEqual(listaTesteResultado, listaExemploSaida)
    # fim do metodo testeColetarTurmas

    def testeGerarConsultas(self):
    # teste da funcao que preeenche os campos da pagina Sigaa para fazer a consulta e chama a funcao para coletar os dados

        listaExemploSaida = []
        listaExemploSaida.append (['CDT1101 - TECNOLOGIA SOCIAL E INOVAÇÃO',' 01','2022','2','TANIA CRISTINA DA SILVA CRUZ','30h','6T1234 (25/10/2022 - 18/02/2023)','40','16','CDT - Sala Interação'])
        listaExemploSaida.append (['CDT1101 - TECNOLOGIA SOCIAL E INOVAÇÃO',' 01','2022','2','JONATHAS FELIPE AIRES FERREIRA','30h','6T1234 (25/10/2022 - 18/02/2023)','40','16','CDT - Sala Interação'])
        
        listaTesteResultado = []
        listaTesteResultado = gerarConsulta('GRADUAÇÃO', 'CENTRO DE APOIO AO DESENVOLVIMENTO TECNOLÓGICO - BRASÍLIA', '2022', '2', listaTesteResultado)

        self.assertEqual(listaTesteResultado, listaExemploSaida)
    # fim do metodo testeGerarConsultas

    def testeGerarCsv(self):
    # teste da funcao que gera os arquivos csv vazios apenas com os nomes das colunas
        
        dfExemploSaida = pd.DataFrame()
        dfExemploSaida = pd.DataFrame(columns=['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor', 'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'salaSeparada', 'predio','lotacao', 'horarioSeparado', 'percDisciplina', 'percOcupacaoReal','percOcupacaoTotal'])
        #Dataframe vazio de exemplo de saida
        dataframeCsv = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])

        gerarCsv()
        self.assertEqual(os.path.exists('./testesUnitarios/csvTurmasColetadasFGA.csv'), True)
        self.assertEqual(os.path.exists('./testesUnitarios/csvTurmasColetadasQueNaoSaoFGA.csv'), True)

        dfTesteResultadoColetados = pd.read_csv('./testesUnitarios/csvTurmasColetadasFGA.csv', encoding="utf-8",   sep=';')
        dfTesteResultadoDesprezados = pd.read_csv('./testesUnitarios/csvTurmasColetadasQueNaoSaoFGA.csv', encoding="utf-8",   sep=';')

        self.assertEqual(dataframeCsv.empty, dfTesteResultadoColetados.empty)
        self.assertEqual(dataframeCsv.empty, dfTesteResultadoDesprezados.empty)
        
        self.assertIsNone(assert_frame_equal(dfTesteResultadoColetados, dfExemploSaida))
        self.assertIsNone(assert_frame_equal(dfTesteResultadoDesprezados, dfExemploSaida))
    # fim do metodo testeGerarCsv

# fim da classe TesteColetaSigaa

if __name__ == '__main__':

    unittest.main()
    # fim do metodo main
