from tests.modellierungs_tests import beispiel_baustellen


def test():
    baustelle = beispiel_baustellen.erstelle_beispiel_baustelle()
    kran = baustelle.kran
    kran.bringe_an(1, 2, 3)
