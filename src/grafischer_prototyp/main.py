from vpython import *
from GrafikKran import *
from GrafikObjekte import *
from GrafikBaufeld import *

"""
Diese main wurde für Standalone Version der grafischen Darstellung und Animation benutzt sowie zum Testen. 
Die Animationen  funktionieren nicht mehr, da die Klassen mit den Animationen sich dem Model Klasse angepasst haben. 
Auf https://github.com/jogerwert/BaukranVisualisierer ist eine frühere Version welche als Standalone funktioneiert. 
"""

def test_baufeld():
    baufeld = GrafikBaufeld()
    baufeld.erzeuge_baufeld(10, 10)


def test_bauteil():
    bauteil1 = GrafikBauteil()
    bauteil2 = GrafikBauteil()
    bauteil1.erzeuge_bauteil(3, 3, 0)
    bauteil2.erzeuge_bauteil(3, 4, 0)
    bauteil2.erhoehe_bauteil(5)
    bauteil1.verschiebe_bauteil(5, 5, 5)


def test_hindernis():
    hindernis1 = GrafikHindernis()
    hindernis2 = GrafikHindernis()
    hindernis3 = GrafikHindernis()
    hindernis1.erzeuge_hindernis(1, 1, 0)
    hindernis2.erzeuge_hindernis(1, 2, 0)
    hindernis3.erzeuge_hindernis(1, 3, 0)


def test_kran():
    kran = GrafikKran()
    kran.erzeuge_kran(1, 1, 5, 7)
    bauteil3 = GrafikBauteil()
    bauteil3.erzeuge_bauteil(4, 4, 0)
    #bauteil4 = GrafikBauteil()
    #bauteil4.erzeuge_bauteil(kran.ausleger.axis.x , kran.ausleger.axis.z , kran.ausleger.axis.y + kran.ausleger.pos.y)
    winkel = -1*kran.berechne_drehwinkel_objekt(bauteil3)
    #kran.drehe_ausleger_Bauteil(winkel, None)
    #bauteil5 = GrafikBauteil()
    #bauteil5.erzeuge_bauteil(1.70711, 1.70711, 4.5)
    pos = GrafikPosition()
    pos.erzeuge_position(4, 3, 0)
    #kran.test_bewege_laufkatze_ausleger_bauteil2(pos.erhalte_position().x, winkel, pos)
    #kran2 = GrafikKran()
    #kran2.erzeuge_kran(0, 0, 5, 7)
    #kran.test_berechne_punkt_kreisgleichung(winkel)
    kran.test_bewege_laufkatze_ausleger_bauteil(pos.erhalte_position().x ,winkel, pos)
    #kran2 = GrafikKran()
    #kran2.erzeuge_kran(1, 1, 5, 7)
    #kran2.drehe_ausleger_Bauteil(winkel, None)
    #kran2.drehe_ausleger_Bauteil(23, None)
    #kran2.test_bewege_laufkatze_ausleger_bauteil(pos.erhalte_position().x, 22.5, pos)
    #kran2.test_bewege_laufkatze_ausleger_bauteil(pos.erhalte_position().x, 22.5, pos)
    #sleep(3)
    #kran.bewege_laufkatze_bauteil(bauteil3.erhalte_position().x, bauteil3)
    #pos = GrafikPosition()
    #pos.erzeuge_position(2, 2, 0)
    #kran.bewege_laufkatze_bauteil(pos.erhalte_position().x, pos)
    #kran.senke_greifarm(1)

    #x = threading.Thread(target=kran.erhoehe_greifarm, args=(4,))
    #y = threading.Thread(target=bauteil3.erhoehe_bauteil, args=(4,))
    #x.start()
    #y.start()
    #kran.erhoehe_greifarm(4)
    #bauteil3.erhoehe_bauteil(4)

def test_kran2():
    kran = GrafikKran()
    kran.erzeuge_kran(1, 1, 5, 7)
    bauteil3 = GrafikBauteil()
    bauteil3.erzeuge_bauteil(3, 5, 0)
    winkel = kran.berechne_drehwinkel_objekt(bauteil3)
    print(winkel)
    sleep(2)
    t_winkel = kran.bringe_an(winkel, bauteil3, 0,,
    kran.senke_greifarm(0)
    kran.erhoehe_greifarm(4)

    bauteil4 = GrafikBauteil()
    bauteil4.erzeuge_bauteil(3, 0, 0)
    winkel2 = kran.berechne_drehwinkel_objekt(bauteil4)
    print(winkel2)
    t_winkel = kran.bringe_an(winkel2, bauteil4, t_winkel,,
    kran.senke_greifarm(0)
    kran.erhoehe_greifarm(4)
    #kran2 = GrafikKran()
    #kran2.erzeuge_kran(0, 0, 5, 7)
    #kran2.drehe_ausleger_Bauteil(winkel, None)
    #kran2.bewege_laufkatze_bauteil(bauteil3.erhalte_position().x, bauteil3)
    #kran2.senke_greifarm(0)

    bauteil5 = GrafikBauteil()
    bauteil5.erzeuge_bauteil(2, 6, 0)
    winkel2 = kran.berechne_drehwinkel_objekt(bauteil5)
    print(winkel2)
    kran.bringe_an(winkel2, bauteil5, t_winkel,,
    kran.senke_greifarm(0)

def test_kran3():
    kran = GrafikKran()
    kran.erzeuge_kran(5, 5, 5, 7)
    bauteil3 = GrafikBauteil()
    bauteil3.erzeuge_bauteil(3, 5, 0)
    winkel = kran.berechne_drehwinkel_objekt(bauteil3)
    print(winkel)
    sleep(2)
    t_winkel = kran.bringe_an(winkel, bauteil3, 0,,
    kran.senke_greifarm(0)
    kran.erhoehe_greifarm(4)

    bauteil4 = GrafikBauteil()
    bauteil4.erzeuge_bauteil(3, 0, 0)
    winkel2 = kran.berechne_drehwinkel_objekt(bauteil4)
    print(winkel2)
    t_winkel = kran.bringe_an(winkel2, bauteil4, t_winkel,,
    kran.senke_greifarm(0)
    kran.erhoehe_greifarm(4)
    #kran2 = GrafikKran()
    #kran2.erzeuge_kran(0, 0, 5, 7)
    #kran2.drehe_ausleger_Bauteil(winkel, None)
    #kran2.bewege_laufkatze_bauteil(bauteil3.erhalte_position().x, bauteil3)
    #kran2.senke_greifarm(0)

    bauteil5 = GrafikBauteil()
    bauteil5.erzeuge_bauteil(2, 6, 0)
    winkel2 = kran.berechne_drehwinkel_objekt(bauteil5)
    print(winkel2)
    kran.bringe_an(winkel2, bauteil5, t_winkel,,
    kran.senke_greifarm(0)

def test_kran4():
    kran = GrafikKran()
    kran.erzeuge_kran(0, 0, 5, 7)
    bauteil3 = GrafikBauteil()
    bauteil3.erzeuge_bauteil(4, 4, 0)
    pos = GrafikPosition()
    pos.erzeuge_position(4, 4, 0)
    winkel = kran.berechne_drehwinkel_objekt(bauteil3)
    print(winkel)
    sleep(2)
    t_winkel = kran.bringe_an(winkel, 0, pos, None, )
    kran.senke_greifarm(4)

    pos = GrafikPosition()
    pos.erzeuge_position(2, 3, 0)
    winkel = kran.berechne_drehwinkel_objekt(pos)
    print(winkel)
    t_winkel = kran.bringe_an(winkel, t_winkel, pos, bauteil3, )
    kran.senke_greifarm(4)
    kran.erhoehe_greifarm(4)

def test_kran5():
    kran = GrafikKran()
    kran.erzeuge_kran(0, 0, 5, 7)
    bauteil3 = GrafikBauteil()
    bauteil3.erzeuge_bauteil(4, 1, 0)
    pos = GrafikPosition()
    pos.erzeuge_position(4, 1 ,0)
    winkel = kran.berechne_drehwinkel_objekt(pos)
    t_winkel = kran.bringe_an(winkel, 0, pos, None, )
    kran.senke_greifarm(4,None)
    kran.erhoehe_greifarm(2,bauteil3)
    pos = GrafikPosition()
    pos.erzeuge_position(4, 4, 0)
    winkel = kran.berechne_drehwinkel_objekt(pos)
    t_winkel = kran.bringe_an(winkel, t_winkel, pos, bauteil3, )
    #kran.senke_greifarm(2, bauteil3)
    #kran.erhoehe_greifarm(4, None)


def ausfuehrung_beispiel():
    beispiel_baufeld = GrafikBaufeld()
    beispiel_baufeld.erzeuge_baufeld(10, 5)

    beispiel_hindernis = []
    beispiel_hindernis.append(GrafikHindernis())
    beispiel_hindernis.append(GrafikHindernis())
    beispiel_hindernis[0].erzeuge_hindernis(3, 2, 0)
    beispiel_hindernis[1].erzeuge_hindernis(3, 2, 1)

    beispiel_bauteile = []
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile[0].erzeuge_bauteil(0, 2, 0)
    beispiel_bauteile[1].erzeuge_bauteil(1, 2, 0)
    beispiel_bauteile[2].erzeuge_bauteil(2, 2, 0)

    beispiel_kran = GrafikKran()
    beispiel_kran.erzeuge_kran(0, 0, 5, 10)

    winkel = beispiel_kran.berechne_drehwinkel_zum_objekt(beispiel_bauteile[1])
    beispiel_kran.drehe_ausleger(winkel)
    beispiel_kran.debug_bewege_laufkatze(beispiel_bauteile[1].erhalte_position().x,
                                              beispiel_bauteile[1].erhalte_position().z)
    beispiel_kran.senke_greifarm(1)
    x = threading.Thread(target=beispiel_kran.erhoehe_greifarm, args=(2,))
    y = threading.Thread(target=beispiel_bauteile[1].erhoehe_bauteil, args=(2,))
    x.start()
    y.start()
    sleep(3)
    placeholder_position = GrafikPosition()
    placeholder_position.erzeuge_position(6, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_zum_objekt(placeholder_position)
    beispiel_kran.drehe_ausleger_Bauteil(winkel, beispiel_bauteile[1])
    print(beispiel_bauteile[1].erhalte_position())
    beispiel_kran.debug_bewege_laufkatze_bauteil(placeholder_position.erhalte_position().x, placeholder_position.erhalte_position().z,
                                                 beispiel_bauteile[1].erhalte_position())
    print(beispiel_bauteile[1].erhalte_position())

def test_kran6():
    beispiel_baufeld = GrafikBaufeld()
    beispiel_baufeld.erzeuge_baufeld(10, 5)

    beispiel_hindernis = []
    beispiel_hindernis.append(GrafikHindernis())
    beispiel_hindernis.append(GrafikHindernis())
    beispiel_hindernis[0].erzeuge_hindernis(3, 2, 0)
    beispiel_hindernis[1].erzeuge_hindernis(3, 2, 1)

    beispiel_bauteile = []
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile[0].erzeuge_bauteil(0, 2, 0)
    beispiel_bauteile[1].erzeuge_bauteil(1, 2, 0)
    beispiel_bauteile[2].erzeuge_bauteil(2, 2, 0)

    beispiel_kran = GrafikKran()
    beispiel_kran.erzeuge_kran(0, 0, 5, 10)

    #anweisung 1
    pos = GrafikPosition()
    pos.erzeuge_position(1, 2, 0)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, 0, pos, None, )
    beispiel_kran.senke_greifarm(4, None)
    beispiel_kran.erhoehe_greifarm(2, beispiel_bauteile[1])
    pos = GrafikPosition()
    pos.erzeuge_position(6, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, beispiel_bauteile[1], )
    beispiel_kran.senke_greifarm(2,beispiel_bauteile[1])

    # anweisung 2
    beispiel_kran.erhoehe_greifarm(2, None)
    pos = GrafikPosition()
    pos.erzeuge_position(0, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, None, )
    beispiel_kran.senke_greifarm(2, None)
    beispiel_kran.erhoehe_greifarm(2, beispiel_bauteile[0])
    pos = GrafikPosition()
    pos.erzeuge_position(5, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, beispiel_bauteile[0], )
    beispiel_kran.senke_greifarm(2, beispiel_bauteile[0])

    # anweisung 3
    beispiel_kran.erhoehe_greifarm(2, None)
    pos = GrafikPosition()
    pos.erzeuge_position(2, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, None, )
    beispiel_kran.senke_greifarm(2, None)
    beispiel_kran.erhoehe_greifarm(2, beispiel_bauteile[2])
    pos = GrafikPosition()
    pos.erzeuge_position(6, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, beispiel_bauteile[2], )
    beispiel_kran.senke_greifarm(1, beispiel_bauteile[2])
    beispiel_kran.erhoehe_greifarm(3, None)

    print(beispiel_bauteile[0].erhalte_position())
    print(beispiel_bauteile[1].erhalte_position())
    print(beispiel_bauteile[2].erhalte_position())

def test_kran7():
    beispiel_baufeld = GrafikBaufeld()
    beispiel_baufeld.erzeuge_baufeld(10, 5)

    beispiel_hindernis = []
    beispiel_hindernis.append(GrafikHindernis())
    beispiel_hindernis.append(GrafikHindernis())
    beispiel_hindernis[0].erzeuge_hindernis(3, 2, 0)
    beispiel_hindernis[1].erzeuge_hindernis(3, 2, 1)

    beispiel_bauteile = []
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile[0].erzeuge_bauteil("a", 0, 2, 0)
    beispiel_bauteile[1].erzeuge_bauteil("b", 1, 2, 0)
    beispiel_bauteile[2].erzeuge_bauteil("c", 2, 2, 0)
    #beispiel_bauteile[3].erzeuge_bauteil(4, 4, 0)

    beispiel_kran = GrafikKran()
    beispiel_kran.erzeuge_kran(1, 1, 5, 10)
    beispiel_kran.animationsgeschwindigkeit(1)

    #anweisung 1
    pos = GrafikPosition()
    pos.erzeuge_position(1, 2, 0)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, 0, pos, None, )
    #beispiel_kran.veraendere_greifarm_hoehe("senke",4, None)
    beispiel_kran.veraendere_greifarm_hoehe("erhoehe",2, beispiel_bauteile[1])
    pos = GrafikPosition()
    pos.erzeuge_position(6, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, beispiel_bauteile[1], )
    beispiel_kran.veraendere_greifarm_hoehe("senke",2,beispiel_bauteile[1])

    # anweisung 2
    beispiel_kran.veraendere_greifarm_hoehe("erhoehe",2, None)
    pos = GrafikPosition()
    pos.erzeuge_position(0, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, None, )
    beispiel_kran.veraendere_greifarm_hoehe("senke",2, None)
    beispiel_kran.veraendere_greifarm_hoehe("erhoehe",2, beispiel_bauteile[0])
    pos = GrafikPosition()
    pos.erzeuge_position(5, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, beispiel_bauteile[0], )
    beispiel_kran.veraendere_greifarm_hoehe("senke",2, beispiel_bauteile[0])

    # anweisung 3
    beispiel_kran.veraendere_greifarm_hoehe("erhoehe",2, None)
    pos = GrafikPosition()
    pos.erzeuge_position(2, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, None, )
    beispiel_kran.veraendere_greifarm_hoehe("senke", 2, None)
    beispiel_kran.veraendere_greifarm_hoehe("erhoehe", 2, beispiel_bauteile[2])
    pos = GrafikPosition()
    pos.erzeuge_position(6, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, beispiel_bauteile[2], )
    beispiel_kran.veraendere_greifarm_hoehe("senke", 1, beispiel_bauteile[2])
    beispiel_kran.veraendere_greifarm_hoehe("erhoehe",3, None)

    #pos = GrafikPosition()
    #pos.erzeuge_position(4, 4, 2)
    #winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    #t_winkel = beispiel_kran.test_func(winkel, t_winkel, pos, None)
    #beispiel_kran.veraendere_greifarm_hoehe("senke",4, None)
    #beispiel_kran.veraendere_greifarm_hoehe("erhoehe",2, beispiel_bauteile[3])
    #pos = GrafikPosition()
    #pos.erzeuge_position(7, 3, 2)
    #winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    #t_winkel = beispiel_kran.test_func(winkel, t_winkel, pos, beispiel_bauteile[3])
    #beispiel_kran.veraendere_greifarm_hoehe("senke",2, beispiel_bauteile[3])
    #beispiel_kran.veraendere_greifarm_hoehe("erhoehe",4, None)

    print(beispiel_bauteile[0].erhalte_position())
    print(beispiel_bauteile[1].erhalte_position())
    print(beispiel_bauteile[2].erhalte_position())
    #print(beispiel_bauteile[3].erhalte_position())
    while True:
        pass

def test_kran8():
    beispiel_baufeld = GrafikBaufeld()
    beispiel_baufeld.erzeuge_baufeld(10, 10)

    beispiel_kran = GrafikKran()
    beispiel_kran.erzeuge_kran(5, 5, 5, 10)

    beispiel_bauteile = []
    beispiel_bauteile.append(GrafikBauteil())
    beispiel_bauteile[0].erzeuge_bauteil("a",2,2,0)
    pos = GrafikPosition()
    pos.erzeuge_position(2, 2, 0)
    beispiel_kran.animationsgeschwindigkeit(1)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, 0, pos, None, None)
    #beispiel_kran.veraendere_greifarm_hoehe("senke", 4, None)
    beispiel_kran.veraendere_greifarm_hoehe("erhoehe", 2, beispiel_bauteile[0])
    pos = GrafikPosition()
    pos.erzeuge_position(4, 4, 2)
    winkel = beispiel_kran.berechne_drehwinkel_objekt(pos)
    t_winkel = beispiel_kran.bringe_an(winkel, t_winkel, pos, beispiel_bauteile[0], None)
    beispiel_kran.veraendere_greifarm_hoehe("senke", 2, beispiel_bauteile[0])
    while True:
        pass

scene.background = color.white
scene.width = 1920
scene.height = 1080
#ausfuehrung_beispiel()
#test_baufeld()
#test_bauteil()
#test_hindernis()
#sleep(3)
test_kran7()
while True:
    pass