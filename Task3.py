from re import *


text = str(input("Введите текст: "))

text = text.lower()

words = findall(r"\b\w+\b", text)

cnt_words = {}

for word in words:
    if cnt_words.get(word, 0) == 0:
        cnt_words[word] = 1
    else:
        cnt_words[word] += 1

most_words = []

for word, cnt in cnt_words.items():
    most_words.append((word, cnt))

for i in range(len(most_words)):
    max_cnt = i

    for j in range(i + 1, len(most_words)):
        if most_words[max_cnt][1] < most_words[j][1]:
            max_cnt = j
            
    most_words[max_cnt], most_words[i] = most_words[i], most_words[max_cnt]

print("\nТоп-5 самых частых слов:")

for i in range(5):
    print(most_words[i][0], "-", most_words[i][1])