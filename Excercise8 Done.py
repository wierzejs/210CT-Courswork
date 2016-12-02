def removeVowels(sentence):
    if not sentence: # case for empty string
        return sentence
    elif sentence[0] in "eaiouyEAIOUY": #checks if first letter is a vovel and removes it if is it gets discarded and fuction is called again
        return removeVowels(sentence[1:]) 
    return sentence[0] + removeVowels(sentence[1:]) #if none of the above is true then first letter is probably not a vovel and gets saved

sentence=input("What is your given sentence/word?")

print(removeVowels(sentence))
