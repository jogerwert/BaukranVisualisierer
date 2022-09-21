from typing import Callable

from baukran_visualisierer.exceptions.bas_logic_error import BasLogicError


class Bewegungsanweisung:

    def __init__(self, kranfunktion: Callable, parameter: int | tuple[int, int, int]) -> None:
        """
        Eine Anweisung fuer einen Baukran, die in einer Bewegung des Kranarms resultiert.

        :param kranfunktion: Die Funktion des Krans, die ausgefuehrt wird
        :param parameter: Die Parameter, mit denen die Kranfunktion ausgefuehrt wird
        """
        self.kranfunktion = kranfunktion
        self.parameter = parameter

    def ausfuehren(self) -> None:
        """
        Fuehrt die Kranfunktion der Bewegungsanweisung mit den Parametern aus.

        :return: None
        """
        # Funktion ausfuehren, wenn Hoehe vorhanden
        if isinstance(self.parameter, int):
            self.kranfunktion(self.parameter)
            return

        # Ausfuehren, wenn alle Koordinaten vorhanden
        if isinstance(self.parameter, tuple) and len(self.parameter) == 3:
            self.kranfunktion(self.parameter[0], self.parameter[1], self.parameter[2])
            return

        # Fehler, falls irgendwas durch die Bedingungen rutscht
        raise BasLogicError(f'Ein undefiniertes Verhalten wurde bei einer Bewegungsanweisung festgestellt! '
                            f'Bitte kontaktieren Sie einen Verantwortlichen.')
