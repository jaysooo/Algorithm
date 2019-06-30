str="5 6 + -"
    
comd=str.split(" ")
#print(comd)

top=0
stack=[]

def stackIsEmpty(top):
    if top==0:
        return 1
    else:
        return 0
def elemIsNotEnough(top):
    if top<2:
        return 1
    else:
        return 0

for elem in comd:
    print(stack)
    if elem.isdigit():
        stack.insert(top,elem)
        top+=1
    else:
        if stackIsEmpty(top):
            print("error")
        elif elem=="DUP":
            tmp=stack[top-1]
            stack.insert(top,tmp)
            top+=1
        elif elem=="POP":
            stack.pop(top-1)
            top-=1
        elif elemIsNotEnough(top):
            print("error")
        elif elem=="+":
            n1=stack.pop(top-1)
            n2=stack.pop(top-2)
            stack.insert(top-2,int(n1)+int(n2))
            top-=1
        elif elem=='-':
            n1=stack.pop(top-1)
            n2=stack.pop(top-2)
            stack.insert(top-2,int(n1)-int(n2))
            top-=1


print(stack[top-1])





select secondary.event_type as event_type,(latest.value-secondary.value) as value
from (
select *
from events join 
(
select a.event_type,max(a.time) as time
from events as a join (select event_type,max(time) as time
    from events 
    group by event_type having count(event_type) >= 2)
 as b on (a.event_type=b.event_type and a.time < b.time)
 group by a.event_type
 ) c using(event_type,time)) as secondary join
 (
select *
from events join (select event_type,max(time) as time
    from events 
    group by event_type having count(event_type) >= 2) as b
    using (event_type,time)
)  as latest on (secondary.event_type=latest.event_type)
order by event_type e,max(time) as time
    from events 
    group by event_type having count(event_type) >= 2) as b on 
    (a.event_type=b.event_type and a.time = b.time)
) as f on (f.event_type=s.event_type)


def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]


    import java.util.*;

class Solution {
    int solution(int M, int[] A) {
        int N = A.length;
        int[] count = new int[M + 1];
        for (int i = 0; i <= M; i++)
            count[i] = 0;
        int maxOccurence = 1;
        int index = -1;
        for (int i = 0; i < N; i++) {
            if (count[A[i]] > 0) {
                int tmp = count[A[i]];
                if (tmp > maxOccurence) {
                    maxOccurence = tmp;
                    index = i;
                }
                count[A[i]] = tmp + 1;
            } else {
                count[A[i]] = 1;
            }
        }
        return A[index];
    }
}



object Solution {
    import scala.util._
    def solution(M: Int, A: Array[Int]): Int = {
        var N: Int = A.length;
        var count: Array[Int] = Array.fill(M + 1)(0);
        var maxOccurence: Int = 1;
        var index: Int = -1;
        var i: Int = 0;
        while (i < N) {
            if (count(A(i)) > 0) {
                var tmp: Int = count(A(i));
                if (tmp > maxOccurence) {
                    maxOccurence = tmp;
                    index = i;
                }
                count(A(i)) = tmp + 1;
            } else {
                count(A(i)) = 1;
            }
            i = i + 1;
        }
        return A(index);
    }
}