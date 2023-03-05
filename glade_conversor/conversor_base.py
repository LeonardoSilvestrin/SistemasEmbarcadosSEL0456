import sympy as sp
#abre o documento com os dados de conversão:
#with open('C:\\msys64\\home\\Leo\\unidades.txt') as unidades_base:
with open('unidades.txt') as unidades_base: 
    dados = unidades_base.readlines()
unidades_conv = list()
for expressao in dados:
    unidades_conv.append(expressao.replace('\n','')) #tira os \n

#função criada para isolar cada parte da expressão
#fica na forma ["tipo unidade1 unidade2 expressao"] --> ["tempo,"segundos","minutos","x/60-y"]
def unidades_do_tipo(tipo):
    unidades = list()
    for operacao in unidades_conv:
        [tipo0,un1,un2,_] = separa_expressao(operacao)
        if tipo0 == tipo:
            if un1 not in unidades:
                unidades.append(un1)
            if un2 not in unidades:
                unidades.append(un2)
    return unidades
def tipos_de_unidade():
        tipos = list()
        for operacao in unidades_conv:
            [tipo,_,_,_] = separa_expressao(operacao)
            if tipo not in tipos:
                tipos.append(tipo)
        return tipos
def separa_expressao(expressao): #retorna uma lista de strings
    aux = expressao.split()
    tipo = aux[0]
    un1 = aux[1]
    un2 = aux[2]
    taxa_conversao = aux[3]
    return [tipo, un1, un2, taxa_conversao]

# funcao que calcula quais conversões são possíveis dada uma unidade

def conversoes_possiveis(unidade_1):
    unidades_possiveis_de_converter = list()
    for expressao in unidades_conv:
        separada = separa_expressao(expressao)
        if unidade_1 in separada:
            if separada[1] == unidade_1:
                unidades_possiveis_de_converter.append(separada[2])
            if separada[2] == unidade_1:
                unidades_possiveis_de_converter.append(separada[1])
    return unidades_possiveis_de_converter

#função que realiza a conversão de unidades 

def converte(unidade_1,unidade_2,valor):
    possiveis = conversoes_possiveis(unidade_1)
    if unidade_2 not in possiveis: #checa se a unidade pode ser diretamente convertida na outra
        for unidade in possiveis:
            if unidade_2 not in conversoes_possiveis(unidade): #checa se a unidade pode ser convertida na outra via 1 intermediario
                pass
            else:
                unidade_intermediaria = unidade #unidade de conversão intermediaria
                intermed = converte(unidade_1,unidade_intermediaria,valor) 
                for num in intermed:
                    return converte(unidade_intermediaria,unidade_2,num)
    else:
        for expressao in unidades_conv:
            if unidade_1 in expressao and unidade_2 in expressao:
                [_, un_1, _, equacao] = separa_expressao(expressao)
                if unidade_1 == un_1:
                    x = valor
                    y = sp.Symbol('y')
                    equacao_nova = equacao.replace('x',str(x))
                    return sp.solve(equacao_nova,y)
                if unidade_2 == un_1:
                    x = sp.Symbol('x')
                    y = valor
                    equacao_nova = equacao.replace('y',str(y))
                    return sp.solve(equacao_nova,x)
