def print_upper_words(list)

for words in list:
    words.upper()

return words

for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words(list, must_start_with):

for word in list:
    for letter in must_start_with:
        if word.startswith(letter):
            print(word.upper())
