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

# Chatting --------------------------


def SUBchat():
    #Variablen
    orders = [f"{Prefix}help", f"{Prefix}sethostadress", f"{Prefix}connecttohost", f"{Prefix}hostsession"]
    order = ["GeneralOutput(x)"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[...])\n{Prefix}sethostadress\n{Prefix}connecttohost\n{Prefix}hostsession"
    # Vorschläge
    GeneralOutput("Switched to Stage [chat]")
    MainNavigation("chat ", orders, order, x)


# Kryptographic --------------------------


def SUBkrypto():  # Kryptografie Subroutine
    # Variablen
    orders = [f"{Prefix}help", f"{Prefix}set_symetric", f"{Prefix}set_mono", f"{Prefix}set_vige"]
    order = ["GeneralOutput(x)", "krypto_symetric()", "krypto_mono()", "krypto_vige()"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[...])\n({Prefix}set_[(mono / symetric / vige)])"
    # Vorschläge
    GeneralOutput("Switched to Stage [Krypto]")
    MainNavigation("krypto ", orders, order, x)


def krypto_vige():
  #Variablen
  backtosub = False
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabets = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "BCDEFGHIJKLMNOPQRSTUVWXYZA",
            "CDEFGHIJKLMNOPQRSTUVWXYZAB",
            "DEFGHIJKLMNOPQRSTUVWXYZABC",
            "EFGHIJKLMNOPQRSTUVWXYZABCD",
            "FGHIJKLMNOPQRSTUVWXYZABCDE",
            "GHIJKLMNOPQRSTUVWXYZABCDEF",
            "HIJKLMNOPQRSTUVWXYZABCDEFG",
            "IJKLMNOPQRSTUVWXYZABCDEFGH",
            "JKLMNOPQRSTUVWXYZABCDEFGHI",
            "KLMNOPQRSTUVWXYZABCDEFGHIJ",
            "LMNOPQRSTUVWXYZABCDEFGHIJK",
            "MNOPQRSTUVWXYZABCDEFGHIJKL",
            "NOPQRSTUVWXYZABCDEFGHIJKLM",
            "OPQRSTUVWXYZABCDEFGHIJKLMN",
            "PQRSTUVWXYZABCDEFGHIJKLMNO",
            "QRSTUVWXYZABCDEFGHIJKLMNOP",
            "RSTUVWXYZABCDEFGHIJKLMNOPQ",
            "STUVWXYZABCDEFGHIJKLMNOPQR",
            "TUVWXYZABCDEFGHIJKLMNOPQRS",
            "UVWXYZABCDEFGHIJKLMNOPQRST",
            "VWXYZABCDEFGHIJKLMNOPQRSTU",
            "WXYZABCDEFGHIJKLMNOPQRSTUV",
            "XYZABCDEFGHIJKLMNOPQRSTUVW",
            "YZABCDEFGHIJKLMNOPQRSTUVWX",
            "ZABCDEFGHIJKLMNOPQRSTUVWXY"]
  #General
  GeneralOutput("Switched to Stage [krypto::vigenere]")
  while backtosub == False:
    userinput = CommandInput("krypto::vigenere ")

    if userinput == f"{Prefix}back":
      SUBkrypto()
    elif userinput == f"{Prefix}encode":
      source = input("[System.Output] Please specify source: ")
      key = input("[System.Output] Please specify key: ")
      ret = ""
      stelle = 0
      for zeichen in source:
        if zeichen == " ":
          ret += " "
        else:
          ret += alphabet[alphabets[alphabets[0].find(key[stelle % len(key)])].find(zeichen)]
          stelle += 1
      GeneralOutput(f"Encoded Source: {ret}")
    elif userinput == f"{Prefix}decode":
      source = input("[System.Output] Please specify source: ")
      key = input("[System.Output] Please specify key: ")
      ret = ""
      stelle = 0
      for zeichen in source:
        if zeichen == " ":
          ret += " "
        else:
          ret += alphabets[alphabets[0].find(key[stelle % len(key)])][alphabet.find(zeichen)]
          stelle += 1
      GeneralOutput(f"Decoded Source: {ret}")
    else:
      GeneralOutput(f"Das Kommando: [{userinput}] existiert nicht!")

def krypto_symetric():  # Symetrische Verschlüsselung
    # Variablen
    backtosub = False
    # General
    GeneralOutput("Switched to Stage [krypto::symetric]")
    while backtosub == False:
        userinput = CommandInput("krypto::symetric ")

        if userinput == f"{Prefix}back":
            SUBkrypto()
        elif userinput == f"{Prefix}encode":
            source = input("[System.Output] Please specify source: ")
            key = input("[System.Output] Please specify key: ")
            ret = ""
            for zeichen in range(len(source)):
                ret = ret + chr(ord(source[zeichen]) + ord(key[zeichen % len(key)]))
            GeneralOutput(f"Encoded Source: {ret}")
        elif userinput == f"{Prefix}decode":
            source = input("[System.Output] Please specify encoded-source: ")
            key = input("[System.Output] Please specify key: ")
            ret = ""
            for zeichen in range(len(source)):
                ret = ret + chr(ord(source[zeichen]) - ord(key[zeichen % len(key)]))
            GeneralOutput(f"Decoded Source: {ret}")
        else:
            GeneralOutput(f"Das Kommando: [{userinput}] existiert nicht!")


def krypto_mono():  # Substitutions Verschlüsselung
    # Variablen
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    backtosub = False
    #General
    GeneralOutput("Switched to Stage [krypto::mono]")
    while backtosub == False:
        userinput = CommandInput("krypto::mono ")

        if userinput == f"{Prefix}back":
            SUBkrypto()
        elif userinput == f"{Prefix}encode":
            source = input("[System.Output] Please specify source: ")
            key = input("[System.Output] Please specify code-alphabet: ")
            ret = ""
            for zeichen in source:
                if zeichen == " ":
                    ret += " "
                else:
                    position = alphabet.find(zeichen)
                    ret += key[position]
            GeneralOutput(f"Encoded Source: {ret}")
        elif userinput == f"{Prefix}decode":
            source = input("[System.Output] Please specify encoded-source: ")
            key = input("[System.Output] Please specify code-alphabet: ")
            ret = ""
            for zeichen in source:
                if zeichen == " ":
                    ret += " "
                else:
                    position = key.find(zeichen)
                    ret += alphabet[position]
            GeneralOutput(f"Decoded Source: {ret}")
        else:
            GeneralOutput(f"Das Kommando: [{userinput}] existiert nicht!")


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
