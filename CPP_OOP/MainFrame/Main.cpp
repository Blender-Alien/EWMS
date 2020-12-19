#include <iostream>
#include <string>
#include <array>
#include "Subroutine.h"
#include "SubroutineInputManager.h"


int main() {
	using namespace ewms;

	SUBmain Main(MainName, MainBefehle, MainHilfe);
	SUBkrypto Krypto(KryptoName, KryptoBefehle, KryptoHilfe);

	SubroutineInputManager Controller(Main, Krypto);
	
	ewms::Output("Um eine Liste an Befehlen zu erhalten, nutzen Sie: ["+Prefix+"help].");
	
	Controller.RunLoop("main");
	
}