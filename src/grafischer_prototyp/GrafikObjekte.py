from vpython import *

class GrafikBauteil:
    """
        Notes:
        Diese Klasse erzeugt ein für den Nutzer sichtbares Bauteil, was vom Kran bewegt werden kann.
    """
    def erzeuge_bauteil(self,name, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        bauteil_position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)
        self.name = name
        self.bauteil = box(pos=bauteil_position, color=vector(0, 0, 0), opacity=0.8)

    def erhalte_position(self):
        return self.bauteil.pos

    def erhalte_bauteil(self):
        return self.bauteil

class GrafikHindernis:
    """
        Notes:
        Diese Klasse erzeugt ein für den Nutzer sichtbares Hindernis, was vom Kran nicht bewegt werden soll.
    """
    def erzeuge_hindernis(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        bauteil_position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)
        self.hindernis = box(pos=bauteil_position, color=vector(1, 0, 1), opacity=0.8)

    def erhalte_position(self):
        return self.hindernis.pos

    def erhalte_hindernis(self):
        return self.hindernis

class GrafikPosition:
    """
        Notes:
        Diese Klasse erzeugt ein unsichtbares Positionsobjekt, welches an Kranbefehle übergeben werden kann,
        damit diese Befehle wissen, wohin Ausleger,Greifarm und Laufkatze sich hinbewegen sollen.
    """
    def erzeuge_position(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        self.position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)

    def erhalte_position(self):
        return self.position