# glade_conversor

Este conversor foi feito da seguinte maneira:

existem três arquivos:

    interface.glade para gerar a interface
    conversor.py para interagir com a interface e com o usuário
    conversor_base.py para tratar os dados e realizar as conversões de unidade
    unidades.txt listando as unidades possíveis

## entradas.txt

o texto de entrada unidades.txt foi estruturado da seguinte maneira:

    [modo, unidade de entrada, unidade de saída, equação]
    O modo é utilizado para filtrar o tipo de conversão que iremos fazer (tempo, comprimento, temperatura etc)
    A equação é o que relaciona a unidade de entrada com a unidade de saída

Por exemplo:
    [temperatura Celsius Farenheit x*9/5+32-y]

    modo: temperatura
    unidade de entrada: celsius
    unidade de saida: farenheit
    equação x*9/5+32-y

A forma da equação foi escolhida para facilitar o uso do sympy, dessa forma se o usuário entrar um valor em celsius ele irá substituir o valor em x, caso o usuario escolha farenheit o sympy vai substituir o valor no valor de y, dessa forma, não precisamos fazer uma equação de farenheit para celsius, facilitando os calculos e diminuindo o número de entradas do "unidades.txt"

## estrutura
o programa foi feito de forma que ele consiga usar passos intermediários para o cálculo da conversão. 

Temos uma equação que relaciona horas e semanas, mas não temos uma equação que relaciona segundos a semanas, porém se quisermos converter segundos em semanas, o programa é capaz de realizar a conversão (segundos -> dias -> semanas), dispensando assim a necessidade de implementar uma função que relacione segundos e semanas diretamente.

## Execução

Para executar este programa é necessário todos os arquivos na pasta "C:\msys64\home\user" , executar o msys64 e executar o seguinte comando no terminal do msys64:

python conversor.py

Dessa forma a interface gráfica deve aparecer.