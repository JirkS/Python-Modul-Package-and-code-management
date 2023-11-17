import Ohmuv_zakon
from Ohmuv_zakon import get_coulomb

try:
    # 7.1 Vytvoření vlastního modulu
    print("U=10V, R=100Ohm, kolik je proud? Výsledek = " + str(Ohmuv_zakon.get_i(10, 1000)))
    print("Namerite-li proud 2A a napeti 3V, jaka musi byt hodnota R? Výsledek = " + str(Ohmuv_zakon.get_r(2, 3)))

    # 7.2 Coulumbuv zakon
    print("1. náboj: 50C, 2. náboj: 7C, vzdálenost: 1cm, Výsledek: " + str(get_coulomb(50, 7, 1)))
except Exception as e:
    print(e)
