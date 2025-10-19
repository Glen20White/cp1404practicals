"""
CP1404/CP5632 Practical 5
Question 3
Word Occurrences
Estimate: 15 minutes
Actual:   15 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max((len(word) for word in words))
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")