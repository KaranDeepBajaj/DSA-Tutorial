def backtrack(comb,n,input):
    if len(comb)==len(input):
        print(comb)
        return
    for i in input:
        if i not in comb:
            backtrack(comb + i, n + 1,input)

backtrack("",0,["A","B","C","D"])