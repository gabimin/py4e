import re
allnum = []

handle = open('regex_sum_2097249.txt')

for line in handle:
    chain = re.findall('([0-9]+)', line)
    if len(chain) == 0 :  continue
    else:
        for number in chain:
            allnum.append(int(number))
 
print(sum(allnum))
