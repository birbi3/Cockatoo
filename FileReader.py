#take blocks in from file in size 256 bytes and return them as a list
def read_in_blocks():
    #testttext is just a temp file for testing
    with open("TestText.txt") as file:
        #the list thsi method will return
        blockList = []
        
        #start the loop reading through the file
        while True:
            block = file.read(256)
            if not block:
                break
            if len(block) <256:
                #padAmt holds the number of 0/1's to pad
                padAmt = 256 - len(block)
                for i in range(padAmt):
                    if i % 2 == 0:
                        block += '1'
                    else:
                        block += '0'
            blockList.append(block)          
            
            #for testing
            #print(block)
        
    #for demonstration    
    for x in blockList:
        print(x)
        
    return blockList
           
#turns the blocks into binary          
def to_binary(blockList):
    #this is the list this method returns
    binList = []
    #start loop of every block(x) in blocklist
    for x in blockList:
        bBlock = ""
        #start loop of every character(y) in blocklist
        for y in x:
            #gets the ordinate value, then formats it to be in binary
            #and pad 0's if it's less than 8. Also returns as a string
            b = str(format(ord(y), '0>8b'))
            #bBlock gets a whole byte (all 8 character)
            bBlock += b
            
            #for testing
            #print("b= " + b)
            #print("bBlock = " + bBlock)
            
        #binlist collects all the bBlocks
        binList.append(bBlock)
    return binList
        

#demonstration
if __name__ == '__main__':
    newList = read_in_blocks()
    for i in newList:
        print(i)
    
    binList = to_binary(newList)
    for x in binList:
        print(x)