# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

list_words = []


quit = False
while False:
    response = input("Enter a word please")
    list_words.append(response)
    if response.strip() == "quit":
        quit == True

list_words = sort.list_words()
print(list_words)




