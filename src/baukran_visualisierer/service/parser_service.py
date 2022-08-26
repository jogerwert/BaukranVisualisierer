from src.baukran_visualisierer.model.anweisungen.bewegunsanweisung import Bewegungsanweisung
from src.baukran_visualisierer.model.anweisungen.hakenhandlung import Hakenhandlung
from src.baukran_visualisierer.model.anweisungen.montageanweisung import Montageanweisung
from src.baukran_visualisierer.model.baufeld import Baufeld
from src.baukran_visualisierer.model.baustelle import Baustelle
from src.baukran_visualisierer.model.bauteil import Bauteil
from src.baukran_visualisierer.model.gegenstand import Gegenstand
from src.baukran_visualisierer.model.kran import Kran

from src.baukran_visualisierer.parser import parser


def parse_baustelle(eingabedatei):
    return parse_baustelle(eingabedatei)


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

    krananweisungen_basis_rechts = [
        Bewegungsanweisung(kran.bringe_an, (1, 2, 0)),
        Hakenhandlung(kran.greife),
        Bewegungsanweisung(kran.hebe_um, 2),
        Bewegungsanweisung(kran.bringe_an, (6, 2, 2)),
        Bewegungsanweisung(kran.senke_um, 2),
        Hakenhandlung(kran.richte_aus),
        Hakenhandlung(kran.lasse_los)
    ]
    krananweisungen_basis_links = [
        Bewegungsanweisung(kran.hebe_um, 2),
        Bewegungsanweisung(kran.bringe_an, (0, 2, 2)),
        Bewegungsanweisung(kran.senke_um, 2),
        Hakenhandlung(kran.greife),
        Bewegungsanweisung(kran.hebe_um, 2),
        Bewegungsanweisung(kran.bringe_an, (5, 2, 2)),
        Bewegungsanweisung(kran.senke_um, 2),
        Hakenhandlung(kran.richte_aus),
        Hakenhandlung(kran.lasse_los)
    ]
    krananweisungen_dach = [
        Bewegungsanweisung(kran.hebe_um, 2),
        Bewegungsanweisung(kran.bringe_an, (2, 2, 2)),
        Bewegungsanweisung(kran.senke_um, 2),
        Hakenhandlung(kran.greife),
        Bewegungsanweisung(kran.hebe_um, 2),
        Bewegungsanweisung(kran.bringe_an, (6, 2, 2)),
        Bewegungsanweisung(kran.senke_um, 1),
        Hakenhandlung(kran.richte_aus),
        Hakenhandlung(kran.lasse_los)
    ]
    montageanweisungen = [Montageanweisung(bauteile[1], kran, krananweisungen_basis_rechts),
                          Montageanweisung(bauteile[0], kran, krananweisungen_basis_links),
                          Montageanweisung(bauteile[2], kran, krananweisungen_dach)]

    baustelle = Baustelle(name, baufeld, kran, gegenstaende, bauteile, montageanweisungen)

    return baustelle
