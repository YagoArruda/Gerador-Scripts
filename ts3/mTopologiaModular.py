import subprocess
import mFunctions

class Equipamento:
    def __init__(self, oid,nome, ip, portaA, portaB, posX, posY):
        self.oid = oid
        self.nome = nome
        self.ip = ip
        self.portaA = portaA
        self.portaB = portaB
        self.posX = posX
        self.posY = posY

def switch(equipamento):
    
    switch = f"""<mxCell id="{equipamento.oid}-porta-b" value="{equipamento.portaB}" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX+60}" y="{equipamento.posY-5}" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}" value="" style="sketch=0;points=[[0.015,0.015,0],[0.985,0.015,0],[0.985,0.985,0],[0.015,0.985,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.rect;prIcon=l2_switch;fillColor=#FAFAFA;strokeColor=#005073;shadow=1;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX}" y="{equipamento.posY}" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-porta-a" value="{equipamento.portaA}" style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX-100}" y="{equipamento.posY-5}" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-desc-linha1" value="{equipamento.nome}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="{equipamento.posX-85}" y="{equipamento.posY+50}" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-desc-linha2" value="{equipamento.ip}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="{equipamento.posX-85}" y="{equipamento.posY+70}" width="220" height="30" as="geometry" />
        </mxCell>"""
    
    return switch

def router(equipamento):
    
    router = f"""<mxCell id="{equipamento.oid}-porta-a" value="Porta A" style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX-100}" y="{equipamento.posY-5}" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-porta-b" value="Porta B" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX+60}" y="{equipamento.posY-5}" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}" value="" style="sketch=0;points=[[0.5,0,0],[1,0.5,0],[0.5,1,0],[0,0.5,0],[0.145,0.145,0],[0.8555,0.145,0],[0.855,0.8555,0],[0.145,0.855,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.rect;prIcon=router;fillColor=#FAFAFA;strokeColor=#005073;shadow=1;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX}" y="{equipamento.posY}" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-desc-linha1" value="NOME-ROUTER" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="{equipamento.posX-85}" y="{equipamento.posY+50}" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-desc-linha2" value="0.0.0.0" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="{equipamento.posX-85}" y="{equipamento.posY+70}" width="220" height="30" as="geometry" />
        </mxCell>"""
    
    return router

def l3switch(equipamento):
    
    router = f"""<mxCell id="{equipamento.oid}-porta-a" value="Porta A" style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX-100}" y="{equipamento.posY-5}" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-porta-b" value="Porta B" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX+60}" y="{equipamento.posY-5}" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}" value="" style="sketch=0;points=[[0.015,0.015,0],[0.985,0.015,0],[0.985,0.985,0],[0.015,0.985,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.rect;prIcon=l3_switch;fillColor=#FAFAFA;strokeColor=#005073;shadow=1;" parent="1" vertex="1">
          <mxGeometry x="{equipamento.posX}" y="{equipamento.posY}" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-desc-linha1" value="NOME-L3-SWITCH" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="{equipamento.posX-85}" y="{equipamento.posY+50}" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="{equipamento.oid}-desc-linha2" value="0.0.0.0" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="{equipamento.posX-85}" y="{equipamento.posY+70}" width="220" height="30" as="geometry" />
        </mxCell>"""
    
    return router

def seta(oid,equipamentoA,equipamentoB):
    
    router = f"""<mxCell id="{oid}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;startArrow=classic;startFill=1;" edge="1" parent="1" source="{equipamentoA}" target="{equipamentoB}">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>"""
    
    return router

def gerarEquipmento(oid, posX, posY):
    nome = input("Nome do equipamento: ")
    ip = mFunctions.validarIp("Ip do equipamento: ")
    portaA = input("Porta A: ")
    portaB = input("Porta B: ")
    
    return Equipamento(oid, nome, ip, portaA, portaB, posX, posY)

def teste():
    
    inicio = f"""<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0" version="26.2.14">
  <diagram name="Page-1" id="c37626ed-c26b-45fb-9056-f9ebc6bb27b6">
    <mxGraphModel dx="1418" dy="820" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />"""

    fim = f"""
     </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

    equipamentos = []

    meio = f""""""
    tip = ""
    posX = 0
    posY = 0
    iid = 0
    while (tip != "0"):
        tip = input("1 - RT 2 - SWITCH 3 - L3 SWITCH")
        
        if(tip == "1"):
            equipamentos.append(gerarEquipmento(f"ROUTER-{iid}", posX, posY))
            meio = meio + router(equipamentos[-1])
            posX = posX + 200
            iid = iid + 1
        if(tip == "2"):
            equipamentos.append(gerarEquipmento(f"SWITCH-{iid}", posX, posY))
            meio = meio + switch(equipamentos[-1])
            posX = posX + 200
            iid = iid + 1
        if(tip == "3"):
            equipamentos.append(gerarEquipmento(f"L3SWITCH-{iid}", posX, posY))
            meio = meio + l3switch(equipamentos[-1])
            posX = posX + 200
            iid = iid + 1
        if(tip == "4"):
            seta(f"SETA-{iid}",equipamento[0],equipamento[1])
            iid = iid + 1
    
        circuito = inicio + meio + fim

    with open("arquivos/receivers/teste.drawio", "w") as arquivo:
        arquivo.write(circuito)
    subprocess.Popen(["notepad.exe", "arquivos/receivers/teste.drawio"])