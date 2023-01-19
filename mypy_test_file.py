phrase1 = 'Clean Couch'
phrase1 = phrase1.split()
phrase2 = 'Giant Table'
phrase2 = phrase2.split()
print('Does Phrase1 start with the same letter?', phrase1[0][0] == phrase1[1][0])
print('Does Phrase2 start with the same letter?', phrase2[0][0] == phrase2[1][0])


my_string1 = 'This is a short phrase'
my_string2 = 'This is actually a significantly longer phrase than the previous one'
print("Word order and letter order reversed: \n", my_string1[::-1], '\n', my_string2[::-1])

split_string1 = my_string1.split( )
new_string1 = ' '.join(str(word) for word in split_string1[::-1])
split_string2 = my_string2.split( )
new_string2 = ' '.join(str(word) for word in split_string2[::-1])
print("Only word order reversed:  \n", new_string1, '\n', new_string2)

def new_string(my_string):
    my_string = my_string.split( )
    new_string=[]
    for word in my_string:
        new_string.append(word[::-1])
    new_string = ' '.join(str(word) for word in new_string)
    return new_string

print("Only letter order in each word reversed:  \n", new_string(my_string1), '\n', new_string(my_string2))


