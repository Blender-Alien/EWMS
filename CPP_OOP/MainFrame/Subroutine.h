#include <iostream>
#include <string>
#include <array>
#include "namespace_ewms.h"


class Subroutine {
private:

	std::string Name;
	std::array<std::string, 4> Befehle;
	std::string Hilfe;

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
		std::string HilfeBefehl = { "Moegliche Befehle:\n" + Hilfe + "\n[" + Prefix + "help]" + "\n[" + Prefix + "exit]" };
		
		return HilfeBefehl;
	}

	void ExitBefehl() {
		exit(0);
	}

};

class SUBmain: public Subroutine {
public:
	

	void BefehlsHandler() {

	}

};

class SUBkrypto: public Subroutine {
public:


	void BefehlsHandler() {

	}

};