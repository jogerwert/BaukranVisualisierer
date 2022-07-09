from vpython import *

class GrafikBauteil:
    def erzeuge_bauteil(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        bauteil_position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)
        self.bauteil = box(pos=bauteil_position, color=vector(0, 0, 0), opacity=0.8)

    def erhalte_position(self):
        return self.bauteil.pos

class GrafikHindernis:
    def erzeuge_hindernis(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        bauteil_position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)
        self.hindernis = box(pos=bauteil_position, color=vector(1, 0, 1), opacity=0.8)

    def erhalte_position(self):
        return self.hindernis

class GrafikPosition:
    def erzeuge_position(self, eingabe_position_wert_x, eingabe_position_wert_y, eingabe_position_wert_z):
        self.position = vector(eingabe_position_wert_x, eingabe_position_wert_z, eingabe_position_wert_y)

    def erhalte_position(self):
        return self.position