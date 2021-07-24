from Files.Subroutines import Main
from Files.Subroutines import Krypto

class Namespace:

    def __init__(self):
        self.Subroutines = ["main", "krypto"]
        self.prefix = "/"

        self.main = Main(self.Subroutines, self.prefix)
        self.krypto = Krypto(self.Subroutines, self.prefix)
