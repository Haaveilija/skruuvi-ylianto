class Kortti:
    def __init__(self, maa, nro):
        self.maa = self.tarkista_maa(str(maa))
        self.nro = self.merkki_to_nro(str(nro))

    def tarkista_maa(self, maa):
        if maa in "prRH":
            return maa
        elif maa in "♠♣♥♦":
            return list(Kortti.maamerkit().keys())[list(Kortti.maamerkit().values()).index(maa)]
        else:
            print(f"Epäkelpo maa: {maa}")
            return "p"

    def merkki_to_nro(self, merkki):
        merkit = {
            "A" : 14,
            "K" : 13,
            "Q" : 12,
            "J" : 11,
            "T" : 10
        }
        if merkki in merkit:
            return merkit[merkki]
        else:
            try:
                nro = int(merkki)
                if 0 < nro < 15:
                    return nro
                else:
                    print(f"Epäkelpo merkki: {merkki}")
                    return 14
            except:
                print(f"Epäkelpo merkki: {merkki}")
                return 0
            
    def nro_to_merkki(self, nro):
        nrot = {
            14: "A",
            13: "K",
            12: "Q",
            11: "J",
            10: "T"
        }
        if nro in nrot:
            return nrot[nro]
        else:
            return str(nro)

    def __str__(self):
        return Kortti.maamerkit()[self.maa] + self.nro_to_merkki(self.nro)
    
    def __repr__(self):
        return Kortti.maamerkit()[self.maa] + self.nro_to_merkki(self.nro)
    
    @classmethod
    def maamerkit(cls):
        return {
            "p" : "♠",
            "r" : "♣",
            "R" : "♦",
            "H" : "♥",
        }
    
    def __eq__(self, other):
        return self.maa == other.maa and self.nro == other.nro

    def __gt__(self, other):
        return self.nro > other.nro
    
    def __lt__(self, other):
        return self.nro < other.nro
    
    def __ge__(self, other):
        return self.nro >= other.nro
    
    def __le__(self, other):
        return self.nro <= other.nro
    
    def sama_maa(self, other):
        return self.maa == other.maa
    
    def sama_nro(self, other):
        return self.nro == other.nro
    
    @classmethod
    def uusi_pakka(cls):
        pakka = []
        for maa in "prRH":
            for n in range(2, 15):
                pakka.append(Kortti(maa, n))
        return pakka