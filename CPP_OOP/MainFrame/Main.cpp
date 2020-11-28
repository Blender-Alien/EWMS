#include <iostream>
#include <string>
#include <array>
#include "Subroutine.h"
#include "SubroutineInputManager.h"


int main() {
	using namespace ewms;
	
	SubroutineInputManager Controller;
	
	ewms::Output("Um eine Liste an Befehlen zu erhalten, nutzen Sie: ["+Prefix+"help].");
	Controller.Navigation("main");
}