def word_counter(string): #Counts how many words in a string.
    if string:
        return(len(string.split(' ')))
    else:
        return(0)

print(word_counter("Hello world")) # returns 2

print(word_counter("This is a sentence")) # returns 4

print(word_counter("")) # returns 0
