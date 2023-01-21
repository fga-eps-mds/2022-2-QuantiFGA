import csv
from pymongo import MongoClient


mongoClient = MongoClient('mongodb+srv://quanti_fga:projeto-sigaa@cluster0.fnaahap.mongodb.net/test') 
db = mongoClient.disciplinas
db.segment.drop()

header = ['codigNomeMateria','codigoTurma','ano','semestre','professor','cargahoraria','horario','vagasOfertadas','vagasOcupadas','local','horarioSeparado','percDisciplina','salaSeparada','predio','lotacao','percOcupacaoReal','percOcupacaoTotal']
csvfile = open('csvDadosAtualizados.csv', 'r', encoding="utf8")
reader = csv.DictReader(csvfile, delimiter=";")

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
        
    print (row)
    db.segment.insert(row)