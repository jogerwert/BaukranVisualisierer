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
        laufkatze_position = vector(eingabe_position_wert_x+1, eingabe_hoehe_kran-0.5, eingabe_position_wert_y)
        greifarm_position = vector(eingabe_position_wert_x+1, eingabe_hoehe_kran-1, eingabe_position_wert_y)
        box(pos=turm_position)
        self.turm = cylinder(pos=turm_position, radius=0.5, length=eingabe_hoehe_kran, axis=vector(0, 1, 0))
        self.ausleger = cylinder(pos=ausleger_position, radius=0.5, length=eingabe_ausladung_kran, axis=vector(1, 0, 0))
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
        return numpy.degrees(numpy.arccos(wert_fuer_arccos))

    def berechne_geradengleichung_laufkatzeposition_objekt(self, x, eingabe_objekt):
        print(self.laufkatze.pos)
        if not eingabe_objekt.erhalte_position().x - self.laufkatze.pos.x == 0:
            steigung = (eingabe_objekt.erhalte_position().z - self.laufkatze.pos.z) / (eingabe_objekt.erhalte_position().x - self.laufkatze.pos.x)
        else:
            steigung = 0
        h = self.laufkatze.pos.z - steigung * self.laufkatze.pos.x
        y = steigung * x + h
        return y

    def berechne_punkt_links_oder_rechts_gerade(self, eingabe_objekt, akuell_winkel):
        temp_objekt = GrafikPosition()
        temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                     self.laufkatze.pos.z,
                                     self.laufkatze.pos.y)
        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(akuell_winkel - 1, None, temp_objekt)
        temp_punkt_2D_nach_rotation_minus = numpy.array(
            [temp_punkt_3D.erhalte_position().x, temp_punkt_3D.erhalte_position().z])
        temp_punkt_2D = numpy.array([eingabe_objekt.erhalte_position().x,eingabe_objekt.erhalte_position().z])
        abstand1 = numpy.linalg.norm(temp_punkt_2D - temp_punkt_2D_nach_rotation_minus)

        temp_objekt = GrafikPosition()
        temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                     self.laufkatze.pos.z,
                                     self.laufkatze.pos.y)
        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(akuell_winkel + 1, None, temp_objekt)
        temp_punkt_2D_nach_rotation_plus = numpy.array(
            [temp_punkt_3D.erhalte_position().x, temp_punkt_3D.erhalte_position().z])
        temp_punkt_2D = numpy.array([eingabe_objekt.erhalte_position().x, eingabe_objekt.erhalte_position().z])
        abstand2 = numpy.linalg.norm(temp_punkt_2D - temp_punkt_2D_nach_rotation_plus)

        if abstand1 < abstand2:
            return -1
        else:
            return 1

    def berechne_punkt_kreisgleichung_abhaengig_winkel(self, winkel, e_radius, objekt):
        if objekt is not None:
            if e_radius is None:
                radius = sqrt( pow(objekt.erhalte_position().x - self.turm.pos.x, 2) + pow(objekt.erhalte_position().z - self.turm.pos.z, 2) )
            else:
                radius = sqrt(pow(objekt.erhalte_position().x - self.turm.pos.x, 2) + pow(
                    objekt.erhalte_position().z - self.turm.pos.z, 2)) + e_radius
            x = radius * cos(radians(winkel)) + self.turm.pos.x
            y = radius * sin(radians(winkel)) + self.turm.pos.z
            z = objekt.erhalte_position().y
            punkt = GrafikPosition()
            punkt.erzeuge_position(x, y, z)
            return punkt

    def berechne_bewegunszeit_laufkatze_ausleger(self, winkel, abstand):
        laufkatzenzeit = abstand
        auslegerzeit = winkel/10

        if laufkatzenzeit < auslegerzeit:
            faktor = laufkatzenzeit / auslegerzeit
            laufkatzenbewegung_pro_sekunde = 1 * faktor
            auslegerbewegung_pro_sekund = winkel / auslegerzeit
        else:
            faktor = auslegerzeit / laufkatzenzeit
            laufkatzenbewegung_pro_sekunde = 1 #/ laufkatzenzeit
            auslegerbewegung_pro_sekund = 10 * faktor
        return laufkatzenbewegung_pro_sekunde, auslegerbewegung_pro_sekund

    def test_func(self, winkel, aktueller_winkel_ausleger_anfang, objekt_pos, objekt_bauteil):
        #winkel = round(winkel,1)
        #temp_objekt = GrafikPosition()
        #temp_objekt.erzeuge_position(self.ausleger.pos.x+self.ausleger.axis.x, self.ausleger.pos.z+self.ausleger.axis.z, self.ausleger.pos.y+self.ausleger.axis.y-0.5)
        #temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(winkel, None, temp_objekt)
        #temp_punkt_2D = numpy.array([temp_punkt_3D.erhalte_position().x, temp_punkt_3D.erhalte_position().z])
        #print(temp_punkt_3D.erhalte_position())

        #temp_objekt = GrafikPosition()
        #temp_objekt.erzeuge_position(objekt.erhalte_position().x,
        #                             objekt.erhalte_position().z,
        #                             objekt.erhalte_position().y - 0.5)
        #temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(winkel, None, temp_objekt)
        #temp_punkt_2D = numpy.array([temp_punkt_3D.erhalte_position().x, temp_punkt_3D.erhalte_position().z])
        temp_punkt_2D = numpy.array([objekt_pos.erhalte_position().x, objekt_pos.erhalte_position().z])

        temp_objekt = GrafikPosition()
        temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                     self.laufkatze.pos.z,
                                     self.laufkatze.pos.y)
        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(winkel, None, temp_objekt)
        temp_punkt_2D_nach_rotation = numpy.array([temp_punkt_3D.erhalte_position().x, temp_punkt_3D.erhalte_position().z])
        #print(temp_punkt_3D.erhalte_position())

        x_abstand_zwischen_zwei_puntken = numpy.linalg.norm(temp_punkt_2D - temp_punkt_2D_nach_rotation)
        x_erhoehung, i_winkel = self.berechne_bewegunszeit_laufkatze_ausleger(winkel, x_abstand_zwischen_zwei_puntken)
        print("abstand zwei punkte und stuffs")
        print(x_abstand_zwischen_zwei_puntken)
        print(x_erhoehung)
        print(i_winkel)
        bereits_gedreht = 0
        x_zahler = 0
        t_winkel = 0
        #i_winkel = 7.5
        #i_winkel = round(i_winkel,2)
        #print(i_winkel)
        sleep(2)

        a = self.berechne_punkt_links_oder_rechts_gerade(objekt_pos ,aktueller_winkel_ausleger_anfang)

        while True:
            rate(1)
            #sleep(1)
            if bereits_gedreht < winkel:
                t_winkel += i_winkel
                if t_winkel > winkel:
                    t_winkel = t_winkel - i_winkel
                    t_winkel = (winkel - t_winkel) + t_winkel

                temp_objekt = GrafikPosition()
                temp_objekt.erzeuge_position(self.ausleger.pos.x + self.ausleger.axis.x,
                                             self.ausleger.pos.z + self.ausleger.axis.z,
                                             self.ausleger.pos.y + self.ausleger.axis.y - 0.5)
                temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel,  None, temp_objekt)
                self.ausleger.axis.x = temp_punkt_3D.erhalte_position().x-self.ausleger.pos.x
                self.ausleger.axis.z = temp_punkt_3D.erhalte_position().z-self.ausleger.pos.z

                temp_objekt = GrafikPosition()
                temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                             self.laufkatze.pos.z,
                                             self.laufkatze.pos.y)
                temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel,  None, temp_objekt)

                self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
                self.laufkatze.pos.y = temp_punkt_3D.erhalte_position().y
                self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
                self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
                self.greifarm.pos.y = temp_punkt_3D.erhalte_position().y -0.5
                self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
                if objekt_bauteil is not None:
                    objekt_bauteil.erhalte_position().x = temp_punkt_3D.erhalte_position().x
                    objekt_bauteil.erhalte_position().y = temp_punkt_3D.erhalte_position().y-0.5
                    objekt_bauteil.erhalte_position().z = temp_punkt_3D.erhalte_position().z

                bereits_gedreht += i_winkel #round(bereits_gedreht + i_winkel,1)

                if x_zahler < x_abstand_zwischen_zwei_puntken:
                    x_zahler += x_erhoehung
                    b = 1
                    if x_zahler > x_abstand_zwischen_zwei_puntken:
                        b = x_abstand_zwischen_zwei_puntken - (x_zahler - x_erhoehung)
                    temp_objekt = GrafikPosition()
                    temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                                 self.laufkatze.pos.z,
                                                 self.laufkatze.pos.y)
                    temp_punkt_2D0 = numpy.array([objekt_pos.erhalte_position().x, objekt_pos.erhalte_position().z])
                    temp_punkt_2D1 = numpy.array([self.laufkatze.pos.x, self.laufkatze.pos.z])
                    temp_punkt_2D2 = numpy.array([self.turm.pos.x,self.turm.pos.z])
                    x_abstand_1 = numpy.linalg.norm(temp_punkt_2D0 - temp_punkt_2D2)
                    x_abstand_2 = numpy.linalg.norm(temp_punkt_2D1 - temp_punkt_2D2)
                    if x_abstand_2 < x_abstand_1:
                        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel, x_erhoehung*b, temp_objekt)
                    elif x_abstand_2 > x_abstand_1:
                        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel, -1*x_erhoehung*b,
                                                                                            temp_objekt)
                    print("abstände")
                    print(x_abstand_1)
                    print(x_abstand_2)
                    print("")
                    self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
                    self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
                    self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
                    self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
                    self.greifarm.pos.y = self.laufkatze.pos.y - 0.5
                    if objekt_bauteil is not None:
                        objekt_bauteil.erhalte_position().x = temp_punkt_3D.erhalte_position().x
                        objekt_bauteil.erhalte_position().y = temp_punkt_3D.erhalte_position().y - 0.5
                        objekt_bauteil.erhalte_position().z = temp_punkt_3D.erhalte_position().z

            else:
                break


        print("end")
        print(self.laufkatze.pos)
            #print(self.laufkatze.pos)
        return a*t_winkel + aktueller_winkel_ausleger_anfang