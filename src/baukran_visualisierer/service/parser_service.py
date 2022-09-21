from baukran_visualisierer.datei_management import parser
from baukran_visualisierer.model.baustelle import Baustelle


def parse_baustelle(eingabedatei: str) -> Baustelle:
    """
    Service-Funktion der Schichtenarchitektur, um das Parsen der Baustelle zu kapseln.

    :param eingabedatei: Der Pfad zur Datei, die geparst werden soll
    :return: Das geparste Baustellenobjekt
    """
    return parser.parse_baustelle(eingabedatei)
