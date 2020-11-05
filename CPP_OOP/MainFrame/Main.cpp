#include <iostream>
#include <string>
#include <array>

namespace ewms {
	std::string Prefix = "/";
}

class Subroutine {
private:
	
	std::string Name;
	std::array<std::string, 4> Befehle;
	std::string Hilfe;

public:
	
	Subroutine(std::string Cname, std::array<std::string, 4> Cbefehle, std::string Chilfe) {
		Name = Cname;
		Hilfe = Chilfe;
		Befehle = Cbefehle;
	}

	void BefehlsHandler() {};
	
	void HilfeBefehl() {
		using namespace ewms;
		std::cout << "Moegliche Befehle:\n" << Hilfe << "\n[" + Prefix + "help]" << "\n[" + Prefix + "exit]" << std::endl;
	}

	void ExitBefehl() {
		exit(0);
	}

};

int main() {
	using namespace ewms;

	std::array<std::string, 4> Befehle = { "Befehl1", "Befehl2", "Befehl3", "Befehl4" };
	std::string Hilfe = { "[" + Prefix + "Behel1]\n[" + Prefix + "Befehl2]\n[" + Prefix + "Befel3]\n[" + Prefix + "Befehl4]" };
	
	Subroutine SUBmain("Main", Befehle, Hilfe);

	SUBmain.HilfeBefehl();
	SUBmain.ExitBefehl();

	std::cerr << "Exit hat nicht funktioniert";
}