s = 'azcbobobegghakl'

names = ["bob"]
count = 0

for i in range(len(s) - 2):
    count += names.count(s[i] + s[i+1] + s[i+2])

print("Number of times name occurs is: {}".format(count))