import os
import subprocess

import mTextos
import mCircuito
import m2301
import mFunctions
import mDrawio
import mActions
import mTopologiaModular

def mainFlow():
    
    tip = ""
    while (tip != "0"):
        os.system('cls')
        tip = input(f"""###############################
#      GERADOR CIRCUITO       #
###############################
#     Opções Disponíveis      #
# 0 - Sair                    #
# 1 - Circuito                #
# 2 - Upgrade                 #
# 3 - Topologia Modular       #
###############################
# Escolhido: """)
        
        if(tip == "1"):
            mActions.gerarCircuitoPadrao()
        if(tip == "2"):
            mActions.gerarUpgradePadrao()
        if(tip == "3"):
            mTopologiaModular.gerarTopologiaModular()
    
    mainFlow()
  
mainFlow()  