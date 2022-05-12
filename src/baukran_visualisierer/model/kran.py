import math

from src.baukran_visualisierer.model.bauteil import Bauteil


class Kran:

    def __init__(self, position_x, position_y, hoehe, ausladung):
        self.position_x = position_x
        self.position_y = position_y
        self.hoehe = hoehe
        self.ausladung = ausladung

        # Haken ganz oben
        self.haken_hoehe = hoehe

        # Laufkatze direkt am Mast
        self.laufkatze_position = 1

        # Ausleger in Richtung x-Achse
        self.winkel = 0

        self.baustelle = None
        self.haken_anhaengsel = None

    def greife(self):
        if self.baustelle is None:
            raise RuntimeError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_anhaengsel is not None:
            raise RuntimeError("An dem Haken haengt bereits ein Bauteil!")

        # TODO: Positionsberechnung testen
        haken_x = self.laufkatze_position * math.cos(math.radians(self.winkel))
        haken_y = self.laufkatze_position * math.sin(math.radians(self.winkel))
        haken_z = self.haken_hoehe
        haken_anhaengsel = self.baustelle.erhalte_inhalt_koordinate(haken_x, haken_y, haken_z)

        if isinstance(haken_anhaengsel, Bauteil):
            self.haken_anhaengsel = haken_anhaengsel
        else:
            raise RuntimeError(f'An der Koordinate ({haken_x}, {haken_y}, {haken_z}) befindet sich kein Bauteil!')

    def richte_aus(self):
        pass

    def lasse_los(self):
        pass

    def bringe_an(self, x, y, z):
        # TODO: pruefe ob hoehe kran ueberschritten
        # TODO: pruefe ob out-of-bounds
        # TODO: pruefe ob Koordinate erreichbar
        pass

    def senke_um(self, hoehe):
        # TODO: pruefe ob positiv
        # TODO: pruefe ob out-of-bounds
        self.haken_hoehe = self.haken_hoehe - hoehe

    def hebe_um(self, hoehe):
        # TODO: pruefe ob positiv
        # TODO: pruefe ob hoehe kran ueberschritten
        self.haken_hoehe = self.haken_hoehe + hoehe
