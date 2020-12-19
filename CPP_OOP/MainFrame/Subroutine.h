#include <iostream>
#include <string>
#include <array>
#include "namespace_ewms.h"


class Subroutine {
protected:

	std::string Name;
	std::array<std::string, 4> Befehle;
	std::string Hilfe;
	const std::string GotoOrder = "[" + ewms::Prefix + "goto_[" + ewms::StringSubroutines + "]]\n";

public:

	Subroutine() = default;

	Subroutine(const std::string& Cname, const std::array<std::string, 4>& Cbefehle, const std::string& Chilfe) {
		Name = Cname;
		Hilfe = Chilfe;
		Befehle = Cbefehle;
	}

	int BefehlsHandler(std::string& Eingabe) const {
		for (int OrderCounter = 0; OrderCounter < 4; OrderCounter++) {
			if (Eingabe == Befehle[OrderCounter]) {
				return 1;
			}
		}
		return 0;
	}

	void SetToHilfe(std::string& HilfeAssign) {
		using namespace ewms;
		const std::string HilfeBefehl = { "Moegliche Befehle:\n" + GotoOrder + Hilfe + "\n[" + Prefix + "help]" + "\n[" + Prefix + "exit]" };
		HilfeAssign = HilfeBefehl;
	}

	void ExitBefehl() {
		exit(0);
	}

	virtual int Test() = 0;

};

class SUBmain: public Subroutine {
public:
	
	using Subroutine::Subroutine;

	int BefehlsHandler(std::string& Eingabe) {
		if (Subroutine::BefehlsHandler(Eingabe) == 0) {
			return 0;
		}
		return 1;
	}

	int Test() {
		return 0;
	}

};

class SUBkrypto: public Subroutine {
public:

	using Subroutine::Subroutine;

	int BefehlsHandler(std::string& Eingabe) {
		if (Subroutine::BefehlsHandler(Eingabe) == 0) {
			return 0;
		}
		if (Eingabe == Befehle[0]) {
			VigenereCipher();
		}
		return 1;
	}

	void VigenereCipher() {
		using namespace ewms;
		std::string Eingabe;
		Output("Switched to Subroutine: [vigenere]");
		
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

	std::string Calc(std::string& Original, std::string& Schluessel, int Method) {
		std::string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		std::string Ergebnis;
		int Stelle = 0;
		
		for (const char& zeichen : Original) {
			using namespace std;
			
			size_t Buchstabenwert1 = Alphabet.find(zeichen);
			size_t Buchstabenwert2 = Alphabet.find(Schluessel[Stelle % Schluessel.length()]);
		
			if (Method == 0) {
				Ergebnis += Alphabet[(Buchstabenwert1 + (26 - Buchstabenwert2)) % 26];
			}
			else {
				int Rohwert = Buchstabenwert1 - (26 - Buchstabenwert2);
				Ergebnis += Alphabet[(26 + (Rohwert % 26)) % 26];
			}
			Stelle++;
		}
		return Ergebnis;
	}

	int Test(){
		return 1;
	}

};