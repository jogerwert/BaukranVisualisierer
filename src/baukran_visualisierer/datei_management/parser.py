import re
from typing import TextIO

from baukran_visualisierer.exceptions.bas_parser_error import BasParserError
from baukran_visualisierer.model.anweisungen.bewegunsanweisung import Bewegungsanweisung
from baukran_visualisierer.model.anweisungen.hakenhandlung import Hakenhandlung
from baukran_visualisierer.model.anweisungen.montageanweisung import Montageanweisung
from baukran_visualisierer.model.baufeld import Baufeld
from baukran_visualisierer.model.baustelle import Baustelle
from baukran_visualisierer.model.bauteil import Bauteil
from baukran_visualisierer.model.gegenstand import Gegenstand
from baukran_visualisierer.model.kran import Kran
from baukran_visualisierer.datei_management import regulaere_ausdruecke


def _parse_zeile(zeile: str, regex_dict: dict) -> tuple[str, re.Match] | tuple[None, None]:
    """
    Ueberprueft eine Zeile auf das Vorkommen von regulaeren Ausdruecken.
    
    :param zeile: Die Zeile, die geparst werden soll.
    :param regex_dict: Die regulaeren Ausdruecke, die ueberprueft werden sollen.
    :return: Schluessel und Match des ersten gefunden regulaeren Ausdrucks oder None und None, falls kein regulaerer
             Ausdruck gematcht werden konnte.
    """
    for key, regex in regex_dict.items():
        match_regex = regex.match(zeile)
        if match_regex:
            return key, match_regex

    return None, None


def parse_baustelle(dateipfad: str) -> Baustelle:
    """
    Oeffnet die Datei zum gegebenen Dateipfad und parst aus der Datei ein Baustellen-Objekt.
    
    :param dateipfad: Der Dateipfad zur Datei.
    :return: Das geparste Baustellenobjekt.
    """

    with open(dateipfad, mode="r") as datei:
        baustelle = _parse_baustelle(datei)

    return baustelle


def _parse_baustelle(datei: TextIO) -> Baustelle:
    """
    Parst die erste gefundene Baustelle aus einer Datei.

    :param datei: Die zu parsende Datei.
    :return: Das Obekt der Baustelle.
    """
    zeile = datei.readline()

    while zeile:
        key, match_regex = _parse_zeile(zeile, regulaere_ausdruecke.baustelle_regex_dict)

        if key == 'baustelle':
            name = match_regex.group('name')

            baufeld, kran, gegenstaende, bauteile_dict, montageanweisungen = _parse_komponenten(datei)
            bauteile = list(bauteile_dict.values())

            baustelle = Baustelle(name, baufeld, kran, gegenstaende, bauteile, montageanweisungen)
            return baustelle

        elif key == 'kommentar':
            pass

        elif key == 'leere_zeile':
            pass

        elif key == 'mehrzeiliger_kommentar':
            _parse_kommentar(datei)

        else:
            raise BasParserError('Es muss zuerst eine Baustelle definiert werden!')

        zeile = datei.readline()


def _parse_komponenten(datei: TextIO) -> tuple[Baufeld, Kran, list[Gegenstand], dict[Bauteil], list[Montageanweisung]]:
    """
    Parst die Komponenten fuer eine Baustelle.

    :param datei: Die zu parsende Datei.
    :return: Die Objekte fuer die Komponenten.
    """
    baufeld = None
    kran = None
    gegenstaende = []
    bauteile_dict = {}
    montageanweisungen = []

    zeile = datei.readline()
    while zeile:
        key, match_regex = _parse_zeile(zeile, regulaere_ausdruecke.komponenten_regex_dict)

        if key == 'baufeld':
            x = int(match_regex.group('x'))
            y = int(match_regex.group('y'))

            baufeld = Baufeld(x, y)

        elif key == 'gegenstand':
            pos_x = int(match_regex.group('x'))
            pos_y = int(match_regex.group('y'))
            pos_z = int(match_regex.group('z'))

            gegenstand = Gegenstand(pos_x, pos_y, pos_z)
            gegenstaende.append(gegenstand)

        elif key == 'kran':
            pos_x = int(match_regex.group('x'))
            pos_y = int(match_regex.group('y'))
            hoehe = int(match_regex.group('hoehe'))
            ausladung = int(match_regex.group('ausladung'))

            kran = Kran(pos_x, pos_y, hoehe, ausladung)

        elif key == 'bauteil':
            name = match_regex.group('name')
            pos_x = int(match_regex.group('x'))
            pos_y = int(match_regex.group('y'))
            pos_z = int(match_regex.group('z'))

            bauteil = Bauteil(name, pos_x, pos_y, pos_z)
            bauteile_dict[name] = bauteil

        elif key == 'montageanweisung':
            bauteil_name = match_regex.group('name')
            bauteil = bauteile_dict[bauteil_name]
            krananweisungen = _parse_krananweisungen(datei, kran)

            montageanweisung = Montageanweisung(bauteil, kran, krananweisungen)
            montageanweisungen.append(montageanweisung)

        elif key == 'kommentar':
            pass

        elif key == 'leere_zeile':
            pass

        elif key == 'mehrzeiliger_kommentar':
            _parse_kommentar(datei)

        elif key == 'ende_komponenten':
            return baufeld, kran, gegenstaende, bauteile_dict, montageanweisungen

        else:
            raise BasParserError('Es wurde versucht eine ungueltige Komponente zu definieren!')

        zeile = datei.readline()


def _parse_krananweisungen(datei: TextIO, kran: Kran) -> list[Hakenhandlung | Bewegungsanweisung]:
    """
    Parst die Krananweisungen, also Hakenhandlungen oder Bewegungsanweisungen, aus einer Datei.

    :param datei: Die zu parsende Datei.
    :param kran: Der Kran, zu dem die Anweisungen gehoeren.
    :return: Die Krananweisungen.
    """
    krananweisungen = []

    zeile = datei.readline()
    while zeile:
        key, match_regex = _parse_zeile(zeile, regulaere_ausdruecke.krananweisungen_regex_dict)

        if key == 'hebe_um':
            hoehe = int(match_regex.group('hoehe'))
            anweisung = Bewegungsanweisung(kran.hebe_um, hoehe)
            krananweisungen.append(anweisung)

        elif key == 'senke_um':
            hoehe = int(match_regex.group('hoehe'))
            anweisung = Bewegungsanweisung(kran.senke_um, hoehe)
            krananweisungen.append(anweisung)

        elif key == 'bringe_an':
            pos_x = int(match_regex.group('x'))
            pos_y = int(match_regex.group('y'))
            pos_z = int(match_regex.group('z'))
            anweisung = Bewegungsanweisung(kran.bringe_an, (pos_x, pos_y, pos_z))
            krananweisungen.append(anweisung)

        elif key == 'greife':
            anweisung = Hakenhandlung(kran.greife)
            krananweisungen.append(anweisung)

        elif key == 'richte_aus':
            anweisung = Hakenhandlung(kran.richte_aus)
            krananweisungen.append(anweisung)

        elif key == 'lasse_los':
            anweisung = Hakenhandlung(kran.lasse_los)
            krananweisungen.append(anweisung)

        elif key == 'kommentar':
            pass

        elif key == 'leere_zeile':
            pass

        elif key == 'mehrzeiliger_kommentar':
            _parse_kommentar(datei)

        elif key == 'ende_krananweisungen':
            return krananweisungen

        else:
            raise BasParserError('Es wurde versucht eine ungueltige Krananweisung zu definieren!')

        zeile = datei.readline()


def _parse_kommentar(datei: TextIO) -> None:
    """
    Parst so lange durch Zeilen, bis das Ende des Kommentars gefunden wurde.

    :param datei: Die zu parsende Datei.
    :return: None
    """
    zeile = datei.readline()

    while zeile:
        key, match_regex = _parse_zeile(zeile, regulaere_ausdruecke.kommentar_regex_dict)

        if key == 'kommentar_ende':
            return

        zeile = datei.readline()


