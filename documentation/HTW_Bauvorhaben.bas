Baustelle HTWSaar {
    # Baufeld
    Baufeld : Abmessung(10, 5)
    # Gegenstaende
    Gegenstand : Position(3, 2, 0)
    Gegenstand : Position(3, 2, 1)
    # Kran
    Kran : Position(0, 0) Hoehe 5 Ausladung 10
    # Bauteile
    Bauteil BasisLinks : Position(0, 2, 0)
    Bauteil BasisRechts : Position(1, 2, 0)
    Bauteil Dach : Position(2, 2, 0)
    # Montageanweisungen
    montiere BasisRechts {
        bringe an Position(1, 2, 0)
        greife
        hebe um 2
        bringe an Position(6, 2, 2)
        senke um 2
        richte aus
        lasse los
    }
    montiere BasisLinks {
        hebe um 2
        bringe an Position(0, 2, 2)
        senke um 2
        greife
        hebe um 2
        bringe an Position(5, 2, 2)
        senke um 2
        richte aus
        lasse los
    }
    montiere Dach {
        hebe um 2
        bringe an Position(2, 2, 2)
        senke um 2
        greife
        hebe um 2
        bringe an Position(6, 2, 2)
        senke um 1
        richte aus
        lasse los
    }
}