import mahasiswa as mhs

def merge(a):
    if len(a) > 1:
        mid = len(a) // 2
        kiri = a[:mid]
        kanan = a[mid:]
        merge(kiri)
        merge(kanan)
        i = 0;
        j = 0;
        k = 0
        while (i < len(kiri) and j < len(kanan)):
            if kiri[i].uang < kanan[j].uang:
                a[k] = kiri[i]
                i = i + 1
            else:
                a[k] = kanan[j]
                j = j + 1
            k = k + 1
        while i < len(kiri):
            a[k] = kiri[i]
            i = i + 1
            k = k + 1
        while j < len(kanan):
            a[k] = kanan[j]
            j = j + 1
            k = k + 1

def partition( arr, low, high):
    i = (low - 1)
    pivot = arr[high].uang
    for j in range(low, high):
        if arr[j].uang <= pivot:
            i = i + 1
            arr[i].uang, arr[j].uang = arr[j].uang, arr[i].uang
    arr[i + 1].uang, arr[high].uang = arr[high].uang, arr[i + 1].uang
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

c1 = mhs.mhsTIF("Rafi",11,"Surakarta",245000)
c2 = mhs.mhsTIF("Fitria",12,"Sragen",230000)
c3 = mhs.mhsTIF("Nata",23,"Magelang",250000)
c4 = mhs.mhsTIF("Dodo",26,"Semarang",240000)
c5 = mhs.mhsTIF("Hana",27,"Yogyakarta",235000)

x = [c1, c2, c3, c4, c5]

merge(x)
for i in x:
    print(i.uang)

print("------------------------------------")
quickSort(x,0,len(x)-1)
for i in x:
    print(i.uang)
