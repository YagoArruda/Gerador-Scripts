import os
import subprocess

import functions
import s2301

def config():
    os.system('cls')

    #-------------------------------------------------
    designacao = input("Designação do cliente: ")
    nome = input("Nome do cliente: ")
    #-------------------------------------------------
    protocolo = input("Protocolo do cliente: ")
    while(functions.validar_protocolo(protocolo) == False):
        print(f"Exemplo de protocolo: 2501.0000")
        protocolo = input("Protocolo do cliente: ")
    #-------------------------------------------------
    print(f"Texto para provisionamento: IP - WAN [{designacao}] {nome}")
    #-------------------------------------------------
    #voltar a utilizar futuramente
    #vlan = functions.escolher_vlan()
    #vlan = int(vlan)
    vlan = input("Vlan do cliente: ")
    vlan = int(vlan)
    
    #-------------------------------------------------
    bloco_ip = input("Bloco ip do cliente: ")
    while(functions.validar_bloco_ip(bloco_ip) == False):
        print(f"Exemplo de bloco ip: 192.168.10.7/31")
        bloco_ip = input("Bloco ip do cliente: ")
    #-------------------------------------------------

    ip = functions.calcular_ip(bloco_ip)
    gateway = functions.calcular_gateway(bloco_ip)
    mascara = functions.calcular_mascara(bloco_ip)

    #-------------------------------------------------
    banda = input("Banda do cliente (sem Mbps): ")
    while(functions.validar_banda(banda) == False):
        print(f"Exemplo de banda: 10")
        banda = input("Banda do cliente (sem Mbps): ")
    #-------------------------------------------------
    ip_gerencia = input("Ip de gerencia do cliente: ")
    while(functions.validar_ip_gerencia(ip_gerencia) == False):
        print(f"Exemplo de ip de gerencia: 192.168.10.7")
        ip_gerencia = input("Ip de gerencia do cliente: ")
    #-------------------------------------------------

    saida = f"""{nome}_{designacao}_{protocolo}

IP - WAN [{designacao}] {nome}

DESIGNAÇÃO: {designacao}
BLOCO IP: {bloco_ip}
IP: {ip}
GATEWAY: {gateway}
MÁSCARA: {mascara}
VLAN: {vlan}
BANDA: {banda} Mbps

IP DE GERENCIA: {ip_gerencia}

###### RNG
{functions.gerar_script_huawei(vlan,designacao)}

###### CORE-RNG
{functions.gerar_script_cisco(vlan,designacao)}

###### JUNIPER
{functions.gerar_script_juniper(vlan,"["+ designacao + "]" + nome,bloco_ip)}

"""

    with open("Arquivos/Receivers/config.txt", "w") as arquivo:
        arquivo.write(saida)
    
    op_2301 = input("Gerar script para 2301? Y/N: ")
    if(op_2301 == "Y" or op_2301 == "y"):
        with open("Arquivos/Receivers/config.txt", "a") as arquivo:
            arquivo.write(F"""###### 2301
""")
        s2301.config(designacao,nome,bloco_ip,vlan,ip_gerencia,"a","Arquivos/Receivers/config.txt")
    else:
        subprocess.Popen(["notepad.exe", "Arquivos/Receivers/config.txt"])
        ls = input("Aperte qualquer tecla para prosseguir.....")
        import main
    

