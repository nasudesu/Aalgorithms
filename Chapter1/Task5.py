string = input("Give a word: ")

vowels = ('a', 'e', 'i', 'o', 'u')

vowelsInList = 0

for car in string:
    if vowels.__contains__(car.lower()):
        vowelsInList += 1

print(f"Number of vowels: {vowelsInList}")