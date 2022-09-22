from baukran_visualisierer.exceptions.bas_logic_error import BasLogicError
from baukran_visualisierer.model.bauteil import Bauteil
from baukran_visualisierer.model.gegenstand import Gegenstand
from baukran_visualisierer.model.kran import Kran


class Baufeld:

    def __init__(self, laenge_x: int, breite_y: int) -> None:
        """
        Das Baufeld verkoerpert die statischen Inhalte der Baustelle, die aktuell nicht bewegt werden.
        Der Kran, Bauteile und Gegenstaende werden in einem dreidimensionalen Koordinatensystem platziert, das durch
        ein Dictionary mit den Koordinaten als Schluessel repraesentiert wird.

        :param laenge_x: Laenge des Baufelds
        :param breite_y: Breite des Baufelds
        """
        self.laenge_x = laenge_x
        self.breite_y = breite_y

        # Ein Dictionary wird verwendet, um ein dreidimensionales Koordinatensystem zu simulieren.
        self.inhalt = {}

    def platziere_baustellenobjekt(self, baustellen_objekt: Kran | Bauteil | Gegenstand) -> None:
        """
        Platziert ein Objekt mit x, y und z Koordinaten im Baufeld.
        Dies ist ueblicherweise ein Kran, ein Bauteil oder ein Gegenstand.

        :param baustellen_objekt: Das zu platzierende Objekt.
        """

        x = baustellen_objekt.position_x
        y = baustellen_objekt.position_y
        z = baustellen_objekt.position_z

        if x < 0 or x >= self.laenge_x or y < 0 or y >= self.breite_y:
            raise BasLogicError(f'Ein Gegenstand wurde ausserhalb des Baufelds platziert!')

        if (x, y, z) in self.inhalt:
            raise BasLogicError(f'An der Koordinate ({x}, {y}, {z}) existiert bereits ein Gegenstand!')

        if baustellen_objekt is None:
            raise BasLogicError(f'Das zu platzierende Objekt besitzt keinen Inhalt!')

        self.inhalt[x, y, z] = baustellen_objekt

    def erhalte_baustellenobjekt(self, x: int, y: int, z: int) -> Kran | Bauteil | Gegenstand | None:
        """
        Ruft den Inhalt der gewuenschten Koordinate ab und gibt diesen zurueck.
        Inhalte sind ueblicherweise der Kran, ein Bauteil oder ein Gegenstand.

        :param x: Koordinate x
        :param y: Koordinate y
        :param z: Koordinate z
        :return: Der Inhalt der Koordinate; None falls die Koordinate leer ist.
        """

        if x < 0 or x >= self.laenge_x or y < 0 or y >= self.breite_y:
            raise BasLogicError(f'Die Koordinate ({x}, {y}, {z}) liegt ausserhalb des Baufelds!')
        if (x, y, z) in self.inhalt:
            return self.inhalt[x, y, z]

        return None

    def entferne_baustellenobjekt(self, x: int, y: int, z: int) -> Kran | Bauteil | Gegenstand | None:
        """
        Entfernt den Inhalt an der gewuenschten Koordinate und gibt diesen zurueck.
        Inhalte sind ueblicherweise der Kran, ein Bauteil oder ein Gegenstand.

        :param x: Koordinate x
        :param y: Koordinate y
        :param z: Koordinate z
        :return: Der Inhalt der Koordinate; None falls die Koordinate leer ist.
        """

        if (x, y, z) in self.inhalt:
            return self.inhalt.pop((x, y, z))

        return None
