# Working with Lists, Split/Join, and Tuples


sentence = input("Enter a sentence: ")

words_list = sentence.split()


print("List of words:", words_list)


joined_sentence = ' - '.join(words_list)
print("Joined sentence:", joined_sentence)


name_tuple = ("Moaaz", "Saeed")

print("First name:", name_tuple[0])
print("Last name:", name_tuple[1])