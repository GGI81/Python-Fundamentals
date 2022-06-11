# It returns the word with replaced character code as a list
def replace_chr_code(word: str):
    chr_code_str = ""
    new_word = []

    for ch in word:
        if ch.isnumeric():
            chr_code_str += ch
        else:
            new_word.append(ch)

    ch_at_beginning = chr(int(chr_code_str))

    new_word.insert(0, ch_at_beginning)

    return new_word


def decipher_word(word: str):
    new_word = replace_chr_code(word)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]   # Easy syntax for moving two indices with different position

    return "".join(new_word)


word_input = input().split()

deciphered_words = [decipher_word(word) for word in word_input]

print(" ".join(deciphered_words))