testCases = int(input())
half = testCases // 2
listLetters = []
listNum = []
while testCases:
    nk = input().split(' ')
    listNum.append(int(nk[0]))
    if testCases > half:
        listLetters.append('-')
    else:
        listLetters.append(nk[1])
    testCases -= 1

list1, list2 = (list(t) for t in zip(*sorted(zip(listNum, listLetters))))

strout = ''
sortedRes = sorted(zip(listNum, listLetters), key=lambda x: x[0])



for v in sortedRes:
    strout += v[1] + ' '

strout = strout.strip()
print(strout, end='')
