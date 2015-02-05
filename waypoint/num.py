# -*- coding: cp1252 -*-
arquivo = open("C:\\2014-01-04-XCT-ELE-01.igc","r")
leitura = arquivo.readlines()
leitura = filter(lambda s: s[0]=='B', leitura)
linhas = len(leitura)
pontos = input("Entre com o numero de pontos vagão que deseja extrair:")
corte_de_linhas = linhas/pontos
corte_de_linhas = int(corte_de_linhas)
print corte_de_linhas
for i,linha in enumerate(leitura):
    if i % corte_de_linhas == 0:
        linha = linha.strip()
        alturaint = int(float(linha[30:]))
        latitude = linha[7:14] + "S"
        longitude = linha[15:23] + "W"
        print (i, alturaint, latitude, longitude)

