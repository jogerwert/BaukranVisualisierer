from src.baukran_visualisierer.exceptions.logic_error import LogicError


class Bewegungsanweisung:

    def __init__(self, name, kran, kranfunktion, hoehe=None, x=None, y=None, z=None):
        self.name = name
        self.kran = kran
        self.kranfunktion = kranfunktion
        self.hoehe = hoehe
        self.x = x
        self.y = y
        self.z = z

    def ausfuehren(self):
        # Fehler, wenn keine Argumente zugewiesen wurden
        if self.hoehe is None and self.x is None and self.y is None and self.z is None:
            raise LogicError(f'Der Bewegungsanweisung "{self.name}" wurden keine Argumente zugewiesen!')

        # Fehler, wenn zu viele Argumente zugewiesen wurden
        if self.hoehe is not None and (self.x is not None or self.y is not None or self.z is not None):
            raise LogicError(f'Der Bewegungsanweisung "{self.name}" wurden sowohl eine Hoehe als auch eine '
                             f'Koordinate zugewiesen!')

        # Funktion ausfuehren, wenn Hoehe vorhanden
        if self.hoehe is not None:
            self.kran.kranfunktion(self.hoehe)

        # Fehler, wenn nicht alle Koordinaten vorhanden sind
        if self.x is None or self.y is None or self.z is None:
            raise LogicError(f'Der Bewegungsanweisung "{self.name}" wurden nicht genuegend Koordinaten '
                             f'zugewiesen, um eine Position definieren zu koennen!')

        # Ausfuehren, wenn alle Koordinaten vorhanden
        if self.x is not None and self.y is not None and self.z is not None:
            self.kran.kranfunktion(self.x, self.y, self.z)

        # Fehler, falls irgendwas durch die Bedingungen rutscht
        raise RuntimeError(f'Ein undefiniertes Verhalten wurde bei der Bewegungsanweisung "{self.name}" '
                           f'festgestellt! Bitte kontaktieren Sie einen Verantwortlichen.')

