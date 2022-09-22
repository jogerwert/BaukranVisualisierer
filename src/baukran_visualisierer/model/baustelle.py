import weakref

from baukran_visualisierer.model.anweisungen.montageanweisung import Montageanweisung
from baukran_visualisierer.model.baufeld import Baufeld
from baukran_visualisierer.model.bauteil import Bauteil
from baukran_visualisierer.model.gegenstand import Gegenstand
from baukran_visualisierer.model.kran import Kran


class Baustelle:

    def __init__(self, name: str, baufeld: Baufeld, kran: Kran, gegenstaende: list[Gegenstand],
                 bauteile: list[Bauteil], montageanweisungen: list[Montageanweisung]) -> None:
        """
        Die Baustelle mit allen Objekten und Anweisungen.

        :param name: Name der Baustelle
        :param baufeld: Das Baufeld
        :param kran: Der Kran
        :param gegenstaende: Die Liste mit allen Gegenstaenden
        :param bauteile: Die Liste mit allen Bauteilen
        :param montageanweisungen: Die Liste mit allen Montageanweisungen
        """
        self.name = name
        self.baufeld = baufeld

        self.kran = kran
        baufeld.platziere_baustellenobjekt(kran)
        kran.baustelle = weakref.proxy(self)

        self.gegenstaende = gegenstaende
        for gegenstand in gegenstaende:
            baufeld.platziere_baustellenobjekt(gegenstand)

        self.bauteile = bauteile
        for bauteil in bauteile:
            baufeld.platziere_baustellenobjekt(bauteil)

        self.montageanweisungen = montageanweisungen
        self.montageanweisungs_zaehler = 0

    def alle_montageanweisungen_ausfuehren(self) -> None:
        """
        Fuehrt alle Montageanweisungen aus.
        Falls bereits Montageanweisungen oder Krananweisungen partiell ausgefuehrt wurden, werden alle restlichen
        Anweisungen ausgefuehrt.
        """
        if self.montageanweisungs_zaehler < len(self.montageanweisungen):

            # Bereits durchgefuehrte Anweisungen werden nicht wiederholt
            montageanweisungen = self.montageanweisungen[self.montageanweisungs_zaehler:]

            for anweisung in montageanweisungen:
                anweisung.alle_krananweisungen_ausfuehren()
                self.montageanweisungs_zaehler += 1

    def naechste_montageanweisung_ausfuehren(self) -> None:
        """
        Fuehrt die naechste Montageanweisung aus.
        Falls bereits Krananweisungen der Montageanweisung partiell ausgefuehrt wurden, wird der Rest der begonnenen
        Montageanweisung ausgefuehrt.
        """
        if self.montageanweisungs_zaehler < len(self.montageanweisungen):
            self.montageanweisungen[self.montageanweisungs_zaehler].alle_krananweisungen_ausfuehren()
            self.montageanweisungs_zaehler += 1

    def naechste_krananweisung_ausfuehren(self) -> None:
        """
        Fuehrt die naechste Krananweisung aus.
        """
        if self.montageanweisungs_zaehler < len(self.montageanweisungen):
            anweisung = self.montageanweisungen[self.montageanweisungs_zaehler]
            anweisung.naechste_krananweisung_ausfuehren()
            if anweisung.pruefe_alle_anweisungen_ausgefuehrt():
                self.montageanweisungs_zaehler += 1

    def platziere_baustellenobjekt(self, baustellenobjekt: Kran | Bauteil | Gegenstand) -> None:
        """
        Platziert ein Baustellenobjekt.
        Dies ist ueblicherweise der Kran, ein Bauteil oder ein Gegenstand.

        :param baustellenobjekt: Das zu platzierende Baustellenobjekt.
        """
        self.baufeld.platziere_baustellenobjekt(baustellenobjekt)

    def erhalte_baustellenobjekt(self, x: int, y: int, z: int) -> Kran | Bauteil | Gegenstand:
        """
        Ruft den Inhalt der gewuenschten Koordinate ab und gibt diesen zurueck.
        Inhalte sind ueblicherweise der Kran, ein Bauteil oder ein Gegenstand.

        :param x: Koordinate x
        :param y: Koordinate y
        :param z: Koordinate z
        :return: Der Inhalt der Koordinate; None falls die Koordinate leer ist.
        """
        return self.baufeld.erhalte_baustellenobjekt(x, y, z)

    def entferne_baustellenobjekt(self, x: int, y: int, z: int) -> Kran | Bauteil | Gegenstand:
        """
        Entfernt den Inhalt an der gewuenschten Koordinate und gibt diesen zurueck.
        Inhalte sind ueblicherweise der Kran, ein Bauteil oder ein Gegenstand.

        :param x: Koordinate x
        :param y: Koordinate y
        :param z: Koordinate z
        :return: Der Inhalt der Koordinate; None falls die Koordinate leer ist.
        """
        baustellen_objekt = self.baufeld.entferne_baustellenobjekt(x, y, z)
        return baustellen_objekt

    def pruefe_koordinate_leer(self, x: int, y: int, z: int) -> bool:
        """
        Prueft ob eine bestimmte Koordinate leer ist.

        :param x: Koordinate x
        :param y: Koordinate y
        :param z: Koordinate z
        :return: True, falls die Koordinate leer ist, False sonst
        """
        if self.baufeld.erhalte_baustellenobjekt(x, y, z) is None:
            return True
        else:
            return False
