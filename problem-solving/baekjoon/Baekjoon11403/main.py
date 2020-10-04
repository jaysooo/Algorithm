

def floydWarshall(dag, N):
    for i in range(0, N):
        for j in range(0, N):
            if dag[i][j] == 0 and i != j:
                dag[i][j] = -1  # INF

    for k in range(0, N):
        for i in range(0, N):
            for j in range(0, N):
                if dag[i][k] > 0 and dag[k][j] > 0:
                    dag[i][j] = 1

    for i in range(0, N):
        for j in range(0, N):
            if dag[i][j] <= 0:
                print('{} '.format(0), end='')
            else:
                print('{} '.format(dag[i][j]), end='')
        print()


def main():
    N = int(input())
    dag = []
    for i in range(0, N):
        line = input().split(' ')
        dag += [[int(x) for x in line]]

    floydWarshall(dag, N)


if __name__ == '__main__':
    main()
