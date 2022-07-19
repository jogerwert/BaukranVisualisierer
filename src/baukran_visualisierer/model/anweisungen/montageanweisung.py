
class Montageanweisung:

    def __init__(self, bauteil, kran, krananweisungen):
        self.bauteil = bauteil
        self.kran = kran
        self.krananweisungen = krananweisungen
        self.krananweisungs_zaehler = 0

    def alle_krananweisungen_ausfuehren(self):

        if self.krananweisungs_zaehler < len(self.krananweisungen):

            # Bereits durchgefuehrte Anweisungen werden nicht wiederholt
            krananweisungen = self.krananweisungen[self.krananweisungs_zaehler:]

            for anweisung in krananweisungen:
                anweisung.ausfuehren()
                self.krananweisungs_zaehler += 1

    def naechste_krananweisung_ausfuehren(self):
        if self.krananweisungs_zaehler < len(self.krananweisungen):
            self.krananweisungen[self.krananweisungs_zaehler].ausfuehren()
            self.krananweisungs_zaehler += 1

        return self.krananweisungs_zaehler

    def pruefe_alle_anweisungen_ausgefuehrt(self):
        if self.krananweisungs_zaehler >= len(self.krananweisungen):
            return True
        else:
            return False
