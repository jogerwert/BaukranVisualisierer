from src.baukran_visualisierer.service import parser_service


def test():
    baustelle = parser_service.erstelle_beispiel_baustelle()
    kran = baustelle.kran
    kran.bringe_an(1, 2, 3)
