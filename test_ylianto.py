from Ylianto import Ylianto
from Kortti import Kortti
import unittest

class TestYlianto22(unittest.TestCase):

    def test_aabb(self):
        maat = "pprr"
        nrot = "2345"
        kortit = []
        for i in range(4):
            kortit.append(Kortti(maat[i],nrot[i]))
        ylianto = Ylianto(kortit)
        tulkinta = ylianto.tulkitse()
        self.assertEqual(tulkinta, "♠ ei ole reno, ♣ on reno")

    def test_abab(self):
        maat = "prpr"
        nrot = "2345"
        kortit = []
        for i in range(4):
            kortit.append(Kortti(maat[i],nrot[i]))
        ylianto = Ylianto(kortit)
        tulkinta = ylianto.tulkitse()
        self.assertEqual(tulkinta, "Molemmat ♠ ja ♣ ovat renoja")

    def test_abba(self):
        maat = "prrp"
        nrot = "2345"
        kortit = []
        for i in range(4):
            kortit.append(Kortti(maat[i],nrot[i]))
        ylianto = Ylianto(kortit)
        tulkinta = ylianto.tulkitse()
        self.assertEqual(tulkinta, "Kumpikaan ♠ tai ♣ eivät ole renoja")


class TestYlianto31(unittest.TestCase):
    def test_aaab(self):
        maat = "HHHR"
        nrot = "854T"
        kortit = []
        for i in range(4):
            kortit.append(Kortti(maat[i],nrot[i]))
        ylianto = Ylianto(kortit)
        tulkinta = ylianto.tulkitse()
        self.assertEqual(tulkinta, "♥ ei ole reno, ♦ on reno")

    def test_aaba(self):
        maat = "HHRH"
        nrot = "AJKQ"
        kortit = []
        for i in range(4):
            kortit.append(Kortti(maat[i],nrot[i]))
        ylianto = Ylianto(kortit)
        tulkinta = ylianto.tulkitse()
        self.assertEqual(tulkinta, "Molemmat ♥ ja ♦ ovat renoja")

    def test_abaa(self):
        maat = "HRRH"
        nrot = "KQJT"
        kortit = []
        for i in range(4):
            kortit.append(Kortti(maat[i],nrot[i]))
        ylianto = Ylianto(kortit)
        tulkinta = ylianto.tulkitse()
        self.assertEqual(tulkinta, "Kumpikaan ♥ tai ♦ eivät ole renoja")

    def test_abbb(self):
        maat = "HRRR"
        nrot = "A234"
        kortit = []
        for i in range(4):
            kortit.append(Kortti(maat[i],nrot[i]))
        ylianto = Ylianto(kortit)
        tulkinta = ylianto.tulkitse()
        self.assertEqual(tulkinta, "♥ ei ole reno, ♦ on reno")



if __name__ == '__main__':
    unittest.main()
