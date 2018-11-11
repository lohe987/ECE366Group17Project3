def disassember(M, Nlines, mode):
    print("ECE 366 Group 17 Disassembler")
    print("----------------")
    if(mode == 1)
        output_file = open("project2_group_17_p1_asm.txt", "w")
    if(mode == 2)
        output_file = open("project2_group_17_p2_asm.txt", "w")
    else
        print("Invalid Mode")
        break
    
    
	#write to output file
    for i in range(Nlines):
         if(line[0:7] == "0000000"):
            output_file.write("lw $7, P            #$7 = P \n")
        elif(line[0:7] == "0000001"):
            output_file.write("add $9, $0, 1       #$9 = 1\n")
        elif(line[0:7] == "0000010"):
            output_file.write("addi $10, $0, $0    # $10 =0 = counter N =exponent\n")
        elif(line[0:7] == "0000011"):
            output_file.write("andi $10, $7, 1     # $10-$7 and 1(0/1) \n")
        elif(line[0:7] == "0000100"):
            output_file.write("srl $7, $7, 1       # $7 >>1 \n")
        elif(line[0:7] == "0000101"):
            output_file.write("beq $10, $0, Mult2  # if zero go to Mult2")
        elif(line[0:7] == "0000110"):
            output_file.write("add $10, $9, $9     # temp $10 = $9 + $9 + $10 =2\n")
        elif(line[0:7] == "0000111"):
            output_file.write("add $9, $9, $9      # $9 = $9 + $9 =$9 =2 $0\n")
        elif(line[0:7] == "0001000"):
            output_file.write("add $9, $10, $9     # $9 = $10 +$9 = $9 = 6\n")
        elif(line[0:7] == "0001001"):
            output_file.write("beq $10, $0, Mult4  # $if zero, go Mult2, check to multiply next bit by 4, else multiply by 2\n")
        elif(line[0:7] == "0001010"):
            output_file.write("beq $10, $0, Mult16  # $if zero, go Mult2, check to multiply next bit by 16, else MOD")
        elif(line[0:7] == "0001011"):
            output_file.write("beq $10, $0, Mod     # $if zero, go Mult2, check yo multiply next bit by 4, else multiply by 2\n")
        elif(line[0:7] == "0001100"):
            output_file.write("slti $10, $9, 17     # if $9< $8, $10 = 1, else $10 = 0, these next 3 lines will subract by 17 until the is only the remainder\n")
        elif(line[0:7] == "0001101"):
            output_file.write("bne $10, $0, End     # if($10 = 1) Save2, else cont\n")
        elif(line[0:7] == "0001110"):
            output_file.write("subi  $9, $9, 17 	# $9 = $9 -17 = 36 -17 = 19\n")
        elif(line[0:7] == "0001111"):
            output_file.write("j Mod	            # Will loop back to Mod to get remainder  \n")
        elif(line[0:7] == "0010000"):
            output_file.write("sw $9, R	            #Stores the remainder value into R\n")
        elif(line[0:7] == "0010001"):
            output_file.write("addi $5  $0, 0	    # Counter i \n")
        elif(line[0:7] == "0010010"):
            output_file.write("addi $7  $0, 0   	# Counter J\n")
        elif(line[0:7] == "0010011"):
            output_file.write("addi $6  $0, 400	    # stop value of array\n")
        elif(line[0:7] == "0010100"):
            output_file.write("beq  $5, $6, Exit	# if $5 = 400, Exit program\n")
        elif(line[0:7] == "0010101"):
            output_file.write("lw   $1, 0xC($0)	# $1 = T = Value to compare to / first Anded value\n")
        elif(line[0:7] == "0010110"):
            output_file.write("lw   $2, 0x2020($5)	# $2 = mem(0x2020 + $5)\n")
        elif(line[0:7] == "0010111"):
            output_file.write("addi $5, $5, 4	    # Increment $5 for next array index\n")
        elif(line[0:7] == "0011000"):
            output_file.write("addi $15, $15, 1\t\t\tIf they are equal, the score is incrementedand  $1, $1, $2	# $1 = $1 and $2 = T and Array(i) = Anded value/rid of T to save on registers\n")
        elif(line[0:7] == "0011001"):
            output_file.write("addi $8  $0, 16	# stop value for bit \n")
        elif(line[0:7] == "0011010"):
            output_file.write("beq  $7, $8, Save	# Once $7 equals 16, go to next array index\n")
        elif(line[0:7] == "0011011"):
            output_file.write("addi $7, $7, 1	# Increment $7 by 1\n")
        elif(line[0:7] == "0011100"):
            output_file.write("andi $2, $1, 1	# $2 = $1 and 1 = Anded value and 1, $2 is temp value\n")
        elif(line[0:7] == "0011101"):
            output_file.write("add  $3, $3, $2	# counts # of 1s in $1 (# of matching bits)\n")
        elif(line[0:7] == "0011110"):
            output_file.write("srl  $1, $1, 1	# $1 = $1 >> 1, reduces it by 1 bit till = 0\n")
        elif(line[0:7] == "0011111"):
            output_file.write("j    Compare	    # now Compare with old values\n")
        elif(line[0:7] == "0100000"):
            output_file.write("lw   $1, 0x2010($0)	# reuse $1 = S\n")
        elif(line[0:7] == "0100001"):
            output_file.write("lw   $2, 0x2014($0)	# reuse $2 = C\n")
        elif(line[0:7] == "0100010"):
            output_file.write("slt  $6, $1, $3	# $6 = 1 if( $1(S) < $3), else $6 = 0\n")
        elif(line[0:7] == "0100011"):
            output_file.write("beq  $6, $0, Check1	# if (s>= $3 then $6 = 0) => if ($6 = 0) go to check 1, else continue\n")
        elif(line[0:7] == "0100100"):
            output_file.write("\add  $1, $0, $3	# $1 = $3, $1 will now take highest value\n")
        elif(line[0:7] == "0100101"):
            output_file.write("addi $2, $0, 1	# $2(T) will be set to one since it's first highest value\n")
        elif(line[0:7] == "0100110"):
            output_file.write("sw   $1, 0x2010($0)	# mem(0x2010) = $1 = S\n")
        elif(line[0:7] == "0100111"):
            output_file.write("sw   $2, 0x2014($0)	# mem(0x2014) = $2 = T\n")
        elif(line[0:7] == "0101000"):
            output_file.write("j    Start	# start over/chech next array\n")
        elif(line[0:7] == "0101001"):
            output_file.write("beq  $1, $3, Check2	# if ($1 = $3) go to check 2, else continue\n")
        elif(line[0:7] == "0101010"):
            output_file.write("addi $2, $2, 1	# Increment 2(T) by 1 since matching count was found\n")
        else
            output_file.write("Instructions not supported/n")
        
def simulate(Instructions,Memory,Nlines,Memlines):
    print("Project 3  Group 17 Ulitmately Simple: Simulator")
    PC = 0 #prgram counter
    DIC= 0 #dynamic instruction counter
    Reg = [0,0,0,0,0,0,0,0,0,0] # intializing all ten registers to zero
   # Memory = [0 for i in range(10)] # data memory, 
   print("********** Simluation starts **********")
   finished = False
   while( not(finished)):
        fetch = Instructions[PC]
        DIC += 1
        print(fetch)
    
    for i in range(Nlines):
         if(line[0:7] == "0000000"):
            #output_file.write("lw $7, P            #$7 = P \n")
        elif(line[0:7] == "0000001"):
            #output_file.write("add $9, $0, 1       #$9 = 1\n")
        elif(line[0:7] == "0000010"):
            #output_file.write("addi $10, $0, $0    # $10 =0 = counter N =exponent\n")
        elif(line[0:7] == "0000011"):
            #output_file.write("andi $10, $7, 1     # $10-$7 and 1(0/1) \n")
        elif(line[0:7] == "0000100"):
            #output_file.write("srl $7, $7, 1       # $7 >>1 \n")
        elif(line[0:7] == "0000101"):
            #output_file.write("beq $10, $0, Mult2  # if zero go to Mult2")
        elif(line[0:7] == "0000110"):
            #output_file.write("add $10, $9, $9     # temp $10 = $9 + $9 + $10 =2\n")
        elif(line[0:7] == "0000111"):
            #output_file.write("add $9, $9, $9      # $9 = $9 + $9 =$9 =2 $0\n")
        elif(line[0:7] == "0001000"):
            #output_file.write("add $9, $10, $9     # $9 = $10 +$9 = $9 = 6\n")
        elif(line[0:7] == "0001001"):
            #output_file.write("beq $10, $0, Mult4  # $if zero, go Mult2, check to multiply next bit by 4, else multiply by 2\n")
        elif(line[0:7] == "0001010"):
            #output_file.write("beq $10, $0, Mult16  # $if zero, go Mult2, check to multiply next bit by 16, else MOD")
        elif(line[0:7] == "0001011"):
            #output_file.write("beq $10, $0, Mod     # $if zero, go Mult2, check yo multiply next bit by 4, else multiply by 2\n")
        elif(line[0:7] == "0001100"):
            #output_file.write("slti $10, $9, 17     # if $9< $8, $10 = 1, else $10 = 0, these next 3 lines will subract by 17 until the is only the remainder\n")
        elif(line[0:7] == "0001101"):
            #output_file.write("bne $10, $0, End     # if($10 = 1) Save2, else cont\n")
        elif(line[0:7] == "0001110"):
            #output_file.write("subi  $9, $9, 17 	# $9 = $9 -17 = 36 -17 = 19\n")
        elif(line[0:7] == "0001111"):
            #output_file.write("j Mod	            # Will loop back to Mod to get remainder  \n")
        elif(line[0:7] == "0010000"):
            #output_file.write("sw $9, R	            #Stores the remainder value into R\n")
        elif(line[0:7] == "0010001"):
            #output_file.write("addi $5  $0, 0	    # Counter i \n")
        elif(line[0:7] == "0010010"):
            #output_file.write("addi $7  $0, 0   	# Counter J\n")
        elif(line[0:7] == "0010011"):
            #output_file.write("addi $6  $0, 400	    # stop value of array\n")
        elif(line[0:7] == "0010100"):
            #output_file.write("beq  $5, $6, Exit	# if $5 = 400, Exit program\n")
        elif(line[0:7] == "0010101"):
            #output_file.write("lw   $1, 0xC($0)	# $1 = T = Value to compare to / first Anded value\n")
        elif(line[0:7] == "0010110"):
            #output_file.write("lw   $2, 0x2020($5)	# $2 = mem(0x2020 + $5)\n")
        elif(line[0:7] == "0010111"):
            #output_file.write("addi $5, $5, 4	    # Increment $5 for next array index\n")
        elif(line[0:7] == "0011000"):
            #output_file.write("addi $15, $15, 1\t\t\tIf they are equal, the score is incrementedand  $1, $1, $2	# $1 = $1 and $2 = T and Array(i) = Anded value/rid of T to save on registers\n")
        elif(line[0:7] == "0011001"):
            #output_file.write("addi $8  $0, 16	# stop value for bit \n")
        elif(line[0:7] == "0011010"):
            #output_file.write("beq  $7, $8, Save	# Once $7 equals 16, go to next array index\n")
        elif(line[0:7] == "0011011"):
            #output_file.write("addi $7, $7, 1	# Increment $7 by 1\n")
        elif(line[0:7] == "0011100"):
            #output_file.write("andi $2, $1, 1	# $2 = $1 and 1 = Anded value and 1, $2 is temp value\n")
        elif(line[0:7] == "0011101"):
            #output_file.write("add  $3, $3, $2	# counts # of 1s in $1 (# of matching bits)\n")
        elif(line[0:7] == "0011110"):
            #output_file.write("srl  $1, $1, 1	# $1 = $1 >> 1, reduces it by 1 bit till = 0\n")
        elif(line[0:7] == "0011111"):
            #output_file.write("j    Compare	    # now Compare with old values\n")
        elif(line[0:7] == "0100000"):
            #output_file.write("lw   $1, 0x2010($0)	# reuse $1 = S\n")
        elif(line[0:7] == "0100001"):
            #output_file.write("lw   $2, 0x2014($0)	# reuse $2 = C\n")
        elif(line[0:7] == "0100010"):
            #output_file.write("slt  $6, $1, $3	# $6 = 1 if( $1(S) < $3), else $6 = 0\n")
        elif(line[0:7] == "0100011"):
            #output_file.write("beq  $6, $0, Check1	# if (s>= $3 then $6 = 0) => if ($6 = 0) go to check 1, else continue\n")
        elif(line[0:7] == "0100100"):
            #output_file.write("\add  $1, $0, $3	# $1 = $3, $1 will now take highest value\n")
        elif(line[0:7] == "0100101"):
            #output_file.write("addi $2, $0, 1	# $2(T) will be set to one since it's first highest value\n")
        elif(line[0:7] == "0100110"):
            #output_file.write("sw   $1, 0x2010($0)	# mem(0x2010) = $1 = S\n")
        elif(line[0:7] == "0100111"):
            #output_file.write("sw   $2, 0x2014($0)	# mem(0x2014) = $2 = T\n")
        elif(line[0:7] == "0101000"):
            #output_file.write("j    Start	# start over/chech next array\n")
        elif(line[0:7] == "0101001"):
            #output_file.write("beq  $1, $3, Check2	# if ($1 = $3) go to check 2, else continue\n")
        elif(line[0:7] == "0101010"):
            #output_file.write("addi $2, $2, 1	# Increment 2(T) by 1 since matching count was found\n")
        else
            #output_file.write("Instructions not supported/n")
     
     
def main():
    #instr_file = open("P1_Instruction.txt","r")
    data_file = open("project3_group_17_p1_bin.txt" ,"r")
    data_file2 = open("project3_group_17_p2_bin.txt", "r")
    data_fileA = open("patternA.txt", "r")
    data_fileB = open("patternB.txt", "r")
    #we need a file for the data set
    #Nsteps = 3  #How many cycles to run before output
    Nlines = 0   #How may instrs total in input.txt
    MemLines = 0
    Instructions = [] #all instructions will be stored here
    Memory = [] # where the data is being stored
    print( " ECE 366 Group 8")
	print( " 1 = simulator")
    print( " 2 = disassembler")
    print( " 3 = assembler")

    mode= int(input( "Please enter the mode of Program: "))
    print( "Mode selected: ",end=" ")
    #modedis= int(input( "Please enter the which program 1 or 2:  "))
    #print( "Mode selected: ", end=" ")
    pattern = char(input( "Please enter the which pattern A or B: ")
    print( "Pattern selected: ", end=" ")
    #if (modedis == 1):
    P = int(input( "Program 1 was selected, What is the value of P: ")
    print( "P selected: ", end=" ")
    q = 17;
    Memory[1]= q;
    result = 0;
       #Memory[2] = result; #yo bitch use this in a another place 
    #if (modeis == 2):
    T = int(input( " Program 2 was selected, What is the 16 bit value of T: ")
    print( "T selected: ", end=" ")
    s = 0;
    c = 0;
    Memory[4] = s
    Memory[5] = c
        
    
    for line in data_fileA: #read in the pattern A data
        if(pattern == A):
            if(line== "\n" or line[0] =='#'):
                    continue
                Memory.append(line)
                MemLines+=1
        if(pattern == B): #reads in the pattern B data
            if(line== "\n" or line[0] =='#'):
                    continue
                Memory.append(line)
                MemLines+=1
        else
            print(" Incorrect pattern input ")
            
    if (modedis == 1):
            for line in data_file: # Read in data P1
                if(line== "\n" or line[0] =='#'):
                    continue
                Instructions.append(line)
                Nlines+=1
        elif(modedis == 2):
            for line in data_file2: # Read in data  from P2
                if(line== "\n" or line[0] =='#'):
                    continue
                Istructions.append(line)
                Nlines+=1
        else:
            print("That is not one of the options")
            
        
                
    if(mode == 1): #Check whether to use disassembler of assembler or simulator
        simulate(Instructions,Memory,Nlines,Memlines)
        print("simulator")
        
    elif(mode== 2):
        disassembler(Instructions,Nlines,mode)
        print("disassembler is being done")
    elif(mode== 3):
        #assembler(Instructions,Nlines)
        print("assembler is being done")
    else:
        print("Error. Unrecognized mode. Exiting")
        exit()
		
    #instr_file.close()
    data_file2.close()
    data_file.close()
    data_fileA.close()
    data_fileB.close()
	
if __name__ == "__main__":
    main()
	