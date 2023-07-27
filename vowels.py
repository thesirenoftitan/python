from collections import Counter

sentence = input("What is your sentence? ").lower()

counter = Counter(sentence)

vowels = ['a', 'e', 'i', 'o', 'u']

for vowel in vowels:
    print(f"{vowel} : {'*' * counter[vowel]}")
