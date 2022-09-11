def word_replacement():
    str = "Hi, this is a very easy project!"
    print(str)
    word_to_replace = input("Enter the the word to replace: ")
    new_word = input("Enter the the new word: ")
    print(str.replace(word_to_replace, new_word))


word_replacement()
