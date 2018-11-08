def simulate(I,Nsteps):
    print("Project 3  Group 17 Ulitmately Simple: Simulator")
    PC = 0 #prgram counter
    DIC= 0
    Reg = [0,0,0,0]
   # Memory = [0 for i in range(10)] # data memory, 
   print("********** Simluation starts **********")
   finished = False
   while( not(finished)):
        fetch = Instructions[PC]
        DIC += 1
        print(fetch)
        
def main():
    //instr_file = open("P1_Instruction.txt","r")
    data_file = open("project3_group_17_p1_bin.txt" ,"r")
    data_file2 = open("project3_group_17_p2_bin.txt", "r")
    #we need a file for the data set
    #Nsteps = 3  #How many cycles to run before output
    Nlines = 0   #How may instrs total in input.txt
    Instructions = [] #all instructions will be stored here
    Memory = []
    print( " ECE 366 Group 8")
	#print( " 1 = simulator")
    print( " 2 = disassembler")
    #print( " 3 = assembler")
	
    mode= int(input( "Please enter the mode of Program: "))
    print( "Mode selected: ",end=" ")
    modedis= int(input( "Please enter the which program 1 or 2:  "))
    print( "Mode selected: ", end=" ")
    
    #if(mode== 1):
        #print("Simulator")
    #elif(mode== 2):
       # print( "disassembler")
        #disassembler(Instructions,Nlines)
    #elif(mode== 3):
       # print( "assembler")
	    #assemble(Instructions, Nlines)
    
		
    #for line in instr_file: # Reading in the instructions
    #    if (line == "/n" or line[0] == '#'):  #empty lines, comments ignored
    #       line = line.replace("\n"," ")
    #        Instructions.append(line)             #Copy all instruction into a list
        #Nline+=1
		
    #for line in data_file: # Read in data P1_Machine.txt
     #   if(line== "\n" or line[0] =='#'):
	 #      continue
      #  Memory.append(line)
        #Nlines+=1
    if(mode == 1): #Check whether to use disassembler of assembler or simulator
        #simulator(Instructions,Nsteps,debug_mode,Memory)
        print("assembler")
    elif(mode== 2):
        if (modedis == 1):
            for line in data_file: # Read in data P1_Machine.txt
                if(line== "\n" or line[0] =='#'):
                    continue
                Memory.append(line)
                Nlines+=1
        elif(modedis == 2):
            for line in data_file2: # Read in data P1_Machine.txt
                if(line== "\n" or line[0] =='#'):
                    continue
                Memory.append(line)
                Nlines+=1
        else:
            print("That is not one of the options")
            
        disassembler(Memory,Nlines)
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
	
if __name__ == "__main__":
    main()
	