
#Take input of word
string = input("Please enter your own word: ")
#Take input of a character
char = input("Please enter your own character: ")
i = 0
count = 0
#Loop willl to find the occurence of a character
while(i < len(string)): #string operation

    if(string[i]== char): #condition 1
        count = count + 1
    i = i + 1   

#Display the result
print("The total Number of Times ", char, "has Occured = " , count)    