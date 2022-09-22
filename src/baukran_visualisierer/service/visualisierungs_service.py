import grafischer_prototyp.GrafikBaufeld
import grafischer_prototyp.GrafikObjekte
import grafischer_prototyp.GrafikKran
import baukran_visualisierer.model.baustelle
from vpython import *
import ctypes  # An included library with Python install.
from baukran_visualisierer.datei_management import file_picker
from baukran_visualisierer.service import parser_service #,visualisierungs_service

class virt_Baustelle:
    def __init__(self, baustelle):
        self.baustelle = baustelle

    def speichere_Baustelle(self, baustelle):
        self.baustelle = baustelle

    def erhalte_Baustelle(self):
        return self.baustelle

global_baustelle = virt_Baustelle(None)
global_kran = grafischer_prototyp.GrafikKran.GrafikKran()
bauteil_liste = []
button_liste = []
slider_liste = []
hindernis_liste = []
beispiel_baufeld = grafischer_prototyp.GrafikBaufeld.GrafikBaufeld()

def setze_visualisierungs_funktionen(baustelle):
    baustelle.kran.visualisiere_greife = visualisiere_greife
    baustelle.kran.visualisiere_richte_aus = visualisiere_richte_aus
    baustelle.kran.visualisiere_lasse_los = visualisiere_lasse_los
    baustelle.kran.visualisiere_bringe_an = visualisiere_bringe_an
    baustelle.kran.visualisiere_senke_um = visualisiere_senke_um
    baustelle.kran.visualisiere_hebe_um = visualisiere_hebe_um

def visualisiere_baustelle(baustelle):
    global_baustelle.speichere_Baustelle(baustelle)
    erzeuge_menu_elemente()
    einstellen_Bildwerte()
    beispiel_baufeld.erzeuge_baufeld(global_baustelle.erhalte_Baustelle().baufeld.laenge_x,
                                     global_baustelle.erhalte_Baustelle().baufeld.breite_y)
    global_kran.erzeuge_kran(global_baustelle.erhalte_Baustelle().kran.position_x,
                             global_baustelle.erhalte_Baustelle().kran.position_y,
                             global_baustelle.erhalte_Baustelle().kran.hoehe,
                             global_baustelle.erhalte_Baustelle().kran.ausladung)
    for bauteil in global_baustelle.erhalte_Baustelle().bauteile:
        temp_bauteil = grafischer_prototyp.GrafikObjekte.GrafikBauteil()
        temp_bauteil.erzeuge_bauteil(bauteil.name, bauteil.position_x, bauteil.position_y, bauteil.position_z)
        bauteil_liste.append(temp_bauteil)
    for hindernisse in global_baustelle.erhalte_Baustelle().gegenstaende:
        temp_hindernisse = grafischer_prototyp.GrafikObjekte.GrafikHindernis()
        temp_hindernisse.erzeuge_hindernis(hindernisse.position_x, hindernisse.position_y, hindernisse.position_z)
        hindernis_liste.append(temp_hindernisse)

    while True:
        pass

def erzeuge_menu_elemente():
    def Mbox(title, text):
        MB_SYSTEMMODAL = 0x00001000
        return ctypes.windll.user32.MessageBoxW(0, text, title, MB_SYSTEMMODAL)

    def deaktivieren_button():
        button_liste[0].disabled = True
        button_liste[1].disabled = True
        button_liste[2].disabled = True
        button_liste[4].disabled = True

    def reaktivieren_button():
        button_liste[0].disabled = False
        button_liste[1].disabled = False
        button_liste[2].disabled = False
        button_liste[4].disabled = False

    def button_naechste_krananweisung():
        deaktivieren_button()
        global_baustelle.erhalte_Baustelle().naechste_krananweisung_ausfuehren()
        reaktivieren_button()

    def button_naechste_montageanweisung():
        deaktivieren_button()
        global_baustelle.erhalte_Baustelle().naechste_montageanweisung_ausfuehren()
        reaktivieren_button()

    def button_alle_montageanweisungen(b):
        deaktivieren_button()
        global_baustelle.erhalte_Baustelle().alle_montageanweisungen_ausfuehren()
        reaktivieren_button()

    def button_zeit(b):
        Mbox('Zeitberechnung', 'Für den Bauablauf sind ' + str(global_kran.time) + ' Sekunden vergangen')

    def button_neues_bauprojekt(b):
        from baukran_visualisierer.main import start_file_picker

        for element in bauteil_liste:
            element.erhalte_bauteil().visible = False
            del element
        for element in hindernis_liste:
            element.erhalte_hindernis().visible = False
            del element
        for element in beispiel_baufeld.erhalte_baufeld_liste():
            element.visible = False
            del element

        global_kran.loesche_kran()

        for element in button_liste:
            element.delete()
        for element in slider_liste:
            element.delete()
        while len(button_liste) > 0:
            button_liste.pop(0)
        while len(slider_liste) > 0:
            slider_liste.pop(0)
        while len(bauteil_liste) > 0:
            bauteil_liste.pop(0)
        while len(hindernis_liste) > 0:
            hindernis_liste.pop(0)

        beispiel_baufeld.loesche_liste()
        scene.caption = ""
        start_file_picker()

    def button_kollision(m):
        if len(global_kran.get_collision())>0:
            Mbox('Kollision', 'Kollisionen sind bei Befehle ' + str(global_kran.get_collision()) + ' aufgetreten')
        else:
            Mbox('Kollision', 'Keine Kollisionen aufgetreten')

    def slider_animationsgeschwindigkeit(s):
        global_kran.animationsgeschwindigkeit(s.value)

    def erzeuge_elemente():
        button_liste.append(button(bind=button_naechste_krananweisung, text='Naechste Krananweisung'))
        button_liste.append(button(bind=button_naechste_montageanweisung, text='Naechste Montageanweisung'))
        button_liste.append(button(bind=button_alle_montageanweisungen, text='Alle Montageanweisungen'))
        button_liste.append(button(bind=button_zeit, text='Zeit'))
        scene.append_to_caption('\n\n')
        slider_liste.append(slider(bind=slider_animationsgeschwindigkeit))
        scene.append_to_caption('\n\n')
        button_liste.append(button(bind=button_neues_bauprojekt, text='Neues Bauprojekt'))
        button_liste.append(button(bind=button_kollision, text='Kollision'))
        scene.append_to_caption('\n\n')

    erzeuge_elemente()

def visualisiere_bringe_an(winkel_vorher, winkel_nachher, haken_x, haken_y, haken_z, bauteil_name):
    pos = grafischer_prototyp.GrafikObjekte.GrafikPosition()
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

    global_kran.test_func(winkel, winkel_vorher, pos, Objekt, hindernis_liste)

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

def visualisiere_greife():
    global_kran.greife()

def visualisiere_richte_aus():
    global_kran.richte_aus()

def visualisiere_lasse_los():
    global_kran.lasse_los()

def einstellen_Bildwerte():
    scene.background = color.white
    scene.width = 640
    scene.height = 480
    scene.resizable = True
