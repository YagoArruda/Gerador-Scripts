import os

arquivo_vlans = 'Arquivos/A_lsm/vlans.txt'
arquivo_estacoes = 'Arquivos/A_lsm/estacoes.txt'

def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        vlans_lidas = file.readlines()
    return vlans_lidas

def write_list_to_file(file_path, vlans):
    with open(file_path, 'w') as file:
        file.writelines(vlans)

def calcular_mascara(bloco_ip):
    # ainda em processo
    dados_ip = bloco_ip.split("/")
    barra = dados_ip[1]
    mascara = ""
    
    # if(barra != "31"):
        # print(f"Exemplo de mascara completa: 255.255.255.254")
        # mascara = input("Digite a mascara completa: ")
    # else:
        # mascara = "255.255.255.254"
        
        
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
    # ainda em processo
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
    
def validar_bloco_ip(bloco_ip):
    pontos = bloco_ip.count('.')
    barra = bloco_ip.count('/')
    if(pontos == 3 and barra == 1):
        return True
    return False
    
def escolher_vlan():
    # Ler o arquivo em uma lista
    vlans = read_file_to_list(arquivo_vlans)
    vlanreturn = 0

    print(f"Vlans disponivei: {len(vlans)}")
    print(f"#########")
    for i in range(len(vlans)):
        print(f"{i+1} - {vlans[i].strip()}")
        print(f"#########")
    
    vlan_escolhida = -1 
    while(True):
        vlan_escolhida = input("Escolha a vlan a ser utilizada: ")
        if(pode_ser_convertido_em_int(vlan_escolhida)):
            if(int(vlan_escolhida) > 0 and int(vlan_escolhida) < len(vlans) + 1):
                vlan_escolhida = int(vlan_escolhida)-1
                break
   
    vlanreturn = vlans.pop(vlan_escolhida)

    # Escrever a lista de volta no arquivo
    write_list_to_file(arquivo_vlans, vlans)
    return vlanreturn

def pode_ser_convertido_em_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def gerar_script_juniper(_vlan,_description,_bloco_ip):
    _modo = input("Digite o ae7 ou et-0/0/0: ")
    
    temp = f"""set interfaces {_modo} unit {_vlan} description "{_description}"
set interfaces {_modo} unit {_vlan} vlan-id {_vlan}
set interfaces {_modo} unit {_vlan} family inet rpf-check
set interfaces {_modo} unit {_vlan} family inet address {_bloco_ip}
set routing-instances INTERNET interface {_modo}.{_vlan}"""
    return temp
    
def gerar_script_2301(_modo,_vlan,_description,_bloco_ip):
    temp = f"""hostname AC2.PTRI.14.20371.1
username admin privilege 15 password unencrypted WQM$9!#%
vlan 2021 
name NMS_SEFI
exit
vlan {_vlan}
name 1.AC2.PTRI.14.20371.1
exit
ip route 0.0.0.0 0.0.0.0 10.10.21.254 
snmp-server community v2c C3ntury:T3l3c0m RO
interface GigabitEthernet 1/1
no shut
description TRANSPORTE-LD-PROVIDER-0/
switchport trunk allowed vlan 2021, {_vlan}
switchport mode trunk
exit
interface GigabitEthernet 1/5
no shut
description ORCHEST DO BRASIL LTDA-1.AC2.PTRI.14.20371.1
switchport access vlan {_vlan}
no spanning-tree
exit
interface vlan 1.AC2.PTRI.14.20371.1
ip address 10.10.20.240 255.255.252.0
exit"""
    return temp

def validar_banda(banda):
    if(pode_ser_convertido_em_int(banda) and banda != ""):
        return True
    return False
#banda.count('Mbps') <= 0 and banda.count('mbps') <= 0 and banda.count('Mb') <= 0 and banda.count('mb') <= 0 and banda != ""
   
def validar_ip_gerencia(ip_gerencia):
    pontos = ip_gerencia.count('.')
    if(pontos == 3):
        return True
    return False
 
def gerar_script_huawei(_vlan,_designacao):
    ip_alvo = input("Ip do RNG-CORE: ")
    
    while(validar_ip_gerencia(ip_alvo) == False):
        print(f"Exemplo de ip: 192.168.10.7")
        ip_alvo = input("Ip do RNG-CORE: ")
    
    temp = f"""vlan {_vlan}
name {_designacao}
description {_designacao}
quit

interface Vlanif {_vlan}
description {_designacao}
mpls l2vc {ip_alvo} {_vlan}
mpls l2vpn flow-label both"""
    return temp
 
def gerar_script_cisco(_vlan,_designacao):
    ip_alvo = input("Ip do RNG: ")
    equipamento_alvo = input("Nome do RNG: ")
    
    while(validar_ip_gerencia(ip_alvo) == False):
        print(f"Exemplo de ip: 192.168.10.7")
        ip_alvo = input("Ip do RNG: ")
    
    temp = f"""config 
mpls l2vpn 
vpws-group {equipamento_alvo}
vpn {_designacao}
neighbor {ip_alvo}
pw-type vlan {_vlan}
pw-load-balance
flow-label both
pw-id {_vlan}
pw-mtu 1500
access-interface lag-7
dot1q {_vlan}"""
    return temp
    
def validar_protocolo(protocolo):
    pontos = protocolo.count('.')
    if(pontos == 1):
        return True
    return False
   
def formatar_2301(entrada): 
    
    entrada = entrada.replace(".","-")
    #entrada = entrada.replace("","-")
    entrada = entrada.replace(" ","-")

    return entrada    

def detectar_estacao(designacao):
    partes = designacao.split(".")
    
    return partes[2]
    
def dados_estacao(estacao_alvo):
    estacoes = read_file_to_list(arquivo_estacoes)
    
    for i in range(len(estacoes)):
        aux_estacao = estacoes[i].split(",")
        if(aux_estacao[0] == estacao_alvo):
            return aux_estacao
    else:
        return "Undefined"
    