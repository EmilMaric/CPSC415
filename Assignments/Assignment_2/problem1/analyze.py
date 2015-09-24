cipher = { 
            'a' : 'k',
            'b' : 'g',
            'c' : '_',
            'd' : 'c',
            'e' : 't',
            'f' : 'i',
            'g' : 'f',
            'h' : 'y',
            'i' : 'n',
            'j' : 'b',
            'k' : 'e',
            'l' : 'o',
            'm' : 'a',
            'n' : 'q',
            'o' : 'r',
            'p' : 'm',
            'q' : 'p',
            'r' : 's',
            's' : '_',
            't' : 'l',
            'u' : 'v',
            'v' : 'u',
            'w' : 'w',
            'x' : 'd',
            'y' : 'h',
            'z' : '_',
}


with open("cipher.txt") as f:
    ciphertext = f.readlines()
ciphertext = ciphertext[0].split("\n")[0].lower()

letter_freq = {}
for letter in cipher:
    letter_freq[ letter ] = 0
for letter in ciphertext:
    letter_freq[letter] += 1

# sort letter_freq by most frequently occuring letter to least
sorted_alphabet = reversed(sorted( letter_freq, key=letter_freq.get))

# Frequency Analysis
with open("frequency_analysis.txt", "w") as f:
    for letter in sorted_alphabet:
        freq = letter_freq[letter]
        pct = round(freq * 100.0 / len(ciphertext), 2)
        hashes = "#" * freq
        f.write("%s {%i} [%s%%] = %s\n" % (letter, freq, format(pct, '.2f'), hashes))

# Find the most repeated sequences in the ciphertext
string_count = {}
for start_idx in range(0, len(ciphertext) - 1):
    for end_idx in range(start_idx + 2, len(ciphertext) + 1):
        string = ciphertext[start_idx:end_idx]
        if string in string_count:
            string_count[string] += 1
        else:
            string_count[string] = 1

# delete all the strings that only occur once
for string in string_count.keys():
    if string_count[string] <= 1:
        del string_count[string]

# sort string_count so most occuring string is listed first
string_count_sorted = reversed(sorted( string_count, key=string_count.get))
with open("string_count.txt", "w") as f:
    for string in string_count_sorted:
        f.write("\"%s\" [%i] : %i\n" % (string, len(string), string_count[string]))

# Perform letter substitutions
substitute = []
for letter in ciphertext:
    substitute.append(cipher[letter])
substitute = ''.join(substitute)
print substitute
