array = [
    [ 1 , 2 ,3, 4, 5 ],
    [ 6, 7, 8, 9, 10],
    [ 11, 12, 13, 14, 15],
    [ 16, 17, 18, 19, 20]
]

seenPositions = set()
def dfs(numRows, array, pair):
    if pair not in seenPositions:
        print(str(array[pair[0]][pair[1]]) + " ")
        seenPositions.add(pair)

    direction = numRows % 4
    lastInsertedPair = None
    # print(numRows, pair, direction)
    for childPair in generateChildPairs(direction, array, pair):
        if childPair not in seenPositions:
            print(str(array[childPair[0]][childPair[1]]) + " ")
            seenPositions.add(childPair)
            lastInsertedPair = childPair

    if lastInsertedPair is not None:
        dfs(numRows+1, array, lastInsertedPair)


def generateChildPairs(direction, array, pair):
    if direction == 1: # right
        for j in range(pair[1], len(array[pair[0]])):
            yield (pair[0], j)
    elif direction == 2: # down
        for i in range(pair[0], len(array)):
            yield (i, pair[1])
    elif direction == 3: # left
        for j in range(pair[1], -1, -1):
            yield (pair[0], j)
    elif direction == 0: # up
        for i in range(pair[0], -1, -1):
            yield (i, pair[1])


print(array)

dfs(1, array, (0, 0))


# go right
numRows+=1

for jNext in range(int(numRows/4), len(array[i])-):
    print(array[i][jNext])

j = len(array[i])
# go down
for iNext in range(i+1, len(array)):
    print(array[i][j])

# go left
i = len(array)
for jNext in range(len(array[i])-1, -1, -1):
    print(array[i][j])

# go up
for iNext in range(len(array)-1, -1+(numRows/4), -1):
    print(array[iNext][j])


