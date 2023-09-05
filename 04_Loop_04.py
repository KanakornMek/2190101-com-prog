s = list(input())

for i in range(len(s)):
    if s[i] == '(':
        s[i] = '['
    elif s[i] == '[':
        s[i] = '('
    elif s[i] == ')':
        s[i] = ']'
    elif s[i] == ']':
        s[i] = ')'

s = ''.join(s)
print(s)
