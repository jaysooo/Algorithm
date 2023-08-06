import sys
input = sys.stdin.readline

class MyStack():
    def __init__(self) -> None:
        self.stack = []

    # 3: 스택에 들어있는 정수의 개수를 출력한다.
    def item_count(self):
        return len(self.stack)

    # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    def item_pop(self):
        item = -1
        if len(self.stack) > 0:
            item = self.stack.pop(-1)
            pass

        return item

    # 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
    def item_insert(self, item):
        result = 0
        self.stack.append(item)

        return result

    # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    def is_empty(self):
        item = 1
        if len(self.stack) > 0:
            item = 0
        return item

    #: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 - 1을 대신 출력한다.
    def top_item(self):
        item = -1
        if len(self.stack) > 0:
            item = self.stack[-1]
        return item


def solution():
    stack = MyStack()
    N = int(input())
    for i in range(0, N):
     #   while(True):
        prompt = input().split(" ")
        if int(prompt[0]) == 1:
            stack.item_insert(int(prompt[1]))
        elif int(prompt[0]) == 2:
            print(stack.item_pop())
        elif int(prompt[0]) == 3:
            print(stack.item_count())
        elif int(prompt[0]) == 4:
            print(stack.is_empty())
        elif int(prompt[0]) == 5:
            print(stack.top_item())
        else:
            # command not found Exception
         #   break
            pass


solution()
# if __name__ == '__main__':
#     solution()
