import csv
from pymongo import MongoClient


#seleciona a string de conexão
def alimentarBanco():

    #conectando ao banco pela string de conexão
    mongoClient = MongoClient('mongodb+srv://quanti_fga:projeto-sigaa@cluster0.fnaahap.mongodb.net/test') 
    #seleciona a tabela
    db = mongoClient.disciplinas
    #remove as informações passadas do banco
    db.segment.drop()

    header = ['codigNomeMateria','codigoTurma','ano','semestre','professor','cargahoraria','horario','vagasOfertadas','vagasOcupadas','local','horarioSeparado','percDisciplina','salaSeparada','predio','lotacao','percOcupacaoReal','percOcupacaoTotal']
    csvfile = open('csvDadosAtualizados.csv', 'r', encoding="utf8")
    #lendo o csv separando por semicolon
    reader = csv.DictReader(csvfile, delimiter=";")

    #adicionando ao banco linha por linha
    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]
            
        #print (row)
        db.segment.insert(row)

    print("Banco de dados atualizado com sucesso")


#main
alimentarBanco()
