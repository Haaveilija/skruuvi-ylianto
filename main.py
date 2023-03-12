import Kortti
import Ylianto
from random import shuffle

def main():

    pakka = Kortti.Kortti.uusi_pakka()
    #print(pakka)
    shuffle(pakka)
    #print(pakka)
    print(pakka[0:4])

    ylianto = Ylianto.Ylianto(pakka[0:4])
    #print(ylianto.laske_maat())
    print(ylianto.tulkitse())


if __name__ == "__main__":
    main()