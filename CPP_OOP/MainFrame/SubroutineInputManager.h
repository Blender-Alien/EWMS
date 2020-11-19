#include <iostream>
#include <string>
#include <array>

class SubroutineInputManager {
private:

	std::array<std::string, 4> MainBefehle = { "Befehl1", "Befehl2", "Befehl3", "Befehl4" };
	std::string MainHilfe = { "[" + ewms::Prefix + "Befhel1]\n[" + ewms::Prefix + "Befehl2]\n[" + ewms::Prefix + "Befehl3]\n[" + ewms::Prefix + "Befehl4]" };
	std::string MainName = "Main";

	std::array<std::string, 4> KryptoBefehle = { "Befehl1", "Befehl2", "Befehl3", "Befehl4" };
	std::string KryptoHilfe = { "[" + ewms::Prefix + "Befhel1]\n[" + ewms::Prefix + "Befehl2]\n[" + ewms::Prefix + "Befehl3]\n[" + ewms::Prefix + "Befehl4]" };
	std::string KryptoName = "Krypto";


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
					StageOutput("[Main]");
					Navigation("main");
				}
				else if (subroutine == "SUBkrypto") {
					StageOutput("[Krypto]");
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
				Output("Dieses Kommando ist unbekannt!");
			}
		}
		Navigation(stage);
	}
	

	void Output(std::string OutputArgument) {
		std::cout << "<< Output >> " << OutputArgument << std::endl;
	}

	std::string Input(std::string subroutine) {
		std::string Input;

		std::cout << "< " + subroutine + " $> ";
		std::cin >> Input;

		if (!Input.rfind(ewms::Prefix, 0) == 0) {
			Input = "Prefix_Error";
		}

		return Input;
	}

	void StageOutput(std::string stage) {
		Output("Switched to Stage: " + stage);
	}

};