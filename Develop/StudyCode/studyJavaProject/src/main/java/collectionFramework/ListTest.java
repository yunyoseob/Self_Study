package collectionFramework;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class ListTest {
    public void basicList(){
        List list = new ArrayList();

        for(int idx=0; idx<101; idx++){
            list.add(idx);
        }
        list.add("A");

        System.out.println("1. firstValue : "+Integer.valueOf(list.get(0).toString())); // 0
        System.out.println(list.indexOf("0")); // 0
        System.out.println(list.lastIndexOf("A")); // 101

        list.remove(0);
        list.remove("A");

        System.out.println("2. firstValue : "+Integer.valueOf(list.get(0).toString())); // 1
        System.out.println(list.indexOf("0")); // -1
        System.out.println(list.lastIndexOf("A")); // -1

        // 1부터 100까지 20개씩 끊어서 5개의 리스트로
        List subList1 = list.subList(0, 20);
        List subList2 = list.subList(20, 40);
        List subList3 = list.subList(40, 60);
        List subList4 = list.subList(60, 80);
        List subList5 = list.subList(80, 100);

        Collection collection= new ArrayList();
        collection.addAll(subList1);
        collection.addAll(subList2);
        collection.addAll(subList3);
        collection.addAll(subList4);
        collection.addAll(subList5);
        System.out.println("================");

        System.out.println("collection size : "+collection.size()); // collection size >> : 100

        Collection collection2 = new ArrayList();
        Collection collection3 = new ArrayList();
        for(int idx2=1; idx2<201; idx2++){
            collection2.add(idx2);
            collection3.add(idx2);
        }

        // 1 ~ 200까지 중에 1~100까지 삭제
        collection2.removeAll(collection);
        System.out.println("collection2's first value : "+collection2.toArray()[0].toString()); // 101

        // 1 ~ 200까지 중에 1~100을 남겨두고 나머지 삭제
        collection3.retainAll(collection);
        System.out.println("collection3's first value : "+collection3.toArray()[0].toString()); // 1
    }
    public static void main(String args[]){
        ListTest listTest = new ListTest();
        listTest.basicList();
    }
}
