def find_characters(word_list, char):
    # empty list to hold words that have the selected character
    found_words = []
    # iterates through the words in the word_list and uses the built in .find() method for strings
    for word in word_list:
        if word.find(char)>=0:
            found_words.append(word)
    return found_words

# Test the function
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

print "Expected: ['hello','world']"
print find_characters(word_list, char)