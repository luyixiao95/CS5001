# Task 3: Write a function pigLatin. Given a single word, if the word           
# begins with a vowel, add the suffix 'way'. If the word begins with a          
# consonant, take all consonants before the first vowel, move them to           
# the end of the string, and add the suffix 'ay'. If a y is the first           
# letter, treat it as a consonant.  If a y is not the first letter, treat       
# it as a vowel. The function should remove any initial or trailing spaces.     
# example: computer -> omputercay                                               
# example: python -> ythonpay                                                   
# example: chai -> aichay                                                       
# example: apple -> appleway                                                    
# example: outside -> outsideway                                                
# if the function generates an error, it should return the empty string         
# but it should not print an error message                                      

# write your function here                                                      
def pigLatin(word):
    try:
        word = word.strip()

   #when the first letter is consonant:
        if word[0] in "aeiou":
            word = word + "way"
            return word

        elif word[0] not in "aeiou":
            rest = word[0]
            word = word[1:]
            while word[0] not in "aeiouy":
                rest += word[0]
                word = word[1:]
            word = word+ rest + "ay"
            return word
    except:
        return " "

    
         
# test function for pigLatin                                                    
def testPigLatin():

    words = [ 'computer', 'science', 'is', 'awesome', "y'all", 60 ]
    collect = ""
    for word in words:
        collect += pigLatin( word ) + ' '
    print( "output is:", collect )

    print("should be: omputercay iencescay isway awesomeway ally'ay\n" )


if __name__ == "__main__":

    testPigLatin()