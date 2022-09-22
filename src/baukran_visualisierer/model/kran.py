import math
from typing import Any

from baukran_visualisierer.exceptions.bas_logic_error import BasLogicError
from baukran_visualisierer.model.bauteil import Bauteil


class Kran:

    def __init__(self, position_x: int, position_y: int, hoehe: int, ausladung: int) -> None:
        """
        Klasse fuer den Kran der Baustelle.
        Der Kran bewegt die Bauteile an die vorgesehenen Koordinaten.
        Dazu wird dieser mithilfe von Anweisungen, die die Funktionen des Krans aufrufen, gesteuert.

        :param position_x: Koordinate x
        :param position_y: Koordinate y
        :param hoehe: Hoehe des Krans
        :param ausladung: Reichweite des Auslegers des Krans
        """
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
        # Die Angabe des Winkels ist immer relativ zur Ausgangsposition
        self.winkel = 0

        # Kran steht in der Mitte des Kaestchens, nicht auf der Ecke
        self.raster_versatz = 0.5

        self.baustelle = None
        self.haken_bauteil = None

        # Schnittstelle, um die Kranbewegungen modular zu visualisieren
        self.visualisiere_greife = self._do_nothing
        self.visualisiere_richte_aus = self._do_nothing
        self.visualisiere_lasse_los = self._do_nothing
        self.visualisiere_bringe_an = self._do_nothing
        self.visualisiere_senke_um = self._do_nothing
        self.visualisiere_hebe_um = self._do_nothing

    def greife(self) -> None:
        """
        Der Kran greift den Inhalt der aktuellen Koordinate.
        Wenn der Inhalt ein Bauteil ist, wird dieses aus dem Baufeld entfernt und im Kran gespeichert.
        """
        if self.baustelle is None:
            raise BasLogicError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_bauteil is not None:
            raise BasLogicError("An dem Haken haengt bereits ein Bauteil!")

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
            raise BasLogicError(f'An der Koordinate ({haken_x}, {haken_y}, {haken_z}) befindet sich kein Bauteil!')

        self.visualisiere_greife()

    def richte_aus(self) -> None:
        """
        Das Bauteil, das am Haken haengt, wird ausgerichtet.
        Diese Funktion wird hauptsaechlich dazu verwendet, dass Bauteil in seine endgueltige Ausrichtung vor
        der Platzierung zu drehen.
        """
        if self.baustelle is None:
            raise BasLogicError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_bauteil is None:
            raise BasLogicError("An dem Haken haengt kein Bauteil!")

        self.visualisiere_richte_aus()

    def lasse_los(self) -> Bauteil:
        """
        Der Haken laesst das gegriffene Bauteil los.
        Wenn am Haken ein Bauteil haengt und die Koordinate frei ist, wird das Bauteil vom Haken entfernt und
        im Baufeld platziert.

        :return: Das losgelassene Bauteil
        """
        if self.baustelle is None:
            raise BasLogicError("Kran wurde keiner Baustelle zugewiesen!")

        if self.haken_bauteil is None:
            raise BasLogicError("An dem Haken haengt kein Bauteil!")

        haken_koordinaten_tuple = self.berechne_koordinaten_aus_kranposition(
            self.laufkatze_entfernung, self.winkel, self.haken_hoehe)

        haken_x = haken_koordinaten_tuple[0]
        haken_y = haken_koordinaten_tuple[1]
        haken_z = haken_koordinaten_tuple[2]

        if not self.baustelle.pruefe_koordinate_leer(haken_x, haken_y, haken_z):
            raise BasLogicError(f'An der Koordinate ({haken_x}, {haken_y}, {haken_z}) existiert bereits ein Bauteil')

        bauteil = self.haken_bauteil

        bauteil.position_x = haken_x
        bauteil.position_y = haken_y
        bauteil.position_z = haken_z

        self.haken_bauteil = None
        self.baustelle.platziere_baustellenobjekt(bauteil)

        self.visualisiere_lasse_los()

        return bauteil

    def bringe_an(self, x: int, y: int, z: int = None) -> tuple[float, float, float]:
        """
        Der Haken des Krans wird auf direktem Weg an die gegebene Koordinate bewegt.
        Falls keine z-Koordinate uebergeben wird, bleibt der Haken auf der gleichen Hoehe.

        :param x: Koordinate x
        :param y: Koordinate y
        :param z: Koordinate z
        :return: Die Entfernung der Laufkatze vom Mast, der Winkel relativ zum Ausgangswinkel und die Hoehe des Hakens
        """
        if x == self.position_x and y == self.position_y:
            raise BasLogicError(f'Bauteile koennen nicht auf der Position des Krans platziert werden!')

        if z is None:
            z = math.floor(self.haken_hoehe)

        if z > self.hoehe:
            raise BasLogicError(f'Die Hoehe des Krans wurde ueberschritten!')

        if x < 0 or x >= self.baustelle.baufeld.laenge_x or y < 0 or y >= self.baustelle.baufeld.breite_y:
            raise BasLogicError(f'Der Haken wurde ausserhalb des Baufelds bewegt!')

        winkel_vorher = self.winkel

        hakenposition_tuple = self.berechne_hakenposition_aus_koordinaten(x, y, z)
        laufkatze_entfernung = hakenposition_tuple[0]
        winkel_nachher = hakenposition_tuple[1]
        haken_hoehe = hakenposition_tuple[2]

        if laufkatze_entfernung > self.ausladung:
            raise BasLogicError(f'Die maximale Reichweite der Laufkatze wurde ueberschritten!')

        self.laufkatze_entfernung = laufkatze_entfernung
        self.winkel = winkel_nachher
        self.haken_hoehe = haken_hoehe

        bauteil_name = None
        if self.haken_bauteil is not None:
            bauteil_name = self.haken_bauteil.name

        self.visualisiere_bringe_an(winkel_vorher, winkel_nachher, x, y, z, bauteil_name)

        return self.laufkatze_entfernung, self.winkel, self.haken_hoehe

    def senke_um(self, hoehe: int) -> float:
        """
        Der Haken wird um eine relative Hoehenangabe gesenkt.

        :param hoehe: Die Anzahl an Einheiten, um die der Haken gesenkt wird
        :return: Die aktualisierte Hoehe des Hakens
        """
        if hoehe <= 0:
            raise BasLogicError(f'Hoehe muss positiv sein!')

        if (self.haken_hoehe - hoehe) < 0:
            raise BasLogicError(f'Ein Bauteil wurde unter das Baufeld bewegt!')

        self.haken_hoehe = self.haken_hoehe - hoehe

        bauteil_name = None
        if self.haken_bauteil is not None:
            bauteil_name = self.haken_bauteil.name

        self.visualisiere_senke_um(hoehe, bauteil_name)

        return self.haken_hoehe

    def hebe_um(self, hoehe: int) -> float:
        """
        Der Haken wird um eine relative Hoehenangabe gehoben.

        :param hoehe: Die Anzahl an Einheiten, um die der Haken gehoben wird
        :return: Die aktualisierte Hoehe des Hakens
        """
        if hoehe <= 0:
            raise BasLogicError(f'Hoehe muss positiv sein!')

        if (self.haken_hoehe + hoehe) > self.hoehe:
            raise BasLogicError(f'Die Hoehe des Hakens darf die Hoehe des Krans nicht ueberschreiten!')

        self.haken_hoehe = self.haken_hoehe + hoehe

        bauteil_name = None
        if self.haken_bauteil is not None:
            bauteil_name = self.haken_bauteil.name

        self.visualisiere_hebe_um(hoehe, bauteil_name)

        return self.haken_hoehe

    def berechne_koordinaten_aus_kranposition(self, laufkatze_entfernung: float, winkel: float,
                                              haken_hoehe: float) -> tuple[int, int, int]:
        """
        Die Position des Hakens im Koordinatensystem wird aus der Ausrichtung des Krans berechnet.

        :param laufkatze_entfernung: Die Entfernung der Laufkatze vom Kranmast
        :param winkel: Der Winkel des Krans relativ zum Ausgangswinkel
        :param haken_hoehe: Die Hoehe des Hakens
        :return:
        """
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

    def berechne_hakenposition_aus_koordinaten(self, haken_x: int, haken_y: int,
                                               haken_z: int) -> tuple[float, float, float]:
        """
        Die Ausrichtung die der Kran annehmen muss, um den Haken an einen bestimmten Punkt im Koordinatensystem
        zu bringen, wird berechnet.

        :param haken_x: Koordinate x
        :param haken_y: Koordinate y
        :param haken_z: Koordinate z
        :return: Die Entfernung der Laufkatze vom Mast, der Winkel relativ zum Ausgangswinkel und die Hoehe des Hakens
        """
        x_normiert = haken_x - self.position_x
        y_normiert = haken_y - self.position_y

        # Berechnung: Abstand zwischen zwei Punkten, Rasterversatz kuerzt sich raus
        laufkatze_entfernung = math.sqrt(
            math.pow(self.position_x - haken_x, 2)
            + math.pow(self.position_y - haken_y, 2)
        )

        if laufkatze_entfernung > self.ausladung:
            raise BasLogicError(f'Das Bauteil an Position ({haken_x}, {haken_y}, {haken_z}) '
                                f'liegt ausserhalb der Reichweite des Krans!')

        # Berechnung: Winkel im Dreieck aus Hypotenuse und Ankathete
        winkel = math.degrees(math.acos(x_normiert / laufkatze_entfernung))

        if y_normiert < 0:
            winkel = 0 - winkel

        haken_hoehe = haken_z

        return laufkatze_entfernung, winkel, haken_hoehe

    def _do_nothing(self, *args: Any) -> None:
        """
        Platzhalter-Funktion für den Fall, dass keine Visualisierung des Krans benoetigt wird.
        Diese Funktion tut nichts.

        :param args: Beliebige Parameter, die ignoriert werden
        """
        pass
