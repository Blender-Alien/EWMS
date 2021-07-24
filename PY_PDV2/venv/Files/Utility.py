class InterfaceManager:

    def __init__(self):
        pass

    def Input(self, stage, Prefix):
        x = input(f"<< {stage} >> ")

        if not x.startswith(Prefix):
            return 0
        else:
            return x

    def Output(self, args):
        print(f"<< Output >> {args}")