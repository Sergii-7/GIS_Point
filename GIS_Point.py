import re
from collections import Counter

paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]



def word_frequency(paragraph):
    items = []
    for y in paragraph:
        x = re.findall(r'\b\w+\b', y)
        [items.append(i.lower()) for i in x]
    return dict(Counter(items))


print(word_frequency(paragraph))



