
def disassembler(I, lines, mode):
    print("ECE 366 Group 17 Disassembler")
    print("----------------")
    if(mode == 1):
        output_file = open("project3_group_17_p1_asm.txt", "w")
    elif(mode == 2):
        output_file = open("project3_group_17_p2_asm.txt", "w")
    else:
        print("Invalid Mode")
   # output_file.write("This is a test before loop")
    print( lines)
	#write to output file
    for i in range(lines):
        line =I[i]
        #output_file.write("This is a Test in loop")
        if(line[0:8] == "00000000"):
            output_file.write("lw $7, P            #$7 = P \n")
        elif(line[0:8] == "00000011"):
            output_file.write("add $9, $0, 1       #$9 = 1\n")
        elif(line[0:8] == "00000101"):
            output_file.write("addi $10, $0, $0    # $10 =0 = counter N =exponent\n")
        elif(line[0:8] == "00000110"):
            output_file.write("andi $10, $7, 1     # $10-$7 and 1(0/1) \n")
        elif(line[0:8] == "00001001"):
            output_file.write("srl $7, $7, 1       # $7 >>1 \n")
        elif(line[0:8] == "00001010"):
            output_file.write("beq $10, $0, Mult2  # if zero go to Mult2\n")
        elif(line[0:8] == "00001100"):
            output_file.write("add $10, $9, $9     # temp $10 = $9 + $9 + $10 =2\n")
        elif(line[0:8] == "00001111"):
            output_file.write("add $9, $9, $9      # $9 = $9 + $9 =$9 =2 $0\n")
        elif(line[0:8] == "00010001"):
            output_file.write("add $9, $10, $9     # $9 = $10 +$9 = $9 = 6\n")
        elif(line[0:8] == "00010010"):
            output_file.write("beq $10, $0, Mult4  # $if zero, go Mult2, check to multiply next bit by 4, else multiply by 2\n")
        elif(line[0:8] == "00010100"):
            output_file.write("beq $10, $0, Mult16  # $if zero, go Mult2, check to multiply next bit by 16, else MOD\n")
        elif(line[0:8] == "00010111"):
            output_file.write("beq $10, $0, Mod     # $if zero, go Mult2, check yo multiply next bit by 4, else multiply by 2\n")
        elif(line[0:8] == "00011000"):
            output_file.write("slti $10, $9, 17     # if $9< $8, $10 = 1, else $10 = 0, these next 3 lines will subract by 17 until the is only the remainder\n")
        elif(line[0:8] == "00011011"):
            output_file.write("bne $10, $0, End     # if($10 = 1) Save2, else cont\n")
        elif(line[0:8] == "00011101"):
            output_file.write("subi  $9, $9, 17 	# $9 = $9 -17 = 36 -17 = 19\n")
        elif(line[0:8] == "00011110"):
            output_file.write("j Mod	            # Will loop back to Mod to get remainder  \n")
        elif(line[0:8] == "00100001"):
            output_file.write("sw $9, R	            #Stores the remainder value into R\n")
        elif(line[0:8] == "00100010"):
            output_file.write("addi $5  $0, 0	    # Counter i \n")
        elif(line[0:8] == "00100100"):
            output_file.write("addi $7  $0, 0   	# Counter J\n")
        elif(line[0:8] == "00100111"):
            output_file.write("addi $6  $0, 400	    # stop value of array\n")
        elif(line[0:8] == "00101000"):
            output_file.write("beq  $5, $6, Exit	# if $5 = 400, Exit program\n")
        elif(line[0:8] == "00101011"):
            output_file.write("lw   $1, 0xC($0)	# $1 = T = Value to compare to / first Anded value\n")
        elif(line[0:8] == "00101101"):
            output_file.write("lw   $2, 0x2020($5)	# $2 = mem(0x2020 + $5)\n")
        elif(line[0:8] == "00101110"):
            output_file.write("addi $5, $5, 4	    # Increment $5 for next array index\n")
        elif(line[0:8] == "00110000"):
            output_file.write("and  $1, $1, $2	# $1 = $1 and $2 = T and Array(i) = Anded value/rid of T to save on registers\n")
        elif(line[0:8] == "00110011"):
            output_file.write("addi $8  $0, 16	# stop value for bit \n")
        elif(line[0:8] == "00110101"):
            output_file.write("beq  $7, $8, Save	# Once $7 equals 16, go to next array index\n")
        elif(line[0:8] == "00110110"):
            output_file.write("addi $7, $7, 1	# Increment $7 by 1\n")
        elif(line[0:8] == "00111001"):
            output_file.write("andi $2, $1, 1	# $2 = $1 and 1 = Anded value and 1, $2 is temp value\n")
        elif(line[0:8] == "00111010"):
            output_file.write("add  $3, $3, $2	# counts # of 1s in $1 (# of matching bits)\n")
        elif(line[0:8] == "00111100"):
            output_file.write("srl  $1, $1, 1	# $1 = $1 >> 1, reduces it by 1 bit till = 0\n")
        elif(line[0:8] == "00111111"):
            output_file.write("j    Compare	    # now Compare with old values\n")
        elif(line[0:8] == "01000001"):
            output_file.write("lw   $1, 0x2010($0)	# reuse $1 = S\n")
        elif(line[0:8] == "01000010"):
            output_file.write("lw   $2, 0x2014($0)	# reuse $2 = C\n")
        elif(line[0:8] == "01000100"):
            output_file.write("slt  $6, $1, $3	# $6 = 1 if( $1(S) < $3), else $6 = 0\n")
        elif(line[0:8] == "01000111"):
            output_file.write("beq  $6, $0, Check1	# if (s>= $3 then $6 = 0) => if ($6 = 0) go to check 1, else continue\n")
        elif(line[0:8] == "01001000"):
            output_file.write("add  $1, $0, $3	# $1 = $3, $1 will now take highest value\n")
        elif(line[0:8] == "01001011"):
            output_file.write("addi $2, $0, 1	# $2(T) will be set to one since it's first highest value\n")
        elif(line[0:8] == "01001101"):
            output_file.write("sw   $1, 0x2010($0)	# mem(0x2010) = $1 = S\n")
        elif(line[0:8] == "01001110"):
            output_file.write("sw   $2, 0x2014($0)	# mem(0x2014) = $2 = T\n")
        elif(line[0:8] == "01010000"):
            output_file.write("j    Start	# start over/chech next array\n")
        elif(line[0:8] == "01010011"):
            output_file.write("beq  $1, $3, Check2	# if ($1 = $3) go to check 2, else continue\n")
        elif(line[0:8] == "01010101"):
            output_file.write("addi $2, $2, 1	# Increment 2(T) by 1 since matching count was found\n")
        elif(line[0:8] == "01010110"):
            output_file.write("slt $10, $9, $8      # if $9 < $8, $10 = 1, else $10 = 0\n")
        elif(line[0:8] == "01011001"):
            output_file.write("sub $9, $9, $8    # $16 = $16 -17 = 36 -17 = 19\n")
        else:
            output_file.write("Instructions not supported\n")
        
def simulate(I,Memory,Nlines,program):
    print("Project 3  Group 17 Ulitmately Simple: Simulator")
    PC = 0 #program counter
    DIC= 0 #dynamic instruction counter
    Reg = [0,0,0,0,0,0,0,0,0,0,0] # intializing all ten registers to zero, reg[0] is $0
    Mem = 8; # Where the memory for the  arrays starts
   # Memory = [0 for i in range(10)] # data memory, 
    print("********** Simluation starts **********")
   # finished = False
   #while( not(finished)):
    #    fetch = Instructions[PC]
     #   DIC += 1
      #  print(fetch)
    if (program == 1):
        max = 31 #When it will stop running the program for P1
    elif(program == 0):
        max = 10
    else:
        max = 32 # When it will stop running the program for P2
    while(PC < max):  # Based on the program length its the max pc can run
        line=I[PC]
        if(line[0:8] == "00000000"):
            #output_file.write("lw $7, P            #$7 = P \n")
            Reg[7] = int(Memory[0])
            Reg[8] = int(Memory[1]) # loads Q even thou its fixed at 17
            PC += 1             
        elif(line[0:8] == "00000011"):
            #output_file.write("add $9, $0, 1       #$9 = 1\n")
            Reg[9] = Reg[0] + 1
            PC += 1
        elif(line[0:8] == "00000101"):
            #output_file.write("addi $10, $0, $0    # $10 =0 = counter N =exponent\n")
            Reg[10] = 0
            PC += 1
        elif(line[0:8] == "00000110"):
            #output_file.write("andi $10, $7, 1     # $10-$7 and 1(0/1) \n")
            Reg[10] = Reg[7] + 1
            PC += 1
        elif(line[0:8] == "00001001"):
            #output_file.write("srl $7, $7, 1       # $7 >>1 \n")
            Reg[7] = Reg[7] >> 1
            PC +=1
            
        elif(line[0:8] == "00001010"):
            #output_file.write("beq $10, $0, Mult2  # if zero go to Mult2")
            if(Reg[10] == Reg[0]):
                PC = 12 #PC 11 should be Mult2
            else:
                PC += 1
                
        elif(line[0:8] == "00001100"):
            #output_file.write("add $10, $9, $9     # temp $10 = $9 + $9 + $10 =2\n")
            Reg[10] = Reg[9] +Reg[9]
            PC += 1
        elif(line[0:8] == "00001111"):
            #output_file.write("add $9, $9, $9      # $9 = $9 + $9 =$9 =2 $0\n")
            Reg[9] = Reg[9]+ Reg[9]
            PC += 1
        elif(line[0:8] == "00010001"):
            #output_file.write("add $9, $10, $9     # $9 = $10 +$9 = $9 = 6\n")
            Reg[9] = Reg[10]+ Reg[9]
            PC += 1
            
        elif(line[0:8] == "00010010"):
            #output_file.write("beq $10, $0, Mult4  # $if zero, go Mult2, check to multiply next bit by 4, else multiply by 2\n")
            if(Reg[10] == Reg[0]):
                PC = 16 # Mult4 should be PC 15
            else:
                PC += 1
                
        elif(line[0:8] == "00010100"):
            #output_file.write("beq $10, $0, Mult16  # $if zero, go Mult2, check to multiply next bit by 16, else MOD")
            if(Reg[10] == Reg[0]):
                PC = 21 #PC Mult16
            else:
                PC += 1
                
        elif(line[0:8] == "00010111"):
            #output_file.write("beq $10, $0, Mod     # $if zero, go Mult2, check to multiply next bit by 4, else multiply by 2\n")
            if(Reg[10] == Reg[0]):
                PC = 28 #PC for MOD
            else:
                PC += 1
                
        elif(line[0:8] == "00011000"):
            #output_file.write("slti $10, $9, 17     # if $9< $8, $10 = 1, else $10 = 0, these next 3 lines will subract by 17 until the is only the remainder\n")
            if( Reg[9] < Reg[8]):
                Reg[10] = 1
            else:
                Reg[10]= 0
                
            PC += 1
                
        elif(line[0:8] == "00011011"): #PC 28
            #output_file.write("bne $10, $0, End     # if($10 = 1) Save2, else cont\n")
            if( Reg[10] == 1): # or 10 != 0
                #PC = What ever "Save2"s 
                PC = 32 # should excute instruction with PC 31 then end
            else:
                PC += 1
                
        elif(line[0:8] == "00011101"):
            #output_file.write("subi  $9, $9, 17 	# $9 = $9 -17 = 36 -17 = 19\n")
            Reg[9] = Reg[9] - 17
            PC += 1
            
        elif(line[0:8] == "00011110"):
            #output_file.write("j Mod	            # Will loop back to Mod to get remainder  \n")
            PC= 28 # PC for MOD
            
        elif(line[0:8] == "00100001"):
            #output_file.write("sw $9, R	            #Stores the remainder value into R\n")
            Memory[2] = str(Reg[9]) #Memory[2] is R (result) !!Memory is a string not a int
            PC += 1
        
        elif(line[0:8] == "00100010"):
            #output_file.write("addi $5  $0, 0	    # Counter i \n")
            Reg[5] = Reg[0] + 0
            PC += 1
        elif(line[0:8] == "00100100"):
            #output_file.write("addi $7  $0, 0   	# Counter J\n")
            Reg[7] = Reg[0]+ 0
            PC += 1
        elif(line[0:8] == "00100111"):
            #output_file.write("addi $6  $0, 400	    # stop value of array\n")
            Reg[6] = Reg[0]+ 400
            PC += 1
        elif(line[0:8] == "00101000"):
            #output_file.write("beq  $5, $6, Exit	# if $5 = 400, Exit program\n")
            if (Reg[5] == 400):
                PC = 31
            else:
                PC += 1
                
        elif(line[0:8] == "00101011"):
            #output_file.write("lw   $1, 0xC($0)	# $1 = T = Value to compare to / first Anded value\n")
            Reg[1] = int(Memory[3])
            PC += 1
        elif(line[0:8] == "00101101"):
            #output_file.write("lw   $2, 0x2020($5)	# $2 = mem(0x2020 + $5)\n")
            Reg[2] = int(Memory[Mem +Reg[5]])
            PC +=1
            
        elif(line[0:8] == "00101110"):
            #output_file.write("addi $5, $5, 4	    # Increment $5 for next array index\n")
            Reg[5] = Reg[5]+ 1  #array index is only by one using python
            PC += 1
            
        elif(line[0:8] == "00110000"):
            #output_file.write("and  $1, $1, $2	# $1 = $1 and $2 = T and Array(i) = Anded value/rid of T to save on registers\n")
            Reg[1] = Reg[1]+ Reg[2]
            PC += 1
            
        elif(line[0:8] == "00110011"):
            #output_file.write("addi $8  $0, 16	# stop value for bit \n")
            Reg[8] = Reg[0] + 16
            PC += 1
            
        elif(line[0:8] == "00110101"):
            #output_file.write("beq  $7, $8, Save	# Once $7 equals 16, go to next array index\n")
            if( Reg[7] == Reg[8]):
                #PC = what ever "Save" is
                PC= 17
            else:
                PC += 1
                
        elif(line[0:8] == "00110110"):
            #output_file.write("addi $7, $7, 1	# Increment $7 by 1\n")
            Reg[7] = Reg[7]+ 1
            PC += 1 
        elif(line[0:8] == "00111001"):
            #output_file.write("andi $2, $1, 1	# $2 = $1 and 1 = Anded value and 1, $2 is temp value\n")
            Reg[2] = Reg[1]+ 1
            PC += 1
        elif(line[0:8] == "00111010"):
            #output_file.write("add  $3, $3, $2	# counts # of 1s in $1 (# of matching bits)\n")
            Reg[3] = Reg[3]+ Reg[2]
            PC += 1
        elif(line[0:8] == "00111100"):
            #output_file.write("srl  $1, $1, 1	# $1 = $1 >> 1, reduces it by 1 bit till = 0\n")
            Reg[1] = Reg[1] >> 1
            PC +=1
            
        elif(line[0:8] == "00111111"):
            #output_file.write("j    Compare	    # now Compare with old values\n")
            PC = 9
            
        elif(line[0:8] == "01000001"):
            #output_file.write("lw   $1, 0x2010($0)	# reuse $1 = S\n")
            Reg[1] = int(Memory[4])
            PC += 1
            
        elif(line[0:8] == "01000010"):
            #output_file.write("lw   $2, 0x2014($0)	# reuse $2 = C\n")
            Reg[2] = int(Memory[5])
            PC += 1
            
        elif(line[0:8] == "01000100"):
            #output_file.write("slt  $6, $1, $3	# $6 = 1 if( $1(S) < $3), else $6 = 0\n")
            if (Reg[1] < Reg[3]):
                Reg[6] = 1
            else:
                Reg[6] = 0
            PC +=1
            
        elif(line[0:8] == "01000111"):
            #output_file.write("beq  $6, $0, Check1	# if (s>= $3 then $6 = 0) => if ($6 = 0) go to check 1, else continue\n")
            if( Reg[1] >= Reg[3]):
                Reg[6] = 0
                PC +=1
            else:
                PC = 28
            
        elif(line[0:8] == "01001000"):
            #output_file.write("add  $1, $0, $3	# $1 = $3, $1 will now take highest value\n")
            Reg[1] = Reg[0]+ Reg[3]
            PC += 1
            
        elif(line[0:8] == "01001011"):
            #output_file.write("addi $2, $0, 1	# $2(T) will be set to one since it's first highest value\n")
            Reg[2] = Reg[0]+ 1
            PC += 1
            
        elif(line[0:8] == "01001101"):
            #output_file.write("sw   $1, 0x2010($0)	# mem(0x2010) = $1 = S\n")
            Memory[4] = str(Reg[1])
            PC += 1
            
        elif(line[0:8] == "01001110"):
            #output_file.write("sw   $2, 0x2014($0)	# mem(0x2014) = $2 = T\n")
            Memory[5] = str(Reg[2])
            PC += 1
            
        elif(line[0:8] == "01010000"):
            #output_file.write("j    Start	# start over/chech next array\n")
            PC = 3
        elif(line[0:8] == "01010011"):
            #output_file.write("beq  $1, $3, Check2	# if ($1 = $3) go to check 2, else continue\n")
            if (Reg[1] ==Reg[3]):
                PC = 28
            else:
                PC += 1
                
        elif(line[0:8] == "01010101"):
            #output_file.write("addi $2, $2, 1	# Increment 2(T) by 1 since matching count was found\n")
            Reg[2] = Reg[2]+ 1
            PC += 1
            
        elif(line[0:8] == "01010110"):
            #output_file.write("slt $10, $9, $8 \n")
            if (Reg[9] < Reg[8]):
                Reg[10] = 1
            else:
                Reg[10] = 0
            PC += 1
            
        elif(line[0:8] == "01011001"): #PC 29
            #output_file.write("sub $9, $9, $8 \n")
            Reg[9] = Reg[9] - Reg[8]
            PC += 1
        else:
            #output_file.write("Instructions not supported/n")
            print("instruction not supported")
        DIC+=1
        #print("PC value: ", PC)
        #print("Instruction[", PC, "]: ", I[PC-1])
    
    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R10: ",Reg) 
    print(" data Memory: Mem[0] to Mem[5]: \n", Memory[0],Memory[1], Memory[2],Memory[3], Memory[4],Memory[5] )
        
     
     
def main():
    data_file = open("project3_group_17_p1_bin.txt" ,"r")
    data_file2 = open("project3_group_17_p2_bin.txt", "r")
    data_file0 = open("project3_group_17_p0_bin.txt", "r")
    data_fileA = open("patternA.txt", "r")
    data_fileB = open("patternB.txt", "r")
    data_fileC = open("patternC.txt", "r")
    data_fileD = open("patternD.txt", "r")
    
    #we need a file for the data set
    #Nsteps = 3  #How many cycles to run before output
    Nlines = 0   #How may instrs total in input.txt for P1
    Mlines = 0   # How many instrs total in input.txt for P2
    MemLines = 0
    zlines = 0
    Instructions0 = []
    Instructions = [] #all instructions will be stored here for P1
    Instructions2 = [] #all instructions will be stored here for P2
    Memory = [] # where the data is being stored
    
    print( " ECE 366 Group 17")
    print( " 1 = simulator")
    print( " 2 = disassembler")
    print( " 3 = assembler")

    mode= input( "Please enter the mode of Program: ")
    print( "Mode selected: ", mode)
    #modedis= int(input( "Please enter the which program 1 or 2:  "))
    #print( "Mode selected: ", end=" ")
    pattern = input( "Please enter the which pattern A,B,C,D: ")
    print( "Pattern selected: ", pattern)
    
    #if (modedis == 1):
    #P = int(input( "Program 1 was selected, What is the value of P: ")
    #print( "P selected: ", end=" ")
    

        
    if (pattern == 'A'or'a'):
        for line in data_fileA:
            if(line == "\n" or line[0] =='#'):
                continue
            Memory.append(line)
            MemLines+=1
    elif(pattern == 'B'or'b'):
        for line in data_fileB:
            if(line == "\n" or line[0] =='#'):
                continue
            Memory.append(line)
            MemLines+=1
        if (Memory[1] != '0000000000010001'):
            Memory[1] = '0000000000010001'
            print(" Program 1 has fixed Q = 17 ")
    elif(pattern == 'C'or'c'):
        for line in data_fileC:
            if(line == "\n" or line[0] =='#'):
                continue
            Memory.append(line)
            MemLines+=1
        if (Memory[1] != '0000000000010001'):
            Memory[1] = '0000000000010001'
            print(" Program 1 has fixed Q = 17 ")
    elif(pattern == 'D'or'd'):
        for line in data_fileD:
            if(line == "\n" or line[0] =='#'):
                continue
            Memory.append(line)
            MemLines+=1
        if (Memory[1] != '0000000000010001'):
            Memory[1] = '0000000000010001'
            print(" Program 1 has fixed Q = 17 ")
    else:
        print(" Incorrect pattern input ")
            
            
    
    for line in data_file0: # Read in data  from P2
        if(line== "\n" or line[0] =='#'):
            continue
        Instructions0.append(line)
        zlines+=1
        
    for line in data_file: # Read in data P1
        if(line== "\n" or line[0] =='#'):
            continue
        Instructions.append(line)
        Nlines+=1
      
    for line in data_file2: # Read in data  from P2
        if(line== "\n" or line[0] =='#'):
            continue
        Instructions2.append(line)
        Mlines+=1
        
            
        
                
    if(mode == '1'): #Check whether to use disassembler, assembler or simulator
        simulate(Instructions0,Memory,zlines,0)
        print("simulation complete for Program 0 \n")
        # needs memory information printed here
        print("**************************************")
        simulate(Instructions,Memory,Nlines,1)
        print("simulation complete for Program 1 \n")
        # needs memory information printed here
        print("**************************************")
        simulate(Instructions2,Memory,Mlines,2)
        print("simulation complete for Program 2 \n")
        # needs memory information printed here
    elif(mode== '2'):
        disassembler(Instructions,Nlines,1)
        print("disassembler is done for P1")
        print("**************************************")
        disassembler(Instructions2,Mlines,2)
        print("disassembler is done for P2")
        print("**************************************")
    elif(mode== '3'):
    
        #assembler(Instructions,Nlines,1)
        #assembler(Instructions2,Mlines,2)
        print("assembler is being done")
    else:
        print("Error. Unrecognized mode. Exiting")
        exit()
        
    data_file2.close()
    data_file.close()
    data_fileA.close()
    data_fileB.close()
    data_fileC.close()
    data_fileD.close()
	
if __name__ == "__main__":
    main()
	