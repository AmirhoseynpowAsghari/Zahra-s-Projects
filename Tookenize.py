def tokenize_and_remove_duplicates(sentence):

    words = []  # List to store the words
    word = ""  # Variable to build each word

    for char in sentence:
        if char == " ":  # If a space is encountered
            if word:  # Check if word is not empty
                if word not in words:  # Check if word is not already in the list
                    words.append(word)  # Add the word to the list
                word = ""  # Reset the word variable
        else:
            word += char  # Add the character to the word

    if word:  # Check if there's a word remaining after the loop
        if word not in words:  # Check if the last word is not already in the list
            words.append(word)  # Add the last word to the list

    return words



input = ["This is the test", "Python is the best"]


# Tokenize each sentence, remove duplicates, and store the results
output = []
for sentence in input:
    words = tokenize_and_remove_duplicates(sentence)
    output.extend(words)
print(sorted(set(output)))
