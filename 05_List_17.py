ids = []
grades = []
uids = []
grade_lists = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A']

while True:
    x = input()
    if x == 'q':
        break
    a,b = x.split()
    ids.append(a)
    grades.append(b)

upgrade = input().split()

for i in upgrade:
    idx = ids.index(i)
    grades[idx] = grade_lists[grade_lists.index(grades[idx])+1]

for i in range(len(ids)):
    print(ids[i], grades[i])
