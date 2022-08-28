

def solution():
    input_str = input().split()
    dice_set = set()
    dice_ods = [int(x) for x in input_str]
    dice_set = set(map(int,dice_ods))
    dice_dict = {i:dice_ods.count(i) for i in dice_ods}

    price = 0
    if len(dice_set) == 1:
        price = 10000 + dice_set.pop() * 1000
    elif len(dice_set) == 2:
        dice_a = dice_set.pop()
        dice_b = dice_set.pop()
        if dice_dict[dice_a] > dice_dict[dice_b]:
            price = 1000 + dice_a * 100
        else:
            price = 1000 + dice_b * 100
            
            
    else:
        price = max(dice_ods) * 100
    
    print(price)
solution()