c_ans = input()
s_ans = input()

sum = 0
if(len(c_ans) == len(s_ans)):
    for i in range(len(c_ans)):
        if(s_ans[i] == c_ans[i]):
            sum += 1
    print(sum)
else:
    print("Incomplete answer")

