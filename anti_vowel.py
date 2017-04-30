def anti_vowel(text):
    x = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in x:
        text = text.replace(i, "")
    return text