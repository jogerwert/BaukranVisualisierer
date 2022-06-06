from src.baukran_visualisierer.model.baufeld import Baufeld
from src.baukran_visualisierer.model.baustelle import Baustelle
from src.baukran_visualisierer.model.bauteil import Bauteil
from src.baukran_visualisierer.model.gegenstand import Gegenstand
from src.baukran_visualisierer.model.kran import Kran

import src.baukran_visualisierer.parameter.variablen_beispiel as var


def erstelle_beispiel_baustelle():
    name = var.baustelle_name
    baufeld = Baufeld(var.baufeld_tupel[0], var.baufeld_tupel[1])
    kran = Kran(var.kran_tupel[0], var.kran_tupel[1], var.kran_tupel[2], var.kran_tupel[3], var.kran_tupel[4])

    gegenstaende = [Gegenstand(var.gegenstand_1_tupel[0], var.gegenstand_1_tupel[1], var.gegenstand_1_tupel[2]),
                    Gegenstand(var.gegenstand_2_tupel[0], var.gegenstand_2_tupel[1], var.gegenstand_2_tupel[2])]

    bauteile = [Bauteil(var.bauteil_1_tupel[0], var.bauteil_1_tupel[1], var.bauteil_1_tupel[2], var.bauteil_1_tupel[3]),
                Bauteil(var.bauteil_2_tupel[0], var.bauteil_2_tupel[1], var.bauteil_2_tupel[2], var.bauteil_2_tupel[3]),
                Bauteil(var.bauteil_3_tupel[0], var.bauteil_3_tupel[1], var.bauteil_3_tupel[2], var.bauteil_3_tupel[3]),
                Bauteil(var.bauteil_4_tupel[0], var.bauteil_4_tupel[1], var.bauteil_4_tupel[2], var.bauteil_4_tupel[3]),
                Bauteil(var.bauteil_5_tupel[0], var.bauteil_5_tupel[1], var.bauteil_5_tupel[2], var.bauteil_5_tupel[3]),
                Bauteil(var.bauteil_6_tupel[0], var.bauteil_6_tupel[1], var.bauteil_6_tupel[2], var.bauteil_6_tupel[3])]

    montageanweisungen = []

    baustelle = Baustelle(name, baufeld, kran, gegenstaende, bauteile, montageanweisungen)

    return baustelle
