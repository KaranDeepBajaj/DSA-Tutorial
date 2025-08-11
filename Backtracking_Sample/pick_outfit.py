tops = ["Red", "Blue"]
bottoms = ["Jeans", "Shorts"]


def backtrack(current_top_index, current_combination):
    if len(current_combination)==2:
        print(current_combination)
        return

    if len(current_combination)==0:
        for i in range(len(tops)):
            current_combination.append(tops[i])
            backtrack(i,current_combination)
            current_combination.pop()
    else:
        for i in range(len(bottoms)):
            current_combination.append(bottoms[i])
            backtrack(i,current_combination)
            current_combination.pop()


backtrack(0, [])