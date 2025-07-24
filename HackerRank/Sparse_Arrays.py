def matchingStrings(stringList, queries):
    result= [0]*len(queries)
    j=0
    for query in queries:
        for i in stringList:
            if query==i:
                result[j]=result[j]+1
        j=j+1
    return result



print(matchingStrings(["aba","ab","abc"],["ab","abc"]))