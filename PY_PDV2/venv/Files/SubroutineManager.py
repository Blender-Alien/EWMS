from Files.Utility import InterfaceManager
from Files.Database import Namespace

class SubroutineManager:

    def __init__(self, prefix, im = InterfaceManager(), ns = Namespace()):
        self.Prefix = prefix

        self.IM = im
        self.NS = ns

        self.RunLoop("main")

    def RunLoop(self, stage): # Primäre Programmschleife für Nutzerinteraktion
        while True:
            Eingabe = self.IM.Input(stage, self.Prefix)

            if str(Eingabe).startswith(self.Prefix + "goto_"):
                rvalue = self.SwitchSubroutine(Eingabe)
                if rvalue == 0:
                    continue
                elif rvalue == stage:
                    self.IM.Output(f"Stage: [{stage}] is already set!")
                else:
                    self.IM.Output(f"Switching to subroutine: [{rvalue}].")
                    stage = rvalue

            elif Eingabe == self.Prefix + "help":
                self.HilfeOutput(stage)

            elif Eingabe == 0:
                self.IM.Output("!Error, unkown Prefix!")
                continue

            elif Eingabe == self.Prefix + "exit":
                exit(0)

            else:
                self.CallCommand(Eingabe, stage)

    def SwitchSubroutine(self, Eingabe):
        subroutine = Eingabe.replace(self.Prefix + "goto_", "")

        for counter in self.NS.Subroutines:
            if counter == subroutine:
                return subroutine
        self.IM.Output(f"!Error, {subroutine} is not a kown Subroutine!")
        return 0

    def HilfeOutput(self, stage):
        if self.ExecuteCheck(stage) == 1:
            exec(f"self.NS.{stage}.Help()")

    def CallCommand(self, Eingabe, stage):
        if self.ExecuteCheck(stage) == 1:
            for counter in self.NS.Subroutines:
                if counter == stage:
                    exec(f"self.NS.{stage}.BefehlsHandler(Eingabe)")

    def ExecuteCheck(self, stage):
        for counter in self.NS.Subroutines:
            if counter == stage:
                return 1
        self.IM.Output(f"!Error, the current subroutine {stage} was not recognized!")
        return 0