#include <iostream>
#include <string>
#include <array>

class SubroutineInputManager {
private:

	SUBmain* Main;
	SUBkrypto* Krypto;
	std::string Eingabe;

public:
	
	SubroutineInputManager(SUBmain& main, SUBkrypto& krypto) {
		Main = &main;
		Krypto = &krypto;

		if (ewms::test == true) {
			SubroutineTests();
		}

		RunLoop("main");
	}

	void RunLoop(std::string stage) {
		using namespace ewms;

		while (true) {
			Eingabe = Input(stage);

			if (Eingabe == Prefix + "exit") { exit(0); }

			else if (Eingabe.rfind(Prefix + "goto_", 0) == 0) {
				SwitchSubroutine(Eingabe);
			}

			else if (Eingabe == Prefix + "help") {
				HilfeOutput(stage);
			}

			else if (Eingabe == "Prefix_Error") {
				Output("Falsches Prefix!");
			}
			else {
				CallSubroutine(Eingabe, stage);
			}
		}
		RunLoop(stage);
	}
	
	void SwitchSubroutine(std::string& Eingabe) {
		std::string subroutine = { "SUB" + ewms::replace(Eingabe, ewms::Prefix + "goto_", "") };
		std::string subroutinename = { ewms::replace(subroutine, "SUB", "") };
		std::string new_sub_name;

		if (subroutine == "SUBmain") {
			new_sub_name = "main";
		}
		else if (subroutine == "SUBkrypto") {
			new_sub_name = "krypto";
		}
		else {
			ewms::Output("Diese Subroutine ist unbekannt!");
			return;
		}
		StageOutput(new_sub_name);
		RunLoop(new_sub_name);
	}

	void HilfeOutput(std::string& stage) {
		std::string help;
		if (stage == ewms::Subroutines[0]) {
			Main->SetToHilfe(help);
		}
		else if (stage == ewms::Subroutines[1]) {
			Krypto->SetToHilfe(help);
		}
		ewms::Output(help);
	}

	void CallSubroutine(std::string& Eingabe, std::string& stage) {
		int succes;
		if (stage == ewms::Subroutines[0]) {
			succes = Main->BefehlsHandler(Eingabe);
		}
		else if (stage == ewms::Subroutines[1]) {
			succes = Krypto->BefehlsHandler(Eingabe);
		}
		if (succes == 0) {
			ewms::Output("Dieses Kommando ist unbekannt!");
		}
		else {
			StageOutput(stage);
		}
	}

	void StageOutput(std::string& stage) {
		ewms::Output("Switched to Stage: [" + stage + "]");
	}

	void SubroutineTests() {
		int iTest;
		std::string sTest;

		iTest = Krypto->Test();
		if (iTest == 1) {
			LOG("Instanztest bestanden!");
		}
		else {
			LOG("/// Instanztest nicht bestanden !!!");
		}

		std::string Original = "HELLOTHERE";
		std::string Schluessel = "KEYWORD";
		sTest = Krypto->Calc(Original, Schluessel, 0);
		if (sTest == "XANPACEUNG") {
			sTest += Krypto->Calc(sTest, Schluessel, 1);
			if (sTest == "XANPACEUNGHELLOTHERE")
			{
				LOG("Kryptotest bestanden!");
			}
			else {
				LOG("/// Kryptotest nicht bestanden !!!");
			}
		}
		else {
			LOG("/// Kryptotest nicht bestanden !!!");
		}
	}
};