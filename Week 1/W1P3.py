#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh

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
