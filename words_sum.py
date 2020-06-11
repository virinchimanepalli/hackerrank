def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    words = words.split(" ")
    print(words)
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                print(word)
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score = score+1
    return score

words= "hacker book"
print(score_words(words))