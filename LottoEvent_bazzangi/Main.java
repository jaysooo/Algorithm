import java.util.*;
public class Main{
    public static void main(String[] args){
            System.out.println("program Run");
            // int n=6;
            // int d=1;
            // int k=1;
            // int j=1;

            int n=4;
            int d=0;
            int k=2;
            int j=2;

            int winner=0;
            ArrayList<Integer> lottoBucket = new ArrayList<Integer>();
            lottoBucket.add(1);
            for (int i = 4; i >= 2; i --){₩
                lottoBucket.add(i);
            }

            ListIterator<Integer> itr = lottoBucket.listIterator();

            int moveCnt=0;
            while(true){
                itr.next();
                //System.out.println(itr.next());
  //              System.out.println("MoveCnt:"+moveCnt+"\tk:"+k+"\tbucketSize:"+lottoBucket.size());
                
                if (moveCnt==k){   
//                    System.out.print("탈락자:"+lottoBucket.get(itr.nextIndex()-1));
                    itr.remove();
                    k=k+j;
                    moveCnt=0;
//                 System.out.println("\tMoveCnt:"+moveCnt+"\tk:"+k);
                }
                moveCnt++;
                if (lottoBucket.size()==1){
                    winner=lottoBucket.get(0);
                    break;
                }
                if (!itr.hasNext()){
                    itr=lottoBucket.listIterator();
                  }
            }
            System.out.println(winner);
            System.out.println("program End");
    }

}