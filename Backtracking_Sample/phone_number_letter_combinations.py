list2=['a','b','c']
list3=['d','e','f']

def backtrack(comb,n2,n3):
    if len(comb)==2:
        print(comb)
        return
    if len(comb)==0:
        for i in list2:
            backtrack(comb+i,n2+1,n3)
    else:
        for j in list3:
            backtrack(comb+j,n2+1,n3+1)

backtrack("",0,0)