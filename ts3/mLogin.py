import os
import subprocess
import time
import mCor

def loading():
    carregado = 10
    while (carregado < 100):
        os.system('cls')
        print(f"""##################################################
#        TS - Topology System - 3.5 - 5/25       #
##################################################
#     By: {mCor.amarelo("Yago A")}                                 #
#                                                #
#     Loading/> {mCor.amarelo(f"{carregado}")}%                              #
#                                                #
# Access for help:                               #
# {mCor.verde("https://github.com/YagoArruda/Gerador-Scripts")}  #
##################################################""")
        carregado = carregado + 35
        if(carregado > 100):
            carregado = 100
        time.sleep(1)

def end():
    os.system('cls')
    print(f"""##################################################
#        TS - Topology System - 3.5 - 5/25       #
##################################################""")
    
    
    
    
    