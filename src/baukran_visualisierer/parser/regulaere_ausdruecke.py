import re

# Regulaere Ausdruecke, um die Baustelle zu finden
baustelle_regex_dict = {
    'baustelle': re.compile(r'\s*Baustelle (?P<name>\w+) \{\s*\n'),
    'kommentar': re.compile(r'\s*#.*\n'),
    'mehrzeiliger_kommentar': re.compile(r'\s*#\*.*\n'),
    'leere_zeile': re.compile(r'\s*\n')
}

# Regulaere Ausdruecke, um die Komponenten der Baustelle zu finden, z.B.: Baufeld, Kran, Bauteile
komponenten_regex_dict = {
    'baufeld': re.compile(r'\s*Baufeld : Abmessung ?\((?P<breite>\d{1,3}), (?P<laenge>\d{1,3})\)\s*\n'),
    'gegenstand': re.compile(r'\s*Gegenstand : Position ?\((?P<x>\d{1,3), (?P<y>\d{1,3}), (?P<z>\d{1,3})\)\s*\n'),
    'kran': re.compile(r'\s*Kran : Position ?\((?P<x>\d{1,3}), (?P<y>\d{1,3})\) '
                       r'Hoehe (?P<hoehe>\d{1,3}) Ausladung (?P<ausladung>\d{1,3}) \s*\n'),
    'bauteil': re.compile(r'\s*Bauteil (?P<name>\w+) : '
                          r'Position ?\((?P<x>\d{1,3), (?P<y>\d{1,3}), (?P<z>\d{1,3})\)\s*\n'),
    'kommentar': re.compile(r'\s*#.*\n'),
    'mehrzeiliger_kommentar': re.compile(r'\s*#\*.*\n'),
    'leere_zeile': re.compile(r'\s*\n')
}

# Regulaere Ausdruecke, um die Montageanweisungen zu finden
montageanweisungen_regex_dict = {
    'montageanweisung': re.compile(r'\s*montiere (?P<name>\w+) {\s*\n'),
    'ende_montageanweisungen': re.compile(r'\s*}\s*\n'),
    'kommentar': re.compile(r'\s*#.*\n'),
    'mehrzeiliger_kommentar': re.compile(r'\s*#\*.*\n'),
    'leere_zeile': re.compile(r'\s*\n')
}

# Regulaere Ausdruecke, um die Krananweisungen in den Montageanweisungen zu finden, z.B.: greife, hebe
krananweisungen_regex_dict = {
    'hebe_um': re.compile(r'\s*hebe um (?P<hoehe>\d{1,3})\s*\n'),
    'senke_um': re.compile(r'\s*senke um (?P<hoehe>\d{1,3})\s*\n'),
    'bringe_an': re.compile(r'\s*bringe an Position ?\((?P<x>\d{1,3}), (?P<y>\d{1,3}), (?P<z>\d{1,3})\)\s*\n'),
    'greife': re.compile(r'\s*greife\s*\n'),
    'richte_aus': re.compile(r'\s*richte aus\s*\n'),
    'lasse_los': re.compile(r'\s*lasse los\s*\n'),
    'ende_krananweisungen': re.compile(r'\s*}\s*\n'),
    'kommentar': re.compile(r'\s*#.*\n'),
    'mehrzeiliger_kommentar': re.compile(r'\s*#\*.*\n'),
    'leere_zeile': re.compile(r'\s*\n')
}

# Regulaere Ausdruecke, um Text innerhalb von mehrzeiligen Kommentaren korrekt zu behandeln
kommentar_regex_dict = {
    'kommentar_ende': re.compile(r'\*#\s*\n')
}
