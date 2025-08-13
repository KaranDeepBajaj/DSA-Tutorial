
def sliding_window(input,k):
    l=len(input)
    if k>l:
        return None
    window_sum=sum(input[:k])
    max_sum=window_sum
    for i in range(k,l):
        window_sum+=input[i]-input[i-k]
        max_sum=max(max_sum,window_sum)

    print(max_sum)




sliding_window([2, 1, 5, 1, 3, 2],3)