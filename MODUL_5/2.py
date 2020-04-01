def bubbleSort(N):
    for x in range(len(N)-1,0,-1):
        for i in range(x):
            if N[i]>N[i+1]:
                tmp = N[i]
                N[i] = N[i+1]
                N[i+1] = tmp
 
a = [21,45,67,89,12,17,4,25]
bubbleSort(a)
b = a
a1 = [21,45,67,89,12,17,4,25]
bubbleSort(a1)
c = a1
a2 = (b+c)
bubbleSort(a2)
d = a2
print(d)
