""" Word Occurrences
Estimate: 15 mins
Actual: 26 mins
"""
text = input("Enter text: ")
word_to_wordcount = {}
words = text.split()
for word in words:
    if word in word_to_wordcount:
        word_to_wordcount[word] += 1
    else:
        word_to_wordcount[word] = 1
max_width = max(len(word) for word in words)
for word in sorted(word_to_wordcount):

    print(f"{word:{max_width}} : {word_to_wordcount[word]}")


