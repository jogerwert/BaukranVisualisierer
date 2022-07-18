import weakref


class Baustelle:

    def __init__(self, name, baufeld, kran, gegenstaende, bauteile, montageanweisungen):
        self.name = name
        self.baufeld = baufeld

        self.kran = kran
        baufeld.platziere_baustellenobjekt(kran)
        kran.baustelle = weakref.proxy(self)

        self.gegenstaende = gegenstaende
        for gegenstand in gegenstaende:
            baufeld.platziere_baustellenobjekt(gegenstand)

        self.bauteile = bauteile
        for bauteil in bauteile:
            baufeld.platziere_baustellenobjekt(bauteil)

        self.montageanweisungen = montageanweisungen
        self.montageanweisungs_zaehler = 0

    def alle_montageanweisungen_ausfuehren(self):

        if self.montageanweisungs_zaehler < len(self.montageanweisungen):

            # Bereits durchgefuehrte Anweisungen werden nicht wiederholt
            montageanweisungen = self.montageanweisungen[self.montageanweisungs_zaehler:]

            for anweisung in montageanweisungen:
                anweisung.alle_krananweisungen_ausfuehren()
                self.montageanweisungs_zaehler += 1

    def naechste_montageanweisung_ausfuehren(self):
        if self.montageanweisungs_zaehler < len(self.montageanweisungen):
            self.montageanweisungen[self.montageanweisungs_zaehler].alle_krananweisungen_ausfuehren()
            self.montageanweisungs_zaehler += 1

    def naechste_krananweisung_ausfuehren(self):
        if self.montageanweisungs_zaehler < len(self.montageanweisungen):
            anweisung = self.montageanweisungen[self.montageanweisungs_zaehler]
            anweisung.naechste_krananweisung_ausfuehren()
            if anweisung.pruefe_alle_anweisungen_ausgefuehrt():
                self.montageanweisungs_zaehler += 1

    def platziere_baustellenobjekt(self, baustellenobjekt):
        # TODO: Testen
        self.baufeld.platziere_baustellenobjekt(baustellenobjekt)

    def erhalte_baustellenobjekt(self, x, y, z):
        # TODO: Testen
        return self.baufeld.erhalte_baustellenobjekt(x, y, z)

    def entferne_baustellenobjekt(self, x, y, z):
        # TODO: Testen
        baustellen_objekt = self.baufeld.entferne_baustellenobjekt(x, y, z)
        return baustellen_objekt

    def bewege_baustellenobjekt(self, x1, y1, z1, x2, y2, z2):
        # TODO: Testen
        # TODO: Pruefe ob Listen aktualisiert
        return self.baufeld.bewege_baustellenobjekt(x1, y1, z1, x2, y2, z2)

    def pruefe_koordinate_leer(self, x, y, z):
        # TODO: Testen

        if self.baufeld.erhalte_baustellenobjekt(x, y, z) is None:
            return True
        else:
            return False
