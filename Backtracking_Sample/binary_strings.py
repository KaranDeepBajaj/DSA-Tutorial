def backtracking(current,n):
    if len(current)==n:
        print (current)
        return
    backtracking(current+"0",n)
    backtracking(current+"1",n)

backtracking("",3)
