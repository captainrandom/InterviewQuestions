# problem url: https://www.hackerrank.com/challenges/sherlock-and-anagrams

T = int(input().strip())

def frequencyMap(word):
    dict = {}
    for character in word:
        dict[character] = dict.get(character,0) + 1
    return dict

def choose(n, k):
    return (n * (n-1)) / k

for i in range(T):
    case = input().strip()
    totalSum = 0

    multipleCharFrequencies = {} # will be in the form of a2b3... -> [ (i1,j1), (i2,j2), ... ]
    for i in range(len(case)):
        for j in range(i, len(case)+1):
            if i == j: continue

            rangedFrequencyMap = frequencyMap(case[i:j])

            frequencyList = list(rangedFrequencyMap.items())
            frequencyList.sort(key=lambda x: x[0])
            frequencyKeyStr = ''.join([ pair[0] + str(pair[1]) for pair in frequencyList])
            positionsList = multipleCharFrequencies.get(frequencyKeyStr, [])
            positionsList.append((i, j))
            multipleCharFrequencies[frequencyKeyStr] = positionsList

    # now we need to count all the pairs
    for key, positionsList in multipleCharFrequencies.items():
        if len(positionsList) > 1:
            totalSum += choose(len(positionsList), 2)


    print(int(totalSum))