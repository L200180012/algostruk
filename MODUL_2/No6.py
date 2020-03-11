from tgs2 import Manusia
class SiswaSMA(Manusia):
    jurusan = "Belum Ditentukan"
    pt = "Belum Ditentukan"
    def __init__(self, nama, nisn, sma):
        self.nama = nama
        self.nisn = nisn
        self.sma = sma
    def __str__(self):
        return "\n\nData Diri\n"\
               +"Nama   : "+self.nama\
               +"\nNISN   : "+str(self.nisn)\
               +"\nSMA    : "+self.sma\
               +"\nPerguruan Tinggi Pilihan : "+self.univ\
               +"\nJurusan Pilihan : "+self.jurusan
    def ambil(self):
        print("\n\nUpdate Data Perguruan Tinggi Pilihan...")
        self.univ = input("Pilih Perguruan Tinggi : ")
        self.jurusan = input("Ambil Jurusan : ")
