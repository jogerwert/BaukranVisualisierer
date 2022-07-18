from src.baukran_visualisierer.exceptions.logic_error import LogicError


class Baufeld:
    """Das Baufeld verkoerpert die statischen Inhalte der Baustelle, die aktuell nicht bewegt werden."""

    def __init__(self, laenge_x, breite_y):
        self.laenge_x = laenge_x
        self.breite_y = breite_y

        # Ein Dictionary wird verwendet, um ein dreidimensionales Koordinatensystem zu simulieren.
        self.inhalt = {}

    def platziere_baustellenobjekt(self, baustellen_objekt):
        # TODO: Testen

        x = baustellen_objekt.position_x
        y = baustellen_objekt.position_y
        z = baustellen_objekt.position_z

        if x < 0 or x >= self.laenge_x or y < 0 or y >= self.breite_y:
            raise LogicError(f'Ein Gegenstand wurde ausserhalb des Baufelds platziert!')

        if (x, y, z) in self.inhalt:
            raise LogicError(f'An der Koordinate ({x}, {y}, {z}) existiert bereits ein Gegenstand!')

        if baustellen_objekt is None:
            raise LogicError(f'Das zu platzierende Objekt besitzt keinen Inhalt!')

        self.inhalt[x, y, z] = baustellen_objekt

    def erhalte_baustellenobjekt(self, x, y, z):
        # TODO: Testen

        if x < 0 or x >= self.laenge_x or y < 0 or y >= self.breite_y:
            raise LogicError(f'Die Koordinate ({x}, {y}, {z}) liegt ausserhalb des Baufelds!')
        if (x, y, z) in self.inhalt:
            return self.inhalt[x, y, z]

        return None

    def entferne_baustellenobjekt(self, x, y, z):
        # TODO: Testen

        if (x, y, z) in self.inhalt:
            return self.inhalt.pop((x, y, z))

        return None

    def bewege_baustellenobjekt(self, x1, y1, z1, x2, y2, z2):
        # TODO: Testen

        if self.erhalte_baustellenobjekt(x1, y1, z1) is None:
            raise LogicError(f'An der Koordinate ({x1}, {y1}, {z1}) existiert kein Gegenstand!')

        baustellen_objekt = self.erhalte_baustellenobjekt(x1, y1, z1)

        baustellen_objekt.position_x = x2
        baustellen_objekt.position_y = y2
        baustellen_objekt.position_z = z2

        self.entferne_baustellenobjekt(x1, y1, z1)

        self.platziere_baustellenobjekt(baustellen_objekt)

        return baustellen_objekt
