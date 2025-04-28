import os
import subprocess
import re
       
def validarBanda():
    banda = input("Banda do cliente (sem Mbps): ")
    padraoBanda = re.compile(r'^\d{1,6}$')
    
    while(padraoBanda.match(banda) == False):
        print(f"Exemplo de banda: 10")
        banda = input("Banda do cliente (sem Mbps): ")
        
    return banda

def validarBlocoIp():
    bloco_ip = input("Bloco ip do cliente: ")
    padraoIp = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$')
    
    while(padraoIp.match(bloco_ip) == False):
        print(f"Exemplo de bloco ip: 192.168.10.7/31")
        bloco_ip = input("Bloco ip do cliente: ")
    return bloco_ip

def validarProtocolo():
    protocolo = input("Protocolo do cliente: ")
    padraoProtocolo = re.compile(r'^\d{4}\.\d{3,6}$')
    
    while(padraoProtocolo.match(protocolo) is None):
        print(f"Exemplo de protocolo: 2501.0000")
        protocolo = input("Protocolo do cliente: ")
    return protocolo

def validarIp(texto):   
    ip = input(f"{texto}:")
    padraoIp = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    
    while(padraoIp.match(ip) is None):
        print(f"Exemplo de ip de gerencia: 192.168.10.7")
        ip = input(f"{texto}:")
    return ip

def validarIpGerencia(banda):
    ip = ""
    if int(banda) > 300:    
        ip = input("Ip de gerencia do cliente: ")
        padraoIp = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    
        while(padraoIp.match(ip) == False):
            print(f"Exemplo de ip de gerencia: 192.168.10.7")
            ip = input("Ip de gerencia do cliente: ")
    return ip

def validarDesignacao():
    designacao = input("Designacao do cliente: ")
    
    padraoDesignacao = re.compile(r'^\d\.[A-Z0-9]{3}\.[A-Z]{4}\.\d{0,1}\.\d{4,5}\.\d$')



    
    while(padraoDesignacao.match(designacao) is None):
        print(f"Exemplo de designacao: 1.XX1.XXXX.1.11111.1")
        designacao = input("Designacao do cliente: ")
    return designacao

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

    