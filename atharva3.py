def frequent(inputstring):
    letter_freq = {}
    for letter in inputstring:
        if letter.isalpha():
            letter = letter.lower() 
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    for letter, frequency in sorted_letter_freq:
        print(f"{letter} = {frequency:02d}", end=" ")
inputstring = input("ENTER A STRING:")
frequent(inputstring)