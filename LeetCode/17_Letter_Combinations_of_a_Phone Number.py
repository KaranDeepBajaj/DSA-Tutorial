from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig={'2':["a", "b", "c"],'3':["d", "e", "f"],'4':["g", "h", "i"],'5':["j", "k", "l"] , '6':["m","n", "o"],'7':["p", "q", "r", "s"],'8':["t", "u", "v"],'9':["w", "x", "y", "z"]}
        final=[]
        l=0
        for i in digits:
            fin = []
            if (l==0):
                final=dig[i]
                l+= 1
            else:
                for j in final:
                    for k in dig[i]:
                        fin.append(j+k)
                final=fin
        return(final)


if __name__ in '__main__':
    obj=Solution()
    o=obj.letterCombinations("9")
    print(o)