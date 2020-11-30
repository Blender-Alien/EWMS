#include <iostream>
#include <string>
#include <array>

class SubroutineInputManager {
public:
	

	void Navigation(std::string stage) {
		using namespace ewms;
		std::string Eingabe;

		SUBmain Main(MainName, MainBefehle, MainHilfe);
		SUBkrypto Krypto(KryptoName, KryptoBefehle, KryptoHilfe);

		while (true) {
			
			Eingabe = Input(stage);

			if (Eingabe == Prefix + "exit") { exit(0); }

			else if (Eingabe.rfind(Prefix + "goto_", 0) == 0) {
				std::string subroutine = { "SUB" + replace(Eingabe, Prefix + "goto_", "") };
				std::string subroutinename = { replace(subroutine, "SUB", "") };

				if (subroutine == "SUBmain") {
					StageOutput(stage);
					Navigation("main");
				}
				else if (subroutine == "SUBkrypto") {
					StageOutput(stage);
					Navigation("krypto");
				}
				else {
					Output("Diese Subroutine ist unbekannt!");
				}
			}

			else if (Eingabe == Prefix + "help") {
				std::string help;
				if (stage == Subroutines[0]) {
					help = Main.HilfeBefehl();
				}
				else if (stage == Subroutines[1]) {
					help = Krypto.HilfeBefehl();
				}
				Output(help);
			}

			else if (Eingabe == "Prefix_Error") {
				Output("Falsches Prefix!");
			}
			else {
				int succes;
				if (stage == Subroutines[0]) {
					succes = Main.BefehlsHandler(Eingabe);
				}
				else if (stage == Subroutines[1]) {
					succes = Krypto.BefehlsHandler(Eingabe);
				}
				if (succes == 0) {
					Output("Dieses Kommando ist unbekannt!");
				}
				else {
					StageOutput(stage);
				}
			}
		}
		Navigation(stage);
	}
	

	void StageOutput(std::string stage) {
		ewms::Output("Switched to Stage: [" + stage + "]");
	}

};