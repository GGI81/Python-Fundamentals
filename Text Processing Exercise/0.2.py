words = input().split()
word_one = words[0]
word_two = words[1]
total = 0

shorter_word_len = min(len(word_one), len(word_two))

# Process shorter string
for i in range(shorter_word_len):
    word_one_curr_ch = word_one[i]
    word_two_curr_ch = word_two[i]

    ch_sum = ord(word_one_curr_ch) * ord(word_two_curr_ch)

    total += ch_sum

# If hte strings have different lengths we have to process characters of the longer string

longer_word_len = max(len(word_one), len(word_two))

for i in range(shorter_word_len, longer_word_len):
    if len(word_one) > len(word_two):
        curr_word_ch  = word_one[i]
    else:
        curr_word_ch = word_two[i]

    total += ord(curr_word_ch)

print(total)