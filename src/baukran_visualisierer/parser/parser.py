from src.baukran_visualisierer.exceptions.bas_parser_error import BasParserError
from src.baukran_visualisierer.model.anweisungen.bewegunsanweisung import Bewegungsanweisung
from src.baukran_visualisierer.model.anweisungen.hakenhandlung import Hakenhandlung
from src.baukran_visualisierer.model.anweisungen.montageanweisung import Montageanweisung
from src.baukran_visualisierer.model.baufeld import Baufeld
from src.baukran_visualisierer.model.baustelle import Baustelle
from src.baukran_visualisierer.model.bauteil import Bauteil
from src.baukran_visualisierer.model.gegenstand import Gegenstand
from src.baukran_visualisierer.model.kran import Kran
from src.baukran_visualisierer.parser import regulaere_ausdruecke


def _parse_zeile(zeile, regex_dict):

    for key, regex in regex_dict.items():
        match_regex = regex.match(zeile)
        if match_regex:
            return key, match_regex

    return None, None


def parse_baustelle(dateipfad):
    baustelle = None

    with open(dateipfad, mode="r") as datei:
        baustelle = _parse_baustelle(datei)

    return baustelle


def _parse_baustelle(datei):
    zeile = datei.readline()

    baustelle = None
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


def _parse_komponenten(datei):
    baufeld = None
    kran = None
    gegenstaende = []
    bauteile_dict = {}
    montageanweisungen = []

    zeile = datei.readline()
    while zeile:
        key, match_regex = _parse_zeile(zeile, regulaere_ausdruecke.komponenten_regex_dict)

        if key == 'baufeld':
            breite = int(match_regex.group('breite'))
            laenge = int(match_regex.group('laenge'))

            baufeld = Baufeld(laenge, breite)

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


def _parse_krananweisungen(datei, kran):
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


def _parse_kommentar(datei):
    zeile = datei.readline()

    while zeile:
        key, match_regex = _parse_zeile(zeile, regulaere_ausdruecke.kommentar_regex_dict)

        if key == 'kommentar_ende':
            return

        zeile = datei.readline()


