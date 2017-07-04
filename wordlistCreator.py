####WELCOME TO MY WORDLIST CREATOR FOR BRUTEFORCE ATTACKS####
####FIRST WE ASK FOR INFO THE GENERATE THE WORDLIST
print("Enter words that migth be on your target password")
wordInput=" "
words=[]
wordList=[]
subset=[]
while(wordInput!=""):
    wordInput=input()
    if (wordInput==""):
        break
    else:
        words.append(wordInput)
####NOW WE WILL CALCULATE ALL POSIBLE SUBSETS
binLenght=len(words)
amountOfSubsets=2**len(words)
for i in range(amountOfSubsets):
    bini=str(bin(i)[2:].zfill(binLenght))
    subset=[]
    for e in range(binLenght):
        if(bini[e]=="1"):
       	    subset.append(words[e])
    wordList.append(subset)
print(wordList)
print("amount of potential passwords: " + str(amountOfSubsets))
