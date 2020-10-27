// Variablen / Imports -------------------------------------------------------
#include <iostream>
#include <string>
#include "Subroutines.h"
#include <fstream>

using namespace std;

bool Exit = false;
string subroutines[5] = { "SUBmain", "SUBkrypto"};
bool firststart = true;



// Subroutinen Deklaration

void SUBkrypto();

// Hauptfunktionen -----------------------------------------------------------
int MainNavigation(string stage, string Befehle[5], string help);
void GeneralOutput(string args);
void SUBmain();
string CommandInput(string stage);

// Tools ----------------------------------------------------------------------

int readFile() {
	ifstream myfile;
	myfile.open("Prefix.txt");
	myfile >> ewms::Prefix;
	return 0;
}

int writeFile(string wPrefix) {
	ofstream myfile;
	myfile.open("Prefix.txt");
	myfile << wPrefix;
	myfile.close();
	return 0;
}

string replace(string str, const string from, const string to) {
	size_t start_pos = str.find(from);
	if (start_pos == string::npos)
		return "Error";
	str.replace(start_pos, from.length(), to);
	return str;
}

// Hauptfunktionen Deklarationen ----------------------------------------------

int main_prefix() {
	// Variablen
	bool correctlen = false;
	string UserPrefix;
	//Eingabe
	GeneralOutput("Altes Prefix: " + ewms::Prefix);
	while (correctlen == false) {
		cout << "<< Output >> Neues Prefix: ";
		cin >> UserPrefix;
		int Length = UserPrefix.length();
		if (Length > 1) {
			GeneralOutput("Das Prefix erfuellt nicht die Leange 1!");
			continue;
		}
		else {
			ewms::Prefix = UserPrefix;
			writeFile(ewms::Prefix);
			GeneralOutput("EWMS wird neu gestartet...");
			cin.get();
			exit(0);
		}
	}
	return 0;
}

int main() {
	// Prefixcheck
	try {
		readFile();
	}
	catch (const exception&){
		ewms::Prefix = "/";
		GeneralOutput("Standard Eingabeprefix: " + ewms::Prefix);
	}
	// Hilfestellung
	GeneralOutput("Nutzen Sie [" + ewms::Prefix + "setPrefix] fuer ein personalisiertes Prefix.");
	GeneralOutput("Um eine Liste an Befehlen zu erhalten, nutzen Sie: [" + ewms::Prefix + "help].");
	// Start der Menüschleife
	SUBmain();
}

void SUBmain() {
	// Befehle
	string Befehle[5] = { ewms::Prefix+"help", ewms::Prefix+"setPrefix" };
	string help = { "Moegliche Befehle:\n(" + ewms::Prefix + "help)\n(" + ewms::Prefix + "goto_[" + subroutinenames + "])\n(" + ewms::Prefix + "setPrefix)" };
	// Anmerkung der Stage
	GeneralOutput("Switched to Stage [Main]");
	// Main Navigationsaufruf
	while (true) {
		int Anweisung = MainNavigation("main ", Befehle, help);
		// Neustart?
		if (Anweisung == -1)
			continue;
		// Anweisungen
		if (Anweisung == 0){
			// PASS
		}
		else if (Anweisung == 1) {
			main_prefix();
		}
	}
	
}

int MainNavigation(string stage, string Befehle[5], string help) {
	// Variablen
	string exitstring = { "\n(" + ewms::Prefix + "exit)" };
	string userinput = "Error";
	string recognized = "Error";
	// Eingabeschleife
	while (userinput + recognized == "ErrorError") {
		userinput = "Error";
		userinput = CommandInput(stage);
		//Kommandos
		if (userinput == Prefix + "exit") {
			Exit = true;
			exit(0);
		}
		else if (userinput.rfind(ewms::Prefix + "goto_", 0) == 0) { // Subroutine ?
			string subroutine = { "SUB" + replace(userinput, ewms::Prefix + "goto_", "") };
			string showsubroutine = { replace(userinput, ewms::Prefix + "goto_", "") };
			if (subroutine == "SUBmain")
				SUBmain();
			else if (subroutine == "SUBkrypto") {
				SUBkrypto();
			}
			else {
				if (Exit == true)
					exit(0);
				GeneralOutput("Die Subroutine: [" + showsubroutine + "] existiert nicht!");
			}
		}
		else if (userinput == ewms::Prefix + "help" ) { // Help Befehl ?
			GeneralOutput(help + exitstring);
		}
		else {
			if (Exit == true) {
				exit(0);
			}
			for (int Stelle = 0; Stelle < 5; Stelle++) {
				if (userinput == Befehle[Stelle]) {
					return Stelle;
				}
			}

			if (userinput != "Error")
				GeneralOutput("Das Kommando [" + userinput + "] existiert nicht!");
			return -1;
		}
	}
	return -1;
}

void GeneralOutput(string args) {
	// Ausgabe an Nutzer
	cout << "<< Output >> " + args << endl;
}

string CommandInput(string stage) {
	// Variablen
	string returnvalue;
	string userinput;
	// Benutzereingabe
	cout << "< " + stage + "$> ";
	cin >> userinput;
	// Check auf Prefix
	if (!userinput.rfind(ewms::Prefix, 0) == 0) {
		GeneralOutput("Ungueltiges Prefix.");
		returnvalue = "Error";
		return returnvalue;
	}
	// Rückgabe mit Erfolg
	returnvalue = userinput;
	return returnvalue;
}
