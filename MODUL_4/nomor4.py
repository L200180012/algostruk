class MhsTIF(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

class buatArray(object):
    internalData = 11 * [None]

    def __getitem__(self, item):
        return self.internalData[item]
    def __setitem__(self, key, value):
        self.internalData[key] = value
    def cariUangKurang250k(self):
        a = []
        for i in self:
            if i.uangSaku < 250000:
                a.append((i.nama, i.NIM, i.kotaTinggal, i.uangSaku))
        return a

c = buatArray()
c[0] = MhsTIF("Ika",10,"Sukoharjo",240000)
c[1] = MhsTIF("Fitri",12,"Sragen",230000)
c[2] = MhsTIF("Ahmad",2,"Surakarta",250000)
c[3] = MhsTIF("Mela",18,"Surakarta",235000)
c[4] = MhsTIF("Eka",4,"Boyolali",240000)
c[5] = MhsTIF("Fandi",31,"Salatiga",250000)
c[6] = MhsTIF("Deni",13,"Klaten",245000)
c[7] = MhsTIF("Galuh",5,"Wonogiri",220000)
c[8] = MhsTIF("Janto",23,"Klaten",225000)
c[9] = MhsTIF("Hasan",64,"Karanganyar",270000)
c[10] = MhsTIF("Khalid",29,"Purwodadi",265000)

