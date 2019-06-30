

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class NodeTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def preOrderTravel(self):
        self
        
    def main():

    # 이진 트리 생성
    bst = NodeTree()
    # 바이너리 트리의 클래스를 만들고,입력값에 의해 형성된 트리의 형태를 그대로 노드의 인위적인 삽입을 수행한다.
    # 전위 순회와 후위순회를 수행한다.
    # 인위적인 삽입의 조건은 문제에 명시된 조건으로.루트 노드 부터 y 축의 값을 하나하나 줄여 나가면서 트리를 완성해나아감.
    # 리프 노드 삽입시 리프 노드가 없을 경우의 탐색은 부모노드의 x 축 좌표로 범위를 이용해 찾는다.
    # ref.임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다. 
    testCase = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    visited=[False for i in range(0,len(testCase))]
    ordererdCase = 
    # 이진 트리 데이터 삽입
        # 루트 노드 부터 리프노드 까지 탐색
        # y값이 가장 큰 값 = 루트 노드
        #  root.leftNode = v if [ root.x > child.x and root.y > child.x ]  ref.임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다 
        #  root.rightNode= v if [ root.y > child.y and root.y < child.y ] ref.임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다
        # 리프 노드가 없다면 continue
    #전위 순회
    #후위 순회
