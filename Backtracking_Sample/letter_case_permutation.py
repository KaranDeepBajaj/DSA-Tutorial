
def backtrack(start,comb,input):
    if len(comb)==len(input):
        print(comb)
        return
    char=input[start]
    if char.isalpha():
        backtrack(start + 1, comb + char.lower(), input)
        backtrack(start + 1, comb + char.upper(), input)
    else:
        backtrack(start+1, comb + char, input)




backtrack(0,"","a1b")
