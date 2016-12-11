arr = [ [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36]]

# arr = [ [1,2,3,4,5,6] ]

# arr = [ [1],
#         [2],
#         [3],
#         [4],
#         [5],
#         [6]]

# when break out up = over and down = down (literally)
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

    # go back one (aka back inside the box aka back inside the matrix)
    i -= iDirection
    j -= jDirection

    if i >= len(arr)-1 and j >= len(arr[i]) -1:
        print("arr len", len(arr), "sub arr", len(arr[i]), "i", i)
        haveReachedTheEnd = True
    else: # to be here we have to be on one of the edges.

        if i == len(arr)-1:
            j += 1
        else: # we know that i = 0
            if j != 0 and j != len(arr[i]) - 1:
                j += 1
            else:
                i += 1

        # need to toggle direction
        iDirection *= -1
        jDirection *= -1