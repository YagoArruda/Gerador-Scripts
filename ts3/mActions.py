import mFunctions
from datetime import date
import subprocess

import m2301
import mDrawio
import mActions
import mTopologiaModular
import mTextos
import mCircuito
import mCor

def gerarCircuitoPadrao():
    designacao = mFunctions.validarDesignacao()
    nome = input("# Nome do cliente: ")
    protocolo = mFunctions.validarProtocolo()
    
    print(f"# Texto para provisionamento: IP - WAN [{designacao}] {nome}")
    vlan = mFunctions.validarVlan()
    bloco_ip = mFunctions.validarBlocoIp()
    
    ip = mFunctions.calcular_ip(bloco_ip)
    gateway = mFunctions.calcular_gateway(bloco_ip)
    mascara = mFunctions.calcular_mascara(bloco_ip)
    
    banda = mFunctions.validarBanda()
    ip_gerencia = mFunctions.validarIpGerencia(banda)

    mTextos.gerar(nome,designacao,protocolo,bloco_ip,ip,gateway,mascara,vlan,banda,ip_gerencia)
    mCircuito.gerarCircuitoCompletoCondicional(vlan,designacao,"["+ designacao + "]" + nome,bloco_ip)
    m2301.gerar(nome, designacao, vlan, bloco_ip, ip_gerencia)
    mDrawio.gerarCondicional(nome,designacao,protocolo,bloco_ip,vlan,banda,ip_gerencia)

    subprocess.Popen(["notepad.exe", "arquivos/receivers/config.txt"])

def gerarUpgradePadrao():
    
    temp = f"""###### UPGRADE
    """
    
    mFunctions.salvarEmArquivo(temp,"arquivos/receivers/upgrade.txt")
    
    opg = mFunctions.validarProsseguir("Limitação no GPON? ")
    opj = ""
    opd = ""
    
    if(opg == False):
        opj = mFunctions.validarProsseguir("Limitação no Juniper? ")
    if(opj == False):
        opd = mFunctions.validarProsseguir("Limitação no Datacom? ")
    
    
    if(opg == True):
        mFunctions.adicionarEmArquivo(textoGPON(),"arquivos/receivers/upgrade.txt")
    if(opj == True):
        mFunctions.adicionarEmArquivo(textoJuniper(),"arquivos/receivers/upgrade.txt")
    if(opd == True):
        mFunctions.adicionarEmArquivo(textoDatacom(),"arquivos/receivers/upgrade.txt")
    if(opg == opj == opd == False):
        gerarUpgradePadrao()
    
    subprocess.Popen(["notepad.exe", "arquivos/receivers/upgrade.txt"])
    
def textoDatacom():
    banda = mFunctions.validarBanda()
    bandaUp = int(banda) * 1024
    print(f"# Exemplo de interface: {mCor.amarelo("ten-gigabit-ethernet-1/1/4")}")
    interface = input("# Interface do datacom: ")
    
    mFunctions.adicionarEmArquivo(emailUpgrade(banda),"arquivos/receivers/upgrade.txt")
    
    return f"""## Datacom
qos interface {interface}
rate-limit
egress
bandwidth {bandaUp}
exit
ingress
bandwidth {bandaUp}

#########################

rate-limit input rate {bandaUp} burst 512
rate-limit output rate {bandaUp} burst 512

"""

def textoJuniper():
    vlan = mFunctions.validarVlan()
    policer = input("# Policer do Juniper: ")
    print(f"Exemplo de interface: {mCor.amarelo("et-0/0/1 ou ae7.000")}")
    interface = input("# Interface do juniper: ")
    
    banda = mFunctions.validarBanda()
    mFunctions.adicionarEmArquivo(emailUpgrade(banda),"arquivos/receivers/upgrade.txt")
    
    return f"""## Juniper
set interfaces {interface} unit {vlan} family inet policer input {policer}
set interfaces {interface} unit {vlan} family inet policer output {policer}

"""

def textoGPON():
    servicePort = input("# Service Port: ")
    index = input("# Index: ")
    lineProfile = input("# Line Profile: ")
    
    banda = mFunctions.validarBanda()
    mFunctions.adicionarEmArquivo(emailUpgrade(banda),"arquivos/receivers/upgrade.txt")
    
    return f"""## GPON
service-port {servicePort} inbound traffic-table index {index} outbound traffic-table index {index}

ont-lineprofile gpon profile-id {lineProfile}
tcont 1 dba-profile-id {index}

"""
    
def emailUpgrade(banda):
    data_atual = date.today()
    data = data_atual.strftime('%d/%m/%Y')
    return f"""
Prezados, bom dia!

Informamos que o pedido de upgrade definitivo para {banda} Mbps foi realizado no dia {data}. Favor realizar o teste da banda e, se houver algum problema referente ao pedido, entrar em contato com nossa equipe.

Att
    
"""