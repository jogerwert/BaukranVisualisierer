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
        self.haken_bauteil = None

    def greife(self):
        # TODO: Testen

        if self.baustelle is None:
            raise LogicError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_bauteil is not None:
            raise LogicError("An dem Haken haengt bereits ein Bauteil!")

        haken_koordinaten_tuple = self.berechne_koordinaten_aus_kranposition(
            self.laufkatze_entfernung, self.winkel, self.haken_hoehe)

        haken_x = haken_koordinaten_tuple[0]
        haken_y = haken_koordinaten_tuple[1]
        haken_z = haken_koordinaten_tuple[2]

        haken_bauteil = self.baustelle.erhalte_baustellenobjekt(haken_x, haken_y, haken_z)

        if isinstance(haken_bauteil, Bauteil):
            self.haken_bauteil = haken_bauteil
            self.baustelle.entferne_baustellenobjekt(haken_x, haken_y, haken_z)
        else:
            raise LogicError(f'An der Koordinate ({haken_x}, {haken_y}, {haken_z}) befindet sich kein Bauteil!')

    def richte_aus(self):
        # TODO: Testen

        if self.baustelle is None:
            raise LogicError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_bauteil is None:
            raise LogicError("An dem Haken haengt kein Bauteil!")

    def lasse_los(self):
        # TODO: Testen

        if self.baustelle is None:
            raise LogicError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_bauteil is None:
            raise LogicError("An dem Haken haengt kein Bauteil!")

        haken_koordinaten_tuple = self.berechne_koordinaten_aus_kranposition(
            self.laufkatze_entfernung, self.winkel, self.haken_hoehe)

        haken_x = haken_koordinaten_tuple[0]
        haken_y = haken_koordinaten_tuple[1]
        haken_z = haken_koordinaten_tuple[2]

        if not self.baustelle.pruefe_koordinate_leer(haken_x, haken_y, haken_z):
            raise LogicError(f'An der Koordinate ({haken_x}, {haken_y}, {haken_z}) existiert bereits ein Bauteil')

        bauteil = self.haken_bauteil

        bauteil.position_x = haken_x
        bauteil.position_y = haken_y
        bauteil.position_z = haken_z

        self.haken_bauteil = None
        self.baustelle.platziere_baustellenobjekt(bauteil)

        return bauteil

    def bringe_an(self, x, y, z):
        # TODO: Testen

        if x == self.position_x and y == self.position_y:
            raise LogicError(f'Bauteile koennen nicht auf der Position des Krans platziert werden!')

        if z > self.hoehe:
            raise LogicError(f'Die Hoehe des Krans wurde ueberschritten!')

        if x < 0 or x >= self.baustelle.baufeld.laenge_x or y < 0 or y >= self.baustelle.baufeld.breite_y:
            raise LogicError(f'Der Haken wurde ausserhalb des Baufelds bewegt!')

        hakenposition_tuple = self.berechne_hakenposition_aus_koordinaten(x, y, z)
        laufkatze_entfernung = hakenposition_tuple[0]
        winkel = hakenposition_tuple[1]
        haken_hoehe = hakenposition_tuple[2]

        if laufkatze_entfernung > self.ausladung:
            raise LogicError(f'Die maximale Reichweite der Laufkatze wurde ueberschritten!')

        self.laufkatze_entfernung = laufkatze_entfernung
        self.winkel = winkel
        self.haken_hoehe = haken_hoehe

        return self.laufkatze_entfernung, self.winkel, self.haken_hoehe

    def senke_um(self, hoehe):
        # TODO: Testen

        if hoehe <= 0:
            raise LogicError(f'Hoehe muss positiv sein!')

        if (self.haken_hoehe - hoehe) < 0:
            raise LogicError(f'Ein Bauteil wurde unter das Baufeld bewegt!')

        self.haken_hoehe = self.haken_hoehe - hoehe

        return self.haken_hoehe

    def hebe_um(self, hoehe):
        # TODO: Testen

        if hoehe <= 0:
            raise LogicError(f'Hoehe muss positiv sein!')

        if (self.haken_hoehe + hoehe) > self.hoehe:
            raise LogicError(f'Die Hoehe des Hakens darf die Hoehe des Krans nicht ueberschreiten!')

        self.haken_hoehe = self.haken_hoehe + hoehe

        return self.haken_hoehe

    def berechne_koordinaten_aus_kranposition(self, laufkatze_entfernung, winkel, haken_hoehe):
        # TODO: Testen

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

    def berechne_hakenposition_aus_koordinaten(self, haken_x, haken_y, haken_z):
        # TODO: Testen

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
