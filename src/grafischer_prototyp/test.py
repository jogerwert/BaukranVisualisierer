import numpy
from vpython import *
from math import *
from GrafikObjekte import *

class GrafikKran:
    def erzeuge_kran(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_hoehe_kran,
                     eingabe_ausladung_kran):
        laenge = breite = hoehe = 0.5
        turm_position = vector(eingabe_position_wert_x, 0, eingabe_position_wert_y)
        ausleger_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran, eingabe_position_wert_y)
        drehkranz_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran, eingabe_position_wert_y)
        laufkatze_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran-0.5, eingabe_position_wert_y+1)
        greifarm_position = vector(eingabe_position_wert_x, eingabe_hoehe_kran-1, eingabe_position_wert_y+1)
        box(pos=turm_position)
        self.turm = cylinder(pos=turm_position, radius=0.5, length=eingabe_hoehe_kran, axis=vector(0, 1, 0))
        self.ausleger = cylinder(pos=ausleger_position, radius=0.5, length=eingabe_ausladung_kran, axis=vector(0, 0, 1))
        self.drehkranz = sphere(pos=drehkranz_position, radius=0.5)
        self.laufkatze = box(pos=laufkatze_position, length=laenge, height=hoehe, width=breite, color=vector(0, 1, 0))
        self.greifarm = pyramid(pos=greifarm_position, size=vector(0.5, 0.5, 0.5), axis=vector(0, 1, 0))
        return self.ausleger

    def drehe_ausleger_Bauteil(self, eingabe_drehwinkel, bauteil):
        bereits_gedreht = 0
        while True:
            rate(20)
            if bereits_gedreht < eingabe_drehwinkel:
                bereits_gedreht += 1
                self.ausleger.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.laufkatze.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.greifarm.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                if bauteil is not None:
                    bauteil.erhalte_position().x = self.greifarm.pos.x
                    bauteil.erhalte_position().y = self.greifarm.pos.y
                    bauteil.erhalte_position().z = self.greifarm.pos.z
            else:
                break
        print(self.ausleger.axis)

    def berechne_drehwinkel_objekt(self, eingabe_objekt):
        werte_turm_als_array = numpy.array([self.turm.pos.x, self.turm.pos.z])
        werte_ausleger_als_array = numpy.array([self.ausleger.axis.x + self.turm.pos.x, self.ausleger.axis.z + self.turm.pos.z])
        werte_objekt_als_array = numpy.array([eingabe_objekt.erhalte_position().x,
                                              eingabe_objekt.erhalte_position().z])
        abstand_ausleger_zu_objekt = numpy.linalg.norm(werte_ausleger_als_array - werte_objekt_als_array)
        abstand_ausleger_zu_turm = numpy.linalg.norm(werte_ausleger_als_array - werte_turm_als_array)
        abstand_turm_zu_objekt = numpy.linalg.norm(werte_turm_als_array - werte_objekt_als_array)
        wert_fuer_arccos = (pow(abstand_ausleger_zu_objekt, 2) - pow(abstand_ausleger_zu_turm, 2) - \
                            pow(abstand_turm_zu_objekt, 2)) / (-2 * abstand_ausleger_zu_turm * abstand_turm_zu_objekt)
        #print(numpy.degrees(numpy.arccos(wert_fuer_arccos)))
        return numpy.degrees(numpy.arccos(wert_fuer_arccos))

    def berechne_geradengleichung_laufkatzeposition_objekt(self, x, eingabe_objekt):
        if not eingabe_objekt.erhalte_position().x - self.laufkatze.pos.x == 0:
            steigung = (eingabe_objekt.erhalte_position().z - self.laufkatze.pos.z) / (eingabe_objekt.erhalte_position().x - self.laufkatze.pos.x)
        else:
            steigung = 0
        h = self.turm.pos.y - steigung * self.turm.pos.x
        y = steigung * x #+ h
        #print("steigung")
        #print(steigung)
        return y

    def berechne_punkt_kreisgleichung(self, winkel):
        radius = sqrt( pow(self.laufkatze.pos.x - self.turm.pos.x, 2) + pow(self.laufkatze.pos.z - self.turm.pos.z, 2) )
        x = self.turm.pos.x + radius * cos(radians(winkel))
        y = self.turm.pos.z + radius * sin(radians(winkel))
        z = self.laufkatze.pos.y
        punkt = GrafikPosition()
        punkt.erzeuge_position(x, y, z)
        return punkt

    def bewege_laufkatze_bauteil(self, eingabe_position_wert_x, bauteil):
        x_zahler = 0
        x_abstand_zwischen_zwei_puntken = eingabe_position_wert_x - self.laufkatze.pos.x
        x_erhoehung = x_abstand_zwischen_zwei_puntken / 10
        while True:
            rate(1)
            if x_abstand_zwischen_zwei_puntken > 0:
                x = self.laufkatze.pos.x + x_erhoehung
                y = self.berechne_geradengleichung_laufkatzeposition_objekt(x, bauteil)
                self.laufkatze.pos.x = x
                self.greifarm.pos.x = x
                # bauteil.erhalte_position().x = x
                self.laufkatze.pos.z = y
                self.greifarm.pos.z = y
                # bauteil.erhalte_position().z = y
                x_zahler += x_erhoehung
                if x_zahler >= x_abstand_zwischen_zwei_puntken:
                    break
            else:
                x = self.laufkatze.pos.x + x_erhoehung
                y = self.berechne_geradengleichung_laufkatzeposition_objekt(x, bauteil)
                self.laufkatze.pos.x = x
                self.greifarm.pos.x = x
                bauteil.x = x
                self.laufkatze.pos.z = y
                self.greifarm.pos.z = y
                bauteil.z = y
                x_zahler += x_erhoehung
                if x_zahler <= x_abstand_zwischen_zwei_puntken:
                    break

    def berechne_bewegunszeit_laufkatze_ausleger(self, winkel, abstand):
        laufkatzenzeit = abstand
        auslegerzeit = winkel

        if laufkatzenzeit < auslegerzeit:
            faktor = laufkatzenzeit / auslegerzeit
            #laufkatzenbewegung_pro_sekunde = 1 * faktor
            #auslegerbewegung_pro_sekund = 10
            laufkatzenbewegung_pro_sekunde = 1 * faktor
            auslegerbewegung_pro_sekund = 1
        else:
            faktor = auslegerzeit / laufkatzenzeit
            laufkatzenbewegung_pro_sekunde = 1
            auslegerbewegung_pro_sekund = 1 * faktor
            #faktor =  auslegerzeit / laufkatzenzeit
            #laufkatzenbewegung_pro_sekunde = 1
            #auslegerbewegung_pro_sekund = 10 * faktor
        return laufkatzenbewegung_pro_sekunde, auslegerbewegung_pro_sekund

#neu punkt to end punkt = abstand - erhöhung abhängig vom winkel -> zeit
    def test_bewege_laufkatze_ausleger_bauteil(self, eingabe_position_wert_x, eingabe_drehwinkel, bauteil):
        x_zahler = 0
        bereits_gedreht = 0
        temp_punkt_3D = self.berechne_punkt_kreisgleichung(eingabe_drehwinkel)
        print(temp_punkt_3D.erhalte_position())
        temp_punkt_2D = numpy.array([temp_punkt_3D.erhalte_position().x, temp_punkt_3D.erhalte_position().z])
        #print(temp_punkt_3D.erhalte_position())
        #print(temp_punkt_2D)
        temp_punkt_2D_zielort = numpy.array([bauteil.erhalte_position().x, bauteil.erhalte_position().z])

        x_abstand_zwischen_zwei_puntken = numpy.linalg.norm(temp_punkt_2D - temp_punkt_2D_zielort)
        #x_abstand_zwischen_zwei_puntken = eingabe_position_wert_x - self.laufkatze.pos.x
        #print("abstand")
        #print(x_abstand_zwischen_zwei_puntken)
        x_erhoehung, i_winkel = self.berechne_bewegunszeit_laufkatze_ausleger(eingabe_drehwinkel, x_abstand_zwischen_zwei_puntken)
        #print("strecken und winkel pro takt")
        #print(x_erhoehung)
        #print(i_winkel)
        #x_erhoehung = x_abstand_zwischen_zwei_puntken / eingabe_drehwinkel
        #x = self.laufkatze.pos.x + x_erhoehung
        while True:
            rate(1)
            if x_abstand_zwischen_zwei_puntken > 0:
                x = self.laufkatze.pos.x + x_erhoehung
                #print(x) #fehler
                print("laufkatze")
                print(self.laufkatze.pos.x)
                print("axis")
                print(self.ausleger.axis.x)
                print("")
                temp_punkt_2D_1 = GrafikPosition()
                temp_punkt_2D_1.erzeuge_position(self.ausleger.axis.x, self.ausleger.axis.z ,
                     self.ausleger.axis.y + self.ausleger.pos.y - 0.5)
                #print("temp punkt")
                #print(temp_punkt_2D_1.erhalte_position())
                #print(temp_punkt_2D_1.erhalte_position())
                y = self.berechne_geradengleichung_laufkatzeposition_objekt(x, temp_punkt_2D_1)
                #print(x)
                #print(y)
                self.laufkatze.pos.x = x
                self.greifarm.pos.x = x
                # bauteil.erhalte_position().x = x
                self.laufkatze.pos.z = y
                self.greifarm.pos.z = y
                # bauteil.erhalte_position().z = y
                #print("laufkatze")
                #print(self.laufkatze.pos)
                x_zahler += x_erhoehung
                if bereits_gedreht < eingabe_drehwinkel:
                    bereits_gedreht += i_winkel
                    self.ausleger.rotate(angle=radians(i_winkel), axis=vector(0, 1, 0), origin=self.turm.pos)
                    self.laufkatze.rotate(angle=radians(i_winkel), axis=vector(0, 1, 0), origin=self.turm.pos)
                    self.greifarm.rotate(angle=radians(i_winkel), axis=vector(0, 1, 0), origin=self.turm.pos)
                    if bauteil is None:
                        bauteil.erhalte_position().x = self.greifarm.pos.x
                        bauteil.erhalte_position().y = self.greifarm.pos.y
                        bauteil.erhalte_position().z = self.greifarm.pos.z
                sleep(1)
                if x_zahler > x_abstand_zwischen_zwei_puntken:
                    break
            else:
                x = self.laufkatze.pos.x + x_erhoehung
                y = self.berechne_geradengleichung_laufkatzeposition_objekt(x, bauteil)
                self.laufkatze.pos.x = x
                self.greifarm.pos.x = x
                bauteil.x = x
                self.laufkatze.pos.z = y
                self.greifarm.pos.z = y
                bauteil.z = y
                x_zahler += x_erhoehung
                if bereits_gedreht < eingabe_drehwinkel:
                    bereits_gedreht += 1
                    self.ausleger.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                    self.laufkatze.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                    self.greifarm.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                    if bauteil is None:
                        bauteil.erhalte_position().x = self.greifarm.pos.x
                        bauteil.erhalte_position().y = self.greifarm.pos.y
                        bauteil.erhalte_position().z = self.greifarm.pos.z
                if x_zahler <= x_abstand_zwischen_zwei_puntken:
                    break
        #print(self.laufkatze.pos)
        #print(bereits_gedreht)


    def test_berechne_punkt_kreisgleichung(self, winkel):
        radius = sqrt( pow(self.ausleger.axis.x, 2) + pow(self.ausleger.axis.z, 2) )
        x = self.turm.pos.x + radius * cos(radians(winkel))
        y = self.turm.pos.z + radius * sin(radians(winkel))
        z = self.ausleger.pos.y
        punkt = GrafikPosition()
        punkt.erzeuge_position(x, y, z)
        self.ausleger.axis.x = x
        #self.ausleger.axis.y = z
        self.ausleger.axis.z = y
        print(radius)
        print(x)
        print(y)
        return punkt

    def test_bewege_laufkatze_ausleger_bauteil2(self, eingabe_position_wert_x, eingabe_drehwinkel, bauteil):
        bereits_gedreht = 0
        x_zahler = 0
        x_abstand_zwischen_zwei_puntken = eingabe_position_wert_x - self.laufkatze.pos.x
        x_erhoehung = x_abstand_zwischen_zwei_puntken / 10
        while True:
            rate(10)
            if bereits_gedreht < eingabe_drehwinkel:
                bereits_gedreht += 1
                self.ausleger.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.laufkatze.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                self.greifarm.rotate(angle=radians(1), axis=vector(0, 1, 0), origin=self.ausleger.pos)
                if bauteil is None:
                    bauteil.erhalte_position().x = self.greifarm.pos.x
                    bauteil.erhalte_position().y = self.greifarm.pos.y
                    bauteil.erhalte_position().z = self.greifarm.pos.z
            else:
                break

            if x_abstand_zwischen_zwei_puntken > 0:
                x = self.laufkatze.pos.x + x_erhoehung
                y = self.berechne_geradengleichung_laufkatzeposition_objekt(x, bauteil)
                self.laufkatze.pos.x = x
                self.greifarm.pos.x = x
                # bauteil.erhalte_position().x = x
                self.laufkatze.pos.z = y
                self.greifarm.pos.z = y
                # bauteil.erhalte_position().z = y
                x_zahler += x_erhoehung
                if x_zahler >= x_abstand_zwischen_zwei_puntken:
                    break
            else:
                x = self.laufkatze.pos.x + x_erhoehung
                y = self.berechne_geradengleichung_laufkatzeposition_objekt(x, bauteil)
                self.laufkatze.pos.x = x
                self.greifarm.pos.x = x
                bauteil.x = x
                self.laufkatze.pos.z = y
                self.greifarm.pos.z = y
                bauteil.z = y
                x_zahler += x_erhoehung
                if x_zahler <= x_abstand_zwischen_zwei_puntken:
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

    ##---------------
    temp_objekt = GrafikPosition()
    temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                 self.laufkatze.pos.z,
                                 self.laufkatze.pos.y)
    temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(
        aktueller_winkel_ausleger_anfang + a * t_winkel, -x_erhoehung, temp_objekt)
    self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
    self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
    self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
    self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
    self.greifarm.pos.y = self.laufkatze.pos.y - 0.5
    temp_objekt = GrafikPosition()
    temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                 self.laufkatze.pos.z,
                                 self.laufkatze.pos.y)
    temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(
        aktueller_winkel_ausleger_anfang + a * t_winkel, x_erhoehung * 0.656854249492381, temp_objekt)
    self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
    self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
    self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
    self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
    self.greifarm.pos.y = self.laufkatze.pos.y - 0.5
    ##---------------