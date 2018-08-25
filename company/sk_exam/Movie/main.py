t=['spy','ray','spy','room','once','ray','spy','once']
def solution(movie):
    answer = []
    movie_dict={}
    for item in movie:
        if item in movie_dict:
            cur=movie_dict[item]
            movie_dict[item]=(cur+1)
        else:
            movie_dict[item]=1

    answer=sorted(sorted(movie_dict), key=movie_dict.__getitem__,reverse=True)

    return answer



print(solution(t))