# CustomVariables ----------------------------

Prefix = "/"


# InBetweenOperator --------------------------

def NavigateToProceed(): # Zwischenschritt zum Kryptografischem Abteil
    # Variablen
    orders = [f"{Prefix}goto_main", f"{Prefix}help", f"{Prefix}exit", "None"]
    order = ["StartMenu()", "GeneralOutput(x)", "exit()"]
    x = f"Mögliche Befehle:\n({Prefix}goto_main)\n({Prefix}exit)"
    # Vorschläge
    GeneralOutput("Switched to Stage [Krypto]")
    MainNavigation("Krypto ", orders, order, x)


# MainFrameWork ------------------------------

def MainNavigation(stage, orders, order, x):  # Konsolenfunktion
    # Variablen
    userinput = "Error"
    recognized = "Error"
    # Eingabeschleife
    while userinput and recognized == "Error":
        userinput = "Error"
        userinput = CommandInput(stage)
        #Kommandos
        if userinput == orders[0]:
            exec(order[0])
        elif userinput == orders[1]:
            exec(order[1])
        elif userinput == orders[2]:
            exec(order[2])
        elif userinput == orders[3]:
            exec(order[3])
        else:  # Check auf Prefix Fehler
            if userinput != "Error":
                GeneralOutput(f"Das Kommando: [{userinput}] existiert nicht!")
    MainNavigation(stage, orders, order,  x)  # Wiederhohlung der Eingabe bei Print-Befehlen


def CommandInput(stage):  # Multipler Aufruf des User Inputs
    # Variablen
    returnvalue = None
    # Benutzereingabe
    userinput = str(input(stage + ">> "))
    # Checkauf richtiges Prefix
    if userinput.startswith(Prefix):
      pass
    else:  # Rückgabe mit Error
      GeneralOutput("Ungültiges Prefix.")
      returnvalue = "Error"
      return returnvalue
    # Rückgabe mit Erfolg
    returnvalue = userinput
    return returnvalue


def GeneralOutput(args):  # Multiple Ausgabe an Nutzer
    # Ausgabe an Nutzer
    print("[System.Output] " + args)


# StartMenu ----------------------------------

def StartMenu():  # Erste Funktion des Programms
    # Befehle
    orders = [f"{Prefix}help", f"{Prefix}goto_krypto", f"{Prefix}exit", "None"]  # Befehle
    order = ["GeneralOutput(x)", "NavigateToProceed()", "exit()"]
    x = f"Mögliche Befehle:\n({Prefix}help)\n({Prefix}goto_krypto)\n({Prefix}exit)"
    # Anmerkung der Stage
    GeneralOutput("Switched to Stage [Main]")
    # Abfrage nach Navigation
    MainNavigation("Main ", orders, order, x)

# MainProgramm -------------------------------

# Erstausgabe an Nutzer
GeneralOutput("Standard Eingabeprefix: " + Prefix)
# Hilfestellung
GeneralOutput("Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + Prefix + "help] .")
# Start der Menüschleife
StartMenu()
