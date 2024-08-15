#BubbleSort
count = 0
vetor=[]

while True:
    a = int(input('digite um numero , -1 para sair'))

    if a ==-1:
        break

    else:
        vetor.append(a)

    count+=1

def bubble(v,x):
    for j in range(0,len(v)):
        for i in range(0,len(v)-1):
            if v[i]>v[i+1]:
                aux=v[i]
                v[i]=v[i+1]
                v[i+1]=aux
    return v

print(bubble(vetor,2))

