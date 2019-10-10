    
"""This is a Pig Latin translator. It will ask you for a word,
   then take the first letter and puts it to the end of the word
   with an added "ay". """
       
print ("Welcome to the Pig Latin Translator!")

pyg = "ay"
original = input("Enter a word: ")
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
else:
    print("empty")

print(new_word)