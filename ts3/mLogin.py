import os
import subprocess
import time
import mCor

def loading():
    carregado = 10
    while (carregado < 100):
        os.system('cls')
        print(f"""##################################################
#           TS - Topology System - 3.4           #
##################################################
#     By: {mCor.amarelo("Yago A")}                                 #
#                                                #
#     Loading/> {mCor.amarelo(f"{carregado}")}%                              #
#                                                #
# Access for help:                               #
# {mCor.verde("https://github.com/YagoArruda/Gerador-Scripts")}  #
##################################################""")
        carregado = carregado + 25
        time.sleep(1)
    
    
    
    
    