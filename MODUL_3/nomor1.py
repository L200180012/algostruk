def cekKonsisten(n):
    x = len(n[0])
    z = 0
    for i in range(len(n)):
        if (len(n[i]) == x):
           z+=1
    if(z == len(n)):
        print("Matriks konsisten")
    else:
        print("Matriks tidak konsisten")

def cekInt(n):
    x = 0
    y = 0
    for i in n:
        for j in i:
            y+=1
            if(str(j).isdigit()==False):
                print("Mempunyai Tipe Data yang berbeda")
                break
            else:
                x+=1
                break
    if(x==y):
        print("Mempunyai Tipe Data yang sama")
                    
def ordo(n):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    print("Mempunyai ordo "+str(x)+"x"+str(y))

def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("Ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("Ukuran berbeda")

     
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("Dapat Dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("Tidak memenuhi syarat")

def hitungDeterminan(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = hitungDeterminan(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "Tidak bisa menghitung determinan, bukan matrix bujursangkar"
    else:
        return "Tidak bisa menghitung determinan, bukan matrix bujursangkar"
    return total

a = [[1,2],[3,4]]
b = [[3,4],[5,6]]
c = [[1,"a","b"],["c",5]]
d = [[4,1],[2,4],[3,5]]
e = [[1,3,6],[2,4,5]]
f = [[1,2,3],[4,5,6],[2,4,3]]
g = [[0,-3,4,2],[2,-1,-5,2],[3,7,6,5],[6,1,-8,4]]
cekKonsisten(a)
cekKonsisten(c)
cekKonsisten(g)
cekInt(a)
cekInt(c)
cekInt(f)
ordo(a)
ordo(f)
ordo(d)
ordo(e)
jumlah(a,f)
jumlah(a,b)
kali(a,b)
kali(f,e)
print(hitungDeterminan(a))
print(hitungDeterminan(d))
print(hitungDeterminan(g))
print(hitungDeterminan(e))

