# Disassembler for project 2
#This code works for both program 1 and 2

input_file = open("project2_group_15_p1_bin.txt.txt", "r")
output_file = open("project2_group_15_p1_asm.txt", "w")

for line in input_file:
    if(line[0:7] == "0000000"):
        output_file.write("add $8, $18,$0\n")
    elif(line[0:7] == "0000001"):
        output_file.write("add $10, $0, $8\t\t\tTo calculate the modulus 17 we make succesive substractions\n")
    elif(line[0:7] == "0000010"):
        output_file.write("add $10, $0, $14\t\t\tIf not: then current score will be saved as best score\n")
    elif(line[0:7] == "0000011"):
        output_file.write("add $10, $18, $0\t\t\tWe add the result of the hamming count. If it's zero, then nothing happens\n")
    elif(line[0:7] == "0000100"):
        output_file.write("add $13, $13, $14\t\t\tWe add the result of the hamming count. If it's zero, then nothing happens\n")
    elif(line[0:7] == "0000101"):
        output_file.write("add $13, $0, $0\t\t\tWe will be storing the hamming distance in $13, therefore, we load a 0\n")
    elif(line[0:7] == "0000110"):
        output_file.write("add $13, $10, $0\n")
    elif(line[0:7] == "0000111"):
        output_file.write("add $14, $8, $0\n")
    elif(line[0:7] == "0001000"):
        output_file.write("add $14, $10, $0\t\t\tthe base is elevated to the power of two\n")
    elif(line[0:7] == "0001001"):
        output_file.write("add $18, $18, $14\t\t\tWe add the value $14 to the register $18\n")
    elif(line[0:7] == "0001010"):
        output_file.write("addi $8, $0, 1\n")
    elif(line[0:7] == "0001011"):
        output_file.write("addi $10, $0, 6\t\t\tconstant 6 is loaded into register 10\n")
    elif(line[0:7] == "0001100"):
        output_file.write("addi $11, $0, 20\t\t\tWe store the number of words in the array, useful for loops\n")
    elif(line[0:7] == "0001101"):
        output_file.write("addi $10, $10, -17\n")
    elif(line[0:7] == "0001110"):
        output_file.write("addi $11, $11, -1\n")
    elif(line[0:7] == "0001111"):
        output_file.write("addi $12, $0, 0x2000\t\t\tLoad the data address in $12 useful for loading operands\n")
    elif(line[0:7] == "0010000"):
        output_file.write("addi $12, $0, 17\t\t\tWe load a 17 for the modulus\n")
    elif(line[0:7] == "0010001"):
        output_file.write("addi $13, $13, -1\n")
    elif(line[0:7] == "0010010"):
        output_file.write("addi $14, $0, 32\n")
    elif(line[0:7] == "0010011"):
        output_file.write("addi $15, $0, 0x2000\t\t\tstart address of the data is stored in $15\n")
    elif(line[0:7] == "0010100"):
        output_file.write("addi $15, $0, 0x2004\t\t\tWe store the address to which the result shall be saved in the register $15\n")
    elif(line[0:7] == "0010101"):
        output_file.write("addi $15, $0, 20\t\t\tnumbers of words in the array\n")
    elif(line[0:7] == "0010110"):
        output_file.write("addi $15, $15, -1\t\t\tWe must do this for all words in the array\n")
    elif(line[0:7] == "0010111"):
        output_file.write("addi $15, $0, 0\t\t\tCounter of scores\n")
    elif(line[0:7] == "0011000"):
        output_file.write("addi $15, $15, 1\t\t\tIf they are equal, the score is incremented\n")
    elif(line[0:7] == "0011001"):
        output_file.write("addi $17, $17, 4\t\t\tAdvance to next array word\n")
    elif(line[0:7] == "0011010"):
        output_file.write("addi $17, $15, 0xC\t\t\taddress of the array is stored in $17\n")
    elif(line[0:7] == "0011011"):
        output_file.write("addi $17, $17, 4\t\t\tMove to the next position in the array\n")
    elif(line[0:7] == "0011100"):
        output_file.write("addi $17, $0, 0x2004\n")
    elif(line[0:7] == "0011101"):
        output_file.write("addi $17, $0, 0x205C\t\t\tHere we save start address of score array in $17\n")
    elif(line[0:7] == "0011110"):
        output_file.write("addi $17, $0, 0x2008\t\t\tWe recover the given address to store result\n")
    elif(line[0:7] == "0011111"):
        output_file.write("addi $18, $0, 0\n")
    elif(line[0:7] == "0100000"):
        output_file.write("andi $11, $15, 1\t\t\tIf not: it gets lowest bit value by andi operation between $15 and 1\n")
    elif(line[0:7] == "0100001"):
        output_file.write("andi $14, $16, 1\t\t\tWith the handy andi, we get the most significant bit\n")
    elif(line[0:7] == "0100010"):
        output_file.write("beq  $11, $0, Continue\n")
    elif(line[0:7] == "0100011"):
        output_file.write("beq  $11, $0, EndOfProgram\n")
    elif(line[0:7] == "0100100"):
        output_file.write("beq  $13, $0, ReturnToPrevious\t\t\tIf one Operand is zero we return, since the result is zero\n")
    elif(line[0:7] == "0100101"):
        output_file.write("beq  $14, $0, ReturnToPrevious\t\t\tIf one Operand is zero we return, since the result is zero\n")
    elif(line[0:7] == "0100110"):
        output_file.write("beq  $15, $0, ExponentZero\n")
    elif(line[0:7] == "0100111"):
        output_file.write("beq  $16, $0, endHamming\n")
    elif(line[0:7] == "0101000"):
        output_file.write("bne $11, $0, ReturnToPrevious\n")
    elif(line[0:7] == "0101001"):
        output_file.write("bne $13, $0, SkipSaving\n")
    elif(line[0:7] == "0101010"):
        output_file.write("bne $15, $0, LoopWords\n")
    elif(line[0:7] == "0101011"):
        output_file.write("bne $10, $16, NextStep\t\t\tIf it is lower, then nothing will happen\n")
    elif(line[0:7] == "0101100"):
        output_file.write("j MainLoop\t\t\tJump to Mainloop\n")
    elif(line[0:7] == "0101101"):
        output_file.write("j SecondaryLoop\t\t\tWe keep going until $13 is zero\n")
    elif(line[0:7] == "0101110"):
        output_file.write("j EXIT\n")
    elif(line[0:7] == "0101111"):
        output_file.write("j Modulus\t\t\tKeep calculating modulus\n")
    elif(line[0:7] == "0110000"):
        output_file.write("j Hamming\t\t\tKeep looping\n")
    elif(line[0:7] == "0110001"):
        output_file.write("j LoopScores\n")
    elif(line[0:7] == "0110010"):
        output_file.write("jal Multiplication\n")
    elif(line[0:7] == "0110011"):
        output_file.write("jal Modulus\n")
    elif(line[0:7]== "0110100"):
        output_file.write("jal IncrementCount\n")
    elif(line[0:7]== "0110101"):
        output_file.write("jr  $31\n")
    elif(line[0:7]== "0110110"):
        output_file.write("lw  $10, 4($15)\t\t\tThe current best matching score is loading into $10 from memory\n")
    elif(line[0:7]== "0110111"):
        output_file.write("lw  $11, 0($15)\t\t\tPattern is loaded into $11\n")
    elif(line[0:7]== "0111000"):
        output_file.write("lw  $15, 0($12)\t\t\tthe exponent is loaded into 15\n")
    elif(line[0:7]== "0111001"):
        output_file.write("lw  $16, 0($17)\t\t\tWe load a score from array\n")
    elif(line[0:7]== "0111010"):
        output_file.write("slt $11, $10, $12\t\t\tIf we found out that the number is already lower thant seventeen, then we're done\n")
    elif(line[0:7]== "0111011"):
        output_file.write("slt $13, $14, $10\t\t\tIf the score is lower than the best, we will not save it\n")
    elif(line[0:7]== "0111100"):
        output_file.write("srl $15, $15, 1\t\t\tit advances to the next bit\n")
    elif(line[0:7]=="0111101"):
        output_file.write("srl $16, $16, 1\t\t\tWe shift to compare with the next bit\n")
    elif(line[0:7]=="0111110"):
        output_file.write("sub $14, $14, $13\t\t\tCalculation of score\n")
    elif(line[0:7]=="0111111"):
        output_file.write("sw  $8, 4($12)\t\t\tit saves 1 in the result because if the exponent is 0\n")
    elif(line[0:7]=="1000000"):
        output_file.write("sw  $10, 0($17)\t\t\tWe save the best score in the given address\n")
    elif(line[0:7]=="1000001"):
        output_file.write("sw  $10, 0($15)\t\t\tWe save the result\n")
    elif(line[0:7]== "1000010"):
        output_file.write("sw  $14, 80($17)\t\t\tCalculate direction is score array\n")
    elif(line[0:7]== "1000011"):
        output_file.write("sw  $15, 0($17)\t\t\tthe result is stored back into data\n")
    elif(line[0:7]== "1000100"):
        output_file.write("xor $16, $16, $11\t\t\tThe xor will give us the information needed to count for the hamming distance\n")
