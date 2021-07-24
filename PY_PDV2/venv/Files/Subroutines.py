from Files.Utility import InterfaceManager

IM = InterfaceManager()

class Main:
    def __init__(self, subroutines, prefix):
        self.Prefix = prefix

        self.help = f"Commands:\n<[{prefix}goto_{subroutines}]>\n<[{prefix}info]>\n<[{prefix}help]>\n<[{prefix}exit]>"
        self.commands = ["info"]


    def Help(self):
        print(self.help)

    def BefehlsHandler(self, Eingabe):
        for counter in self.commands:
            if counter == Eingabe.replace(self.Prefix, ""):
                return
        IM.Output("!Error, unknown Command given!")

class Krypto:
    def __init__(self, subroutines, prefix):
        self.Prefix = prefix

        self.help = f"Commands:\n<[{prefix}goto_{subroutines}]>\n<[{prefix}help]>\n<[{prefix}exit]>"

    def Help(self):
        print(self.help)