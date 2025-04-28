
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

{ipgerencia(ip_gerencia)}
"""
    with open("arquivos/receivers/config.txt", "w") as arquivo:
        arquivo.write(saida)

def ipgerencia(ip_gerencia):
    if(ip_gerencia != ""):
        return f"IP DE GERENCIA: {ip_gerencia}"
    return ""