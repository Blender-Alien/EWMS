# CustomVariables ----------------------------

Prefix = "/"


# InBetweenOperator --------------------------

def InBetweenNavigation():  # Konsolenfunktion
    #Variablen
    userinput = "Error"
    recognized = "Error"
    # Eingabeschleife
    while userinput and recognized == "Error":
        userinput = "Error"
        userinput = CommandInput("Main/InBetween ")
        #Kommandos
        if userinput == "/help": #Help - Kommando
            GeneralOutput("Mögliche Befehle:\n(/back)")
            recognized = "Erfolg"
        elif userinput == "/back":
            StartMenu()
            recognized = "Erfolg"
        else: # Befehl nicht erkannt
            if userinput != "Error": # Check auf Prefix-Error
                GeneralOutput("[" + userinput + "] ist kein gültiger Befehl! Nutze [/help].")
            recognized = "Error"
    InBetweenNavigation() # Wiederhohlung der Eingabe bei Print-Befehlen

def NavigateToProceed(): # Zwischenschritt zum Kryptografischem Abteil
    #Variablen
    #Vorschläge
    GeneralOutput("Switched to Stage [InBetween]")
    InBetweenNavigation()


# MainFrameWork ------------------------------

def MainNavigation():  # Konsolenfunktion
    #Variablen
    userinput = "Error"
    recognized = "Error"
    # Eingabeschleife
    while userinput and recognized == "Error":
        userinput = "Error"
        userinput = CommandInput("Main ")
        #Kommandos
        if userinput == "/help": #Help - Kommando
            GeneralOutput("Mögliche Befehle:\n(/help)\n(/setproceed)")
            recognized = "Erfolg"
        elif userinput == "/setproceed": #Proceed - Kommando
            NavigateToProceed()
            recognized = "Erfolg"
        else: # Befehl nicht erkannt
            if userinput != "Error": # Check auf Prefix-Error
                GeneralOutput("[" + userinput + "] ist kein gültiger Befehl! Nutze [/help].")
            recognized = "Error"
    MainNavigation() # Wiederhohlung der Eingabe bei Print-Befehlen


def CommandInput(stage):  # Multipler Aufruf des User Inputs
    #Variablen
    returnvalue = None
    #Benutzereingabe
    userinput = str(input(stage + ">> "))
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
    #Anmerkung der Stage
    GeneralOutput("Switched to Stage [Main]")
    # Abfrage nach Navigation
    MainNavigation()

# MainProgramm -------------------------------

# Erstausgabe an Nutzer
PrefixFest = "Standard Eingabeprefix: " + Prefix
GeneralOutput(PrefixFest)
# Hilfestellung
hilfe = "Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + Prefix + "help] ."
GeneralOutput(hilfe)
StartMenu()
