arquivo_estacoes = 'arquivos/a_lsm/estacoes.txt'

def gerar(nome, designacao, vlan, bloco_ip, ip_gerencia):
    if ip_gerencia != "":
        print(f"")
        print(f"####### 2301")
        _dadosNMS = dadosNMS(validarNMS(designacao)).split(",")
        nms = _dadosNMS[0]
        vlan_gerencia = _dadosNMS[1]
        default_gateway = _dadosNMS[2]
    
        descricao_porta = input("# Descrição da porta do 2301: ")
    
        temp = f"""###### 2301
hostname CTL_{designacao}
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
description {formatarTexto(nome)}-{formatarTexto(designacao)}
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
exit

"""

        with open("arquivos/receivers/config.txt", "a") as arquivo:
            arquivo.write(temp)

def validarNMS(designacao):
    dados_nms = designacao.split(".")
    nms = dados_nms[2]
    return nms
 
def formatarTexto(entrada):
    entrada = entrada.replace(".","-")
    #entrada = entrada.replace("","-")
    entrada = entrada.replace(" ","-")

    return entrada 
    
def dadosNMS(estacao_alvo):
    estacoes = ler_arquivo(arquivo_estacoes)
    
    for i in range(len(estacoes)):
        aux_estacao = estacoes[i].split(",")
        if(aux_estacao[0] == estacao_alvo):
            return estacoes[i]
    else:
        return "Undefined,0000,0.0.0.0"

def ler_arquivo(file_path):
    with open(file_path, 'r') as file:
        dados_lidas = file.readlines()
    return dados_lidas