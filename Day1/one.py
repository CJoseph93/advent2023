import os
file1 = open('input.txt', 'r')

lines = file1.readlines()
nums = ''
results = []

for line in lines:
    for x in line:
        if x.isnumeric():
            nums += x
    y = nums[0] + nums[-1]
    results.append(y)
    nums = ''
    
final = 0

for result in results:
    final += int(result)
    
print(final)
    