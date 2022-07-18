from src.baukran_visualisierer.model.baufeld import Baufeld
from src.baukran_visualisierer.model.baustelle import Baustelle
from src.baukran_visualisierer.model.bauteil import Bauteil
from src.baukran_visualisierer.model.gegenstand import Gegenstand
from src.baukran_visualisierer.model.kran import Kran


def erstelle_beispiel_baustelle():
    name = "HTWSaar"
    # (laenge, breite)
    baufeld = Baufeld(10, 5)
    # (x, y, hoehe, ausladung)
    kran = Kran(0, 0, 5, 10)

    # (x, y, z)
    gegenstaende = [Gegenstand(3, 2, 0),
                    Gegenstand(3, 2, 1)]

    # (x, y, z)
    bauteile = [Bauteil("BasisLinks", 0, 2, 0),
                Bauteil("BasisRechts", 1, 2, 0),
                Bauteil("Dach", 2, 2, 0)]

    # TODO: Montageanweisungen
    montageanweisungen = []

    baustelle = Baustelle(name, baufeld, kran, gegenstaende, bauteile, montageanweisungen)

    return baustelle
