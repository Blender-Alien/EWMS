# CustomVariables ----------------------------

Prefix = "/"

# MainFrameWork ------------------------------

def Navigation():  # Konsolenfunktion
    #Variablen
    userinput = "Error"
    # Hilfestellung
    hilfe = "Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + Prefix + "help] ."
    GeneralOutput(hilfe)
    # Eingabeschleife
    while userinput == "Error":
        userinput = CommandInput()


def CommandInput():  # Multipler Aufruf des User Inputs
    #Variablen
    returnvalue = None
    #Benutzereingabe
    userinput = str(input("> "))
    #Checkauf richtiges Prefix
    if userinput.startswith(Prefix):
      pass
    else: # Rückgabe mit Error
      GeneralOutput("Ungültiges Prefix.")
      returnvalue = "Error"
      return returnvalue
    #Rückgabe mit Erfolg
    returnvalue = userinput
    return returnvalue


def GeneralNavigation():  # Multipler Aufruf der Interpretation des User Inputs
    pass


def GeneralOutput(args):  # Multiple Ausgabe an Nutzer
    # Ausgabe an Nutzer
    print("[System.Output] " + args)


# StartMenu ----------------------------------


def StartMenu():  # Erste Funktion des Programms
    # Erstausgabe an Nutzer
    PrefixFest = "Standard Eingabeprefix: " + Prefix
    GeneralOutput(PrefixFest)
    # Abfrage nach Navigation
    FirstNavigation()


StartMenu()
