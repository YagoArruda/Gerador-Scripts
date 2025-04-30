import os
import subprocess

import mTextos
import mCircuito
import m2301
import mfunctions
import mDrawio

os.system('cls')

designacao = mfunctions.validarDesignacao()
nome = input("Nome do cliente: ")
protocolo = mfunctions.validarProtocolo()
    
print(f"Texto para provisionamento: IP - WAN [{designacao}] {nome}")
vlan = input("Vlan do cliente: ")
bloco_ip = mfunctions.validarBlocoIp()
    
ip = mfunctions.calcular_ip(bloco_ip)
gateway = mfunctions.calcular_gateway(bloco_ip)
mascara = mfunctions.calcular_mascara(bloco_ip)
    
banda = mfunctions.validarBanda()
ip_gerencia = mfunctions.validarIpGerencia(banda)

mTextos.gerar(nome,designacao,protocolo,bloco_ip,ip,gateway,mascara,vlan,banda,ip_gerencia)
#mCircuito.gerarRNG(vlan,designacao)
#mCircuito.gerarCoreRNG(vlan, designacao)
#mCircuito.gerarJuniper(vlan,"["+ designacao + "]" + nome,bloco_ip)
mCircuito.gerarCircuitoCompletoCondicional(vlan,designacao,"["+ designacao + "]" + nome,bloco_ip)
m2301.gerar(nome, designacao, vlan, bloco_ip, ip_gerencia)
mDrawio.gerarCondicional(nome,designacao,protocolo,bloco_ip,vlan,banda,ip_gerencia)

subprocess.Popen(["notepad.exe", "arquivos/receivers/config.txt"])