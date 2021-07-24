from Files.Utility import InterfaceManager
from Files.SubroutineManager import SubroutineManager
from Files.Database import Namespace

def main():
    # Instanzierung der Hauptklassen
    IM = InterfaceManager()
    NS = Namespace()
    SM = SubroutineManager(NS.prefix, IM, NS)

main()