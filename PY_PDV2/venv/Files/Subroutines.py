from Files.Utility import InterfaceManager

IM = InterfaceManager()

class SubroutineClass:
    def __init__(self, subroutines, prefix):
        self.Prefix = prefix

        self.help = f"Commands:\n<[{prefix}goto_{subroutines}]>\n<[{prefix}info]>\n<[{prefix}help]>\n<[{prefix}exit]>\n"
        self.commands = ["info"]

    def Help(self):
        print(self.help)

    def BefehlsHandler(self, Eingabe):
        for counter in self.commands:
            if counter == Eingabe.replace(self.Prefix, ""):
                exec(f"self.{Eingabe.replace(self.Prefix, '')}()")
                return
        IM.Output("!Error, unkown Command given!")

    def info(self):
        raise NotImplementedError("!Error, info is not yet implemented in this subroutine!")

# Die Main Funktion ist ebenfalls ein Template für neu angelegte Subroutinen

class Main(SubroutineClass):
    def __init__(self, subroutines, prefix):
        super().__init__(subroutines, prefix)
        self.help += f"<[{prefix}test_order]>"
        self.commands = ["info"]

    def test_order(self):
        IM.Output("This is a test order!")

    def info(self):
        print("< This subroutine represents the main-menu of 'EWMS'. >"
              "\n< All primary functionality is accessably though this subroutine. >")

class Krypto(SubroutineClass):
    def __init__(self, subroutines, prefix):
        super().__init__(subroutines, prefix)
        self.help += f"<[{prefix}set_symm]>"
        self.commands = ["info", "set_symm"]

    def set_symm(self):
        IM.Output("Switched to subroutine-programm: [krypto::symmetrical-cipher].")
        while True:
            Eingabe = IM.Input("krypto::symmetrical-cipher", self.Prefix)
            if Eingabe == self.Prefix + "encode" or Eingabe == self.Prefix + "decode":

                Original = input("<$> Originaltext: ")
                Schluessel = input("<$> Schluessel: ")
                Cipher = input("<$> Cipher [vige / None / None]: ")

                if Cipher == "vige":
                    if Eingabe == self.Prefix + "encode":
                        IM.Output(f"Ergebnis: {self.CalcVige(Original, Schluessel, 0)}")
                    else:
                        IM.Output(f"Ergebnis: {self.CalcVige(Original, Schluessel, 1)}")
                else:
                    IM.Output("!Error, unknown command given!")
            elif Eingabe == self.Prefix + "back":
                return
            else:
                IM.Output(f"!Error, unknown command given!\n< Use [{self.Prefix}encode] or [{self.Prefix}decode] to set the type of calculation. >")

    def CalcVige(self, Original, Schluessel, Type):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret = ""
        stelle = 0
        for zeichen in Original:
            if zeichen == " ":
                ret += " "
            else:
                if Type == 0:
                    ret += alphabet[(alphabet.find(zeichen) + (26 - (alphabet.find(Schluessel[stelle % len(Schluessel)])))) % 26]
                else:
                    ret += alphabet[(alphabet.find(zeichen) - (26 - (alphabet.find(Schluessel[stelle % len(Schluessel)])))) % 26]
                stelle += 1
        return ret

    def info(self):
        print("< This subroutine represents the cryptographic algorithms of 'EWMS'. >"
              "\n< It contains a number of different methods, most promintly featured, the 'Vigénère-Cipher'. >")