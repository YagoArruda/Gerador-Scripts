import m2301
import mFunctions

def gerar(nome,designacao,protocolo,bloco_ip,ip,gateway,mascara,vlan,banda,ip_gerencia):
    saida = f"""|-------------------------------------------------------------------|
{nome}_{designacao}_{protocolo}

IP - WAN [{designacao}] {nome}

DESIGNAÇÃO: {designacao}
BLOCO IP: {bloco_ip}
IP: {ip}
GATEWAY: {gateway}
MÁSCARA: {mascara}
VLAN: {vlan}
BANDA: {banda} Mbps

"""
    with open("arquivos/receivers/config.txt", "w") as arquivo:
        arquivo.write(saida)
        
    ipgerencia(ip_gerencia)
    dadosTecnicoMKCondicional(ip_gerencia,vlan,designacao)

def ipgerencia(ip_gerencia):
    if(ip_gerencia != ""):
        with open("arquivos/receivers/config.txt", "a") as arquivo:
            arquivo.write(f"""IP DE GERENCIA: {ip_gerencia}
            
            """)
    
def dadosTecnicoMK(ip_gerencia,vlan,designacao):
    temp = ""
    print(f"")
    print(f"####### Tecnico MK")
    if ip_gerencia != "":
        juniper = mFunctions.validarIp("Ip do Juniper")
        servico = input("Tipo de serviço: ")
        temp = f"""###### Tecnio - MK
{juniper} | ae7.{vlan}
        
{servico}_[60731.47732 - Alterar]_{m2301.validarNMS(designacao)}
PTP_EDD_{ip_gerencia}
RATE-LIMIT_{juniper}
SINAL-ATIVACAO_

"""
    else:
        juniper = mFunctions.validarIp("Ip do Juniper")
        gpon = mFunctions.validarIp("Ip do GPON")
        servico = input("Tipo de serviço: ")
        temp = f"""###### Tecnico - MK
{juniper} | ae7.{vlan}
        
{servico}_[60731.47732 - Alterar]_{m2301.validarNMS(designacao)}
GPON_HUAWEI_{gpon}
RATE-LIMIT_{gpon}
SINAL-ATIVACAO_

"""
    
    with open("arquivos/receivers/config.txt", "a") as arquivo:
        arquivo.write(temp)

def dadosTecnicoMKCondicional(ip_gerencia,vlan,designacao):
    if(mFunctions.validarProsseguir("Gerar Texto Tecnico MK?") == True):
        dadosTecnicoMK(ip_gerencia,vlan,designacao)