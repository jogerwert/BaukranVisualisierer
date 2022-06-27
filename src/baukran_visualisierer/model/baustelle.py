import weakref


class Baustelle:

    def __init__(self, name, baufeld, kran, gegenstaende, bauteile, montageanweisungen):
        self.name = name
        self.baufeld = baufeld

        self.kran = kran
        baufeld.platziere_objekt(kran, kran.position_x, kran.position_y, kran.position_z)
        kran.baustelle = weakref.ref(self)

        self.gegenstaende = gegenstaende
        for gegenstand in gegenstaende:
            baufeld.platziere_objekt(gegenstand, gegenstand.position_x, gegenstand.position_y, gegenstand.position_z)

        self.bauteile = bauteile
        for bauteil in bauteile:
            baufeld.platziere_objekt(bauteil, bauteil.position_x, bauteil.position_y, bauteil.position_z)

        self.montageanweisungen = montageanweisungen

    def alle_montageanweisungen_ausfuehren(self):
        pass

    def naechste_montageanweisung_ausfuehren(self):
        pass

    def naechste_krananweisung_ausfuehren(self):
        pass

    def erhalte_inhalt_koordinate(self, x, y, z):
        return self.baufeld.erhalte_objekt(x, y, z)

    def pruefe_koordinate_leer(self, x, y, z):

        if self.baufeld.erhalte_objekt(x, y, z) is None:
            return True
        else:
            return False
