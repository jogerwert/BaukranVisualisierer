import grafischer_prototyp.GrafikBaufeld
import grafischer_prototyp.GrafikObjekte
import grafischer_prototyp.GrafikKran
import baukran_visualisierer.model.baustelle
from vpython import *
import ctypes  # An included library with Python install.
import sys
global __server
import socket
import struct
import os
#from pythonping import ping
#from selenium import webdriver
import webbrowser
import threading
from baukran_visualisierer.datei_management import file_picker
from baukran_visualisierer.service import parser_service #,visualisierungs_service

def is_loopback(host):
    loopback_checker = {
        socket.AF_INET: lambda x: struct.unpack('!I', socket.inet_aton(x))[0] >> (32-8) == 127,
        socket.AF_INET6: lambda x: x == '::1'
    }
    for family in (socket.AF_INET, socket.AF_INET6):
        try:
            r = socket.getaddrinfo(host, None, family, socket.SOCK_STREAM)
        except socket.gaierror:
            return False
        for family, _, _, _, sockaddr in r:
            if not loopback_checker[family](sockaddr[0]):
                return False
    return True

class virt_Baustelle:
    def __init__(self, baustelle):
        self.baustelle = baustelle

    def speichere_Baustelle(self, baustelle):
        self.baustelle = baustelle

    def erhalte_Baustelle(self):
        return self.baustelle

global_baustelle = virt_Baustelle(None)
global_kran = \
    grafischer_prototyp.GrafikKran.GrafikKran()
bauteil_liste = []
button_liste = []
slider_liste = []
hindernis_liste = []
beispiel_baufeld = grafischer_prototyp.GrafikBaufeld.GrafikBaufeld()
loop = True

#def Mbox(title, text, style):
#    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def setze_visualisierungs_funktionen(baustelle):
    baustelle.kran.visualisiere_greife = visualisiere_greife
    baustelle.kran.visualisiere_bringe_an = visualisiere_bringe_an
    baustelle.kran.visualisiere_senke_um = visualisiere_senke_um
    baustelle.kran.visualisiere_hebe_um = visualisiere_hebe_um


def visualisiere_baustelle(baustelle):
    global_baustelle.speichere_Baustelle(baustelle)
    # Visualisiert Grundbaustelle
    anordnen_buttons()

    einstellen_Bildwerte()
    # global_baustelle.speichere_Baustelle(baustelle)

    beispiel_baufeld.erzeuge_baufeld(global_baustelle.erhalte_Baustelle().baufeld.laenge_x,
                                     global_baustelle.erhalte_Baustelle().baufeld.breite_y)
    # beispiel_kran = src.grafischer_prototyp.GrafikKran.GrafikKran()
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

    loop_test()

def loop_test():
    global loop
    if loop == True:
        loop=False
        while True:
            pass
        #hostname = "localhost"  # example
        #response = os.system("ping -n 1 " + hostname)

        # and then check the response...
        #if response == 0:
        #    print(hostname, 'is up!')
        #else:
        #    print(hostname, 'is down!')
        #for host in ('localhost', 'alias-of-localhost', 'google.com'):
        #    print(host, is_loopback(host))
        #print(version)
        #ping('localhost', verbose=True)
        #status = os.system('systemctl is-active --quiet service-name')
        #print(status)  # will return 0 for active else inactive.


def Mbox(title, text):
    MB_SYSTEMMODAL = 0x00001000
    return ctypes.windll.user32.MessageBoxW(0, text, title, MB_SYSTEMMODAL)

def anordnen_buttons():
    #from baukran_visualisierer import start_file_picker
    #from baukran_visualisierer import start_visualisierung

    def B(b):
        button_liste[0].disabled = True
        button_liste[1].disabled = True
        global_baustelle.erhalte_Baustelle().naechste_krananweisung_ausfuehren()
        button_liste[0].disabled = False
        button_liste[1].disabled = False
        print("naechste_krananweisung", b.text)

    def C(b):
        button_liste[1].disabled = True
        global_baustelle.erhalte_Baustelle().naechste_montageanweisung_ausfuehren()
        button_liste[1].disabled = False
        print("naechste_montageanweisung", b.text)

    def D(b):
        button_liste[2].disabled = True
        global_baustelle.erhalte_Baustelle().alle_montageanweisungen_ausfuehren()
        button_liste[2].disabled = False
        print("alle_montageanweisungen", b.text)

    def E(b):
        Mbox('Zeitberechnung', 'Für den Bauablauf sind ' + str(global_kran.time) + ' Sekunden vergangen')
        print(global_kran.time)
        print("Zeit", b.text)

    def F(b):
        #from baukran_visualisierer.datei_management import file_picker
        #from baukran_visualisierer.service import parser_service,visualisierungs_service
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

        #dateiname = file_picker.file_picker()
        #if dateiname == "":
        #    anordnen_buttons()
        #baustelle = parser_service.parse_baustelle(dateiname)
        #visualisiere_baustelle(baustelle)
        #print("delete", b.text)

        #src.baukran_visualisierer.start_file_picker()

        for element in button_liste:
            print(element)

    def S(s):
        print(s.value)
        global_kran.animationsgeschwindigkeit(s.value)

    def T(s):
        print(s.text, s.number)

    def M(m):
        print(m.selected, m.index)

    def G(m):
        for element in global_kran.get_collision():
            print(element)
        # button_liste[6].color = vector(1,1,1)

    button_liste.append(button(bind=B, text='Naechste Krananweisung'))
    button_liste.append(button(bind=C, text='Naechste Montageanweisung'))
    button_liste.append(button(bind=D, text='Alle Montageanweisungen'))
    button_liste.append(button(bind=E, text='Zeit'))
    scene.append_to_caption('\n\n')
    slider_liste.append(slider(bind=S))
    # winput(bind=T, text="mi")
    # menu(choices=['cat', 'dog', 'horse'], bind=M)
    scene.append_to_caption('\n\n')
    button_liste.append(button(bind=F, text='Neues Bauprojekt'))
    button_liste.append(button(bind=G, text='Kollision'))
    scene.append_to_caption('\n\n')

def visualisiere_greife(haken_z):
    print(global_baustelle.erhalte_Baustelle())
    hoehe = global_kran.greifarm.pos.y - haken_z
    print(haken_z)
    print(global_kran.greifarm.pos.y)
    global_kran.veraendere_greifarm_hoehe("senke", hoehe, None)

def visualisiere_bringe_an(winkel_vorher, winkel_nachher, haken_x, haken_y, haken_z, bauteil_name):
    #print("test")
    #print(winkel_vorher)
    #print(winkel_nachher)
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

    #global_kran.test_func(winkel, winkel_vorher, pos, Objekt)
    global_kran.test_func(winkel, winkel_vorher, pos, Objekt, hindernis_liste)
    for element in global_kran.get_collision():
        print(element)

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

def einstellen_Bildwerte():
    scene.background = color.white
    scene.width = 640
    scene.height = 480
    scene.resizable = True
