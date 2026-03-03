
def longest_un_word(filename):
    longest_word = ""

    file = open(filename, "r")

    for line in file:
        line = line.strip()
        words = line.split()

        for word in words:
            if len(word) >= 2:
                if word[0] == "u" and word[1] == "n":
                    if len(word) > len(longest_word):
                        longest_word = word

    file.close()

    return longest_word


