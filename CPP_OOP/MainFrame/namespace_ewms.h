#include <string>

namespace ewms {
	std::string Prefix = "/";

	std::string StringSubroutines = "main, krypto";
	std::array<std::string, 2> Subroutines = { "main", "krypto" };

	std::array<std::string, 4> MainBefehle = { "Befehl1", "Befehl2", "Befehl3", "Befehl4" };
	std::string MainHilfe = { "[" + Prefix + "Befhel1]\n[" + Prefix + "Befehl2]\n[" + Prefix + "Befehl3]\n[" + Prefix + "Befehl4]" };
	std::string MainName = "Main";

	std::array<std::string, 4> KryptoBefehle = { "/set_vige", "Befehl2", "Befehl3", "Befehl4" };
	std::string KryptoHilfe = { "[" + Prefix + "Befhel1]\n[" + Prefix + "Befehl2]\n[" + Prefix + "Befehl3]\n[" + Prefix + "Befehl4]" };
	std::string KryptoName = "Krypto";

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