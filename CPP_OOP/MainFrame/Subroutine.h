#include <iostream>
#include <string>
#include <array>
#include "namespace_ewms.h"


class Subroutine {
protected:

	std::string Name;
	std::array<std::string, 4> Befehle;
	std::string Hilfe;
	std::string GotoOrder = "[" + ewms::Prefix + "goto_[" + ewms::StringSubroutines + "]]\n";

public:

	Subroutine() = default;

	Subroutine(std::string Cname, std::array<std::string, 4> Cbefehle, std::string Chilfe) {
		Name = Cname;
		Hilfe = Chilfe;
		Befehle = Cbefehle;
	}

	int BefehlsHandler(std::string Eingabe) {
		for (int OrderCounter = 0; OrderCounter < 4; OrderCounter++) {
			if (Eingabe == Befehle[OrderCounter]) {
				return 1;
			}
		}
		return 0;
	}

	std::string HilfeBefehl() {
		using namespace ewms;
		std::string HilfeBefehl = { "Moegliche Befehle:\n" + GotoOrder + Hilfe + "\n[" + Prefix + "help]" + "\n[" + Prefix + "exit]" };
		return HilfeBefehl;
	}

	void ExitBefehl() {
		exit(0);
	}

};

class SUBmain: public Subroutine {
public:
	
	using Subroutine::Subroutine;

	int BefehlsHandler(std::string Eingabe) {
		if (Subroutine::BefehlsHandler(Eingabe) == 0) {
			return 0;
		}
		return 1;
	}

};

class SUBkrypto: public Subroutine {
public:

	using Subroutine::Subroutine;

	int BefehlsHandler(std::string Eingabe) {
		if (Subroutine::BefehlsHandler(Eingabe) == 0) {
			return 0;
		}
		if (Eingabe == Befehle[0]) {
			VigenereCipher();
			return 0;
		}
		return 1;
	}

	void VigenereCipher() {
		using namespace ewms;
		std::string Eingabe;
		Output("Switched to Subroutine: [Vigenere]");
		
		while (true) {
			Eingabe = Input("krypto::vigenere");
			
			if (Eingabe == Prefix + "encode" || Eingabe == Prefix + "decode") {
				std::string Original;
				std::string Schluessel;
				std::string Ergebnis;

				std::cout << "<$> Originaltext: ";
				std::cin >> Original;
				std::cout << "<$> Schluessel: ";
				std::cin >> Schluessel;

				if (Eingabe == Prefix + "encode") {
					Ergebnis = Calc(Original, Schluessel, 0);
					Output("Ergebnis: " + Ergebnis);
				}
				else {
					Ergebnis = Calc(Original, Schluessel, 1);
					Output("Ergebnis: " + Ergebnis);
				}
			}
			else if (Eingabe == Prefix + "back") {
				return;
			}
			else {
				Output("Das Kommando ist unbekannt!");
			}
		}
	}

	std::string Calc(std::string Original, std::string Schluessel, int Method) {
		std::string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		std::string Ergebnis;
		int Stelle = 0;
		
		for (const char& zeichen : Original) {
			using namespace std;

			cout << "$" << zeichen << ", ";
			
			size_t Buchstabenwert1 = Alphabet.find(zeichen);
			size_t Buchstabenwert2 = Alphabet.find(Schluessel[Stelle % Schluessel.length()]);
			

			cout << "$" << Buchstabenwert1 << ", ";
			cout << "$" << Buchstabenwert2 << ", ";
		
			if (Method == 0) {
				Ergebnis += Alphabet[(Buchstabenwert1 + (26 - Buchstabenwert2)) % 26];
				cout << "\n";
			}
			else {
				int Rohwert = Buchstabenwert1 - (26 - Buchstabenwert2);
				cout << Rohwert << "\n";
				Ergebnis += Alphabet[(26 + (Rohwert % 26)) % 26];
			}
			Stelle++;
		}
		return Ergebnis;
	}

};