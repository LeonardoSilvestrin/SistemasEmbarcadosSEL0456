with open('ponto_e_virgula/data.txt') as texto:
    linhas = texto.readlines() #extrai as linhas do .txt
with open('dados_modificados','w') as output:
    linhas_novas = ''.join(linhas) #junta a lista do readlines em uma string
    linhas_novas = linhas_novas.split(',') #separa a string em uma lista usando a vírgula como separador, separando inclusive as vírgulas das strings, o que precisa ser corrigido
    
    #agora precisamos encontrar as strings que continham uma vírgula e foram errôneamente separadas, iterando por cada item da lista "linhas_novas"
    
    i=0
    while (i < len(linhas_novas)-1):
        if linhas_novas[i].count("\"") == 1: #se houver um caractere ( " ) somente na string, significa que ela foi separada pelo método .split()
            linhas_novas[i:i+2] = [','.join(linhas_novas[i:i+2])] #unimos a string com a metade separada, que fica logo em seguida
        i+=1
    i+=1
    linhas_novas = ';'.join(linhas_novas) #juntamos a lista resultante usando ; como separador, para por fim salvar no arquivo .txt
    output.write(linhas_novas)