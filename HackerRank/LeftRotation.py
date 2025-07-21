def rotateLeft(d, arr):
    for i in range (d):
        arr.append(arr[0])
        arr.remove(arr[0])
    return arr


if __name__ in '__main__':
    print(rotateLeft(2,[1,2,3,4]))