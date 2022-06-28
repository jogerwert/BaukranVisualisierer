
class Hakenhandlung:

    def __init__(self, name, kran, kranfunktion):
        self.name = name
        self.kran = kran
        self.kranfunktion = kranfunktion

    def ausfuehren(self):
        self.kran.kranfunktion()
