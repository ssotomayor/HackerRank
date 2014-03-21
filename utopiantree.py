testCases = int(input())
cycles = []
while testCases:
    cycles.append(input())
    testCases -= 1

for cycle in cycles:
    cyc = int(cycle)
    tree = 1
    for x in range(0, cyc):
        if x % 2 == 0:
            tree *= 2
        else:
            tree += 1
    print(tree)
