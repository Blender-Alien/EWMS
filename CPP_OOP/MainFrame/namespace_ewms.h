#include <string>

#define LOG(args) std::cout << "<< Debug >> " <<  args << std::endl

namespace ewms {
	const bool test = true;
	
	const std::string Prefix = "/";

	const std::string StringSubroutines = "main, krypto";
	const std::array<std::string, 2> Subroutines = { "main", "krypto" };

	const std::array<std::string, 4> MainBefehle = { "Befehl1", "Befehl2", "Befehl3", "Befehl4" };
	const std::string MainHilfe = { "[" + Prefix + "Befhel1]\n[" + Prefix + "Befehl2]\n[" + Prefix + "Befehl3]\n[" + Prefix + "Befehl4]" };
	const std::string MainName = "Main";

	const std::array<std::string, 4> KryptoBefehle = { Prefix + "set_vige", "Befehl2", "Befehl3", "Befehl4" };
	const std::string KryptoHilfe = { "[" + Prefix + "set_vige]\n[" + Prefix + "Befehl2]\n[" + Prefix + "Befehl3]\n[" + Prefix + "Befehl4]" };
	const std::string KryptoName = "Krypto";

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

	void Debug(std::string Args) {
		std::cout << "<< Debug >> " + Args + "\n";
	}

	std::string replace(std::string str, const std::string from, const std::string to) {
		size_t start_pos = str.find(from);
		if (start_pos == std::string::npos)
			return "Error";
		str.replace(start_pos, from.length(), to);
		return str;
	}
}