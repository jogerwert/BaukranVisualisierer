from src.baukran_visualisierer.exceptions.logic_error import LogicError


class Bewegungsanweisung:

    def __init__(self, kranfunktion, parameter):
        self.kranfunktion = kranfunktion
        self.parameter = parameter

    def ausfuehren(self):

        # Funktion ausfuehren, wenn Hoehe vorhanden
        if isinstance(self.parameter, int):
            self.kranfunktion(self.parameter)
            return

        # Ausfuehren, wenn alle Koordinaten vorhanden
        if isinstance(self.parameter, tuple) and len(self.parameter) == 3:
            self.kranfunktion(self.parameter[0], self.parameter[1], self.parameter[2])
            return

        # Fehler, falls irgendwas durch die Bedingungen rutscht
        raise LogicError(f'Ein undefiniertes Verhalten wurde bei einer Bewegungsanweisung festgestellt! '
                         f'Bitte kontaktieren Sie einen Verantwortlichen.')
