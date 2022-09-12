from vpython import *

class GrafikBaufeld:
    def __init__(self):
        self.liste = []

    def erzeuge_baufeld(self, eingabe_laenge_baufeld, eingabe_breite_baufeld):
        laenge_baufeldteil = breite_baufeldteil = 1
        hoehe_baufeldteil = 0.1
        for x in range(0, eingabe_laenge_baufeld):
            for y in range(0, eingabe_breite_baufeld):
                if not x % 2 == 0:
                    if y % 2 == 0:
                        color_baufeld = vector(0.9, 0.9, 0.9)
                    else:
                        color_baufeld = vector(0.8, 0.8, 0.8)
                else:
                    if y % 2 == 1:
                        color_baufeld = vector(0.9, 0.9, 0.9)
                    else:
                        color_baufeld = vector(0.8, 0.8, 0.8)

                #box(pos=vector(x, -0.5, y), length=laenge_baufeldteil, width=breite_baufeldteil, height=hoehe_baufeldteil,
                #    color=color_baufeld)

                self.liste.append(box(pos=vector(x, -0.5, y), length=laenge_baufeldteil, width=breite_baufeldteil,
                                      height=hoehe_baufeldteil,color=color_baufeld))

    def erhalte_baufeld_liste(self):
        return self.liste

    def loesche_liste(self):
        while len(self.liste) > 0:
            self.liste.pop(0)