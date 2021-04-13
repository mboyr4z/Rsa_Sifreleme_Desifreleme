import random
class func():
    def __init__(self,ui):
        self.ui = ui
        self.sayilar = 0


    def aralarindaAsalmi(self,sayi1, sayi2):
        if sayi1 < sayi2:
            kucuk = sayi1
        else:
            kucuk = sayi2
        for bolen in range(2, kucuk + 1):
            if sayi1 % bolen == 0 and sayi2 % bolen == 0:
                return False
        return True


    def randomUret(self):
        ilkSayiAralik = random.randint(100, 200)
        ikinciSayiAralik = random.randint(400, 600)

        ilkSayiAsallar = []
        ikinciSayiAsallar = []

        for i in range(ilkSayiAralik, 300):
            if self.asalKontrol(i):
                ilkSayiAsallar.append(i)

        for i in range(ikinciSayiAralik, 800):
            if self.asalKontrol(i):
                ikinciSayiAsallar.append(i)

        ilkSayiIndis = random.randint(0, len(ilkSayiAsallar) - 1)
        ikinciSayiIndis = random.randint(0, len(ikinciSayiAsallar) - 1)

        ilkSayi = ilkSayiAsallar[ilkSayiIndis]
        ikinciSayi = ikinciSayiAsallar[ikinciSayiIndis]

        return (ilkSayi, ikinciSayi)


    def asalKontrol(self,sayi):
        if sayi < 2:
            return False
        for k in range(2, sayi):
            if sayi % k == 0:
                return False
        return True


    def sifrele(self,metin):

        self.sayilar = self.randomUret()

        p = self.sayilar[0]
        q = self.sayilar[1]

        n = p * q

        L_clear = self.basamakBul(n) - 1
        fi = (p - 1) * (q - 1)
        e = self.eSayisiBul(fi)
        mesajAscii = []

        self.ui.lbl_p.setText(str(p))
        self.ui.lbl_q.setText(str(q))
        self.ui.lbl_n.setText(str(n))
        self.ui.lbl_fi.setText(str(fi))
        self.ui.lbl_e.setText(str(e))



        for i in metin:
            mesajAscii.append(self.ASCII(i))
        self.yaz("ASCII Halleri : \t" + str(mesajAscii))





        for i in range(0, len(mesajAscii)):
            mesajAscii[i] = self.sifirKoy(str(mesajAscii[i]), 3)
        sifirliMetin = ""


        self.yaz("'0' Koyulmuş ASCII :\t" + str(mesajAscii))

        for i in range(0, len(mesajAscii)):         # 1
            sifirliMetin += mesajAscii[i]
        parcaliListe = self.sifreliMetinParcalama(sifirliMetin, L_clear)



        self.yaz("L_Clear'a Göre \nParçalanmış Halleri : \t" + str(parcaliListe))


        sifrelenmis = []

        for i in parcaliListe:
            sifrelenmis.append(pow(int(i), e) % n)



        self.yaz("Şifrelenmiş Halleri : \t" + str(sifrelenmis))



        L_cipher = self.basamakBul(n)
        for i in range(0, len(sifrelenmis)):
            sifrelenmis[i] = self.sifirKoy(sifrelenmis[i], L_cipher)
        sifrelenmisSonHali = ""


        self.yaz("L_Cipher'a Göre \nŞifrelenmişe Sıfır Koy : \t" + str(sifrelenmis))

        for i in sifrelenmis:
            sifrelenmisSonHali += i
        self.yaz("Şifrelenmiş Metin : \t" + sifrelenmisSonHali)
        self.yaz("-----------------------------------------------------------------------")
        return (sifrelenmisSonHali, e)


    def desifrele(self,sifrelenmisMetin, eSayisi):

        p = self.sayilar[0]
        q = self.sayilar[1]
        n = p * q
        L_cipher = self.basamakBul(n)
        L_clear = (self.basamakBul(n) - 1)
        fi = (p - 1) * (q - 1)
        e = eSayisi

        d = 1
        while (True):
            if (e * d - 1) % fi == 0:
                break
            d += 1

        self.ui.lbl_d.setText(str(d))
        parcalar = []
        parcaliMetin = ""
        sayac = 0

        for i in range(0, len(sifrelenmisMetin)):
            if (sayac != L_cipher):
                parcaliMetin += sifrelenmisMetin[i]
                sayac += 1
            if (sayac == L_cipher):
                parcalar.append(parcaliMetin)
                sayac = 0
                parcaliMetin = ""

        self.yaz("Şifre Parçaları : \t" + str(parcalar))

        for i in range(0, len(parcalar)):
            parcalar[i] = pow(int(parcalar[i]) % n, d) % n
        self.yaz("Şifre Çözülmüş Parçaları : \t"+str(parcalar))

        for i in range(0, len(parcalar)):
            parcalar[i] = self.sifirKoy(parcalar[i], L_clear)
        self.yaz("L_Clear'a Göre Parçalar\t" + str(parcalar))

        desifrelemeSonHali = ""
        for i in parcalar:
            desifrelemeSonHali += i

        desifrelemeParcalar = []
        desifrelemeParcaliMetin = ""


        for i in range(0, len(desifrelemeSonHali)):     # 97000
            if (sayac != 3):
                desifrelemeParcaliMetin += desifrelemeSonHali[i]
                sayac += 1
            if (sayac == 3):
                desifrelemeParcalar.append(desifrelemeParcaliMetin)
                sayac = 0
                desifrelemeParcaliMetin = ""





        self.yaz("0'sız ASCII Halleri : \t" + str(desifrelemeParcalar))
        for i in range(0, len(desifrelemeParcalar)):
            desifrelemeParcalar[i] = chr(int(desifrelemeParcalar[i]))
        sonHali = ""

        for i in desifrelemeParcalar:
            sonHali += i

        self.yaz("Deşifrelenmiş Metin : \t" + str(sonHali))
        self.yaz("-----------------------------------------------------------------------")
        return sonHali


    def eSayisiBul(self,fi):
        rand = int(fi / 2) + 100

        sayac = 0
        eSayilari = []
        for i in range(2, fi):
            if self.aralarindaAsalmi(i, fi):
                sayac += 1
                eSayilari.append(i)
            if sayac == 10:
                break
        eSayisi = random.randint(0, len(eSayilari) - 1)

        return eSayilari[eSayisi]


    def ASCII(self,karakter):
        asciiKod = ord(karakter)
        return asciiKod


    def basamakBul(self,sayi):
        basamakSayisi = 1
        x = 1
        while (int(int(sayi) / x) > 9):
            x *= 10
            basamakSayisi += 1

        return basamakSayisi


    def sifirKoy(self,karakterASCII, basamakSayisi):
        say = str(karakterASCII)
        while (self.basamakBul(karakterASCII) < basamakSayisi):
            say = "0" + str(say)
            basamakSayisi -= 1
        return say


    def sifreliMetinParcalama(self,sifreliMetin, L_clear):
        parcalar = []
        parcaliMetin = ""
        sayac = 0

        for i in range(0, len(sifreliMetin)):
            if (sayac != L_clear):
                parcaliMetin += sifreliMetin[i]
                sayac += 1
            if (sayac == L_clear):
                parcalar.append(parcaliMetin)
                sayac = 0
                parcaliMetin = ""
        if (len(parcaliMetin) != 0 and len(parcaliMetin) < L_clear):
            parcalar.append(parcaliMetin)

        sayac2 = len(parcalar[-1])
        while (sayac2 != L_clear):
            parcalar[-1] += "0"
            sayac2 += 1
        return parcalar

    def yaz(self,yazi):
        self.ui.text_yazi.append(yazi)
