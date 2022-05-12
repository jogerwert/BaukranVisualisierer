import weakref


class Baustelle:

    def __init__(self, name, baufeld, gegenstaende, kraene, bauteile, montageanweisungen):
        self.name = name
        self.baufeld = baufeld
        self.gegenstaende = gegenstaende
        self.kraene = kraene
        self.bauteile = bauteile
        self.montageanweisungen = montageanweisungen

        for kran in kraene:
            kran.baustelle = weakref.ref(self)

    def alle_montageanweisungen_ausfuehren(self):
        pass

    def eine_montageanweisung_ausfuehren(self):
        pass

    def ursprungszustand_wiederherstellen(self):
        pass

    def erhalte_inhalt_koordinate(self, x, y, z):
        # TODO: pruefe ob out-of-bounds

        for kran in self.kraene:
            if kran.position_x == x and kran.position_y == y:
                return kran

        for gegenstand in self.gegenstaende:
            if gegenstand.position_x == x and gegenstand.position_y == y and gegenstand.position_z == z:
                return gegenstand

        for bauteil in self.bauteile:
            if bauteil.position_x == x and bauteil.position_y == y and bauteil.position_z == z:
                return bauteil

        return None

    def pruefe_koordinate_leer(self, x, y, z):
        # TODO: pruefe ob out-of-bounds

        if self.erhalte_inhalt_koordinate(x, y, z) is None:
            return True
        else:
            return False
