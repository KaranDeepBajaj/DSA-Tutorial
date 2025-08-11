def backtracking(comb,n):
    if len(comb)==n:
        print(comb)
        return

    backtracking(comb+"H",n)
    backtracking(comb+"T",n)

backtracking("",2)