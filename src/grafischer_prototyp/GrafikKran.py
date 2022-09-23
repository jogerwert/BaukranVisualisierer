import numpy
from vpython import *
from math import *
import grafischer_prototyp.GrafikObjekte


class GrafikKran:
    """
        Notes:
        Klasse für Erzeugung eines Krans und die Funktionalität für dessen Animation. Da diese Klasse als erstes
        erzeugt wurde, sind einige backend Strukturen vorhanden, welche ausgelagert werden sollten.
    """
    def erzeuge_kran(self, ev_x_wert, ev_y_wert, ev_hoehe_kran, ev_ausladung_kran):
        """
            Notes:
            Erzeugt den Kran und auch einige Werte, welche für einige Berechnung benötigt werden.
            Streng genommen sollten diese Werte (time,rate,collsion_error) ausgelagert werden, da aber die
            Porgrammabscnitte für grafische Darstellung als erstes existierte, sind in dieser Klasse einige Backend
            Logik vorhanden, um zeigen zu können, dass die Visualisierung funktioniert.
        """

        iv_laenge = iv_breite = iv_hoehe = 0.5
        iv_turm_position = vector(ev_x_wert, 0, ev_y_wert)
        iv_ausleger_position = vector(ev_x_wert, ev_hoehe_kran+1, ev_y_wert)
        iv_drehkranz_position = vector(ev_x_wert, ev_hoehe_kran+1, ev_y_wert)
        iv_laufkatze_position = vector(ev_x_wert+1, ev_hoehe_kran+0.5, ev_y_wert)
        iv_greifarm_position = vector(ev_x_wert+1, ev_hoehe_kran, ev_y_wert)
        iv_verbindunsseil_position = vector(ev_x_wert+1, ev_hoehe_kran+0.5, ev_y_wert)

        self.fundament = box(pos=iv_turm_position)
        self.turm = cylinder(pos=iv_turm_position, radius=0.5, length=ev_hoehe_kran+1, axis=vector(0, 1, 0))
        self.ausleger = cylinder(pos=iv_ausleger_position, radius=0.5, length=ev_ausladung_kran, axis=vector(1, 0, 0))
        self.drehkranz = sphere(pos=iv_drehkranz_position, radius=0.5)
        self.verbindunsseil = cylinder(pos=iv_verbindunsseil_position,radius=0.01, axis=vector(0, 1, 0), length=0.01)
        self.laufkatze = box(pos=iv_laufkatze_position, length=iv_laenge, height=iv_hoehe, width=iv_breite,
                             color=vector(0, 1, 0))
        self.greifarm = pyramid(pos=iv_greifarm_position, size=vector(0.5, 0.5, 0.5), axis=vector(0, 1, 0))
        self.time = 0
        self.rate = 1
        self.collision_error = []

    def loesche_kran(self):
        self.fundament.visible = False
        self.turm.visible = False
        self.ausleger.visible = False
        self.drehkranz.visible = False
        self.verbindunsseil.visible = False
        self.laufkatze.visible = False
        self.greifarm.visible = False

    def get_collision(self):
        """
            Notes:
            Gibt eine Liste zurück. Diese Liste beinhaltet "bringe an" Befehle, wo eine Kollision vorkam
        """
        return self.collision_error

    def animationsgeschwindigkeit(self, wert):
        """
            Notes:
            Gibt an, wie schnell die Animation abgespielt werden soll.
        """
        self.rate = 1 + wert * 100

    def greife(self):
        """
            Notes:
            Die Krananweisung "greife" wird nicht visuell dargestellt, aber für die Zeitberechnung wird diese
            Funktion benötigt. Hier wird angenommen, dass greife Befehl eine SEkunde dauert.
        """
        self.time = self.time + 1

    def richte_aus(self):
        """
            Notes:
            Die Krananweisung "richte aus" wird nicht visuell dargestellt, aber für die Zeitberechnung wird diese
            Funktion benötigt. Hier wird angenommen, dass greife Befehl eine SEkunde dauert.
        """
        self.time = self.time + 1

    def lasse_los(self):
        """
            Notes:
            Die Krananweisung "lasse los" wird nicht visuell dargestellt, aber für die Zeitberechnung wird diese
            Funktion benötigt. Hier wird angenommen, dass greife Befehl eine SEkunde dauert.
        """
        self.time = self.time + 1

    def veraendere_greifarm_hoehe(self, ev_richtung, ev_erhoehe, ev_objekt):
        """
            Notes:
            Kombiniert die Krananweisungen "Senke um" und "Hebe um", da es programmiertechnisch kein Sinn macht
            zwei Funktionen zu erzeugen, welche nahezu das gleiche macht. (In einem Fall hochziehen des Greifarms und
            im anderen Fall senken des Greifarms.) Zeitrechnung für den Befehl wird ausgeführt, damit angegeben werden
            kann, wie lange ein Bauablauf dauert.
        """
        iv_temp = iv_richtung = 0
        while True:
            rate(self.rate)
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
        self.time = self.time + round(iv_temp,1)

    def erhalte_posistion_laufkatze(self):
        return self.laufkatze.pos

    def berechne_drehwinkel_objekt(self, ev_objekt):
        """
            Notes:
            Diese Funktion ist ein Überbleibsel, welche in den Anfängen des Projektes benötigt wurde, um die
            Animation der Baustelle durchzuführen. Da Winkel von der modellierten Baustelle kommt, ist diese Funktion
            nicht mehr nötig. Die Funktion wird dringelassen als Hinweis, dass es eine frühere Version gibt, die die
            Visualisierung als Standalone ausgeführt hat.
        """
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
        """
            Notes:
            Bestimmt die Drehrichtung des Krans, da durch die Verwendung der Funktion
            "berechne_drehwinkel_objekt(self, ev_objekt):" Nur Werte von 0 bis 180 ermittelt werden kann, was es nicht
            möglich machte, zu wissen in welche Richtung gedreht werden soll.
        """
        iv_objekt = grafischer_prototyp.GrafikObjekte.GrafikPosition()
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
        """
            Notes:
            Berechnet einen Punkt nach der Drehung des Auslegers. Die Funktion wird benutzt, um Auslegerpostionen
            nach der Drehung im Vorfeld zu bestimmen.
        """
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
            iv_punkt = grafischer_prototyp.GrafikObjekte.GrafikPosition()
            iv_punkt.erzeuge_position(iv_x, iv_y, iv_z)
            return iv_punkt

    def berechne_bewegunszeit_laufkatze_ausleger(self, ev_winkel, ev_abstand_laufkatze_punkt, position):
        """
            Notes:
            Dieese Funktion setzt die Bewegungsgeschwindigkeit von Ausleger, Greifarm und Laufkatze in
            Verhältnis, da die Bedingung war, dass Ausleger, Greifarm und Laufkatze synchon bewegt werden bei dem
            "bringe an" Befehl
        """
        iv_laufkatzenzeit = ev_abstand_laufkatze_punkt
        iv_auslegerzeit = ev_winkel / 10
        if self.greifarm.pos.y  < position.erhalte_position().y :
            iv_greifarmzeit = position.erhalte_position().y - self.greifarm.pos.y
        else:
            iv_greifarmzeit = self.greifarm.pos.y - position.erhalte_position().y
        if iv_laufkatzenzeit < iv_auslegerzeit and iv_greifarmzeit < iv_auslegerzeit:
            iv_laufkatzenbewegung_pro_sekunde = 1 * iv_laufkatzenzeit / iv_auslegerzeit
            iv_greifarmbewegung_pro_sekunde = 1 * iv_greifarmzeit / iv_auslegerzeit
            iv_auslegerbewegung_pro_sekund = 10
        elif iv_auslegerzeit < iv_laufkatzenzeit and iv_greifarmzeit < iv_laufkatzenzeit:
            iv_laufkatzenbewegung_pro_sekunde = 1
            iv_auslegerbewegung_pro_sekund = 10 * iv_auslegerzeit / iv_laufkatzenzeit
            iv_greifarmbewegung_pro_sekunde = 1 * iv_greifarmzeit / iv_laufkatzenzeit
        else:
            iv_laufkatzenbewegung_pro_sekunde = 1 * iv_laufkatzenzeit / iv_greifarmzeit
            iv_auslegerbewegung_pro_sekund = 10 * iv_auslegerzeit / iv_greifarmzeit
            iv_greifarmbewegung_pro_sekunde = 1
        return iv_laufkatzenbewegung_pro_sekunde, iv_auslegerbewegung_pro_sekund, iv_greifarmbewegung_pro_sekunde

    def bringe_an(self, winkel, aktueller_winkel_ausleger_anfang, objekt_pos, objekt_bauteil, hindernisse):
        """
            Notes:
            Diese Funktion bewegt Laufkatze, Greifarm und Ausleger. Hier wird auch geprüft, obe diese Funktion
            beim Bewegen eines gegriffenen Bauobjekt Kollision mit Hindernisse hat. Kollision mit anderen Bauteilen wird
            in dieser Version noch nicht geprüft. Auch Kollisoin von Greifarm und Bauteile/Hindernisse werden nicht
            erkannt. Diese Funktion berechnet die Zeit für den Ablauf.
            -die Namen von Variabel und Funktonen können noch weiter refaktorisiert werden
        """
        def bewege_greifarm(bereits_erhoeht,x_erhoehung_hoehe,hoehe):
            t_x_erhoehung_hoehe = x_erhoehung_hoehe
            t_bereits_erhoeht = bereits_erhoeht
            if bereits_erhoeht < hoehe:
                t_bereits_erhoeht = bereits_erhoeht + x_erhoehung_hoehe
                if t_bereits_erhoeht > hoehe:
                    t_x_erhoehung_hoehe = hoehe - (t_bereits_erhoeht - x_erhoehung_hoehe)

                if objekt_pos.erhalte_position().y < self.greifarm.pos.y:
                    self.greifarm.pos.y = self.greifarm.pos.y - t_x_erhoehung_hoehe
                    self.verbindunsseil.pos = self.greifarm.pos
                    self.verbindunsseil.pos.y = self.verbindunsseil.pos.y + 0.5
                    self.verbindunsseil.length = self.verbindunsseil.length + t_x_erhoehung_hoehe
                elif self.greifarm.pos.y < objekt_pos.erhalte_position().y:
                    self.greifarm.pos.y = self.greifarm.pos.y + t_x_erhoehung_hoehe
                    self.verbindunsseil.pos = self.greifarm.pos
                    self.verbindunsseil.pos.y = self.verbindunsseil.pos.y + 0.5
                    self.verbindunsseil.length = self.verbindunsseil.length - t_x_erhoehung_hoehe
            return t_bereits_erhoeht

        def bewege_laufkatze(x_zahler, x_abstand_zwischen_zwei_puntken, x_erhoehung, coll_counter):
            t_x_zahler = x_zahler
            t_coll_counter = coll_counter
            if x_zahler < x_abstand_zwischen_zwei_puntken:
                t_x_zahler += x_erhoehung
                b = 1
                temp_objekt = grafischer_prototyp.GrafikObjekte.GrafikPosition()
                temp_objekt.erzeuge_position(self.laufkatze.pos.x,
                                             self.laufkatze.pos.z,
                                             self.laufkatze.pos.y)
                temp_punkt_2D0 = numpy.array([objekt_pos.erhalte_position().x, objekt_pos.erhalte_position().z])
                temp_punkt_2D1 = numpy.array([self.laufkatze.pos.x, self.laufkatze.pos.z])
                temp_punkt_2D2 = numpy.array([self.turm.pos.x, self.turm.pos.z])
                x_abstand_1 = numpy.linalg.norm(temp_punkt_2D0 - temp_punkt_2D2)
                x_abstand_2 = numpy.linalg.norm(temp_punkt_2D1 - temp_punkt_2D2)
                if t_x_zahler > x_abstand_zwischen_zwei_puntken:
                    x_erhoehung = x_abstand_1 - x_abstand_2
                    if x_erhoehung < 0:
                        x_erhoehung = -1 * x_erhoehung
                if x_abstand_2 < x_abstand_1:
                    temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(
                        aktueller_winkel_ausleger_anfang + drehrichtung * t_winkel, x_erhoehung * b, temp_objekt)
                elif x_abstand_2 > x_abstand_1:
                    temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(
                        aktueller_winkel_ausleger_anfang + drehrichtung * t_winkel, -1 * x_erhoehung * b,
                        temp_objekt)
                self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
                self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
                self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
                self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
                self.verbindunsseil.pos.x = temp_punkt_3D.erhalte_position().x
                self.verbindunsseil.pos.z = temp_punkt_3D.erhalte_position().z

                if objekt_bauteil is not None:
                    objekt_bauteil.erhalte_position().x = temp_punkt_3D.erhalte_position().x
                    objekt_bauteil.erhalte_position().y = self.greifarm.pos.y
                    objekt_bauteil.erhalte_position().z = temp_punkt_3D.erhalte_position().z
                    for element in hindernisse:
                        temp_punkt_3D_1 = numpy.array(
                            [objekt_bauteil.erhalte_position().x, objekt_bauteil.erhalte_position().z,
                             objekt_bauteil.erhalte_position().y])
                        temp_punkt_3D_2 = numpy.array(
                            [element.erhalte_position().x, element.erhalte_position().z,
                             element.erhalte_position().y])

                        x_abstand_coll = numpy.linalg.norm(
                            temp_punkt_3D_1 - temp_punkt_3D_2)
                        if x_abstand_coll < 1:
                            t_coll_counter += 1
                            pass
            return t_x_zahler,t_coll_counter

        def bewege_ausleger(bereits_gedreht,i_winkel,t_winkel,winkel,a):
            t_bereits_gedreht = bereits_gedreht
            t_t_winkel = t_winkel
            if bereits_gedreht < winkel:
                t_t_winkel += i_winkel
                if t_t_winkel > winkel:
                    t_t_winkel = t_t_winkel - i_winkel
                    t_t_winkel = (winkel - t_t_winkel) + t_t_winkel

                temp_objekt = grafischer_prototyp.GrafikObjekte.GrafikPosition()
                temp_objekt.erzeuge_position(self.ausleger.pos.x + self.ausleger.axis.x,
                                             self.ausleger.pos.z + self.ausleger.axis.z,
                                             self.ausleger.pos.y + self.ausleger.axis.y - 0.5)
                temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang +
                                                                                    a * t_t_winkel, None, temp_objekt)
                self.ausleger.axis.x = temp_punkt_3D.erhalte_position().x - self.ausleger.pos.x
                self.ausleger.axis.z = temp_punkt_3D.erhalte_position().z - self.ausleger.pos.z

                temp_objekt = grafischer_prototyp.GrafikObjekte.GrafikPosition()
                temp_objekt.erzeuge_position(self.laufkatze.pos.x, self.laufkatze.pos.z, self.laufkatze.pos.y)
                temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(aktueller_winkel_ausleger_anfang +
                                                                                    a * t_t_winkel, None, temp_objekt)

                self.laufkatze.pos.x = temp_punkt_3D.erhalte_position().x
                self.laufkatze.pos.z = temp_punkt_3D.erhalte_position().z
                self.greifarm.pos.x = temp_punkt_3D.erhalte_position().x
                self.greifarm.pos.z = temp_punkt_3D.erhalte_position().z
                self.verbindunsseil.pos.x = temp_punkt_3D.erhalte_position().x
                self.verbindunsseil.pos.z = temp_punkt_3D.erhalte_position().z
                if objekt_bauteil is not None:
                    objekt_bauteil.erhalte_position().x = temp_punkt_3D.erhalte_position().x
                    objekt_bauteil.erhalte_position().z = temp_punkt_3D.erhalte_position().z

                t_bereits_gedreht += i_winkel
            return t_bereits_gedreht, t_t_winkel

        def pruefe_kollision(coll_counter):
            if coll_counter > 0:
                string = "bringe an Position(" + str(objekt_pos.erhalte_position().x) + ", " + str(
                    objekt_pos.erhalte_position().z) + ", " + str(objekt_pos.erhalte_position().y) + ")"
                self.collision_error.append(string)

        def ermittle_wert_fuer_animation(objekt_pos):
            temp_punkt_2D = numpy.array([objekt_pos.erhalte_position().x, objekt_pos.erhalte_position().z])
            temp_objekt = grafischer_prototyp.GrafikObjekte.GrafikPosition()
            temp_objekt.erzeuge_position(self.laufkatze.pos.x, self.laufkatze.pos.z, self.laufkatze.pos.y)
            temp_punkt_3D = self.berechne_punkt_kreisgleichung_abhaengig_winkel(winkel, None, temp_objekt)
            temp_punkt_2D_nach_rotation = numpy.array([temp_punkt_3D.erhalte_position().x,
                                                       temp_punkt_3D.erhalte_position().z])
            x_abstand_zwischen_zwei_puntken = numpy.linalg.norm(temp_punkt_2D - temp_punkt_2D_nach_rotation)
            x_erhoehung, i_winkel, x_erhoehung_hoehe = self.berechne_bewegunszeit_laufkatze_ausleger(winkel,
                                                                            x_abstand_zwischen_zwei_puntken,objekt_pos)
            return x_abstand_zwischen_zwei_puntken, x_erhoehung, i_winkel, x_erhoehung_hoehe

        def werte_in_kleinere_schritte(x_erhoehung, i_winkel, x_erhoehung_hoehe):
            tx_erhoehung = x_erhoehung / 10
            ti_winkel = i_winkel / 10
            tx_erhoehung_hoehe = x_erhoehung_hoehe / 10
            return tx_erhoehung,ti_winkel,tx_erhoehung_hoehe

        def ermittle_hoehe(objekt_pos):
            if self.greifarm.pos.y < objekt_pos.erhalte_position().y:
                hoehe = objekt_pos.erhalte_position().y - self.greifarm.pos.y
            else:
                hoehe = self.greifarm.pos.y - objekt_pos.erhalte_position().y
            return hoehe

        def berechne_zeit(x_erhoehung,x_abstand_zwischen_zwei_puntken,i_winkel,winkel,x_erhoehung_hoehe,hoehe):
            if x_erhoehung == 0.1:
                self.time = self.time + x_abstand_zwischen_zwei_puntken
            elif i_winkel == 1:
                self.time = self.time + winkel / 10
            elif x_erhoehung_hoehe == 0.1:
                self.time = self.time + hoehe

        bereits_gedreht = x_zahler = t_winkel = bereits_erhoeht = coll_counter =  0
        x_abstand_zwischen_zwei_puntken, x_erhoehung, i_winkel, x_erhoehung_hoehe = ermittle_wert_fuer_animation(
            objekt_pos)
        x_erhoehung, i_winkel, x_erhoehung_hoehe = werte_in_kleinere_schritte(x_erhoehung, i_winkel, x_erhoehung_hoehe)
        drehrichtung = self.berechne_punkt_links_oder_rechts_gerade(objekt_pos, aktueller_winkel_ausleger_anfang)
        hoehe = ermittle_hoehe(objekt_pos)
        berechne_zeit(x_erhoehung, x_abstand_zwischen_zwei_puntken, i_winkel, winkel, x_erhoehung_hoehe, hoehe)

        while True:
            rate(self.rate)
            if winkel == 0:
                while True:
                    if x_zahler < x_abstand_zwischen_zwei_puntken:
                        x_zahler,coll_counter = bewege_laufkatze(x_zahler, x_abstand_zwischen_zwei_puntken, x_erhoehung,
                                                                 coll_counter)
                        bereits_erhoeht = bewege_greifarm(bereits_erhoeht, x_erhoehung_hoehe, hoehe)
                    else:
                        pruefe_kollision(coll_counter)
                        break
                break

            if bereits_gedreht < winkel:
                bereits_gedreht, t_winkel= bewege_ausleger(bereits_gedreht, i_winkel, t_winkel, winkel, drehrichtung)
                x_zahler, coll_counter = bewege_laufkatze(x_zahler, x_abstand_zwischen_zwei_puntken, x_erhoehung,
                                                          coll_counter)
                bereits_erhoeht = bewege_greifarm(bereits_erhoeht, x_erhoehung_hoehe, hoehe)
            else:
                pruefe_kollision(coll_counter)
                break
        self.greifarm.pos.y = round(self.greifarm.pos.y,0)
        return drehrichtung * t_winkel + aktueller_winkel_ausleger_anfang