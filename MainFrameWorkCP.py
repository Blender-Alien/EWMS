# CustomVariables ----------------------------

Prefix = "/"

# Subroutine Template ---------------------


def subroutinename():  # Template Subroutine
    # Variablen
    orders = [f"{Prefix}help", f"{Prefix}exit", "None", "None"]
    order = ["GeneralOutput(x)", "exit()"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[...])\n({Prefix}exit)"
    # Vorschläge
    GeneralOutput("Switched to Stage [subroutinename]")
    MainNavigation("subroutinename ", orders, order, x)


# Kryptographic --------------------------


def krypto():  # Kryptografie Subroutine
    # Variablen
    orders = [f"{Prefix}help", f"{Prefix}exit", "None", "None"]
    order = ["GeneralOutput(x)", "exit()"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[...])\n({Prefix}exit)"
    # Vorschläge
    GeneralOutput("Switched to Stage [Krypto]")
    MainNavigation("krypto ", orders, order, x)


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
        elif userinput.startswith(f"{Prefix}goto_"):
            cmd = userinput.replace(f"{Prefix}goto_", "") + "()"
            try:
                exec(cmd)
            except:
                GeneralOutput(f"Die Subroutine: [{cmd}] existiert nicht!")
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

def main():  # Erste Funktion des Programms
    # Befehle
    orders = [f"{Prefix}help", f"{Prefix}exit", "None", "None"]  # Befehle
    order = ["GeneralOutput(x)", "exit()"]
    x = f"Mögliche Befehle:\n({Prefix}help)\n({Prefix}goto_[...])\n({Prefix}exit)"
    # Anmerkung der Stage
    GeneralOutput("Switched to Stage [Main]")
    # Abfrage nach Navigation
    MainNavigation("main ", orders, order, x)

# MainProgramm -------------------------------

# Erstausgabe an Nutzer
GeneralOutput("Standard Eingabeprefix: " + Prefix)
# Hilfestellung
GeneralOutput("Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + Prefix + "help] .")
# Start der Menüschleife
main()
