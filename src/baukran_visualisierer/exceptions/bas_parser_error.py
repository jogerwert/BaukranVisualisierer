from baukran_visualisierer.exceptions.baustellen_fehler import BaustellenFehler


class BasParserError(BaustellenFehler):
    """Fehlermeldung, die durch Fehler beim Erstellen der Baustelle durch den Parser entstanden ist."""
    pass
