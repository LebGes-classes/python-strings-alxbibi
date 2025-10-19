stroke = str(input("Введите текст: "))

stroke += " "

answer1 = " "
answer2 = ""
words = []
word = ""

for letter in stroke:
    if letter == " ":
        words.append(word)
        word = ""
    else:
        word += letter

for word in range(len(words) - 1, -1, -1):
    answer1 += words[word] + " "

for letter in range(len(stroke) - 1, -1, -1):
    answer2 += stroke[letter]

print(answer1)
print(answer2)
