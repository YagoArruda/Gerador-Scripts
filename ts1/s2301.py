import os
import subprocess

import functions

def config(designacao,nome,bloco_ip,vlan,ip_gerencia,modo,arquivo_destino):
    os.system('cls')

    #-------------------------------------------------
    if(designacao == "-1"):
        designacao = input("Designação do cliente: ")
    if(nome == "-1"):
        nome = input("Nome do cliente: ") 
    #-------------------------------------------------
    if(bloco_ip == "-1"):
        bloco_ip = input("Bloco ip do cliente: ")
        while(functions.validar_bloco_ip(bloco_ip) == False):
            print(f"Exemplo de bloco ip: 192.168.10.7/31")
            bloco_ip = input("Bloco ip do cliente: ")
    #-------------------------------------------------

    ip = functions.calcular_ip(bloco_ip)
    gateway = functions.calcular_gateway(bloco_ip)
    mascara = functions.calcular_mascara(bloco_ip)
    
    #-------------------------------------------------
    if(vlan == "-1"):
        vlan = input("Vlan do cliente: ")
        while(functions.pode_ser_convertido_em_int(vlan) == False):
            print(f"Exemplo de vlan: 1010")
            vlan = input("Vlan do cliente: ")
        vlan = int(vlan)
    #-------------------------------------------------
    if(ip_gerencia == "-1"):
        ip_gerencia = input("Ip de gerencia do cliente: ")
        while(functions.validar_ip_gerencia(ip_gerencia) == False):
            print(f"Exemplo de ip de gerencia: 192.168.10.7")
            ip_gerencia = input("Ip de gerencia do cliente: ")
    #-------------------------------------------------
    
    nms = functions.detectar_estacao(designacao)
    dados_estacao = functions.dados_estacao(nms)
    
    vlan_gerencia = dados_estacao[1]
    default_gateway = dados_estacao[2]
    
    descricao_porta = input("Descrição da porta do 2301: ")


    saida = f"""hostname CTL_{designacao}
username admin privilege 15 password unencrypted WQM$9!#%
vlan {vlan_gerencia}
name NMS_{nms}
exit
vlan {vlan}
name {designacao}
exit
ip route 0.0.0.0 0.0.0.0 {default_gateway} 
snmp-server community v2c C3ntury:T3l3c0m RO
interface GigabitEthernet 1/1
no shut
description {functions.formatar_2301(nome)}-{functions.formatar_2301(designacao)}
switchport access vlan {vlan}
no spanning-tree
exit
interface GigabitEthernet 1/5
no shut
description {descricao_porta}
switchport trunk allowed vlan {vlan_gerencia}, {vlan}
switchport mode trunk
exit
interface vlan {vlan_gerencia}
ip address {ip_gerencia} 255.255.252.0
exit"""

    with open(arquivo_destino, modo) as arquivo:
        arquivo.write(saida)
    if(modo == "w"):
        subprocess.Popen(["notepad.exe", "Arquivos/Receivers/2301.txt"])
    else:
        subprocess.Popen(["notepad.exe", "Arquivos/Receivers/config.txt"])
    ls = input("Aperte qualquer tecla para prosseguir.....")
    import main
    

