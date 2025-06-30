class Solution:
    def intToRoman(self, num: int) -> str:
        intrmn={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I",}
        roman = ""
        for value, symbol in intrmn.items():
            while num >= value:
                roman += symbol
                num -= value
        return roman


if __name__ in "__main__":
    obj=Solution()
    o=obj.intToRoman(4)
    print(o)