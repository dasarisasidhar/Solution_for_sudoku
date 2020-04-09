import numpy as np
import time

a = {1,2,3,4,5,6,7,8,9}
data = dict()

def check_unique(arr):
    i = 0
    j = 7
    col = set(arr[:][i])
    row = list()
    for _ in arr:
        val = _[j]
        row.append(val)
    if(len(set(col)) == len(row)):
        return True
    else:
        return False

def find_possible_values(i,j, data):
    """
    with the give pos and data find all possible values
        by substracting the valid row col and square values
    """
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
    given_values = dict()
    data = list(data)
    for i in range(9):
        for j in range(9):
            if(data[i][j] == 0):
                value = find_possible_values(i,j, data)
                possible_values[value[0]] = value[1]
            else:
                given_values["c"+str(i)+str(j)] = data[i][j]
                
    return possible_values, given_values


def process(arr):
    """
    main fun where the execution will start
    algo: get the 9x9 array
    find all possible values
    check wheathe there is only one possibility and if so fill it with that possibility
    
    call the same fun with the modified array
    """
    arr = list(arr)
    values, given_data = find_zeros_and_get_its_possible_values(arr)
    ## s to arr
    for i in values:
        if(len(values[i]) == 1):
            value = values[i]
            j = int(i)
            data["c"+str(i)] = int(value[0])
            arr[j//10][j%10] = int(value[0])
            process(arr)
    return data, given_data, arr
   

def solve(arr):
    start_time = time.time()
    arr = np.array(arr)
    arr = arr.reshape(9,9)
    data, given_data, arr = process(arr)
    unique = check_unique(arr)
    data.update(given_data)
    print(data)
    print(len(data))
    if(0 in data.values() or len(data)<81 or not(unique)):
        return 0
    return(time.time() - start_time, data)