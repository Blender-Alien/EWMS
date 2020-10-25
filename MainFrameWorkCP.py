# Variables / Imports ---------------

import sys

exit = False # Exit Condition
Prefix = "None" # Prefix
subroutines = "main, krypto, translator"
firststart = True

# Prefix ----------------------------

try:
    with open("Prefix.txt", "r") as readfile:
        readprefix = readfile.read()
        Prefix = readprefix.replace("Â", "")
        loadprefix = True
except:
    loadprefix = False

# Subroutine Template ---------------------


def SUBsubroutinename():  # Template Subroutine
    # Variablen
    orders = [f"{Prefix}help"]
    order = ["GeneralOutput(x+y)"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[{subroutines}])"
    # Vorschläge
    GeneralOutput("Switched to Stage [subroutinename]")
    MainNavigation("subroutinename ", orders, order, x)

# Translater -----------------------------


def SUBtranslator():
    #Variablen
    orders = [f"{Prefix}help", f"{Prefix}set_morse"]
    order = ["GeneralOutput(x+y)", "translator_morse()"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[{subroutines}])\n({Prefix}set_morse)"
    # Vorschläge
    GeneralOutput("Switched to Stage [translator]")
    MainNavigation("translator ", orders, order, x)


def translator_morse():
    #Variablen
    backtosub = False
    morsealphabet = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}
    #General
    GeneralOutput("Switched to Stage [translator::morse]")
    while backtosub == False:
        userinput = CommandInput("translator::morse ")

        if userinput == f"{Prefix}help":
            GeneralOutput(f"Mögliche Befehle:\n({Prefix}encode)\n({Prefix}decode)\n({Prefix}back)")
        elif userinput == f"{Prefix}encode":
            source = input(f"<< Output >> Please specify source: ")
            ret = ""
            stelle = 0
            for zeichen in source:
                if zeichen != " ":
                    ret += morsealphabet[zeichen] + "/"
                else:
                    ret += "/"
            GeneralOutput(f"Encoded Source {ret}")
        elif userinput == f"{Prefix}decode":
            source = input(f"<< Output >> Please specify source: ")
            ret = ""            
            source += '/'
            decipher = '' 
            for zeichen in source:
                if (zeichen != '/'):
                    i = 0
                    ret += zeichen
                else:
                    i += 1
                    if i == 2:
                        decipher += " "
                    else:
                        decipher += list(morsealphabet.keys())[list(morsealphabet.values()).index(ret)]
                        ret = ""
            GeneralOutput(f"Decoded Source {decipher}")
        elif userinput == f"{Prefix}back":
            SUBtranslator()
        else:
            GeneralOutput(f"Das Kommando: [{userinput}] existiert nicht!")


# Kryptographic --------------------------


def SUBkrypto():  # Kryptografie Subroutine
    # Variablen
    orders = [f"{Prefix}help", f"{Prefix}set_symetric", f"{Prefix}set_mono", f"{Prefix}set_vige"]
    order = ["GeneralOutput(x+y)", "krypto_symetric()", "krypto_mono()", "krypto_vige()"]
    x = f"Mögliche Befehle:\n({Prefix}goto_[{subroutines}])\n({Prefix}set_[(mono / symetric / vige)])"
    # Vorschläge
    GeneralOutput("Switched to Stage [Krypto]")
    MainNavigation("krypto ", orders, order, x)


def krypto_vige():
  #Variablen
  backtosub = False
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  #General
  GeneralOutput("Switched to Stage [krypto::vigenere]")
  while backtosub == False:
    userinput = CommandInput("krypto::vigenere ")

    if userinput == f"{Prefix}back":
      SUBkrypto()
    elif userinput == f"{Prefix}encode":
      source = input(f"<< Output >> Please specify source: ")
      key = input(f"<< Output >> Please specify key: ")
      ret = ""
      stelle = 0
      for zeichen in source:
        if zeichen == " ":
          ret += " "
        else:
          ret += alphabet[(alphabet.find(zeichen) + (26 - (alphabet.find(key[stelle % len(key)])))) % 26] 
          stelle += 1
      GeneralOutput(f"Encoded Source: {ret}")
    elif userinput == f"{Prefix}decode":
      source = input(f"<< Output >> Please specify source: ")
      key = input(f"<< Output >> Please specify key: ")
      ret = ""
      stelle = 0
      for zeichen in source:
        if zeichen == " ":
          ret += " "
        else:
          ret += alphabet[(alphabet.find(zeichen) - (26 - (alphabet.find(key[stelle % len(key)])))) % 26] 
          stelle += 1
      GeneralOutput(f"Decoded Source: {ret}")
    elif userinput == f"{Prefix}help":
        GeneralOutput(f"Mögliche Befehle:\n({Prefix}encode)\n({Prefix}decode)\n({Prefix}back)")
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
            source = input(f"<< Output >> Please specify source: ")
            key = input(f"<< Output >>Please specify key: ")
            ret = ""
            for zeichen in range(len(source)):
                ret = ret + chr(ord(source[zeichen]) + ord(key[zeichen % len(key)]))
            GeneralOutput(f"Encoded Source: {ret}")
        elif userinput == f"{Prefix}decode":
            source = input(f"<< Output >> Please specify encoded-source: ")
            key = input(f"<< Output >> Please specify key: ")
            ret = ""
            for zeichen in range(len(source)):
                ret = ret + chr(ord(source[zeichen]) - ord(key[zeichen % len(key)]))
            GeneralOutput(f"Decoded Source: {ret}")
        elif userinput == f"{Prefix}help":
            GeneralOutput(f"Mögliche Befehle:\n({Prefix}encode)\n({Prefix}decode)\n({Prefix}back)")
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
            source = input(f"<< Output >> Please specify source: ")
            key = input(f"<< Output >> Please specify code-alphabet: ")
            ret = ""
            for zeichen in source:
                if zeichen == " ":
                    ret += " "
                else:
                    position = alphabet.find(zeichen)
                    ret += key[position]
            GeneralOutput(f"Encoded Source: {ret}")
        elif userinput == f"{Prefix}decode":
            source = input(f"<< Output >> Please specify encoded-source: ")
            key = input(f"<< Output >> Please specify code-alphabet: ")
            ret = ""
            for zeichen in source:
                if zeichen == " ":
                    ret += " "
                else:
                    position = key.find(zeichen)
                    ret += alphabet[position]
            GeneralOutput(f"Decoded Source: {ret}")
        elif userinput == f"{Prefix}help":
            GeneralOutput(f"Mögliche Befehle:\n({Prefix}encode)\n({Prefix}decode)\n({Prefix}back)")
        else:
            GeneralOutput(f"Das Kommando: [{userinput}] existiert nicht!")


# MainFrameWork ------------------------------

def MainNavigation(stage, orders, order, x):  # Konsolenfunktion
    # Variablen
    y = f"\n({Prefix}exit)"
    userinput = "Error"
    recognized = "Error"
    global exit
    # Eingabeschleife
    while userinput and recognized == "Error":
        userinput = "Error"
        userinput = CommandInput(stage)
        #Kommandos
        if userinput == f"{Prefix}exit":
            exit = True
            sys.exit(0)
        if userinput.startswith(f"{Prefix}goto_"):
            subroutine = "SUB" + userinput.replace(f"{Prefix}goto_", "") + "()"
            try:
                exec(subroutine)
            except:
                if exit == True:
                    sys.exit(0)
                showsubroutine = userinput.replace(f"{Prefix}goto_", "")
                GeneralOutput(f"Die Subroutine: [{showsubroutine}] existiert nicht!")
        else:
            widerhohlung = 0
            finished = False
            while finished == False:
                try:
                    if userinput == orders[widerhohlung]:
                        exec(order[widerhohlung])
                except:
                    finished = True
                widerhohlung += 1
            if exit == True:
                    sys.exit(0)
            if userinput != "Error" and userinput != f"{Prefix}help":  # Check auf Prefix Fehler
                GeneralOutput(f"Das Kommando: [{userinput}] existiert nicht!")
    
    MainNavigation(stage, orders, order,  x)  # Wiederhohlung der Eingabe bei Print-Befehlen


def CommandInput(stage):  # Multipler Aufruf des User Inputs
    # Variablen
    returnvalue = None
    # Benutzereingabe
    userinput = str(input(f"< {stage}$> "))
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
    print(f"<< Output >> {args}")


# StartMenu ----------------------------------

def main_prefix():
    global Prefix
    GeneralOutput(f"Altes Prefix: {Prefix}")
    usable = False
    while usable == False:
        UserPrefix = str(input(f"<< Output >> Neues Prefix: "))
        length = len(UserPrefix)
        if length > 1:
            GeneralOutput("Prefix ist zu lang!")
            continue
        else:
            Prefix = UserPrefix
            try:
                with open("Prefix.txt", "w") as savefile:
                    savefile.write(Prefix)
            except:
                pass
            SUBmain()
        

def SUBmain():  # Erste Funktion des Programms
    # Variablen
    global firststart
    # Befehle
    orders = [f"{Prefix}help", f"{Prefix}setPrefix"]  # Befehle
    order = ["GeneralOutput(x+y)", "main_prefix()"]
    x = f"Mögliche Befehle:\n({Prefix}help)\n({Prefix}goto_[{subroutines}])\n({Prefix}setPrefix)"
    # Anmerkung der Stage
    if firststart == True:
        pass
    else:
        GeneralOutput("Switched to Stage [Main]")
    # Abfrage nach Navigation
    MainNavigation("main ", orders, order, x)

# MainProgramm -------------------------------

# Erstausgabe an Nutzer
if loadprefix == False:
    Prefix = "/"
    GeneralOutput(f"Standard Eingabeprefix: {Prefix}")
GeneralOutput(f"Nutzen Sie [{Prefix}setPrefix] für ein Personalisiertes Prefix.")
# Hilfestellung
GeneralOutput(f"Um eine Liste an Befehlen zu erhalten, nutzen Sie: [{Prefix}help] .")
GeneralOutput(f"############################################################")
# Start der Menüschleife
SUBmain()