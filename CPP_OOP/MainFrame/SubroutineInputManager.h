#include <iostream>
#include <string>
#include <array>

class SubroutineInputManager {
private:

	std::array<std::string, 2> Subroutines = { "main", "krypto" };

public:

	void Navigation(std::string stage) {
		using namespace ewms;
		std::string Eingabe;

		while (true) {
			Eingabe = Input(stage);

			if (Eingabe == Prefix + "exit") { exit(0); }
			
			else if (Eingabe.rfind(Prefix + "goto_", 0) == 0) {
				std::string subroutine = { "SUB" + replace(Eingabe, Prefix + "goto_", "") };
				std::string subroutinename = { replace(subroutine, "SUB", "") };

				if (subroutine == "SUBmain") {}
				else if (subroutine == "SUBkrypto") {}
			}

			else if (Eingabe == Prefix + "help") {
				std::string help;
				if (stage == Subroutines[0]) {
					help = Main.HilfeBefehl(); } // !!! *Klasse muss Objekte von Childklassen kennen* !!!
				}
		}
	}
	
	void Output(std::string OutputArgument) {
		std::cout << "<< Output >> " << OutputArgument << std::endl;
	}

	std::string Input(std::string subroutine) {
		std::string Input;

		std::cout << "< " + subroutine + " $> ";
		std::cin >> Input;

		return Input;
	}

};