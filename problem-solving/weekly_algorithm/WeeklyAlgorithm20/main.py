
# input: 1 -> 2 -> 3 -> 4
# output: 1 -> 4 -> 2 -> 3

class Node:
    def __init__(self, *args, **kwargs):
        self.data=args[0]
        self.next_link=None
    def __str__(self):
        return super().__str__()

class NodeList:
    def __init__(self, *args, **kwargs):
        self.root=None
        self.last_node=None
        self.matrix=[]
        return super().__init__(*args, **kwargs)

    def insert(self,nodedt):
        newnode=Node(nodedt)
        if self.root is None:
            self.root=newnode
            self.last_node=newnode
            self.matrix.append(newnode)
        else:
            self.last_node.next_link=newnode
            self.last_node=newnode
            self.matrix.append(newnode)

    def reOrder(self):
        leng=len(self.matrix)-1
        for idx,va in enumerate(self.matrix):
            if round((leng/2)) == idx:  #마지막 노드
                n=va.next_link	    
                n.next_link=None	 
                break
            else:
                n=va.next_link	   
                va.next_link=self.matrix[leng-idx]
                self.matrix[leng-idx].next_link=n

    def travelNode(self):
        tmpNode=self.root
        while(tmpNode is not None):
            print('{}->'.format(tmpNode.data))
            tmpNode=tmpNode.next_link


mylist=NodeList()
mylist.insert(1)
mylist.insert(2)
mylist.insert(3)
mylist.insert(4)
mylist.insert(5)
mylist.insert(6)
mylist.insert(7)
mylist.insert(8)
#mylist.travelNode()
mylist.reOrder()
mylist.travelNode()
