class Mahasiswa(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
def bubbleSort(N):
    for x in range(len(N)-1,0,-1):
        for i in range(x):
            if N[i]>N[i+1]:
                tmp = N[i]
                N[i] = N[i+1]
                N[i+1] = tmp
                
c0 = Mahasiswa('Caca',7,'Semarang',240000)
c1 = Mahasiswa('Fitria',12,'Sragen',230000)
c2 = Mahasiswa('Hana',2,'Bandung',250000)
c3 = Mahasiswa('Dila',21,'Yogyakarta',235000)
c4 = Mahasiswa('Dodo',17,'Magelang',240000)
c5 = Mahasiswa('Rara',4,'Klaten',250000)
c6 = Mahasiswa('Mela',36,'Surakarta',245000)
c7 = Mahasiswa('Okta',40,'Pacitan',245000)
c8 = Mahasiswa('Lani',27,'Klaten',245000)
c9 = Mahasiswa('Nasha',19,'Boyolali',270000)
c10 = Mahasiswa('Rafi',8,'Surakarta',230000)

a = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
bubbleSort(a)
print(a)
