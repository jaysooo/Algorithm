import sys
#
input = sys.stdin.readline


def solution():
    N = int(input().strip())
    attendance_system = dict()
    for i in range(N):
        log = input().split("")
        name = log[0]
        command = log[1]
        if command == "enter":
            attendance_system[name] = True
        else:
            del(attendance_system[name])

    a = "\n".join([x[0] for x in sorted(attendance_system.items(),key = lambda x: x[0],reverse=True)])
    print(a)




if __name__ == '__main__':
    solution()