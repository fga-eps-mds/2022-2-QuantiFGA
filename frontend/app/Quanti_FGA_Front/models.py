from django.db import models

class sala(models.Model):
    codigNomeMateria = models.CharField(max_length=30)
    codigoTurma = models.CharField(max_length=30)
    ano = models.CharField(max_length=30)
    semestre = models.CharField(max_length=30)
    professor = models.CharField(max_length=30)
    cargahoraria = models.CharField(max_length=30)
    horario = models.CharField(max_length=30)
    vagasOfertadas = models.CharField(max_length=30)
    vagasOcupadas = models.CharField(max_length=30)
    local = models.CharField(max_length=30)
    horarioSeparado = models.CharField(max_length=30)
    percDisciplina = models.CharField(max_length=30)
    salaSeparada = models.CharField(max_length=30)
    predio = models.CharField(max_length=30)
    lotacao = models.CharField(max_length=30)
    percOcupacaoReal = models.CharField(max_length=30)
    percOcupacaoTotal = models.CharField(max_length=30)
    
    def __str__(self):
        return self.codigNomeMateria