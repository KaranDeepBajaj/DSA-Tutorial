def backtracking(open,close,comb,n):
    l=len(comb)
    if l == n*2:
        print(comb)
        return
    if open<n:
        backtracking(open+1,close,comb+"(",n)
    if open>close:
        backtracking(open,close+1,comb+")",n)


backtracking(open=0,close=0,comb="",n=2)