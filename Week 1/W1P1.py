s = 'azcbobobegghakl'

vowels = ["a", "e", "i", "o", "u"]
count = 0

for i in range(len(s)):
    count += vowels.count(s[i])
    print (type(vowels.count(s[i])))

print("Number of vowels: {}".format(count))

