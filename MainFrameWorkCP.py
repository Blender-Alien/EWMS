# CustomVariables ----------------------------

Prefix = "/"


# MainFrameWork ------------------------------

def CommandInput():  # Multipler Aufruf des User Inputs
    pass


def GeneralNavigation():  # Multipler Aufruf der Interpretation des User Inputs
    pass


def GeneralOutput(args):  # Multiple Ausgabe an Nutzer
    # Ausgabe an Nutzer
    print("[System.Output] " + args)


# StartMenu ----------------------------------

def FirstNavigation():  # Erste Funktion von: StartMenu
    # Hilfestellung
    hilfe = "Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + Prefix + "help] ."
    GeneralOutput(hilfe)


def StartMenu():  # Erste Funktion des Programms
    # Erstausgabe an Nutzer
    PrefixFest = "Standard Eingabeprefix: " + Prefix
    GeneralOutput(PrefixFest)
    # Abfrage nach Navigation
    FirstNavigation()


StartMenu()
