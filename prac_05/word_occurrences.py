""" Word Occurrences
Estimate:
Actual:
"""
text = input("Enter text: ")
word_to_wordcount = {}
words = text.split()
for word in words:
    if word in word_to_wordcount:
        word_to_wordcount[word] += 1
    else:
        word_to_wordcount[word] = 1

for word in sorted(word_to_wordcount):
    print(f"{word} : {word_to_wordcount[word]}")


