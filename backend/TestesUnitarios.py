# ==========================================================================================
# area dos import - bibliotecas e funcoes
# ==========================================================================================
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from preencherLotacaoSalas import preencherLotacaoPredio
from calcularPercentuais import calcularPorcentagens
from separarSalasCompostasEHorarios import *

# ======================================================================================================
# cria um dataframe de exemplo de entrada de dados coletados
dfSigaaDadosColetados = []
dfSigaaDadosColetados = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
dfSigaaDadosColetados.loc[len(dfSigaaDadosColetados)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', '-', '-', 0, '-', 0, 0, 0]


# ======================================================================================================
# cria uma lista com exemplos de horários
listaEntradaHorarios = ["46T23","24M12","24M34","2T12"]

# ======================================================================================================
# cria uma lista com exemplos de salas
listaEntradaSalas = ['FGA - SALA S-4 e I-3','FGA - SALAS S7 e I7','FGA - SALA I6 E I7', 'FGA - SALA S1 E S4']

# ======================================================================================================
# cria um dataframe de exemplo de saida de dados ja com horarios separados
dfSigaaSalasHorariosSeparadas = []
dfSigaaSalasHorariosSeparadas = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
dfSigaaSalasHorariosSeparadas.loc[len(dfSigaaSalasHorariosSeparadas)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S4', '-', 0, '4T2', 0, 0, 0]
dfSigaaSalasHorariosSeparadas.loc[len(dfSigaaSalasHorariosSeparadas)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S4', '-', 0, '4T3', 0, 0, 0]
dfSigaaSalasHorariosSeparadas.loc[len(dfSigaaSalasHorariosSeparadas)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I3', '-', 0, '6T2', 0, 0, 0]
dfSigaaSalasHorariosSeparadas.loc[len(dfSigaaSalasHorariosSeparadas)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I3', '-', 0, '6T3', 0, 0, 0]
# ======================================================================================================
# cria um dataframe de exemplo de saida de dados ja com horarios e salas separadas e Horario e predio preenchidos
dfSigaaLotacaoPredio = []
dfSigaaLotacaoPredio = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
dfSigaaLotacaoPredio.loc[len(dfSigaaLotacaoPredio)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S4', 'UAC', 130, '4T2', 0, 0, 0]
dfSigaaLotacaoPredio.loc[len(dfSigaaLotacaoPredio)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S4', 'UAC', 130, '4T3', 0, 0, 0]
dfSigaaLotacaoPredio.loc[len(dfSigaaLotacaoPredio)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I3', 'UAC', 60, '6T2', 0, 0, 0]
dfSigaaLotacaoPredio.loc[len(dfSigaaLotacaoPredio)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I3', 'UAC', 60, '6T3', 0, 0, 0]
# ======================================================================================================
# cria um dataframe de exemplo de saida de dados ja com horarios e salas separadas, 
# Horario e predio preenchidos e percentuais calculados
dfSigaaPorcentagens = []
dfSigaaPorcentagens = pd.DataFrame(columns=    
            ['codigNomeMateria', 'codigoTurma', 'ano', 'semestre', 'professor',
            'cargahoraria', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local','salaSeparada',
            'predio','lotacao', 'horarioSeparado', 'percDisciplina',
            'percOcupacaoReal','percOcupacaoTotal'])
dfSigaaPorcentagens.loc[len(dfSigaaPorcentagens)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S4', 'UAC', 130, '4T2', 98.82352941176471, 64.61538461538461, 65.38461538461539]
dfSigaaPorcentagens.loc[len(dfSigaaPorcentagens)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'S4', 'UAC', 130, '4T3', 98.82352941176471, 64.61538461538461, 65.38461538461539]
dfSigaaPorcentagens.loc[len(dfSigaaPorcentagens)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I3', 'UAC', 60, '6T2', 98.82352941176471, 140.0, 141.66666666666669]
dfSigaaPorcentagens.loc[len(dfSigaaPorcentagens)] = ['FGA0003 - COMPILADORES 1', 1, 2022, 2, 'EDSON ALVES DA COSTA JUNIOR', '60h', '46T23', 85, 84, 'FGA - SALA S-4 e I-3', 'I3', 'UAC', 60, '6T3', 98.82352941176471, 140.0, 141.66666666666669]
# ======================================================================================================
# cria uma lista com exemplos de horarios separados de saida
# separaHoraio

listaSaidaHorarios = [['4T2','4T3','6T2','6T3'],['2M1','2M2','4M1','4M2'] ,['2M3','2M4','4M3','4M4'] ,['2T1','2T2']]
# ======================================================================================================
# cria uma lista com exemplos de salas separadas de saida

listaSaidaSalas = [['S4','I3'], ['S7','I7'], ['I6','I7'], ['S1','S4']]

# ==============================================================================================================
# classe TesteColetaSigaaPublico
# --------------------------------------------------------------------------------------------------------------
# classe que contem os testes unitarios dos metodos do web scrapping
# ==============================================================================================================
class TesteColetaSigaaPublico(unittest.TestCase):

	# Metodo de teste unitario para verificar o  metodo separarSalasCompostas
	def testeSepararSalasCompostasEHorarios(self):
		print(dfSigaaDadosColetados.head())
		print(dfSigaaSalasHorariosSeparadas.head())
		dfTesteResultado = adicionarLinhasPorHorarioSalasSeparadas(dfSigaaDadosColetados)
		dfTesteResultado.to_csv('./testesUnitarios/csvTeste1.csv', encoding="utf-8", sep=';', index = False)
		dfTesteResultadoObtido = pd.read_csv('./testesUnitarios/csvTeste1.csv', encoding="utf-8",   sep=';')
		dfTesteResultadoEsperado = dfSigaaSalasHorariosSeparadas
		
		self.assertIsNone(assert_frame_equal(dfTesteResultadoObtido, dfTesteResultadoEsperado))
	# =========================================================================================================

	# Metodo de teste unitario para verificar o metodo preencherLotacaoPredio
	def testePreencherLotacaoPredio(self):
		print(dfSigaaSalasHorariosSeparadas.head())
		print(dfSigaaLotacaoPredio.head())
		dfTesteResultado = preencherLotacaoPredio(dfSigaaSalasHorariosSeparadas)
		dfTesteResultado.to_csv('./testesUnitarios/csvTeste2.csv', encoding="utf-8", sep=';', index = False)
		dfTesteResultadoObtido = pd.read_csv('./testesUnitarios/csvTeste2.csv', encoding="utf-8",   sep=';')
		dfTesteResultadoEsperado = dfSigaaLotacaoPredio
		
		self.assertIsNone(assert_frame_equal(dfTesteResultadoObtido, dfTesteResultadoEsperado))
	# =========================================================================================================

	# Metodo de teste unitario para verificar o metodo calcularPorcentagens
	def testeCalcularPorcentagens(self):
		print(dfSigaaLotacaoPredio.head())
		print(dfSigaaPorcentagens.head())
		dfTesteResultado = calcularPorcentagens(dfSigaaLotacaoPredio)
		dfTesteResultado.to_csv('./testesUnitarios/csvTeste3.csv', encoding="utf-8", sep=';', index = False)
		dfTesteResultadoObtido = pd.read_csv('./testesUnitarios/csvTeste3.csv', encoding="utf-8",   sep=';')
		dfTesteResultadoEsperado = dfSigaaPorcentagens
		
		self.assertIsNone(assert_frame_equal(dfTesteResultadoObtido, dfTesteResultadoEsperado))
	# =========================================================================================================
	# Metodo de teste unitario para verificar o metodo separarHorario

	def testeSepararHoraio(self):
		resultadoEsperado = listaSaidaHorarios
		resultado0 = separaHorario(listaEntradaHorarios[0])
		resultado1 = separaHorario(listaEntradaHorarios[1])
		resultado2 = separaHorario(listaEntradaHorarios[2])
		resultado3 = separaHorario(listaEntradaHorarios[3])
		resultadoObtido = [resultado0,resultado1,resultado2,resultado3]

		self.assertEqual(resultadoEsperado, resultadoObtido)
	# =========================================================================================================
	# Metodo de teste unitario para verificar o metodo separa Sala
	def testeSeparaSalas(self):
		resultadoEsperado = listaSaidaSalas
		resultado0 = separaSala(listaEntradaSalas[0])
		resultado1 = separaSala(listaEntradaSalas[1])
		resultado2 = separaSala(listaEntradaSalas[2])
		resultado3 = separaSala(listaEntradaSalas[3])
		resultadoObtido = [resultado0,resultado1,resultado2,resultado3]
		
		self.assertEqual(resultadoEsperado, resultadoObtido)
		

# main
# --------------------------------------------------------------------------------------------------------------
# funcao principal que chama todos os metodos
# ==============================================================================================================
if __name__ == '__main__':

	unittest.main()

#========================================================================================
