import os
import re

def letterstonum(lines, help_dict):
    newlines = []
    pattern = '|'.join(help_dict.keys())
    for line in lines:
        newlines.append(re.sub(pattern, lambda m: help_dict.get(m.group(0)), line, flags=re.IGNORECASE))
    return newlines

file1 = open('input.txt', 'r')

lines = file1.readlines()
nums = ''
results = []

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

newlines = letterstonum(lines, help_dict)

for line in newlines:
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

        
    