
def get_registance_map():
    colors = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    registance_map = {}
    for idx,color in enumerate(colors):
        registance_map[color] = [str(idx),10**idx]

    return registance_map

def solution():
    registance_map = get_registance_map()
    input_colors=[]
    for i in range(3):
        input_colors.append(input())

    answer = int(registance_map[input_colors[0]][0]+registance_map[input_colors[1]][0]) * int(registance_map[input_colors[2]][1])


    print(answer)

if __name__=="__main__":
    solution()