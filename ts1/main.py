import os
import subprocess

import functions
import ts
import s2301

os.system('cls')

op = 0

menu = f"""####
# 1 - Circuito completo
# 2 - 2301
####"""

while(True):
    print(f"{menu}")
    op = input("Opcao desejada: ")
    if(functions.pode_ser_convertido_em_int(op)):
        op = int(op)
        if(op > 0 and op <= 2):
            break
  
if(op == 1):
    ts.config()
if(op == 2):
    s2301.config("-1","-1","-1","-1","-1","w","Arquivos/Receivers/2301.txt")
