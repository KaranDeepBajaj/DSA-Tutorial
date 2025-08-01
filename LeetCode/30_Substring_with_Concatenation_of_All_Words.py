from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        count_words=len(words)
        len_words=len(words[0])
        len_s=len(s)
        dict_word=Counter(words)
        result=[]
        for i in range(len_s-len_words+1):
            seen={}
            j=0
            while j<count_words:
                start=i+j*len_words
                word=s[start:start+len_words]
                if word in words:
                    seen[word]=seen.get(word,0)+1
                    if seen[word] > dict_word[word]:
                        break
                else:
                    break
                j+=1
            if j==count_words:
                result.append(i)
        return result


if __name__ == '__main__':
    obj = Solution()
    o = obj.findSubstring("barfoothefoobarman",["foo", "bar"])
    print(o)