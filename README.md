# CO_project
This project is simulating an assembler.
It takes stdin of an assembly code and gives stdout of the corresponding code in machine language, following the rules of given ISA.
It does not actually do any computation, and only prints the machine code.
Each line ofthe generated machine code is a 16-bits instructions in binary number system.

It is capable of handling syntax errors, use of undefined labels and variables, illegal use of FLAG register, missing or misuse of 'hlt' instruction, and other general errors.
Machine code output is generated when there are no errors in the given assembly code.

The format of machine code is <op code - 5 bits>_<unused bits>_<register - 3 bits>_<register - 3 bits/memory address - 7 bits>
After checking for errors and stroing defined set of variables, instructions are assigned memory starting from 0th address.
Each instruction is assembled line-by-line, starting frm first non-declarative instruction, until it encounters the 'hlt' instruction.
'FLAGS' register is used only with 'mov' operation
