import numpy;
import math;

Consumo_Final = []

ImpactoTotalCarbono_Mensal = []

ImpactoTotalCarbono_Anual = []

ImpactoTotal_toneladas = [] 

quantidade = 0

horas = 0

Impacto_por_Kwh = 80
#Numero obtido com base no cálculo do Programa Brasileiro GHG Protocol.

dias = int(input("Quantos dias a empresa opera?"))

ConsumoKwH = 0

KWh = float(input("Digite o valor do Kw/h"))


print("[Calculadora detalhada de Emissão e compensação de Carbono]")
print("[TIPOS DE ELETRÔNICOS]"
"\n (1) Computadores, Notebooks"
"\n (2) Televisões."
"\n (3) Impressoras."
"\n (4) Lâmpadas."
"\n (5) Outros."
"\n (6) Resultado do Calculo."
"\n (7) Calculo Simplificado.")

tipo = 1
while tipo != 0:
  tipo = int(input("Digite o Tipo , caso queira sair digite 0 "))
  
  if tipo == 1:
    
    Quantidade = int(input("Digite a quantidade de eletrónicos "))
    ConsumoKwH = int(input("Qual a Quantidade de Watts que esse produto consome?"))
    horas = int(input("Digite o valor de horas na qual os aparelhos ficam ligados por mês "))

    Consumo_it1 = (ConsumoKwH*horas*dias)/1000
    #Calculará e transformará o calculo do consumo do produto, de Watts, para Kw/h
    ConsumoTotal_it1 = (Quantidade*Consumo_it1)
    #Pegará a quantidade de produtos, e fará "x" o consumo
    Valor = (ConsumoTotal_it1*KWh)
    #Dará o valor em Reais, baseado com o preço do KW/H
    ValorImpactoCO2_Mensal = (ConsumoTotal_it1/Impacto_por_Kwh)
    #Transformará o consumo total em Kw/h no valor de impacto de Co² (RESULTADO EM Kg de Co²)
    ValorImpactoCO2_Anual = (ConsumoTotal_it1*12)/Impacto_por_Kwh
    #Calculará uma estimativa anual de impacto de CO² (RESULTADO EM Kg de Co²)
    ValorImpactoCO2_ToneladasA = (ValorImpactoCO2_Anual/1000)
    #Transformará o impacto (ANUAL) de KG p/ Toneladas (tCO²)
    Consumo_Final.append(Valor)
    #Levará os valores em Reais, gastos com tal eletrônico P/ uma lista.
    ImpactoTotal_toneladas.append(ValorImpactoCO2_ToneladasA)
    #Levará os valores do impacto total em Toneladas para uma lista.
    ImpactoTotalCarbono_Mensal.append(ValorImpactoCO2_Mensal)
    #Levará os valores do impacto total de carbono mensal p/ uma lista
    ImpactoTotalCarbono_Anual.append(ValorImpactoCO2_Anual)
    #Levará os valores do impacto total de carbono anual p/ uma lista
    
    print(f"A sua média de consumo total mensal gasta de energia c/ Computadores e Notebooks é de {ConsumoTotal_it1:.2f} KW/h,
        resultando em uma conta de R${Valor:.2f} e um impacto ambiental mensal de: {ValorImpactoCO2_Mensal:.2f} Kg CO2e, e anual: {ValorImpactoCO2_Anual:.2f} Kg CO2e")

  elif tipo == 2:
    
    Quantidade = int(input("Digite a quantidade de eletrónicos "))
    ConsumoKwH = int(input("Qual a Quantidade de Watts que esse produto consome? (Caso haja diversos tipos, calcule uma média)"))
    horas = int(input("Digite o valor de horas na qual os aparelhos ficam ligados por mês "))

    Consumo_it2 = (ConsumoKwH*horas*dias)/1000
    ConsumoTotal_it2 = (Quantidade*Consumo_it2)
    Valor = (ConsumoTotal_it2*KWh)
    ValorImpactoCO2_Mensal = (ConsumoTotal_it2/Impacto_por_Kwh)
    ValorImpactoCO2_Anual = (ConsumoTotal_it2*12)/Impacto_por_Kwh
    ValorImpactoCO2_ToneladasA = (ValorImpactoCO2_Anual/1000)

    Consumo_Final.append(Valor)
    ImpactoTotal_toneladas.append(ValorImpactoCO2_ToneladasA)
    ImpactoTotalCarbono_Mensal.append(ValorImpactoCO2_Mensal)
    ImpactoTotalCarbono_Anual.append(ValorImpactoCO2_Anual)

    print(f"A sua média de consumo total mensal gasta de energia c/ Televisões é de {ConsumoTotal_it2:.2f} KW/h, resultando em uma conta de R${Valor:.2f} 
    e um impacto ambiental mensal de: {ValorImpactoCO2_Mensal:.2f} Kg CO2e, e anual: {ValorImpactoCO2_Anual:.2f} Kg CO2e")

  elif tipo == 3:
    
    Quantidade = int(input("Digite a quantidade de Impressoras "))
    ConsumoKwH = int(input("Qual a Quantidade de Watts que esse produto consome? (Caso haja diversos tipos, calcule uma média)"))
    horas = int(input("Digite o valor de horas na qual os aparelhos ficam ligados por mês "))

    Consumo_it3 = (ConsumoKwH*horas*dias)/1000
    ConsumoTotal_it3 = (Quantidade*Consumo_it3)
    Valor = (ConsumoTotal_it3*KWh)
    ValorImpactoCO2_Mensal = (ConsumoTotal_it3/Impacto_por_Kwh)
    ValorImpactoCO2_Anual = (ConsumoTotal_it3*12)/Impacto_por_Kwh
    ValorImpactoCO2_ToneladasA = (ValorImpactoCO2_Anual/1000)

    Consumo_Final.append(Valor)
    ImpactoTotal_toneladas.append(ValorImpactoCO2_ToneladasA)
    ImpactoTotalCarbono_Mensal.append(ValorImpactoCO2_Mensal)
    ImpactoTotalCarbono_Anual.append(ValorImpactoCO2_Anual)
    
    print(f"A sua média de consumo total mensal gasta de energia c/ Impressoras é de {ConsumoTotal_it3:.2f} KW/h, resultando em uma conta de R${Valor:.2f} e um impacto ambiental mensal de: {ValorImpactoCO2_Mensal:.2f} Kg CO2e, e anual: {ValorImpactoCO2_Anual:.2f} Kg CO2e")

  elif tipo == 4:
    
    Quantidade = int(input("Digite a quantidade de Lâmpadas "))
    ConsumoKwH = int(input("Qual a Quantidade de Watts que esse produto consome? (Caso haja diversos tipos, calcule uma média)"))
    horas = int(input("Digite o valor de horas na qual os aparelhos ficam ligados por mês "))

    Consumo_it4 = (ConsumoKwH*horas*dias)/1000
    ConsumoTotal_it4 = (Quantidade*Consumo_it4)
    Valor = (ConsumoTotal_it4*KWh)
    ValorImpactoCO2_Mensal = (ConsumoTotal_it4/Impacto_por_Kwh)
    ValorImpactoCO2_Anual = (ConsumoTotal_it4*12)/Impacto_por_Kwh
    ValorImpactoCO2_ToneladasA = (ValorImpactoCO2_Anual/1000)

    Consumo_Final.append(Valor)
    ImpactoTotal_toneladas.append(ValorImpactoCO2_ToneladasA)
    ImpactoTotalCarbono_Mensal.append(ValorImpactoCO2_Mensal)
    ImpactoTotalCarbono_Anual.append(ValorImpactoCO2_Anual)
    
    print(f"A sua média de consumo total mensal gasta de energia c/ Lâmpadas é de {ConsumoTotal_it4:.2f} KW/h, resultando em uma conta de R${Valor:.2f} e um impacto ambiental mensal de: {ValorImpactoCO2_Mensal:.2f} Kg CO2e, e anual: {ValorImpactoCO2_Anual:.2f} Kg CO2e")

  elif tipo == 5:
    
    Quantidade = int(input("Digite a quantidade desse eletrônico "))
    ConsumoKwH = int(input("Qual a Quantidade de Watts que esse produto consome? (Caso haja diversos tipos, calcule uma média)"))
    horas = int(input("Digite o valor de horas na qual os aparelhos ficam ligados por mês "))

    Consumo_it5 = (ConsumoKwH*horas*dias)/1000
    ConsumoTotal_it5 = (Quantidade*Consumo_it5)
    Valor = (ConsumoTotal_it5*KWh)
    ValorImpactoCO2_Mensal = (ConsumoTotal_it5/Impacto_por_Kwh)
    ValorImpactoCO2_Anual = (ConsumoTotal_it5*12)/Impacto_por_Kwh
    ValorImpactoCO2_ToneladasA = (ValorImpactoCO2_Anual/1000)

    Consumo_Final.append(Valor)
    ImpactoTotal_toneladas.append(ValorImpactoCO2_ToneladasA)
    ImpactoTotalCarbono_Mensal.append(ValorImpactoCO2_Mensal)
    ImpactoTotalCarbono_Anual.append(ValorImpactoCO2_Anual)
    
    print(f"A sua média de consumo total mensal gasta de energia c/ Lâmpadas é de {ConsumoTotal_it5:.2f} KW/h, resultando em uma conta de R${Valor:.2f} e um impacto ambiental mensal de: {ValorImpactoCO2_Mensal:.2f} Kg CO2e, e anual: {ValorImpactoCO2_Anual:.2f} Kg CO2e")

  elif tipo == 6:
    SomaValores = sum(Consumo_Final)
    SomaImpacto = sum(ImpactoTotal_toneladas)
    #Fará a junção de todos os valores na lista de Impacto por toneladas, somando-nos e atribuindo o numero a "SomaImpacto"
    Compensacao_Carbono = round(SomaImpacto/0.095)
    #Irá arredondar, e com base na absorção de carbono de uma arvore irá dar a quantia de arvores necessárias p/ compensar o carbono emitido (Arredondará para cima)
    Preco_Arvores = (Compensacao_Carbono*28.5)
    #Esse cálculo simples, pegará a quantidade de arvores e fará * o preço unitário de uma árvore (COM BASE NA ORGANIZAÇÃO IDESAM)
    Preco_Total = SomaValores + Preco_Arvores

    print(f"Você gastará ao mês R${SomaValores:.2f}, com a compensação de carbono o valor subirá para R${Preco_Total:.2f}.")
    print(f" A compensação para a Emissão anual de {SomaImpacto:.2f} Ton CO², com base em todos os eletrónicos é da compra de {round(Compensacao_Carbono)} mudas de arvore, assim sendo {Preco_Arvores:.2f}R$.")

  else: 

    print("Esse é o modo básico da calculadora.")
    
    Basico_Total = int(input("Digite o valor total em KW/H gastos. (Digite um valor Inteiro.) "))
    Basico_Valor = Basico_Total*KWh

    Basico_ImpactoM = Basico_Total/Impacto_por_Kwh
    Basico_ImpactoA = (Basico_Total*12)/Impacto_por_Kwh
    Basico_Impacto_Toneladas = Basico_ImpactoA/1000

    Compensacao_Carbono = Basico_Impacto_Toneladas/0.095
    #0.095 vem do índice de absorção de carbono de uma árvore
    Preco_Arvores = Compensacao_Carbono*28.5
    #28.5, vem do numero de cada compra (Unitária) de arvores, assim, sabendo o quanto ele deve compensar a conta é feita 
    Basico_Soma = Basico_Valor+Preco_Arvores

    print(f"Você gastará ao mês R${Basico_Valor:.2f}, com a compensação de carbono o valor subirá para R${Basico_Soma:.2f}.")
    print(f" A compensação para a Emissão anual de {round(Basico_Impacto_Toneladas, 3)} Ton CO², com base em todos os eletrónicos é da compra de {round(Compensacao_Carbono)} mudas de arvore, assim sendo R${Preco_Arvores:.2f}. (Cálculo de compensação com base no índice da Idesam)")
