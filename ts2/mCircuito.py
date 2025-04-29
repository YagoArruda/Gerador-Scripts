import mfunctions

def gerarRNG(_vlan,_designacao):
    print(f"")
    print(f"####### RNG")
    ip_alvo = mfunctions.validarIp("Ip do RNG-CORE")
    
    temp = f"""###### RNG
vlan {_vlan}
name {_designacao}
description {_designacao}
quit

interface Vlanif {_vlan}
description {_designacao}
mpls l2vc {ip_alvo} {_vlan}
mpls l2vpn flow-label both

"""

    with open("arquivos/receivers/config.txt", "a") as arquivo:
        arquivo.write(temp)

def gerarCoreRNG(_vlan,_designacao):
    print(f"")
    print(f"####### RNG-CORE")
    ip_alvo = mfunctions.validarIp("Ip do RNG")
    equipamento_alvo = input("Nome do RNG: ")
    
    temp = f"""###### CORE-RNG
config 
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
dot1q {_vlan}

"""
    
    with open("arquivos/receivers/config.txt", "a") as arquivo:
        arquivo.write(temp)
    
def gerarJuniper(_vlan,_description,_bloco_ip):
    print(f"")
    print(f"####### JUNIPER")
    _modo = input("Digite o ae7 ou et-0/0/0: ")
    
    temp = f"""###### JUNIPER
set interfaces {_modo} unit {_vlan} description "{_description}"
set interfaces {_modo} unit {_vlan} vlan-id {_vlan}
set interfaces {_modo} unit {_vlan} family inet rpf-check
set interfaces {_modo} unit {_vlan} family inet address {_bloco_ip}
set routing-instances INTERNET interface {_modo}.{_vlan}

"""

    with open("arquivos/receivers/config.txt", "a") as arquivo:
        arquivo.write(temp)

