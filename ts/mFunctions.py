import os
import subprocess
import re
import mCor
 
def validarBanda():
    banda = input("# Banda do cliente (sem Mbps): ")
    padraoBanda = re.compile(r'^\d{1,6}$')
    
    while(padraoBanda.match(banda) == None):
        print(f"# Exemplo de banda: {mCor.amarelo("10")}")
        banda = input("# Banda do cliente (sem Mbps): ")
        
    return banda

def validarBlocoIp():
    bloco_ip = input("# Bloco ip do cliente: ")
    padraoIp = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$')
    while(padraoIp.match(bloco_ip) == None):
        print(f"# Exemplo de bloco ip: {mCor.amarelo("192.168.10.7/31")}")
        bloco_ip = input("# Bloco ip do cliente: ")
    return bloco_ip

def validarProtocolo():
    protocolo = input("# Protocolo do cliente: ")
    padraoProtocolo = re.compile(r'^\d{4}\.\d{1,7}$')
    
    while(padraoProtocolo.match(protocolo) is None):
        print(f"# Exemplo de protocolo: {mCor.amarelo("2501.0000")}")
        protocolo = input("# Protocolo do cliente: ")
    return protocolo

def validarIp(texto):   
    ip = input(f"# {texto}: ")
    padraoIp = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    
    while(padraoIp.match(ip) is None):
        print(f"# Exemplo de ip: {mCor.amarelo("192.168.10.7")}")
        ip = input(f"# {texto}: ")
    return ip

def validarIpGerencia(banda):
    ip = ""
    if int(banda) > 300:    
        ip = input("# Ip de gerencia do cliente: ")
        padraoIp = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    
        while(padraoIp.match(ip) == None):
            print(f"# Exemplo de ip de gerencia: {mCor.amarelo("192.168.10.7")}")
            ip = input("# Ip de gerencia do cliente: ")
    else:
        op = input(F"# Selecionar Ip de gerencia mesmo com banda abaixo de 300?[{mCor.verde("y")}/{mCor.vermelho("n")}]: ")
        if op == "y" or op == "Y":
            return validarIpGerencia(301)
        
    return ip

def validarProsseguir(texto):
    op = input(f"{texto}[{mCor.verde("y")}/{mCor.vermelho("n")}]: ")
    if(op == "y" or op == "Y"):
        return True
    return False

def validarVlan():
    vlan = input("# Vlan do cliente: ")
    
    padraoVlan = re.compile(r'^\d{1,4}\d$')
    
    while(padraoVlan.match(vlan) is None):
        print(f"Exemplo de vlan: {mCor.amarelo("12")}")
        vlan = input("# Vlan do cliente: ")
    return vlan

def calcular_mascara(bloco_ip):
    dados_ip = bloco_ip.split("/")
    barra = dados_ip[1]
    mascara = ""
    
    referencia = 32 - int(barra)
    if(referencia <= 8):
        mascara = "255.255.255." + str(256 - (2 ** referencia))
    elif(referencia <= 16):
        referencia_aux = referencia - 8
        referencia = 8
        mascara = "255.255."+str(256 - (2 ** referencia_aux)) + "." +str(256 - (2 ** referencia))
    elif(referencia <= 24):
        referencia_aux = referencia - 8
        referencia_aux2 = referencia_aux - 8
        referencia_aux = 8
        referencia = 8
        mascara = "255."+str(256 - (2 ** referencia_aux2)) + "." +str(256 - (2 ** referencia_aux)) + "." +str(256 - (2 ** referencia))
    elif(referencia <= 32):
        referencia_aux = referencia - 8
        referencia_aux2 = referencia_aux - 8
        referencia_aux3 = referencia_aux2 - 8
        referencia_aux2 = 8
        referencia_aux = 8
        referencia = 8
        mascara = "255."+str(256 - (2 ** referencia_aux2)) + "." +str(256 - (2 ** referencia_aux)) + "." +str(256 - (2 ** referencia))

    return mascara 

def calcular_gateway(bloco_ip):
    dados_ip = bloco_ip.split("/")
    ip = dados_ip[0]
    gateway = ""
    
    if(dados_ip[1] != "31"):
        partes_ip = ip.split(".")
        final_ip = partes_ip[3]
        final_ip = int(final_ip)+1
        gateway = partes_ip[0] + "." + partes_ip[1] + "." + partes_ip[2] + "." + str(final_ip)
    else:
        gateway = ip
    return gateway
    
def calcular_ip(bloco_ip):
    dados_ip = bloco_ip.split("/")
    ip = dados_ip[0]
    primeiro_ip = ""
    ultimo_ip = ""
    
    if(dados_ip[1] != "31"):
        partes_ip = ip.split(".")
        final_ip = partes_ip[3]
        final_ip = int(final_ip)+2
        primeiro_ip = partes_ip[0] + "." + partes_ip[1] + "." + partes_ip[2] + "." + str(final_ip)
    else:
        partes_ip = ip.split(".")
        final_ip = partes_ip[3]
        final_ip = int(final_ip)+1
        primeiro_ip = partes_ip[0] + "." + partes_ip[1] + "." + partes_ip[2] + "." + str(final_ip)
        
    
    ips_utilizaveis = str(primeiro_ip)
    
    return ips_utilizaveis
 
def pode_ser_convertido_em_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False  

def salvarEmArquivo(entrada,arquivo):  
    with open(f"{arquivo}", "w") as arquivo:
        arquivo.write(entrada)
    
def adicionarEmArquivo(entrada,arquivo):  
    with open(f"{arquivo}", "a") as arquivo:
        arquivo.write(entrada)
        