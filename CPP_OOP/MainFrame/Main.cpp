#include <iostream>
#include <string>
#include <array>
#include "Subroutine.h"
#include "SubroutineInputManager.h"


int main() {
	using namespace ewms;

	std::array<std::string, 4> Befehle = { "Befehl1", "Befehl2", "Befehl3", "Befehl4" };
	std::string Hilfe = { "[" + Prefix + "Behel1]\n[" + Prefix + "Befehl2]\n[" + Prefix + "Befel3]\n[" + Prefix + "Befehl4]" };
	std::string Name = "Main";

	SUBmain Main(Name, Befehle, Hilfe); // !!! *Konstruktor von SUBmain stimmt nicht mit Subroutine überein* !!!

	Main.HilfeBefehl();
	Main.ExitBefehl();

	std::cerr << "Exit hat nicht funktioniert";
}