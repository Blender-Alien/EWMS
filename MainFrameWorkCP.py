# CustomVariables ----------------------------

Prefix = "/"


# InBetweenOperator --------------------------

def NavigateToProceed(): # Zwischenschritt zum Kryptografischem Abteil
    print("Ende")


# MainFrameWork ------------------------------

def Navigation():  # Konsolenfunktion
    #Variablen
    userinput = "Error"
    recognized = "Error"
    # Eingabeschleife
    while userinput and recognized == "Error":
        userinput = "Error"
        userinput = CommandInput()
        #Kommandos
        if userinput == "/help": #Help - Kommando
            GeneralOutput("Mögliche Befehle:\n(/help)\n(/setproceed)")
            recognized = "Erfolg"
        elif userinput == "/setproceed": #Proceed - Kommando
            NavigateToProceed()
            recognized = "Erfolg"
        else: # Befehl nicht erkannt
            if userinput != "Error": # Check auf Prefix-Error
                GeneralOutput("[" + userinput + "] ist kein gültiger Befehl!")
            recognized = "Error"
    Navigation() # Wiederhohlung der Eingabe bei Print-Befehlen


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


def GeneralOutput(args):  # Multiple Ausgabe an Nutzer
    # Ausgabe an Nutzer
    print("[System.Output] " + args)


# StartMenu ----------------------------------

def StartMenu():  # Erste Funktion des Programms
    # Erstausgabe an Nutzer
    PrefixFest = "Standard Eingabeprefix: " + Prefix
    GeneralOutput(PrefixFest)
    # Hilfestellung
    hilfe = "Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + Prefix + "help] ."
    GeneralOutput(hilfe)
    # Abfrage nach Navigation
    Navigation()


StartMenu()
