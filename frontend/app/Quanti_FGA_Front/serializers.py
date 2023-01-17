from rest_framework import serializers
from Quanti_FGA_Front.models import sala

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model=sala
        fields=['codigNomeMateria','codigoTurma','ano','semestre','professor','cargahoraria','horario','vagasOfertadas','vagasOcupadas','local','horarioSeparado','percDisciplina','salaSeparada','predio','lotacao','percOcupacaoReal','percOcupacaoTotal']