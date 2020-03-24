class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(sel, n):
        return n*2
    
####Kali ini melarikannya lewat file yang sama
####lewat python shell juga bisa
##p1 = Manusia("Fatimah")
##p1.ucapkanSalam()

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__ (self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM)\
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' +str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia. Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s,"sambil belajar")
        self.keadaan = "kenyang"

class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print("Python is cool.")
        
c0 = MhsTIF("Ika",10,"Sukoharjo",240000)
c1 = MhsTIF("Budi",51,"Sragen",230000)
c2 = MhsTIF("Ahmad",2,"Surakarta",250000)
c3 = MhsTIF("Candra",18,"Surakarta",235000)
c4 = MhsTIF("Eka",4,"Boyolali",240000)
c5 = MhsTIF("Fandi",31,"Salatiga",250000)
c6 = MhsTIF("Deni",13,"Klaten",245000)
c7 = MhsTIF("Galuh",5,"Wonogiri",245000)
c8 = MhsTIF("Janto",23,"Klaten",245000)
c9 = MhsTIF("Hasan",64,"Karanganyar",270000)
c10 = MhsTIF("Khalid",29,"Purwodadi",265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

target = "Klaten"
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama + " tinggal di "+ target)
