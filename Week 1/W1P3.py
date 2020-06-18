s = 'abcbcd'
permanent = s[0]
temp = permanent

for i in range (1, len(s)):
    if s[i] >= s[i - 1]:
        temp += s[i]
        if len(temp) > len(permanent):
            permanent = temp
    else:
        temp = s[i]

print('Longest substring in alphabetical order is: {} '.format(permanent))