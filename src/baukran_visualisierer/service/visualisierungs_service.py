import src.grafischer_prototyp.GrafikBaufeld
import src.grafischer_prototyp.GrafikObjekte
import src.grafischer_prototyp.GrafikKran
import src.baukran_visualisierer.model.baustelle
from vpython import *

class virt_Baustelle:
    def __init__(self, baustelle):
        self.baustelle = baustelle

    def speichere_Baustelle(self, baustelle):
        self.baustelle = baustelle

    def erhalte_Baustelle(self):
        return self.baustelle

global_baustelle = virt_Baustelle(None)
global_kran = src.grafischer_prototyp.GrafikKran.GrafikKran()
bauteil_liste = []

def visualisiere_baustelle(baustelle):
    # Visualisiert Grundbaustelle
    global_baustelle.speichere_Baustelle(baustelle)

    beispiel_baufeld = src.grafischer_prototyp.GrafikBaufeld.GrafikBaufeld()
    beispiel_baufeld.erzeuge_baufeld(baustelle.baufeld.breite_y, baustelle.baufeld.laenge_x)
    #beispiel_kran = src.grafischer_prototyp.GrafikKran.GrafikKran()
    global_kran.erzeuge_kran(baustelle.kran.position_x, baustelle.kran.position_y, baustelle.kran.hoehe,
                               baustelle.kran.ausladung)
    for bauteil in baustelle.bauteile:
        temp_bauteil = src.grafischer_prototyp.GrafikObjekte.GrafikBauteil()
        temp_bauteil.erzeuge_bauteil(bauteil.name,bauteil.position_x, bauteil.position_y, bauteil.position_z)
        bauteil_liste.append(temp_bauteil)
    for hindernisse in baustelle.gegenstaende:
        temp_hindernisse = src.grafischer_prototyp.GrafikObjekte.GrafikHindernis()
        temp_hindernisse.erzeuge_hindernis(hindernisse.position_x, hindernisse.position_y, hindernisse.position_z)

    box()

    def B(b):
        baustelle.naechste_krananweisung_ausfuehren()
        print("The button said this: ", b.text)

    button(bind=B, text='Click me!')
    scene.append_to_caption('\n\n')
    while True:
        pass

def visualisiere_greife(haken_z):
    print(global_baustelle.erhalte_Baustelle())
    hoehe = global_kran.greifarm.pos.y - haken_z
    print(haken_z)
    print(global_kran.greifarm.pos.y)
    global_kran.veraendere_greifarm_hoehe("senke", hoehe, None)

def visualisiere_bringe_an(winkel_vorher, winkel_nachher, haken_x, haken_y, haken_z, bauteil_name):
    print("test")
    print(winkel_vorher)
    print(winkel_nachher)
    pos = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
    pos.erzeuge_position(haken_x, haken_y, haken_z)
    if winkel_nachher - winkel_vorher < 0:
        winkel = -1 * (winkel_nachher - winkel_vorher)
    else:
        winkel = winkel_nachher - winkel_vorher

    Objekt = None
    if bauteil_name is not None:
        for bauteil in bauteil_liste:
            if bauteil.name == bauteil_name:
                Objekt = bauteil

    global_kran.test_func(winkel, winkel_vorher, pos, Objekt)

def visualisiere_senke_um(hoehe, bauteil_name):
    Objekt = None
    if bauteil_name is not None:
        for bauteil in bauteil_liste:
            if bauteil.name == bauteil_name:
                Objekt = bauteil
    global_kran.veraendere_greifarm_hoehe("senke", hoehe, Objekt)


def visualisiere_hebe_um(hoehe, bauteil_name):
    Objekt = None
    if bauteil_name is not None:
        for bauteil in bauteil_liste:
            if bauteil.name == bauteil_name:
                Objekt = bauteil
    global_kran.veraendere_greifarm_hoehe("erhoehe", hoehe, Objekt)
