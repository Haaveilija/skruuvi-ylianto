import Kortti

class Ylianto:
    def __init__(self, kortit):
        if len(kortit) == 4:
            self.kortit = kortit # indeksi 0 on kasan ylin ja indeksi 3 kasan alin
        else:
            print(f"Väärä määrä kortteja! ({len(kortit)})")

    def laske_maat(self):
        maat = {}
        for kortti in self.kortit:
            if kortti.maa in maat:
                maat[kortti.maa] += 1
            else:
                maat[kortti.maa] = 1
        return list(maat.values())
        
    def korttiasettelu(self):
        asettelu = []
        maat = {}
        maa_indeksi = 0
        dummy_maat = "abcd"
        for kortti in self.kortit:
            if kortti.maa not in maat:
                maat[kortti.maa] = dummy_maat[maa_indeksi]
                maa_indeksi += 1
            asettelu.append(maat[kortti.maa])
        return asettelu, maat

    def tulkitse(self):
        maajako = sorted(self.laske_maat())
        asettelu, maat = self.korttiasettelu()
        asettelu = "".join(asettelu)
        tulkinta = []
        
        #print(asettelu)
        if maajako == [2,2]:
            a = Kortti.Kortti.maamerkit()[list(maat.keys())[list(maat.values()).index("a")]]
            b = Kortti.Kortti.maamerkit()[list(maat.keys())[list(maat.values()).index("b")]]
            if asettelu == "aabb":
                tulkinta.append(f"{a} ei ole reno, {b} on reno")
            elif asettelu == "abab":
                tulkinta.append(f"Molemmat {a} ja {b} ovat renoja")
            elif asettelu == "abba":
                tulkinta.append(f"Kumpikaan {a} tai {b} eivät ole renoja")
        elif maajako == [1,3]:
            a = Kortti.Kortti.maamerkit()[list(maat.keys())[list(maat.values()).index("a")]]
            b = Kortti.Kortti.maamerkit()[list(maat.keys())[list(maat.values()).index("b")]]
            if asettelu == "aaab":
                tulkinta.append(f"{a} ei ole reno, {b} on reno")
            elif asettelu == "aaba":
                tulkinta.append(f"Molemmat {a} ja {b} ovat renoja")
            elif asettelu == "abaa":
                tulkinta.append(f"Kumpikaan {a} tai {b} eivät ole renoja")
            elif asettelu == "abbb":
                tulkinta.append(f"{a} ei ole reno, {b} on reno")
        elif maajako == [4]:
            a = Kortti.Kortti.maamerkit()[list(maat.keys())[list(maat.values()).index("a")]]
            if self.kortit == sorted(self.kortit) or self.kortit == reversed(sorted(self.kortit)):
                tulkinta.append("{a} ei ole reno")
            else:
                tulkinta.append("{a} on reno")
        
        if self.kortit[0].nro < 10:
            a = Kortti.Kortti.maamerkit()[list(maat.keys())[list(maat.values()).index("a")]]
            tulkinta.append(f"Kiinniottokortti {a}")

        alin_on_pienin_ko_maata = False
        for kortti in self.kortit:
            if kortti.maa == self.kortit[3].maa and kortti.nro < self.kortit[3].nro:
                alin_on_pienin_ko_maata = False
                break
            elif kortti.maa == self.kortit[3].maa and kortti.nro > self.kortit[3].nro:
                alin_on_pienin_ko_maata = True
        if alin_on_pienin_ko_maata:
            tulkinta.append("Misäärikortit")

        if len(tulkinta) == 0:
            tulkinta.append("¯\_(ツ)_/¯")
        return "\n".join(tulkinta)