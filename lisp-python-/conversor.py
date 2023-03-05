def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

with open('lisp-python-\input.data') as data:
    linhas = data.readlines()
with open('lisp-python-\output.data', 'w') as output:
    linhas_novas = linhas
    for i in range(0,len(linhas)):
        linhas_novas[i] = 'linha {}:'.format(i) + ' fib({}) = '.format(linhas[i][0]) + str(fibo(int(linhas[i][0]))) + ' fact({}) = '.format(linhas[i][2]) + str(fact(int(linhas[i][2]))) +'\n'
    linhas_novas2 = ''.join(linhas_novas)
    output.write(linhas_novas2)