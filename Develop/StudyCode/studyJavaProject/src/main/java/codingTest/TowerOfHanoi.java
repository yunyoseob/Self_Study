package codingTest;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class TowerOfHanoi {
    public List<Stack<Integer>> moveDisk(Stack<Integer> fromS, Stack<Integer> toS){
        List<Stack<Integer>> sList = new ArrayList<>();
        if(fromS.empty()){
            System.out.println("옮기려는 타워에 원반이 없습니다.");
            sList=null;
        }else if(!toS.empty() && fromS.lastElement() > toS.lastElement()){
            System.out.println("옮기려는 원반 값이 대상 원반 값보다 크므로 옮길 수 없습니다.");
            sList=null;
        }else{
            toS.push(fromS.pop());
            sList.add(fromS);
            sList.add(toS);
        }
        return sList;
    }

    public Integer countMove(Stack<Integer> fstTower, Stack<Integer> sndTower, Stack<Integer> thdTower){
        int cnt =0;

        // 경우의 수는 여섯 가지 : 1 => 2, 1 => 3, 2 => 3, 3 => 2, 3 => 1, 2 => 1
        List<Stack<Integer>> fsList = moveDisk(fstTower, sndTower);
        if(fsList != null){
            fstTower=fsList.get(0);
            sndTower=fsList.get(1);
            cnt++;
            System.out.println("첫 번째 원반에서 두 번째 원반으로 이동 >>> : "+cnt);
            System.out.println("fstTower >> : "+fstTower);
            System.out.println("sndTower >> : "+sndTower);
            countMove(fstTower, sndTower, thdTower);
        }else{
            List<Stack<Integer>> ftList = moveDisk(fstTower, thdTower);
        }



      return cnt;
    }

    public static void main(String args[]){
        TowerOfHanoi toh = new TowerOfHanoi();
        Stack<Integer> fstTower= new Stack();
        Stack<Integer> sndTower = new Stack();
        Stack<Integer> thdTower = new Stack();
        int cnt=0;

        fstTower.push(3);
        fstTower.push(2);
        fstTower.push(1);

        System.out.println(fstTower);
        System.out.println(fstTower.lastElement());
    }
}
