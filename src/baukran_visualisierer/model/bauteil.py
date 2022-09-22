
class Bauteil:

    def __init__(self, name: str, position_x: int, position_y: int, position_z: int) -> None:
        """
        Klasse für ein Bauteil auf einer Baustelle.
        Die Bauteile sind die Gegenstaende, die vom Kran bewegt werden sollen.

        :param name: Name des Bauteils
        :param position_x: Koordinate x
        :param position_y: Koordinate y
        :param position_z: Koordinate z
        """
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z
