# GIS_Point
ТЗ
You are given a list of strings representing a paragraph of text. Your task is to write a Python function called word_frequency that takes in this list as an argument and returns a dictionary where the keys are unique words in the paragraph, and the values are the frequencies of those words.

Consider the following requirements:

The function should treat words in a case-insensitive manner. For example, "apple" and "Apple" should be considered the same word.
The function should strip leading and trailing whitespace from each word.
The function should exclude any punctuation marks attached to words. For example, "apple." and "apple," should be considered the same word "apple".
The function should exclude empty strings as words.
The function should aim for an optimal time complexity.

Example:

paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]

frequency = word_frequency(paragraph)
print(frequency)

Output:

{
    "the": 4,
    "quick": 1,
    "brown": 1,
    "fox": 2,
    "jumps": 1,
    "over": 1,
    "lazy": 1,
    "dog": 2,
    "barks": 1,
    "and": 1,
    "runs": 1,
    "away": 1
}


In the example above, the given paragraph consists of several sentences. The word_frequency function calculates the frequency of each unique word, ignoring case, punctuation marks, and leading/trailing whitespace. The resulting dictionary contains the word frequencies.

Please write your solution in Python and provide the code for the word_frequency function.

