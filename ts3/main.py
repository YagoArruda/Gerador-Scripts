import os
import subprocess

import mTextos
import mCircuito
import m2301
import mFunctions
import mDrawio
import mActions
import mTopologiaModular
import mLogin
import mCor

def mainFlow():
    mLogin.loading()
    tip = ""
    while (tip != "0"):
        os.system('cls')
        tip = input(f"""###############################
#      GERADOR CIRCUITO       #
###############################
#     Opções Disponíveis      #
# {mCor.vermelho("0")} - Sair                    #
# {mCor.verde("1")} - Circuito                #
# {mCor.azul("2")} - Upgrade                 #
# {mCor.amarelo("3")} - Topologia Modular       #
###############################
# Escolhido: """)
        
        if(tip == "1"):
            mActions.gerarCircuitoPadrao()
        if(tip == "2"):
            mActions.gerarUpgradePadrao()
        if(tip == "3"):
            mTopologiaModular.gerarTopologiaModular()
            
    mLogin.end()
  
mainFlow()