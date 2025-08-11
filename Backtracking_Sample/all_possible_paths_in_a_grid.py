def backtracking(Right,Left,comb):
    if len(comb)==4:
        print(comb)
        return
    if Right<2:
        backtracking(Right+1,Left,comb+"R")
    if Left<2:
        backtracking(Right,Left+1,comb+"D")


backtracking(0,0,"")