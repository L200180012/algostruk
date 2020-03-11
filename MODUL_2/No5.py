from tgs2 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    makul=[]
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
    def ambilMK(self,mk):
        self.makul.append(mk)
    def listKuliah(self):
        print(self.makul)
    def hapusKuliah(self, mk):
        return self.makul.remove(mk)
