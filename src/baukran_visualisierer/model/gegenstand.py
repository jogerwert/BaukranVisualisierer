
class Gegenstand:

    def __init__(self, position_x: int, position_y: int, position_z: int) -> None:
        """
        Klasse fuer einen Gegenstand auf einer Baustelle.
        Gegenstaende sind keine Bauteile und stellen Hindernisse dar, die die Bewegung des Krans einschraenken.

        :param position_x: Koordinate x
        :param position_y: Koordinate y
        :param position_z: Koordinate z
        """
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
