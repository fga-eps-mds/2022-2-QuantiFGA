
from datetime import datetime
from separarSalasCompostasEHorarios import *
import pandas as pd


if __name__ == '__main__':
    

    listaEntradaHorarios = ["46T23","24M12","24M34","2T12"]
    listaSaidaHorarios = [['4T2','4T3','6T2','6T3'],['2M1','2M2','4M1','4M2'] ,['2M3','2M4','4M3','4M4'] ,['2T1','2T2']]

    
    
    resultado0 = separaHorario(listaEntradaHorarios[0])
    resultado1 = separaHorario(listaEntradaHorarios[1])
    resultado2 = separaHorario(listaEntradaHorarios[2])
    resultado3 = separaHorario(listaEntradaHorarios[3])

    print(resultado0,resultado1,resultado2,resultado3)



   