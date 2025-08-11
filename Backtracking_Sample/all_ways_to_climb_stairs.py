def backtracking(total,comb,n):
    if total==n:
        print(comb)
        return
    if total>n:
        return
    comb.append(1)
    backtracking(total+1,comb,n)
    comb.pop()
    comb.append(2)
    backtracking(total+2,comb, n)
    comb.pop()


backtracking(0,[],3)