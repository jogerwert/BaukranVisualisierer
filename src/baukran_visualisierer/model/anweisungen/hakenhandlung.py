from typing import Callable


class Hakenhandlung:

    def __init__(self, kranfunktion: Callable) -> None:
        """
        Eine Anweisung fuer einen Baukran, die in einer Statusaenderung des Hakens resultiert.

        :param kranfunktion: Die Funktion des Krans, die ausgefuehrt wird.
        """
        self.kranfunktion = kranfunktion

    def ausfuehren(self) -> None:
        """
        Fuehrt die Kranfunktion der Hakenhandlung aus.
        """
        self.kranfunktion()
