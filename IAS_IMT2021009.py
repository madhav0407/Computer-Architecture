#memory is taken as an array (list)
memory=list(range(1,1000))

# Values of PC,AC and MQ are initialised to '0'
PC=0
AC=0
MQ=0
count=0

'''
    00000000: HALT
    00000001: LOAD M[X]
    00100001: STOR M[X]
    00000101: ADD M[X]
    00000110: SUB M[X]
    00001100: DIV M[X]
    00001010: LOAD MQ
    00001011: MUL M[X]
    00001001: LOAD MQ,M[X]
'''

# This function performs instruction fetch, decodes and also executes the function
def final(x):
    #All of the following variables are made to be global variables
    global PC
    global AC
    global MQ
    global MAR
    global MBR
    global IBR
    global IR
    global count

    #count keeps track of the instruction number
    count=count+1

    print('---------------------')
    print(f'INSTRUCTION {count}')
    print('---------------------')

    #Instruction fetch for the left instruction
    print('LEFT HAND INSTRUCTION')
    MAR=PC
    print('PC is',PC)
    print('MAR is',MAR)
    MBR=x
    IBR=MBR[20:40]
    IR=MBR[0:8]
    MAR=MBR[8:20]

    print('MBR is',MBR)
    print('IBR is',IBR)
    print('IR is',IR)
    print('MAR is',MAR)

    for i in range (0,2):

        #Logic: All if condtions check for opcode stored in IR and decode the instruction
        #Following the if condition, the instructions are executed.

        #LOAD M[X]
        if (IR=='00000001'):
            MBR=memory[(int(MAR,2))]
            AC=MBR
            print ('AC is',AC)
            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue
                
        
        #STOR M[X]
        if (IR=='00100001'):
            MBR=AC
            memory[(int(MAR,2))]=MBR
            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue


        #ADD M[X]
        if (IR=='00000101'):
            MBR=memory[(int(MAR,2))]
            AC=AC+MBR
            if (AC>2**40):
                print("Overflow")
                quit()
            print('AC is',AC)
            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue


        #SUB M[X]
        if (IR=='00000110'):
            MBR=memory[(int(MAR,2))]
            AC=AC-MBR
            print('AC is',AC)
            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue
        
        #DIV M[X]
        if (IR=='00001100'):
            MBR=memory[(int(MAR,2))]
            MQ=AC//MBR
            AC=AC%MBR

            print('MQ is',MQ)
            print('AC is',AC)
            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue

        #LOAD MQ
        if (IR=='00001010'):
            AC=MQ
            print('AC is',AC)
            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue

        #MUL M[X]
        if (IR=='00001011'):
            MBR=memory[(int(MAR,2))]
            MBR=MBR*MQ
            MBR=str(bin(MBR)).replace("0b","")
            zeroes=''
            for j in range(len(MBR),80):
                zeroes = zeroes+'0'
            MBR = zeroes + MBR
            if (int(MBR,2)>2**80):
                print("Overflow")
                quit()

            AC=int(MBR[0:41],2)
            MQ=int(MBR[41:80],2)

            print('AC is',AC)
            print('MQ is',MQ)

            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue
        
        #LOAD MQ,M[X]
        if (IR=='00001001'):
            MBR=memory[(int(MAR,2))]
            MQ=MBR

            print('MQ is',MQ)
            #Instruction fetch for the right instruction
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                IR=IBR[0:8]
                MAR=IBR[8:20]
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
                continue

        #'00000000'=Opcode for Halt
        if (IR=='00000000'):
            if (i==0):
                print ('RIGHT HAND INSTRUCTION')
                PC=PC+1

                print('PC is',PC)
                print('IR is',IR)
                print('MAR is',MAR)
            return
    return

    

#User input for choice of program the user wants to execute
x=int(input('What is your choice?\n 1 for SIMPLE ADDITION\n 2 for SIMPLE SUBTRACTION\n 3 for AVERAGE OF TWELVE NUMBERS\n 4 for PRODUCT OF THIRTEEN NUMBERS\n'))

# Addition
if (x==1):

    #User input for the two numbers
    y=int(input('Enter first number : '))
    z=int(input('Enter second number : '))

    #Numbers are stored in memory
    memory[50]=y
    memory[51]=z

    memory[0]='0000000100000011001000000101000000110011' #'LOAD M[50]', 'ADD M[51]'
    memory[1]='0010000100000011010000000000000000000000' #'STOR M[52]', 'HALT'

    #Function is called for instructions
    final(memory[0])
    final(memory[1])

    #Printing the final sum
    print('Sum is',memory[52])

# Subtraction
if (x==2):

    #User input for the two numbers
    y=int(input('Enter first number : '))
    z=int(input('Enter second number : '))
    
    #Numbers are stored in memory
    memory[50]=y
    memory[51]=z

    memory[0]='0000000100000011001000000110000000110011' #'LOAD M[50]', 'SUB M[51]'
    memory[1]='0010000100000011010000000000000000000000' #'STOR M[52]', 'HALT'

    #Function is called for instructions
    final(memory[0])
    final(memory[1])

    #Printing the final result
    print('Difference is',memory[52])

# Average of twelve numbers
if (x==3):

    #User input for the twelve numbers
    y=[int(i) for i in input().split()]

    #Numbers(data) stored in memory
    memory[50]=y[0]
    memory[51]=y[1]
    memory[52]=y[2]
    memory[53]=y[3]
    memory[54]=y[4]
    memory[55]=y[5]
    memory[56]=y[6]
    memory[57]=y[7]
    memory[58]=y[8]
    memory[59]=y[9]
    memory[60]=y[10]
    memory[61]=y[11]
    memory[63]=12

    memory[0]='0000000100000011001000000101000000110011' #'LOAD M[50]', 'ADD M[51]'
    memory[1]='0000010100000011010000000101000000110101' #'ADD M[52]', 'ADD M[53]'
    memory[2]='0000010100000011011000000101000000110111' #'ADD M[54]','ADD M[55]'
    memory[3]='0000010100000011100000000101000000111001' #'ADD M[56]','ADD M[57]'
    memory[4]='0000010100000011101000000101000000111011' #'ADD M[58]', 'ADD M[59]'
    memory[5]='0000010100000011110000000101000000111101' #'ADD M[60]', 'ADD M[61]'
    memory[6]='0000110000000011111100001010000000000000' #'DIV M[63]', 'LOAD MQ' # Assumed address field as '000000000000' for LOAD MQ instruction
    memory[7]='0010000100000011111000000000000000000000' #'STOR M[62]','HALT'

    #Function is called for instructions
    final(memory[0])
    final(memory[1])
    final(memory[2])
    final(memory[3])
    final(memory[4])
    final(memory[5])
    final(memory[6])
    final(memory[7])

    #Printing the final result
    print('Average is',memory[62])


# Product of thirteen numbers
if (x==4):

    #User input for the thirteen numbers
    y=[int(i) for i in input().split()]

    #Numbers(data) stored in memory
    memory[50]=y[0]
    memory[51]=y[1]
    memory[52]=y[2]
    memory[53]=y[3]
    memory[54]=y[4]
    memory[55]=y[5]
    memory[56]=y[6]
    memory[57]=y[7]
    memory[58]=y[8]
    memory[59]=y[9]
    memory[60]=y[10]
    memory[61]=y[11]
    memory[62]=y[12]

    memory[0]='0000100100000011001000001011000000110011' #'LOAD MQ,M[50]', 'MUL M[51]'
    memory[1]='0000101100000011010000001011000000110101' #'MUL M[52]', 'MUL M[53]'
    memory[2]='0000101100000011011000001011000000110111' #'MUL M[54]', 'MUL M[55]'
    memory[3]='0000101100000011100000001011000000111001' #'MUL M[56], 'MUL M[57]'
    memory[4]='0000101100000011101000001011000000111011' #'MUL M[58]', 'MUL M[59]'
    memory[5]='0000101100000011110000001011000000111101' #'MUL M[60]', 'MUL M[61]'
    memory[6]='0000101100000011111000001010000000000000' #'MUL M[62]', 'LOAD MQ'
    memory[7]='0010000100000011111100000000000000000000' #'STOR M[63]', 'HALT'

    #Function call for instructions
    final(memory[0])
    final(memory[1])
    final(memory[2])
    final(memory[3])
    final(memory[4])
    final(memory[5])
    final(memory[6])
    final(memory[7])

    #Printing the final result
    print('Final Product is',memory[63])







    


