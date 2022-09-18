package collectionFramework;

import java.util.ArrayList;
import java.util.Collections;

public class ArrayListEx1 {
    public static void main(String args[]){
        ArrayList list1=new ArrayList(10);
        list1.add(new Integer(1));
        list1.add(new Integer(2));
        list1.add(new Integer(5));
        list1.add(new Integer(3));

        for (int i=0; i<list1.size(); i++){
            System.out.print(list1.get(i));
            // 1253
        }
        
        // list 정렬
        Collections.sort(list1);
        System.out.println();

        for (int i=0; i<list1.size(); i++){
            System.out.print(list1.get(i));
            // 1235
        }

        ArrayList list2=new ArrayList(10);
        list2.add(new Integer(1));
        list2.add(new Integer(2));
        list2.add(new Integer(3));

        System.out.println();
        // list1 : [1,2,3,5], list2 : [1,2,3]
        // containsAll : 모든 요소를 포함하고 있는가?
        System.out.println("list1.containsAll(list2) >>> : "+list1.containsAll(list2));
        // list1.containsAll(list2) >>> : true
        // 1,2,3,5 ) 1,2,3

        list2.add(new Integer(4));
        System.out.println("list1.containsAll(list2) >>> : "+list1.containsAll(list2));
        // list1.containsAll(list2) >>> : false

        System.out.println("list1.contains(list2) >>> : "+list1.contains(list2));
        // list1.contains(list2) >>> : false

        System.out.println("list2.get(0) >>> : "+list2.get(0));
        // list2.get(0) >>> : 1

        // list1 : [1,2,3,5], list2.get(0) : 1
        // contains : Object를 포함하고 있는가
        System.out.println("list1.contains(list2.get(0)) >>> : "+list1.contains(list2.get(0)));
        // list1.contains(list2.get(0) >>> : true
    }
}
