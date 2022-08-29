import numpy
from vpython import *
from math import *
#from GrafikObjekte import *
import src.grafischer_prototyp.GrafikObjekte

class GrafikKran:
    def erzeuge_kran(self, ev_x_wert, ev_y_wert, ev_hoehe_kran, ev_ausladung_kran):
        iv_laenge = iv_breite = iv_hoehe = 0.5
        iv_turm_position = vector(ev_x_wert, 0, ev_y_wert)
        iv_ausleger_position = vector(ev_x_wert, ev_hoehe_kran+1, ev_y_wert)
        iv_drehkranz_position = vector(ev_x_wert, ev_hoehe_kran+1, ev_y_wert)
        iv_laufkatze_position = vector(ev_x_wert+1, ev_hoehe_kran+0.5, ev_y_wert)
        iv_greifarm_position = vector(ev_x_wert+1, ev_hoehe_kran, ev_y_wert)
        iv_verbindunsseil_position = vector(ev_x_wert+1, ev_hoehe_kran+0.5, ev_y_wert)

        box(pos=iv_turm_position)
        self.turm = cylinder(pos=iv_turm_position, radius=0.5, length=ev_hoehe_kran+1, axis=vector(0, 1, 0))
        self.ausleger = cylinder(pos=iv_ausleger_position, radius=0.5, length=ev_ausladung_kran, axis=vector(1, 0, 0))
        self.drehkranz = sphere(pos=iv_drehkranz_position, radius=0.5)
        self.verbindunsseil = cylinder(pos=iv_verbindunsseil_position ,radius=0.01, axis=vector(0, 1, 0), length=0.01)
        self.laufkatze = box(pos=iv_laufkatze_position, length=iv_laenge, height=iv_hoehe, width=iv_breite, color=vector(0, 1, 0))
        self.greifarm = pyramid(pos=iv_greifarm_position, size=vector(0.5, 0.5, 0.5), axis=vector(0, 1, 0))

    def veraendere_greifarm_hoehe(self, ev_richtung, ev_erhoehe, ev_objekt):
        iv_temp = iv_richtung = 0
        while True:
            rate(1000)
            if iv_temp < ev_erhoehe:
                if ev_richtung == "senke":
                    iv_richtung = -0.1
                elif ev_richtung == "erhoehe":
                    iv_richtung = 0.1
                self.greifarm.pos.y = round(self.greifarm.pos.y + iv_richtung, 1)
                self.verbindunsseil.pos = self.greifarm.pos
                self.verbindunsseil.pos.y = self.verbindunsseil.pos.y + 0.5
                self.verbindunsseil.length = round(self.verbindunsseil.length - iv_richtung, 1)
                iv_temp += 0.1
                if ev_objekt is not None:
                    ev_objekt.erhalte_position().y = round(ev_objekt.erhalte_position().y + iv_richtung, 1)
            else:
                if ev_objekt is not None:
                    ev_objekt.erhalte_position().y = round(ev_objekt.erhalte_position().y, 0)
                self.greifarm.pos.y = round(self.greifarm.pos.y, 0)
                self.verbindunsseil.length = round(self.verbindunsseil.length, 0)
                break
        return "unlock"

    def erhalte_posistion_laufkatze(self):
        return self.laufkatze.pos

    def berechne_drehwinkel_objekt(self, ev_objekt):
        iv_turm_als_array = numpy.array([self.turm.pos.x, self.turm.pos.z])
        iv_ausleger_als_array = numpy.array([self.ausleger.axis.x + self.turm.pos.x, self.ausleger.axis.z +
                                             self.turm.pos.z])
        iv_objekt_als_array = numpy.array([ev_objekt.erhalte_position().x, ev_objekt.erhalte_position().z])
        iv_abstand_ausleger_zu_objekt = numpy.linalg.norm(iv_ausleger_als_array - iv_objekt_als_array)
        iv_abstand_ausleger_zu_turm = numpy.linalg.norm(iv_ausleger_als_array - iv_turm_als_array)
        iv_abstand_turm_zu_objekt = numpy.linalg.norm(iv_turm_als_array - iv_objekt_als_array)
        iv_wert_fuer_arccos = (pow(iv_abstand_ausleger_zu_objekt, 2) - pow(iv_abstand_ausleger_zu_turm, 2) -
                    pow(iv_abstand_turm_zu_objekt, 2)) / (-2 * iv_abstand_ausleger_zu_turm * iv_abstand_turm_zu_objekt)
        if iv_wert_fuer_arccos > 1:
            iv_wert_fuer_arccos = 1
        elif iv_wert_fuer_arccos < -1:
            iv_wert_fuer_arccos = -1
        return numpy.degrees(numpy.arccos(iv_wert_fuer_arccos))

    def berechne_punkt_links_oder_rechts_gerade(self, ev_objekt, ev_akueller_winkel_gerade):
        iv_objekt = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
        iv_objekt.erzeuge_position(self.laufkatze.pos.x, self.laufkatze.pos.z, self.laufkatze.pos.y)

        iv_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(ev_akueller_winkel_gerade - 1, None, iv_objekt)
        iv_punkt_2D_links_gerade = numpy.array(
            [iv_punkt_3D.erhalte_position().x, iv_punkt_3D.erhalte_position().z])
        iv_punkt_2D = numpy.array([ev_objekt.erhalte_position().x, ev_objekt.erhalte_position().z])
        iv_abstand1 = numpy.linalg.norm(iv_punkt_2D - iv_punkt_2D_links_gerade)

        iv_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(ev_akueller_winkel_gerade + 1, None, iv_objekt)
        iv_punkt_2D_rechts_gerade = numpy.array(
            [iv_punkt_3D.erhalte_position().x, iv_punkt_3D.erhalte_position().z])
        iv_punkt_2D = numpy.array([ev_objekt.erhalte_position().x, ev_objekt.erhalte_position().z])
        iv_abstand2 = numpy.linalg.norm(iv_punkt_2D - iv_punkt_2D_rechts_gerade)

        if iv_abstand1 < iv_abstand2:
            return -1
        else:
            return 1

    def berechne_punkt_kreisgleichung_abhaengig_winkel(self, ev_winkel, ev_zusaetzlicher_radius, ev_objekt):
        if ev_objekt is not None:
            if ev_zusaetzlicher_radius is None:
                iv_radius = sqrt(pow(ev_objekt.erhalte_position().x - self.turm.pos.x, 2) +
                                 pow(ev_objekt.erhalte_position().z - self.turm.pos.z, 2))
            else:
                iv_radius = sqrt(pow(ev_objekt.erhalte_position().x - self.turm.pos.x, 2) + pow(
                    ev_objekt.erhalte_position().z - self.turm.pos.z, 2)) + ev_zusaetzlicher_radius
            iv_x = iv_radius * cos(radians(ev_winkel)) + self.turm.pos.x
            iv_y = iv_radius * sin(radians(ev_winkel)) + self.turm.pos.z
            iv_z = ev_objekt.erhalte_position().y
            iv_punkt = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
            iv_punkt.erzeuge_position(iv_x, iv_y, iv_z)
            return iv_punkt

    def berechne_bewegunszeit_laufkatze_ausleger(self, ev_winkel, ev_abstand_laufkatze_punkt, position):
        iv_laufkatzenzeit = ev_abstand_laufkatze_punkt
        iv_auslegerzeit = ev_winkel / 10
        if self.greifarm.pos.y  < position.erhalte_position().y :
            iv_greifarmzeit = position.erhalte_position().y - self.greifarm.pos.y
        else:
            iv_greifarmzeit = self.greifarm.pos.y - position.erhalte_position().y
        #iv_greifarmzeit = ev_hoehe
        print(iv_greifarmzeit)
        if iv_laufkatzenzeit < iv_auslegerzeit and iv_greifarmzeit < iv_auslegerzeit:
            iv_laufkatzenbewegung_pro_sekunde = 1 * iv_laufkatzenzeit / iv_auslegerzeit
            iv_greifarmbewegung_pro_sekunde = 1 * iv_greifarmzeit / iv_auslegerzeit
            iv_auslegerbewegung_pro_sekund = 10
            print("if")
        elif iv_auslegerzeit < iv_laufkatzenzeit and iv_greifarmzeit < iv_laufkatzenzeit:
            iv_laufkatzenbewegung_pro_sekunde = 1
            iv_auslegerbewegung_pro_sekund = 10 * iv_auslegerzeit / iv_laufkatzenzeit
            iv_greifarmbewegung_pro_sekunde = 1 * iv_greifarmzeit / iv_laufkatzenzeit
            print("elif")
        else:
            iv_laufkatzenbewegung_pro_sekunde = 1 * iv_laufkatzenzeit / iv_greifarmzeit
            iv_auslegerbewegung_pro_sekund = 10 * iv_auslegerzeit / iv_greifarmzeit
            iv_greifarmbewegung_pro_sekunde = 1
            print("else")
        return iv_laufkatzenbewegung_pro_sekunde, iv_auslegerbewegung_pro_sekund, iv_greifarmbewegung_pro_sekunde

    def test_func(self, winkel, aktueller_winkel_ausleger_anfang, objekt_pos, objekt_bauteil):
        temp_punkt_2D = numpy.array([objekt_pos.erhalte_position().x, objekt_pos.erhalte_position().z])

        temp_objekt = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
        temp_objekt.erzeuge_position(self.laufkatze.pos.x, self.laufkatze.pos.z, self.laufkatze.pos.y)
        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(winkel, None, temp_objekt)
        temp_punkt_2D_nach_rotation = numpy.array([temp_punkt_3D.erhalte_position().x, temp_punkt_3D.erhalte_position().z])

        x_abstand_zwischen_zwei_puntken = numpy.linalg.norm(temp_punkt_2D - temp_punkt_2D_nach_rotation)
        x_erhoehung, i_winkel, x_erhoehung_hoehe = self.berechne_bewegunszeit_laufkatze_ausleger(winkel,
                                                                            x_abstand_zwischen_zwei_puntken,objekt_pos)
        bereits_gedreht = x_zahler = t_winkel = 0
        x_erhoehung = x_erhoehung/10
        i_winkel = i_winkel/10
        x_erhoehung_hoehe = x_erhoehung_hoehe/10
        bereits_erhoeht = 0
        a = self.berechne_punkt_links_oder_rechts_gerade(objekt_pos ,aktueller_winkel_ausleger_anfang)
        if self.greifarm.pos.y < objekt_pos.erhalte_position().y:
            hoehe = objekt_pos.erhalte_position().y - self.greifarm.pos.y
        else:
            hoehe = self.greifarm.pos.y - objekt_pos.erhalte_position().y
        print(x_erhoehung)
        print(i_winkel)
        print(x_erhoehung_hoehe)
        #print(hoehe)

        while True:
            rate(10)
            if winkel == 0:
                print(winkel == 0)
                while True:
                    if x_zahler < x_abstand_zwischen_zwei_puntken:
                        x_zahler += x_erhoehung
                        b = 1
                        temp_objekt = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
                        temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                                     self.laufkatze.pos.z,
                                                     self.laufkatze.pos.y)
                        temp_punkt_2D0 = numpy.array([objekt_pos.erhalte_position().x, objekt_pos.erhalte_position().z])
                        temp_punkt_2D1 = numpy.array([self.laufkatze.pos.x, self.laufkatze.pos.z])
                        temp_punkt_2D2 = numpy.array([self.turm.pos.x,self.turm.pos.z])
                        x_abstand_1 = numpy.linalg.norm(temp_punkt_2D0 - temp_punkt_2D2)
                        x_abstand_2 = numpy.linalg.norm(temp_punkt_2D1 - temp_punkt_2D2)
                        if x_zahler > x_abstand_zwischen_zwei_puntken:
                            x_erhoehung = x_abstand_1-x_abstand_2 #x_abstand_zwischen_zwei_puntken - x_zahler - x_erhoehung#
                            if x_erhoehung < 0:
                                x_erhoehung = -1*x_erhoehung
                        if x_abstand_2 < x_abstand_1:
                            temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel, x_erhoehung*b, temp_objekt)
                        elif x_abstand_2 > x_abstand_1:
                            temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel, -1*x_erhoehung*b,
                                                                                                temp_objekt)
                        self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
                        self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
                        self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
                        self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
                        self.verbindunsseil.pos.x = temp_punkt_3D.erhalte_position().x
                        self.verbindunsseil.pos.z = temp_punkt_3D.erhalte_position().z
                        #self.greifarm.pos.y = self.laufkatze.pos.y - 0.5
                        if objekt_bauteil is not None:
                            objekt_bauteil.erhalte_position().x = temp_punkt_3D.erhalte_position().x
                            objekt_bauteil.erhalte_position().y = self.greifarm.pos.y#temp_punkt_3D.erhalte_position().y - 0.5
                            objekt_bauteil.erhalte_position().z = temp_punkt_3D.erhalte_position().z
                    else:
                        break
                break

            if bereits_erhoeht < hoehe:
                bereits_erhoeht = bereits_erhoeht + x_erhoehung_hoehe
                if bereits_erhoeht > hoehe:
                    x_erhoehung_hoehe = hoehe - (bereits_erhoeht - x_erhoehung_hoehe)

                if objekt_pos.erhalte_position().y < self.greifarm.pos.y:
                    self.greifarm.pos.y = self.greifarm.pos.y - x_erhoehung_hoehe  # round(self.greifarm.pos.y - x_erhoehung_hoehe, 1)
                    print(self.greifarm.pos.y)
                    self.verbindunsseil.pos = self.greifarm.pos
                    self.verbindunsseil.pos.y = self.verbindunsseil.pos.y + 0.5
                    self.verbindunsseil.length = self.verbindunsseil.length + x_erhoehung_hoehe  # round(self.verbindunsseil.length + x_erhoehung_hoehe, 1)
                elif self.greifarm.pos.y < objekt_pos.erhalte_position().y:
                    self.greifarm.pos.y = self.greifarm.pos.y + x_erhoehung_hoehe  # round(self.greifarm.pos.y + x_erhoehung_hoehe, 1)
                    print(self.greifarm.pos.y)
                    self.verbindunsseil.pos = self.greifarm.pos
                    self.verbindunsseil.pos.y = self.verbindunsseil.pos.y + 0.5
                    self.verbindunsseil.length = self.verbindunsseil.length - x_erhoehung_hoehe  # round(self.verbindunsseil.length - x_erhoehung_hoehe, 1)
            #else:
            #    break

            if bereits_gedreht < winkel:
                t_winkel += i_winkel
                if t_winkel > winkel:
                    t_winkel = t_winkel - i_winkel
                    t_winkel = (winkel - t_winkel) + t_winkel

                temp_objekt = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
                temp_objekt.erzeuge_position(self.ausleger.pos.x + self.ausleger.axis.x,
                                             self.ausleger.pos.z + self.ausleger.axis.z,
                                             self.ausleger.pos.y + self.ausleger.axis.y - 0.5)
                temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel,  None, temp_objekt)
                self.ausleger.axis.x = temp_punkt_3D.erhalte_position().x-self.ausleger.pos.x
                self.ausleger.axis.z = temp_punkt_3D.erhalte_position().z-self.ausleger.pos.z

                temp_objekt = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
                temp_objekt.erzeuge_position(self.laufkatze.pos.x, self.laufkatze.pos.z, self.laufkatze.pos.y)
                temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel,  None, temp_objekt)

                self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
                #self.laufkatze.pos.y = temp_punkt_3D.erhalte_position().y
                self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
                self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
                #self.greifarm.pos.y = temp_punkt_3D.erhalte_position().y -0.5
                self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
                self.verbindunsseil.pos.x = temp_punkt_3D.erhalte_position().x
                self.verbindunsseil.pos.z = temp_punkt_3D.erhalte_position().z
                if objekt_bauteil is not None:
                    objekt_bauteil.erhalte_position().x = temp_punkt_3D.erhalte_position().x
                    #objekt_bauteil.erhalte_position().y = temp_punkt_3D.erhalte_position().y-0.5
                    objekt_bauteil.erhalte_position().z = temp_punkt_3D.erhalte_position().z

                bereits_gedreht += i_winkel

                if x_zahler < x_abstand_zwischen_zwei_puntken:
                    x_zahler += x_erhoehung
                    b = 1
                    temp_objekt = src.grafischer_prototyp.GrafikObjekte.GrafikPosition()
                    temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                                 self.laufkatze.pos.z,
                                                 self.laufkatze.pos.y)
                    temp_punkt_2D0 = numpy.array([objekt_pos.erhalte_position().x, objekt_pos.erhalte_position().z])
                    temp_punkt_2D1 = numpy.array([self.laufkatze.pos.x, self.laufkatze.pos.z])
                    temp_punkt_2D2 = numpy.array([self.turm.pos.x,self.turm.pos.z])
                    x_abstand_1 = numpy.linalg.norm(temp_punkt_2D0 - temp_punkt_2D2)
                    x_abstand_2 = numpy.linalg.norm(temp_punkt_2D1 - temp_punkt_2D2)
                    if x_zahler > x_abstand_zwischen_zwei_puntken:
                        x_erhoehung = x_abstand_1-x_abstand_2 #x_abstand_zwischen_zwei_puntken - x_zahler - x_erhoehung#
                        if x_erhoehung < 0:
                            x_erhoehung = -1*x_erhoehung
                    if x_abstand_2 < x_abstand_1:
                        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel, x_erhoehung*b, temp_objekt)
                    elif x_abstand_2 > x_abstand_1:
                        temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang + a*t_winkel, -1*x_erhoehung*b,
                                                                                            temp_objekt)
                    self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
                    self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
                    self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
                    self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
                    self.verbindunsseil.pos.x = temp_punkt_3D.erhalte_position().x
                    self.verbindunsseil.pos.z = temp_punkt_3D.erhalte_position().z
                    #self.greifarm.pos.y = self.laufkatze.pos.y - 0.5


                    if objekt_bauteil is not None:
                        objekt_bauteil.erhalte_position().x = temp_punkt_3D.erhalte_position().x
                        objekt_bauteil.erhalte_position().y = self.greifarm.pos.y#temp_punkt_3D.erhalte_position().y - 0.5
                        objekt_bauteil.erhalte_position().z = temp_punkt_3D.erhalte_position().z

            else:
                break
        self.greifarm.pos.y = round(self.greifarm.pos.y,0)
        print(self.greifarm.pos)
        return "unlock" #a*t_winkel + aktueller_winkel_ausleger_anfang