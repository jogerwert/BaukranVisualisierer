from baukran_visualisierer.model.anweisungen.bewegunsanweisung import Bewegungsanweisung
from baukran_visualisierer.model.anweisungen.hakenhandlung import Hakenhandlung
from baukran_visualisierer.model.bauteil import Bauteil
from baukran_visualisierer.model.kran import Kran


class Montageanweisung:

    def __init__(self, bauteil: Bauteil, kran: Kran, krananweisungen: list[Hakenhandlung | Bewegungsanweisung]) -> None:
        """
        Sammlung an Anweisungen fuer einen Baukran, die dazu verwendet werden, ein Bauteil zu montieren.

        :param bauteil: Das zu montierende Bauteil.
        :param kran: Der Kran, der die Anweisung ausfuehrt.
        :param krananweisungen: Die Anweisungen, die ausgefuehrt werden sollen.
        """
        self.bauteil = bauteil
        self.kran = kran
        self.krananweisungen = krananweisungen
        self.krananweisungs_zaehler = 0

    def alle_krananweisungen_ausfuehren(self) -> int:
        """
        Fuehrt alle Krananweisungen der Montageanweisung aus.
        Falls bereits Krananweisungen partiell ausgefuehrt wurden, werden alle restlichen Anweisungen ausgefuehrt.

        :return: Der Krananweisungszaehler.
        """
        if self.krananweisungs_zaehler < len(self.krananweisungen):

            # Bereits durchgefuehrte Anweisungen werden nicht wiederholt
            krananweisungen = self.krananweisungen[self.krananweisungs_zaehler:]

            for anweisung in krananweisungen:
                anweisung.ausfuehren()
                self.krananweisungs_zaehler += 1

        return self.krananweisungs_zaehler

    def naechste_krananweisung_ausfuehren(self) -> int:
        """
        Fuehrt die naechste Krananweisung der Montageanweisung aus.

        :return: Der Krananweisungszaehler.
        """
        if self.krananweisungs_zaehler < len(self.krananweisungen):
            self.krananweisungen[self.krananweisungs_zaehler].ausfuehren()
            self.krananweisungs_zaehler += 1

        return self.krananweisungs_zaehler

    def pruefe_alle_anweisungen_ausgefuehrt(self) -> bool:
        """
        Prueft, ob alle Krananweisungen ausgefuehrt wurden.

        :return: True, falls alle Anweisungen ausgefuehrt, False sonst
        """
        if self.krananweisungs_zaehler >= len(self.krananweisungen):
            return True
        else:
            return False
