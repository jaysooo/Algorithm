inputStr="1->2->3->4->5,N=2"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.current = None
        self.num_of_data = 0

    def append(self, data):
        #first node insert
        new_node= Node(data)
        if self.num_of_data==0:
            self.head=new_node
            self.current=new_node
            self.num_of_data += 1
        else:
            self.current.next=new_node
            self.current=new_node
            self.num_of_data += 1
    
    def printList(self):
        if self.num_of_data==0:
            print("No Data ..")
            return
        else:
            tmpPointer=self.head
            while (True):
                print(tmpPointer.data)
                print(" ")
                tmpPointer=tmpPointer.next
                if tmpPointer==None:
                    break
                   

def inputStrParsing(str):
    parsedStr=str.split(",")
    nodeElem= [int(x) for x in parsedStr[0].split("->")]
    
    N=parsedStr[1].split("=")[1]
    li_list=LinkedList()
    li_list.append(5)
    li_list.append(10)
    
    li_list.printList()

    #print(nodeElem)
    #print(N)

inputStrParsing(inputStr)