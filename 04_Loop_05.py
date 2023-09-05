word = input()
sen = input()


sym = ['"', "'", "(",")", ",", "."]
for i in sym:
    sen = sen.replace(i, ' ')
sen = sen.split()

count = 0
for i in sen:
    if i == word:
        count += 1

"""count = 0
idx = 0
for i in range(len(sen)):
    if idx == len(word) - 1:
        count += 1
        idx = 0
        continue
    if(sen[i] != word[idx]):
        idx = 0
        continue
    idx += 1
"""
print(count)
