
def sliding_window(input, k):
    n=len(input)
    result=[]
    if k>n:
        print("Wrong Size")
    for i in range(k,n+1):
        found = False
        l=i-k
        window=input[l:l+k]
        print(window)
        for i in window:
            if i <0:
                result.append(i)
                found=True
                break
        if not found:
            result.append(0)
    print(result)


sliding_window([12, -1, -7, 8, 15, 30, 16, 28],3)