import math

from src.baukran_visualisierer.exceptions.logic_error import LogicError
from src.baukran_visualisierer.model.bauteil import Bauteil


class Kran:

    def __init__(self, position_x, position_y, hoehe, ausladung):
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = 0
        self.hoehe = hoehe
        self.ausladung = ausladung

        # Haken ganz oben
        self.haken_hoehe = self.hoehe

        # Laufkatze direkt am Mast
        self.laufkatze_entfernung = 1

        # Ausleger zeigt in Richtung x-Achse
        self.winkel = 0

        # Kran steht in der Mitte des Kaestchens, nicht auf der Ecke
        self.raster_versatz = 0.5

        self.baustelle = None
        self.haken_anhaengsel = None

    def greife(self):
        if self.baustelle is None:
            raise LogicError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_anhaengsel is not None:
            raise LogicError("An dem Haken haengt bereits ein Bauteil!")

        haken_koordinaten_tuple = self.berechne_koordinaten_aus_kranposition(
            self.laufkatze_entfernung, self.winkel, self.haken_hoehe)

        haken_x = haken_koordinaten_tuple[0]
        haken_y = haken_koordinaten_tuple[1]
        haken_z = haken_koordinaten_tuple[2]

        haken_anhaengsel = self.baustelle.erhalte_inhalt_koordinate(haken_x, haken_y, haken_z)

        if isinstance(haken_anhaengsel, Bauteil):
            self.haken_anhaengsel = haken_anhaengsel
        else:
            raise LogicError(f'An der Koordinate ({haken_x}, {haken_y}, {haken_z}) befindet sich kein Bauteil!')

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

    def berechne_koordinaten_aus_kranposition(self, laufkatze_entfernung, winkel, haken_hoehe):
        # TODO: testen

        # Berechnung: Ankathete im Dreieck aus Winkel und Hypotenuse + Versatz
        haken_x = math.floor(
            self.position_x + self.raster_versatz
            + laufkatze_entfernung * math.cos(math.radians(winkel))
        )

        # Berechnung: Gegenkathete im Dreieck aus Winkel und Hypotenuse + Versatz
        haken_y = math.floor(
            self.position_y + self.raster_versatz
            + laufkatze_entfernung * math.sin(math.radians(winkel))
        )

        haken_z = math.floor(haken_hoehe)

        return haken_x, haken_y, haken_z

    def berechne_kranposition_aus_koordinaten(self, haken_x, haken_y, haken_z):
        # TODO: testen

        # Berechnung: Abstand zwischen zwei Punkten, Rasterversatz kuerzt sich raus
        laufkatze_entfernung = math.sqrt(
            math.pow(self.position_x - haken_x, 2)
            + math.pow(self.position_y - haken_y, 2)
        )

        if laufkatze_entfernung > self.ausladung:
            raise LogicError(f'Das Bauteil an Position ({haken_x}, {haken_y}, {haken_z}) '
                             f'liegt ausserhalb der Reichweite des Krans!')

        # Berechnung: Winkel im Dreieck aus Hypotenuse und Ankathete
        winkel = math.degrees(math.acos(haken_x / laufkatze_entfernung))

        haken_hoehe = haken_z

        return laufkatze_entfernung, winkel, haken_hoehe
