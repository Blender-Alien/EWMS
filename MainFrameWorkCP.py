# CustomVariables ----------------------------

Prefix = "/"


# InBetweenOperator --------------------------


def NavigateToProceed(): # Zwischenschritt zum Kryptografischem Abteil
    #Variablen
    #Vorschläge
    GeneralOutput("Switched to Stage [InBetween]")
    MainNavigation("Main/InBetween ")


# MainFrameWork ------------------------------

def MainNavigation(stage):  # Konsolenfunktion
    #Variablen
    userinput = "Error"
    recognized = "Error"
    # Eingabeschleife
    while userinput and recognized == "Error":
        userinput = "Error"
        userinput = CommandInput(stage)
        #Kommandos
        if stage == "Main ":
            if userinput == f"{Prefix}help": #Help - Kommando
                GeneralOutput(f"Mögliche Befehle:\n({Prefix}help)\n({Prefix}setproceedure)\n({Prefix}exit)")
                recognized = "Erfolg"
            elif userinput == f"{Prefix}setproceedure": #Proceed - Kommando
                NavigateToProceed()
                recognized = "Erfolg"
            elif userinput == f"{Prefix}exit":
                exit()
            else: # Befehl nicht erkannt
                if userinput != "Error": # Check auf Prefix-Error
                    GeneralOutput("[" + userinput + f"] ist kein gültiger Befehl! Nutze [{Prefix}help].")
                recognized = "Error"
        if stage == "Main/InBetween ":
            if userinput == f"{Prefix}help":  # Help - Kommando
                GeneralOutput(f"Mögliche Befehle:\n({Prefix}back)\n({Prefix}exit)")
                recognized = "Erfolg"
            elif userinput == f"{Prefix}back":
                StartMenu()
                recognized = "Erfolg"
            elif userinput == f"{Prefix}exit":
                exit()
            else:  # Befehl nicht erkannt
                if userinput != "Error":  # Check auf Prefix-Error
                    GeneralOutput("[" + userinput + f"] ist kein gültiger Befehl! Nutze [{Prefix}help].")
                recognized = "Error"
    MainNavigation(stage) # Wiederhohlung der Eingabe bei Print-Befehlen


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
    MainNavigation("Main ")

# MainProgramm -------------------------------

# Erstausgabe an Nutzer
PrefixFest = "Standard Eingabeprefix: " + Prefix
GeneralOutput(PrefixFest)
# Hilfestellung
hilfe = "Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + Prefix + "help] ."
GeneralOutput(hilfe)
StartMenu()
