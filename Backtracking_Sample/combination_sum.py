
def backtrack(start,sum,result,candidates,target):
    if sum==target:
        print(result)
        
        return
    if sum>target:
        return
    for i in range(start,len(candidates)):
        result.append(candidates[start])
        backtrack(start,sum+candidates[start],result,candidates,target)
        result.pop()
        start=start+1







backtrack(0,0,[],[2,3,6,7],7)