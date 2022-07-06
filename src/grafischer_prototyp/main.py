import numpy
from vpython import *
import threading

class GrafischesBaufeld:
    def erzeuge_baufeld(self, eingabe_laenge_baufeld, eingabe_breite_baufeld):
        laenge_baufeldteil = breite_baufeldteil = 1
        hoehe_baufeldteil = 0.1
        for x in range(0, eingabe_laenge_baufeld):
            for y in range(0, eingabe_breite_baufeld):
                if not x % 2 == 0:
                    if y % 2 == 0:
                        color_baufeld = vector(0.9, 0.9, 0.9)
                    else:
                        color_baufeld = vector(0.8, 0.8, 0.8)
                else:
                    if y % 2 == 1:
                        color_baufeld = vector(0.9, 0.9, 0.9)
                    else:
                        color_baufeld = vector(0.8, 0.8, 0.8)

                box(pos=vector(x, 0, y), length=laenge_baufeldteil, width=breite_baufeldteil, height=hoehe_baufeldteil,
                    color=color_baufeld)


class GrafischesBauteil:
    def erzeuge_bauteil(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        bauteil_position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)
        self.bauteil = box(pos=bauteil_position, color=vector(0, 0, 0), opacity=0.8)

    def erhoehe_bauteil(self, eingabe_erhoehen):
        while True:
            rate(20)
            if self.bauteil.pos.y < eingabe_erhoehen:
                self.bauteil.pos.y += 0.1
            else:
                break

    def senke_bauteil(self, eingabe_senken):
        while True:
            rate(20)
            if self.bauteil.pos.y > eingabe_senken:
                self.bauteil.pos.y -= 0.1
            else:
                break

    def verschiebe_bauteil(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        while True:
            rate(20)
            if self.bauteil.pos.x < eingabe_position_wert_x:
                self.bauteil.pos.x += 0.1
            if self.bauteil.pos.y < eingabe_position_wert_y:
                self.bauteil.pos.y += 0.1
            if self.bauteil.pos.z < eingabe_position_wert_z:
                self.bauteil.pos.z += 0.1
            if (self.bauteil.pos.x >= eingabe_position_wert_x and self.bauteil.pos.y >= eingabe_position_wert_y and
                self.bauteil.pos.z >= eingabe_position_wert_z):
                break

    def erhalte_position(self):
        return self.bauteil.pos

class GrafischesHindernis:
    def erzeuge_hindernis(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        bauteil_position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)
        box(pos=bauteil_position, color=vector(1, 0, 1), opacity=0.8)


class GrafischesPosition:
    def erzeuge_position(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        self.position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)

    def erhalte_position(self):
        return self.position

class GrafischesKran:
    def erzeuge_kran(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_hoehe_kran,
                     eingabe_ausladung_kran):
        laenge = breite = hoehe = 0.5
        turm_position = vector(eingabe_position_wert_x, 0, eingabe_position_wert_y)
        ausleger_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran, eingabe_position_wert_y)
        drehkranz_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran, eingabe_position_wert_y)
        laufkatze_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran-0.5, eingabe_position_wert_y+1)
        greifarm_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran-1, eingabe_position_wert_y+1)
        self.turm = cylinder(pos=turm_position, radius=0.5, length=eingabe_hoehe_kran, axis=vector(0, 1, 0))
        self.ausleger = cylinder(pos=ausleger_position, radius=0.5, length=eingabe_ausladung_kran, axis=vector(0, 0, 1))
        self.drehkranz = sphere(pos=drehkranz_position, radius=0.5)
        self.laufkatze = box(pos=laufkatze_position, length=laenge, height=hoehe, width=breite, color=vector(0, 1, 0))
        self.greifarm = pyramid(pos=greifarm_position, size=vector(0.5, 0.5, 0.5), axis=vector(0, 1, 0))
        return self.ausleger

    def drehe_ausleger(self, eingabe_drehwinkel):
        bereits_gedreht = 0
        while True:
            rate(20)
            if bereits_gedreht < eingabe_drehwinkel:
                bereits_gedreht += 1
                self.ausleger.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.laufkatze.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.greifarm.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
            else:
                break

    def drehe_ausleger_Bauteil(self, eingabe_drehwinkel, bauteil):
        bereits_gedreht = 0
        while True:
            rate(20)
            if bereits_gedreht < eingabe_drehwinkel:
                bereits_gedreht += 1
                self.ausleger.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.laufkatze.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.greifarm.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                bauteil.x = self.greifarm.pos.x
                bauteil.y = self.greifarm.pos.y
                bauteil.z = self.greifarm.pos.z
            else:
                break

    def debug_drehe_ausleger(self, eingabe_drehwinkel):
            self.ausleger.rotate(angle=radians(eingabe_drehwinkel), axis=vector(0, 1, 0), origin=self.ausleger.pos)
            self.laufkatze.rotate(angle=radians(eingabe_drehwinkel), axis=vector(0, 1, 0), origin=self.ausleger.pos)


    def berechne_drehwinkel_zum_objekt(self, eingabe_objekt):
        werte_turm_als_array = numpy.array([self.turm.pos.x, self.turm.pos.z, self.turm.pos.y])
        werte_ausleger_als_array = numpy.array([self.ausleger.axis.x, self.ausleger.axis.z, self.ausleger.axis.y])
        werte_objekt_als_array = numpy.array([eingabe_objekt.erhalte_position().x,
                                              eingabe_objekt.erhalte_position().z,
                                              eingabe_objekt.erhalte_position().y])
        abstand_ausleger_zu_objekt = numpy.linalg.norm(werte_ausleger_als_array - werte_objekt_als_array)
        abstand_ausleger_zu_turm = numpy.linalg.norm(werte_ausleger_als_array - werte_turm_als_array)
        abstand_turm_zu_objekt = numpy.linalg.norm(werte_turm_als_array - werte_objekt_als_array)
        wert_fuer_arccos = (pow(abstand_ausleger_zu_objekt, 2) - pow(abstand_ausleger_zu_turm, 2) -\
                           pow(abstand_turm_zu_objekt, 2)) / (-2 * abstand_ausleger_zu_turm * abstand_turm_zu_objekt)
        res = numpy.arccos(wert_fuer_arccos)
        return numpy.degrees(numpy.arccos(wert_fuer_arccos))


    def debug_berechne_drehwinkel_zum_objekt(self, eingabe_objekt):
        werte_turm_als_array = numpy.array([self.turm.pos.x, self.turm.pos.z, self.turm.pos.y])
        werte_ausleger_als_array = numpy.array([self.ausleger.axis.x + self.turm.pos.x, self.ausleger.axis.z + self.turm.pos.z, self.ausleger.axis.y  + self.turm.pos.y])
        werte_objekt_als_array = numpy.array([eingabe_objekt.erhalte_bauteil_positionen().x,
                                              eingabe_objekt.erhalte_bauteil_positionen().z,
                                              eingabe_objekt.erhalte_bauteil_positionen().y])
        abstand_ausleger_zu_objekt = numpy.linalg.norm(werte_ausleger_als_array - werte_objekt_als_array)
        abstand_ausleger_zu_turm = numpy.linalg.norm(werte_ausleger_als_array - werte_turm_als_array)
        abstand_turm_zu_objekt = numpy.linalg.norm(werte_turm_als_array - werte_objekt_als_array)
        wert_fuer_arccos = (pow(abstand_ausleger_zu_objekt, 2) - pow(abstand_ausleger_zu_turm, 2) - \
                            pow(abstand_turm_zu_objekt, 2)) / (-2 * abstand_ausleger_zu_turm * abstand_turm_zu_objekt)
        res = numpy.arccos(wert_fuer_arccos)
        return numpy.degrees(numpy.arccos(wert_fuer_arccos))

    def bewege_laufkatze(self, eingabe_position_wert_x, eingabe_position_wert_y):
        x_zahler = y_zahler = 0
        werte_laufkatze_als_array = numpy.array([self.laufkatze.pos.x, self.laufkatze.pos.z])
        werte_objekt_als_array = numpy.array([eingabe_position_wert_x, eingabe_position_wert_y])
        abstand = numpy.linalg.norm(werte_laufkatze_als_array - werte_objekt_als_array)
        while True:
            rate(20)
            if x_zahler < abstand:
                self.laufkatze.pos.x += 0.1
                x_zahler += 0.1
            if y_zahler < abstand:
                self.laufkatze.pos.z += 0.1
                y_zahler += 0.1
            if x_zahler >= abstand and y_zahler >=abstand:
                break


    def debug_bewege_laufkatze(self, eingabe_position_wert_x, eingabe_position_wert_y):
        x_zahler = y_zahler = 0
        x_abstand_erreicht = y_abstand_erreicht = False
        x_abstand_zwischen_zwei_puntken = eingabe_position_wert_x - self.laufkatze.pos.x
        y_abstand_zwischen_zwei_puntken = eingabe_position_wert_y - self.laufkatze.pos.z
        while True:
            rate(20)
            if x_abstand_zwischen_zwei_puntken > 0 and x_abstand_erreicht == False:
                self.laufkatze.pos.x += 0.1
                self.greifarm.pos.x += 0.1
                x_zahler += 0.1
                if x_zahler >= x_abstand_zwischen_zwei_puntken:
                    x_abstand_erreicht = True
            elif x_abstand_erreicht == False:
                self.laufkatze.pos.x -= 0.1
                self.greifarm.pos.x -= 0.1
                x_zahler -= 0.1
                if x_zahler < x_abstand_zwischen_zwei_puntken:
                    x_abstand_erreicht = True
            if y_abstand_zwischen_zwei_puntken > 0 and y_abstand_erreicht == False:
                self.laufkatze.pos.z += 0.1
                self.greifarm.pos.z += 0.1
                y_zahler += 0.1
                if y_zahler >= y_abstand_zwischen_zwei_puntken:
                    y_abstand_erreicht = True
            elif y_abstand_erreicht == False:
                self.laufkatze.pos.z -= 0.1
                self.greifarm.pos.z -= 0.1
                y_zahler -= 0.1
                if y_zahler < y_abstand_zwischen_zwei_puntken:
                    y_abstand_erreicht = True
            if x_abstand_erreicht == True and y_abstand_erreicht == True:
                break

    def debug_bewege_laufkatze_bauteil(self, eingabe_position_wert_x, eingabe_position_wert_y, bauteil):
        x_zahler = y_zahler = 0
        x_abstand_erreicht = y_abstand_erreicht = False
        x_abstand_zwischen_zwei_puntken = eingabe_position_wert_x - self.laufkatze.pos.x
        y_abstand_zwischen_zwei_puntken = eingabe_position_wert_y - self.laufkatze.pos.z
        while True:
            rate(20)
            if x_abstand_zwischen_zwei_puntken > 0 and x_abstand_erreicht == False:
                self.laufkatze.pos.x += 0.1
                self.greifarm.pos.x += 0.1
                bauteil.x = self.greifarm.pos.x
                x_zahler += 0.1
                if x_zahler >= x_abstand_zwischen_zwei_puntken:
                    x_abstand_erreicht = True
            elif x_abstand_erreicht == False:
                self.laufkatze.pos.x -= 0.1
                self.greifarm.pos.x -= 0.1
                bauteil.x = self.greifarm.pos.x
                x_zahler -= 0.1
                if x_zahler < x_abstand_zwischen_zwei_puntken:
                    x_abstand_erreicht = True
            if y_abstand_zwischen_zwei_puntken > 0 and y_abstand_erreicht == False:
                self.laufkatze.pos.z += 0.1
                self.greifarm.pos.z += 0.1
                bauteil.z = self.greifarm.pos.z
                y_zahler += 0.1
                if y_zahler >= y_abstand_zwischen_zwei_puntken:
                    y_abstand_erreicht = True
            elif y_abstand_erreicht == False:
                self.laufkatze.pos.z -= 0.1
                self.greifarm.pos.z -= 0.1
                bauteil.z = self.greifarm.pos.z
                y_zahler -= 0.1
                if y_zahler < y_abstand_zwischen_zwei_puntken:
                    y_abstand_erreicht = True
            if x_abstand_erreicht == True and y_abstand_erreicht == True:
                break

    def senke_greifarm(self, eingabe_senke):
        while True:
            rate(20)
            if self.greifarm.pos.y > eingabe_senke:
                self.greifarm.pos.y -= 0.1
            else:
                break

    def erhoehe_greifarm(self, eingabe_erhoehe):
        while True:
            rate(20)
            if self.greifarm.pos.y < eingabe_erhoehe:
                self.greifarm.pos.y += 0.1
            else:
                break

    def erhalte_posistion_laufkatze(self):
        return self.laufkatze.pos

def test_baufeld():
    baufeld = GrafischesBaufeld()
    baufeld.erzeuge_baufeld(10, 10)


def test_bauteil():
    bauteil1 = GrafischesBauteil()
    bauteil2 = GrafischesBauteil()
    bauteil1.erzeuge_bauteil(3, 3, 0)
    bauteil2.erzeuge_bauteil(3, 4, 0)
    bauteil2.erhoehe_bauteil(5)
    bauteil1.verschiebe_bauteil(5, 5, 5)


def test_hindernis():
    hindernis1 = GrafischesHindernis()
    hindernis2 = GrafischesHindernis()
    hindernis3 = GrafischesHindernis()
    hindernis1.erzeuge_hindernis(1, 1, 0)
    hindernis2.erzeuge_hindernis(1, 2, 0)
    hindernis3.erzeuge_hindernis(1, 3, 0)


def test_kran():
    kran = GrafischesKran()
    kran.erzeuge_kran(0, 0, 5, 7)
    bauteil3 = GrafischesBauteil()
    bauteil3.erzeuge_bauteil(4, 4, 0)
    winkel = kran.debug_berechne_drehwinkel_zum_objekt(bauteil3)
    kran.drehe_ausleger(winkel)
    kran.debug_bewege_laufkatze(bauteil3.erhalte_bauteil_positionen().x, bauteil3.erhalte_bauteil_positionen().z)
    kran.senke_greifarm(1)

    x = threading.Thread(target=kran.erhoehe_greifarm, args=(4,))
    y = threading.Thread(target=bauteil3.erhoehe_bauteil, args=(4,))
    x.start()
    y.start()
    #kran.erhoehe_greifarm(4)
    #bauteil3.erhoehe_bauteil(4)

def ausfuehrung_beispiel():
    beispiel_baufeld = GrafischesBaufeld()
    beispiel_baufeld.erzeuge_baufeld(10, 5)

    beispiel_hindernis = []
    beispiel_hindernis.append(GrafischesHindernis())
    beispiel_hindernis.append(GrafischesHindernis())
    beispiel_hindernis[0].erzeuge_hindernis(3, 2, 0)
    beispiel_hindernis[1].erzeuge_hindernis(3, 2, 1)

    beispiel_bauteile = []
    beispiel_bauteile.append(GrafischesBauteil())
    beispiel_bauteile.append(GrafischesBauteil())
    beispiel_bauteile.append(GrafischesBauteil())
    beispiel_bauteile[0].erzeuge_bauteil(0, 2, 0)
    beispiel_bauteile[1].erzeuge_bauteil(1, 2, 0)
    beispiel_bauteile[2].erzeuge_bauteil(2, 2, 0)

    beispiel_kran = GrafischesKran()
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
    placeholder_position = GrafischesPosition()
    placeholder_position.erzeuge_position(6, 2, 2)
    winkel = beispiel_kran.berechne_drehwinkel_zum_objekt(placeholder_position)
    beispiel_kran.drehe_ausleger_Bauteil(winkel, beispiel_bauteile[1].erhalte_position())
    beispiel_kran.debug_bewege_laufkatze_bauteil(placeholder_position.erhalte_position().x, placeholder_position.erhalte_position().z,
                                                 beispiel_bauteile[1].erhalte_position())


scene.background = color.white
sleep(3)
ausfuehrung_beispiel()
#test_baufeld()
#test_bauteil()
#test_hindernis()
#test_kran()

