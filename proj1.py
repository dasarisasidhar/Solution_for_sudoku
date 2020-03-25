import numpy as np
import time
s = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]  
    ]
data = [1,2,3,4,5,6,7,8,9]

def find_possible_values(i,j, data):
    """
    with the give pos and data find all possible values
        by substracting the valid row col and square values

    """

    a = {1,2,3,4,5,6,7,8,9}
    row = list()
    square = list()
    col = set(data[:][i])
    for _ in data:
        val = _[j]
        row.append(val)
    #x1, y1 are lower and upper limits of squares of i
    #x2, y2 are lower and upper limits of squares of j
    x1 = i//3 *3
    y1 = (i//3 + 1) * 3
    x2 = j//3 * 3
    y2 = (j//3 + 1) * 3
    for k in range(9):
        for l in range(9):
            if(k>=x1 and k<y1  and l>=x2 and l<y2):
                square.append(int(data[k][l]))
    square = set(square)
    row = set(row)
    values = row.copy()
    values.update(col)
    values.update(square)
    possible_values = a.difference(values)
    key = str(i)+str(j)
    return(key, list(possible_values))


def find_zeros_and_get_its_possible_values(data):
    """
    check where the array is empty
    calls the function (find_possible_values())
        to get all possible values for that empty position

    return possible dict with key values returned from function (find_possible_values())

    """
    possible_values = dict()
    data = list(data)
    for i in range(9):
        for j in range(9):
            if(data[i][j] == 0):
                value = find_possible_values(i,j, data)
                possible_values[value[0]] = value[1]
    return possible_values


def solve(arr):
    """
    main fun where the execution will start

    algo: get the 9x9 array
    find all possible values
    check wheathe there is only one possibility and if so fill it with that possibility
    
    call the same fun with the modified array
    """
    start_time = time.time()
    arr = list(arr)
    values = find_zeros_and_get_its_possible_values(s)
    for i in values:
        if(len(values[i]) == 1):
            value = values[i]
            j = int(i)
            arr[j//10][j%10] = int(value[0])
            solve(arr)
    else:
        print("Time taken to solve is %s seconds" % (time.time() - start_time))
        print(arr)
solve(s)

#def test(i, j, data):
#    print(data[i][j])
#    square = list()
#    x1 = i//3 *3
#    y1 = (i//3 + 1) * 3
#    x2 = j//3 * 3
#    y2 = (j//3 + 1) * 3
#    for i in range(9):
#        for j in range(9):
#            if(i>=x1 and i<y1  and j>=x2 and j<y2):
#                square.extend(str(data[i][j]))

#    print(square)

#test(0,5,s)

#def check_unique(value):
#    flag = False
#    unique = len(set(value)) == len(value)
#    if(unique):
#        print("unique")
#    else:
#         print("not unique")



#def squares(data):
#    square1 = list()
#    square2 = list()
#    square3 = list()
#    square4 = list()
#    square5 = list()
#    square6 = list()
#    square7 = list()
#    square8 = list()
#    square9 = list()
#    for i in range(9):
#        for j in range(9):
#            if(i<3 and j<3):
#                square1.extend(str(data[i][j]))
#            if(i<3 and j>=3 and j<6):
#                square2.extend(str(data[i][j]))
#            if(i<3 and j>=6):
#                square3.extend(str(data[i][j]))
#            if(i>=3 and i<=6 and j<3):
#                square4.extend(str(data[i][j]))
#            if(i>=3 and i<=6  and j>=3 and j<6):
#                square5.extend(str(data[i][j]))
#            if(i>=3 and i<=6  and i<6 and j>=6):
#                square6.extend(str(data[i][j]))
#            if(i>=6 and j<3):
#                square7.extend(str(data[i][j]))
#            if(i>=6 and j>=3 and j<6):
#                square8.extend(str(data[i][j]))
#            if(i>=6  and j>=6):
#                square9.extend(str(data[i][j]))
    #print(square1, square2 , square3 , square4 , square5, square6 , square7 , square8 , square9)

#def rows_cols(data):
#    rows = list()
#    cols = list()
#    squares = list()
#    for i in range(9):
#        row = list(data[:][i])
#        rows.append(row)
#    #print("rows :", rows)
#    for j in range(9):
#        col = list()
#        for k in range(9):
#            col.append(data[k][j])
#        cols.append(col)
    #print("cols :", cols)

#rows_cols(s)
#squares(s)
#check_valid(data)

