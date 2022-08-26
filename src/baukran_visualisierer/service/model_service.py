import src.baukran_visualisierer.service.parser_service as parser_service


def parse_baustelle(eingabedatei):
    return parser_service.parse_baustelle(eingabedatei)


def erstelle_beispiel_baustelle():
    return parser_service.erstelle_beispiel_baustelle()
