import getopt
import sys

from baukran_visualisierer.datei_management import file_picker
from baukran_visualisierer.service import visualisierungs_service, parser_service


def parse_baustelle(dateipfad):
    baustelle = parser_service.parse_baustelle(dateipfad)
    return baustelle


def start_file_picker():
    dateiname = file_picker.file_picker()
    start_visualisierung(dateiname)


def start_visualisierung(eingabedatei):
    baustelle = parse_baustelle(eingabedatei)
    visualisierungs_service.setze_visualisierungs_funktionen(baustelle)
    visualisierungs_service.visualisiere_baustelle(baustelle)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:", ["input="])
    except getopt.GetoptError:
        print("Bitte Eingabeparameter ueberpruefen. Hilfestellung mit der Option -h verfuegbar.")
        sys.exit(2)

    if len(opts) == 0:
        start_file_picker()

    for opt, arg in opts:
        match opt:
            case '-h':
                print("main.py -i <Eingabedatei>")
                sys.exit()
            case '-i' | '--input':
                eingabedatei = arg
                start_visualisierung(eingabedatei)
            case _:
                print(f'Unbekannte Option "{opt}" wurde gefunden.')
                sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])
