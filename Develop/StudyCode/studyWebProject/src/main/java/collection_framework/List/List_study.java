package collection_framework.List;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class List_study {
	public static void main(String[] args) {
		/*
		 public interface List<E>
		 extends Collection<E>
		 */
		
		//  List<Map<String, String>>
		Map<String, String> map=new HashMap();
		map.put("R", "레드");
		map.put("W", "우드");
		map.put("K", "케이");
		
		
		List<Map<String, String>> list_map=new ArrayList();
		
		list_map.add(map);
		
		System.out.println(list_map.size());
		// 1
		
		System.out.println(list_map.get(0));
		// {R=레드, W=우드, K=케이}
		System.out.println(list_map.get(0).get("R"));
		// 레드
		
		Map<String, String> map2=new HashMap();
		map2.put("김", "철수");
		map2.put("홍", "길동");
		
		list_map.add(map2);
		
		System.out.println(list_map.size());
		// 2
		
		System.out.println(list_map.get(1));
		// {김=철수, 홍=길동}
		System.out.println(list_map.get(1).get("김"));
		// 철수
	}

}
