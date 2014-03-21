import re

testCases = int(input())
cycles = ''
while testCases:
    cycles += input()
    testCases -= 1

html = cycles
res = re.findall('<([a-z][a-z0-9]*)\b*', html)
list2 = list(set(res))
list2.sort()

strres = ''
for x in list2:
    strres += x + ';'

print(strres[:-1])