package collection_framework.Collection;

import java.util.Collection;
import java.util.Collections;
import java.util.ArrayList;

public class Collection_study {
	public static void main(String[] args) {
		/*
		 ## Collection vs Collections
		 
		 Collection 
		 
		 java.util.Collection<E>
		 
		 public interface Collection<E>
		 extends Iterable<E>
		 
		 ===============================
		 Collections
		 
		 java.util.Collections
		 
		 public class Collections 
		 extends Object
		
		 ## 주요 인터페이스 간의 상속 관계
		 Iterable<E> - Collection<E> - List<E>, Set<E>, Queue<E>
		*/
		
		ArrayList arrList=new ArrayList(10);
		arrList.add(new Integer(5));
		arrList.add(new Integer(4));
		arrList.add(new Integer(3));
		arrList.add(new Integer(2));
		arrList.add(new Integer(1));
		
		System.out.println(arrList);
		// [5, 4, 3, 2, 1]
		
		Collections.sort(arrList);

		System.out.println(arrList);
		// [1, 2, 3, 4, 5]
	}

}
