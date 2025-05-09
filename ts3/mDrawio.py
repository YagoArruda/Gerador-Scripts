import mFunctions
from datetime import date
import subprocess

def gerar(nome,designacao,protocolo,bloco_ip,vlan,banda,ip_gerencia):
    
    print(f"")
    print(f"####### TOPOLOGIA")
    print(f"")
    print(f"## ACS/GPON")
    ip_acsGpon = input("Ip ACS/GPON: ")
    nome_acsGpon = input("Nome ACS/GPON: ")
    porta_acs_cliente = input("Porta ACS->Cliente: ")
    porta_acs_rng = input("Porta ACS->RNG: ")
    
    print(f"## RNG")
    ip_rng = input("Ip RNG: ")
    nome_rng = input("Nome RNG: ")
    porta_rng_acs = input("Porta RNG->ACS: ")
    
    print(f"## RNG-CORE")
    ip_rngCore = input("Ip RNG-CORE: ")
    nome_rngCore = input("Nome RNG-CORE: ")
    
    print(f"## Router")
    ip_router = input("Ip Router: ")
    nome_router = input("Nome Router: ")
    
    data_atual = date.today()
    data = data_atual.strftime('%d/%m/%Y')
    
    gateway = mFunctions.calcular_gateway(bloco_ip)
    mascara = mFunctions.calcular_mascara(bloco_ip)
    ip = mFunctions.calcular_ip(bloco_ip)
    
    temp = f"""<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0" version="26.2.14">
  <diagram name="Page-1" id="c37626ed-c26b-45fb-9056-f9ebc6bb27b6">
    <mxGraphModel dx="2518" dy="820" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="TPHFotOGXAIGz77qLiII-6" value="" style="ellipse;whiteSpace=wrap;html=1;textShadow=0;labelBorderColor=none;labelBackgroundColor=none;opacity=45;fillColor=#dae8fc;strokeColor=#6c8ebf;" parent="1" vertex="1">
          <mxGeometry x="-60" y="480" width="490" height="220" as="geometry" />
        </mxCell>
        <mxCell id="TPHFotOGXAIGz77qLiII-3" value="" style="endArrow=classic;html=1;rounded=0;startArrow=classic;startFill=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;" parent="1" source="h46SICJPrgyOPjBbUtfY-3" target="h46SICJPrgyOPjBbUtfY-4" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="340" y="580" as="sourcePoint" />
            <mxPoint x="500" y="580" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="TPHFotOGXAIGz77qLiII-7" value="MPLS" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="137.5" y="490" width="95" height="30" as="geometry" />
        </mxCell>
        <mxCell id="TPHFotOGXAIGz77qLiII-11" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;startArrow=classic;startFill=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;" parent="1" source="h46SICJPrgyOPjBbUtfY-1" target="h46SICJPrgyOPjBbUtfY-2" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-166.42000000000007" y="580" as="sourcePoint" />
            <mxPoint x="10" y="580" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="TPHFotOGXAIGz77qLiII-12" value="" style="endArrow=classic;html=1;rounded=0;startArrow=classic;startFill=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;" parent="1" source="h46SICJPrgyOPjBbUtfY-2" target="h46SICJPrgyOPjBbUtfY-3" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="110" y="580" as="sourcePoint" />
            <mxPoint x="260" y="580" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="TPHFotOGXAIGz77qLiII-13" value="{nome}&lt;br&gt;{designacao} | {protocolo}" style="text;html=1;align=center;verticalAlign=middle;rounded=0;labelBackgroundColor=none;textShadow=0;whiteSpace=wrap;strokeColor=light-dark(#ffffff, #a9b8c7);" parent="1" vertex="1">
          <mxGeometry x="25" y="430" width="325" height="40" as="geometry" />
        </mxCell>
        <mxCell id="8075vzSek8EXq1Qk1El3-8" value="{nome_acsGpon}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-280.5" y="600" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="8075vzSek8EXq1Qk1El3-9" value="{nome_rng}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-50" y="600" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="8075vzSek8EXq1Qk1El3-10" value="{nome_rngCore}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="190" y="600" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="8075vzSek8EXq1Qk1El3-12" value="{nome_router}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="449.5" y="601" width="220" height="30" as="geometry" />
        </mxCell>
        <mxCell id="9Xov0KzFszH7NUMbsZ65-17" value="ae7.{vlan}" style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="460" y="550" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="9Xov0KzFszH7NUMbsZ65-34" value="{data}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="560" y="680" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="Sjql4_TdowpkSLk0pfY9-3" value="{porta_rng_acs}" style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-60" y="550" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="CPYKce1SLypnUJwbY2Mq-1" value="{ip_acsGpon}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-280.5" y="620" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="CPYKce1SLypnUJwbY2Mq-2" value="{ip_rng}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-20" y="620" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="CPYKce1SLypnUJwbY2Mq-3" value="{ip_rngCore}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="220" y="620" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="CPYKce1SLypnUJwbY2Mq-4" value="{ip_router}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="479.5" y="620" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="CPYKce1SLypnUJwbY2Mq-5" value="Lag 7" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="340" y="550" width="50" height="30" as="geometry" />
        </mxCell>
        <mxCell id="CPYKce1SLypnUJwbY2Mq-6" value="&lt;div&gt;DESIGNACAO: {designacao}&amp;nbsp;&lt;/div&gt;&lt;div&gt;BLOCO IP: {bloco_ip}&amp;nbsp;&amp;nbsp;&lt;/div&gt;&lt;div&gt;IP: {ip}&amp;nbsp;&lt;/div&gt;&lt;div&gt;GATEWAY: {gateway}&amp;nbsp;&lt;/div&gt;&lt;div&gt;MASCARA: {mascara}&lt;/div&gt;&lt;div&gt;VLAN: {vlan}&amp;nbsp;&lt;/div&gt;&lt;div&gt;BANDA: {banda} Mbps&lt;br&gt;&lt;br&gt;IP GERENCIA: {ip_gerencia}&lt;/div&gt;" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-320" y="680" width="260" height="120" as="geometry" />
        </mxCell>
        <mxCell id="JazUjWxsk5tBt9pqyCTI-1" value="{porta_acs_rng}" style="text;html=1;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-160" y="550" width="90" height="30" as="geometry" />
        </mxCell>
        <mxCell id="h46SICJPrgyOPjBbUtfY-1" value="" style="sketch=0;points=[[0.015,0.015,0],[0.985,0.015,0],[0.985,0.985,0],[0.015,0.985,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.rect;prIcon=l2_switch;fillColor=#FAFAFA;strokeColor=#005073;shadow=1;" parent="1" vertex="1">
          <mxGeometry x="-225.5" y="555.5" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="h46SICJPrgyOPjBbUtfY-2" value="" style="sketch=0;points=[[0.015,0.015,0],[0.985,0.015,0],[0.985,0.985,0],[0.015,0.985,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.rect;prIcon=l3_switch;fillColor=#FAFAFA;strokeColor=#005073;shadow=1;" parent="1" vertex="1">
          <mxGeometry x="35" y="555" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="h46SICJPrgyOPjBbUtfY-3" value="" style="sketch=0;points=[[0.015,0.015,0],[0.985,0.015,0],[0.985,0.985,0],[0.015,0.985,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.rect;prIcon=l3_switch;fillColor=#FAFAFA;strokeColor=#005073;shadow=1;" parent="1" vertex="1">
          <mxGeometry x="275" y="555.5" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="h46SICJPrgyOPjBbUtfY-4" value="" style="sketch=0;points=[[0.5,0,0],[1,0.5,0],[0.5,1,0],[0,0.5,0],[0.145,0.145,0],[0.8555,0.145,0],[0.855,0.8555,0],[0.145,0.855,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.rect;prIcon=router;fillColor=#FAFAFA;strokeColor=#005073;shadow=1;" parent="1" vertex="1">
          <mxGeometry x="534.5" y="555.5" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="bOp6rN95UzQHzOXqT7r_-1" value="{porta_acs_cliente}" style="text;html=1;align=right;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="1" vertex="1">
          <mxGeometry x="-330" y="550" width="90" height="30" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>


"""
    
    with open(f"arquivos/receivers/topologias/{formatarTexto(nome)}_{designacao}_{protocolo}.drawio", "a") as arquivo:
        arquivo.write(temp)
        
    subprocess.Popen(["notepad.exe", f"arquivos/receivers/topologias/{formatarTexto(nome)}_{designacao}_{protocolo}.drawio"])

def gerarCondicional(nome,designacao,protocolo,bloco_ip,vlan,banda,ip_gerencia):
    if(mFunctions.validarProsseguir("Gerar Topologia?") == True):
        gerar(nome,designacao,protocolo,bloco_ip,vlan,banda,ip_gerencia)

def formatarTexto(entrada):
    entrada = entrada.replace(".","_")
    entrada = entrada.replace("/","_")
    entrada = entrada.replace(" ","_")

    return entrada 