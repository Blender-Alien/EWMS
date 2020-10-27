// Variablen / Imports -----------------------------------------------
#include <iostream>
#include <string>

using namespace std;

string Prefix;
string subroutinenames;
int MainNavigation(string stage, string Befehle[5], string help);
void GeneralOutput(string args);

namespace ewms {
	std::string Prefix;
}

// Subroutinen ---------------------------------------------

void SUBkrypto() {
	// Befehle
	string Befehle[5] = { ewms::Prefix + "help", ewms::Prefix + "set_vige" };
	string help = { "Moegliche Befehle:\n(" + ewms::Prefix + "help)\n(" + ewms::Prefix + "goto_[" + subroutinenames + "])\n(" + ewms::Prefix + "set_vige)" };
	// Anmerkung der Stage
	GeneralOutput("Switched to Stage [Krypto]");
	// Main Navigationsaufruf
	while (true) {
		int Anweisung = MainNavigation("krypto ", Befehle, help);
		// Neustart?
		if (Anweisung == -1)
			continue;
		// Anweisungen
		if (Anweisung == 0) {
			// PASS
		}
		else if (Anweisung == 1) {
			cout << "VigenereChiffreLOL" << endl;
		}
	}
}
