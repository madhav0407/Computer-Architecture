IAS IMPLEMENTATION IN PYTHON: 

In the assignment, the task was to emulate a few operations in IAS architecture.

The registers present in IAS architecture are:
AC  : Accumulator: It holds the results of ALU operations

IR  : Instructions Register: It stores the 8 bit opcode of the instruction that is to be executed
	
IBR : Instructions Buffer register: Holds the RHS instruction

MQ  : Multiplier/Quotioent Register: Holds LSB of product and also the quotient after division

MBR : Memory Buffer register: Contains a word that is read by in memory or the input/output

MAR : Memory Adress register: Specifies the address in memory of the word to be written/read into MBR

PC  : Program Counter: Stores the address of the next instruction to be executed

A program is performed in 3 cycles:

i) Fetch cycle:
	 First, the opcode of the instruction to be executed is loaded into the IR and the address portion is loaded into the MAR from the PC. 
	 In this phase the PC value is stored in the MAR and the value at the memory location stored in MAR is written into the MBR.
         Once this is done, the Opcode of the Left instruction is loaded into the IR and the address portion is loaded into the MAR and the right instruction is loaded into the 		 		 Instruction Buffer Register(IBR).

ii) Decode Cycle:
		In this phase the intruction is decoded based on the instruction OPCODE and the data stored in the registers. The "binary data" is well read and converted into an assembly
               language for the execute phase.
	
iii) Execute Cycle: 
		 In this phase the ALU performs the tasks as specified by the assembly language for a 
                particular program.


I have executed the following programs to show the working of IAS architecture:

 1 -> Simple Addition
 2 -> Simple Subtraction (2nd Number - 1st Number)
 3 -> Average of twelve numbers
 4 -> Product of thirteen numbers


=============================
** IMT2021009 Madhav Sood **
=============================
