#Binary Search

#dado o vetor:
vetor=[1,5,8,9,12]

def bsearch(v,x):
    li=0
    ls=len(v)-1
    aux=0
    while li<=ls:
        aux=(li+ls)//2
        if v[aux]<x:
            li = aux+1
        elif v[aux]>x:
            ls = aux-1
        else:
            return aux   
    return -1       
        
r = bsearch(vetor,int(input('valor a ser encontrado: ')))
if r != -1:
    print('valor no index:', r)
else:
    print('valor nao esta presente no vetor')
