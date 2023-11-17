import elektrotechnicutils.ohm

from elektrotechnicutils.col import get_coulomb


try:
    print("U=10V, R=100Ohm, kolik je proud? Výsledek = " + str(elektrotechnicutils.ohm.get_i(10, 1000)))
    print("Namerite-li proud 2A a napeti 3V, jaka musi byt hodnota R? Výsledek = " + str(elektrotechnicutils.ohm.get_r(2, 3)))
    print("1. náboj: 50C, 2. náboj: 7C, vzdálenost: 1cm, Výsledek: " + str(get_coulomb(50, 7, 1)))
except Exception as e:
    print(e)
    