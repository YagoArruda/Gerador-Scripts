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
    os.system('cls')

    print("###############################")
    print("#      GERADOR CIRCUITO       #")
    print("###############################")
    print("#     Opções Disponíveis      #")
    print("# 1 - Circuito                #")
    print("# 2 - Upgrade                 #")
    print("###############################")

    opCir = mFunctions.validarProsseguir("# Gerar circuito?")
    if(opCir == False):
        opUp = mFunctions.validarProsseguir("# Gerar upgrade?")
    if(opUp == False):
        mTopologiaModular.gerarTopologiaModular()

    print("###############################")
    if(opCir == True):
        mActions.gerarCircuitoPadrao()
    if(opUp == True):
        mActions.gerarUpgradePadrao()

    if(opCir == opUp == False):
        mainFlow()
  
mainFlow()
    