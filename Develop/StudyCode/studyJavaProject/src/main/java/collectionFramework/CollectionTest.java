package collectionFramework;

import java.util.*;

public class CollectionTest {
    public void basicCollection(){
        Collection listCol=new ArrayList();

        listCol.add("1");
        listCol.add("2");
        listCol.add("3");

        Collection setCol = new HashSet();

        setCol.add("4");
        setCol.add("5");
        setCol.add("6");

        Collection collection = new ArrayList();

        collection.addAll(listCol);
        collection.addAll(setCol);

        collection.forEach(x -> System.out.print(x+", ")); // 1, 2, 3, 4, 5, 6,

        collection.clear();

        System.out.println();
        System.out.println("collection.isEmpty() : "+collection.isEmpty()); // collection.isEmpty() : true
    }

    public void changeType(){
        Collection setCol = new HashSet();

        setCol.add("4");
        setCol.add("5");
        setCol.add("6");

        List<Object> objList = new ArrayList(setCol);

        for(Object obj : objList){
            System.out.print(obj.toString()+", "); // 4, 5, 6,
        }
    }

    public static void main(String args[]){
        CollectionTest collectionTest = new CollectionTest();
        // collectionTest.basicCollection();
        collectionTest.changeType();
    }
}
