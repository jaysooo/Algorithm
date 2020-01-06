#7

import sys
class SimpleTree:
    parent_idx=[]
#    child_idx=[]
    size=0
    remainedNode=[]

    def __init__(self,size):
        self.parent_idx=[0 for i in range(size+1)]
#        self.child_idx=[0 for i in range(size+1)]
        self.parent_idx[1]=1
        self.size=size
        # for i in range(0,size+1):
        #     self.child_idx[i]=list()
        
            


    def insertIntoNode(self,n1,n2):
        if self.parent_idx[n1] ==0 and self.parent_idx[n2]==0:
            self.remainedNode.append([n1,n2])
            return 

        if self.parent_idx[n1]==0:
            self.parent_idx[n1]=n2      #부모 인덱스 셋팅
#            self.child_idx[n2].append(n1)
        else:
            self.parent_idx[n2]= n1
#            self.child_idx[n1].append(n2)
        
    def reBuildTree(self):
        for t in self.remainedNode:
            self.insertIntoNode(t[0],t[1])



    def printNode(self):

        print('parent_node : {}'.format(self.parent_idx))
#        print('child_nodes : {}'.format(self.child_idx))

    def printAnswer(self):
        for i in range(2,self.size+1):
            print(self.parent_idx[i])


def main():
    testCaseSize=int(input())
    
    myTree=SimpleTree(testCaseSize)

    for t in range(0,testCaseSize-1):
        node=input().split(' ')
        n1=int(node[0])
        n2=int(node[1])
        myTree.insertIntoNode(n1,n2)


    myTree.reBuildTree()
#    myTree.printNode()
    myTree.printAnswer()

if __name__=='__main__':
    main()
