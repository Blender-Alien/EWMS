#include <iostream>
#include <string>
#include <array>
#include "namespace_ewms.h"


class Subroutine {
private:

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

	void BefehlsHandler() {};

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

	void BefehlsHandler() {

	}

};

class SUBkrypto: public Subroutine {
public:

	using Subroutine::Subroutine;

	void BefehlsHandler() {

	}

};