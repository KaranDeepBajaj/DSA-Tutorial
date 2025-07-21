

def hourglassSum(arr):
    max_sum=float('-inf')
    for i in range(4):
        for j in range(4):
            top=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            mid=arr[i+1][j+1]
            bottom=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            total=top+mid+bottom

            if total>=max_sum:
                max_sum=total
    return max_sum



if __name__ == '__main__':
    arr=arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
    print(hourglassSum(arr))