import getopt
import sys

from src.baukran_visualisierer.parser import parser


def parse_baustelle(dateipfad):
    baustelle = parser.parse_baustelle(dateipfad)
    return baustelle


def start_cmd(eingabedatei):
    baustelle = parse_baustelle(eingabedatei)


def main(argv):
    eingabedatei = ''

    try:
        opts, args = getopt.getopt(argv, "hi:", ["input="])
    except getopt.GetoptError:
        print("Bitte Eingabeparameter ueberpruefen. Hilfestellung mit der Option -h verfuegbar.")
        sys.exit(2)

    if len(opts) == 0:
        opts.append(("-h", ""))

    for opt, arg in opts:
        match opt:
            case '-h':
                print("main.py -i <Eingabedatei>")
                sys.exit()
            case '-i' | '--input':
                eingabedatei = arg
            case _:
                print(f'Unbekannte Option "{opt}" wurde gefunden.')
                sys.exit(2)

    start_cmd(eingabedatei)


if __name__ == '__main__':
    main(sys.argv[1:])
