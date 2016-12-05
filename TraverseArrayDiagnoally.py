arr = [ [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36]]

for list in arr:
    print(len(list))

print()

# when break out up = over and down = down (literally)
up = False # technically I don't need this variable, but it makes it easier to read
haveReachedTheEnd = False
iDirection = 1
jDirection = -1
i=0
j=0

while not haveReachedTheEnd:


    # print shit in the matrix (on the diagnal)
    while(i >= 0 and j >= 0 and len(arr) > i and len(arr[i]) > j):
        print(arr[i][j])
        i += iDirection
        j += jDirection
        # print("i", i, "j", j)

    # go back one (aka back inside the box aka back inside the matrix)
    i -= iDirection
    j -= jDirection
    # print("i", i, "j", j)

    if i >= len(arr)-1 and j >= len(arr[i]) -1:
        print("arr len", len(arr), "sub arr", len(arr[i]), "i", i)
        haveReachedTheEnd = True
    else:
        if up ^ (i == len(arr) - 1 or j == len(arr[i]) -1):
            j+= 1
        else:
            i+=1

        # need to toggle direction and the
        up ^= True
        iDirection *= -1
        jDirection *= -1