# CustomVariables ----------------------------

Prefix = "/"

# Subroutine Template ---------------------


def SUBsubroutinename():  # Template Subroutine
    # Variablen
    orders = [f"{Prefix}help", "None", "None", "None"]
    order = ["GeneralOutput(x)"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[...])"
    # Vorschläge
    GeneralOutput("Switched to Stage [subroutinename]")
    MainNavigation("subroutinename ", orders, order, x)


# Kryptographic --------------------------


def SUBkrypto():  # Kryptografie Subroutine
    # Variablen
    orders = [f"{Prefix}help", f"{Prefix}set_symetric", "None", "None"]
    order = ["GeneralOutput(x)", "krypto_symetric()"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[...])\n({Prefix}set_[(mono / symetric)])"
    # Vorschläge
    GeneralOutput("Switched to Stage [Krypto]")
    MainNavigation("krypto ", orders, order, x)


def krypto_symetric():  # Symetrische Verschlüsselung
    # Variablen
    backtosub = False
    # General
    GeneralOutput("Switched to Stage [krypto::symetric]")
    while backtosub == False:
        userinput = CommandInput("krypto::symetric ")

        if userinput == f"{Prefix}back":
            SUBkrypto()
        if userinput == f"{Prefix}encode":
            source = input("Please specify source: ")
            key = input("Please specify key: ")
            ret = ""
            for zeichen in range(len(source)):
                ret = ret + chr(ord(source[zeichen]) + ord(key[zeichen % len(key)]))
            GeneralOutput(f"Encoded Source: {ret}")
        if userinput == f"{Prefix}decode":
            source = input("Please specify encoded-source: ")
            key = input("Please specify key: ")
            ret = ""
            for zeichen in range(len(source)):
                ret = ret + chr(ord(source[zeichen]) - ord(key[zeichen % len(key)]))
            GeneralOutput(f"Decoded Source: {ret}")

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
            cmd = "SUB" + userinput.replace(f"{Prefix}goto_", "") + "()"
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

def SUBmain():  # Erste Funktion des Programms
    # Befehle
    orders = [f"{Prefix}help", "None", "None", "None"]  # Befehle
    order = ["GeneralOutput(x)"]
    x = f"Mögliche Befehle:\n({Prefix}help)\n({Prefix}goto_[...])"
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
SUBmain()
