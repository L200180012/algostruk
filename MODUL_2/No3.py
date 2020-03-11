from tgs2 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self,k):
        self.kota=k
    def tambahUangSaku(self,n):
        self.uang+=n
        
nama = input("Masukkan Nama Anda      : ")
NIM  = input("Masukkan NIM Anda       : ")
kota = input("Masukkan Kota Asal Anda : ")
us   = input("Masukkan Uang Saku Anda : ")

m2 = Mahasiswa(nama,NIM,kota,us)
