from re import *


text = str(input("Введите текст:"))

answer = ""
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

words = findall(r"\b\w+\b", text)

for i in range(len(words)):
    max_len = i

    for j in range(i + 1, len(words)):
        if len(words[max_len]) < len(words[j]):
            max_len = j

    words[max_len], words[j] = words[j], words[max_len]

K = len(words[max_len])

for sym in text:
    if sym in ",. ":
        answer += sym
    elif sym in uppercase:
        answer += uppercase[uppercase.index(sym) + K]
    else:
        answer += lowercase[lowercase.index(sym) + K]

print(answer)
