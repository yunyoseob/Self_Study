# CollectionFramework & Stream

발표자 : 윤요섭

발표일 : 2023-02-26

# Collection Framework

컬렉션 프레임 워크 : '데이터 군을 다루고 표현하기 위한 단일화된 구조'

## Collection Framework 종류

 **✔️ public interface Iterable<T>**

![image](https://user-images.githubusercontent.com/81727895/221247582-ed182109-76a3-4812-a020-643faa9935ab.png)

**✔️ public interface Collection<E> extends Iterable**

![image](https://user-images.githubusercontent.com/81727895/221247069-7ab3329b-8279-416d-8ecd-9019d52558fb.png)

**✔️ public interface List<E> extends Collection<E>**

![image](https://user-images.githubusercontent.com/81727895/221247265-48e4d49d-61f4-4913-a5e3-5bd407513820.png)

**✔️ public interface Set<E> extends Collection<E>**

![image](https://user-images.githubusercontent.com/81727895/221247450-36740afd-9619-47e8-8946-2164f9846baf.png)

**🤔 Map은 어디 있을까?**

**✔️ public interface Map<K, V>**

![image](https://user-images.githubusercontent.com/81727895/221248261-d2ea6455-a8ba-4be9-806b-2a67419213d4.png)

## Collection

Collection 인터페이스는 컬렉션 클래스에 저장된 데이터를 읽고, 추가하고 삭제하는 등 컬렉션을 다루는데 가장 기본적인 메서드 들을 정의하고 있다.

```java
package collectionFramework;

import java.util.*;

public class CollectionTest {
    public void basicCollection(){
        Collection listCol=new ArrayList();

        // add(Object o), addAll(Collection c) : 지정된 객체(Object) 
        // 또는 Collection(c)의 객체들을 Collection에 추가한다.
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


        System.out.println("collection.isEmpty() : "+collection.isEmpty()); 
        // collection.isEmpty() : true
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
        collectionTest.basicCollection();
        collectionTest.changeType();
    }
}
```

**🤔 참조변수의 타입을 ArrayList 타입이 아니라 Collection 타입으로 한 이유는 뭔가요?**

```
Collection에는 없고 ArryList에만 있는 메서드를 사용하는게 아니라면, Collection 타입의 참조변수로 선언하는 것이 좋다. 만일 Collection 인터페이스를 구현한 다른 클래스, 예를 들어 LinkedList로 바꿔야 한다면 선언문 하나만 변경하면 나머지 코드는 검토하지 않아도 된다. 

참조변수 타입이 Collection이므로 Collection에 정의되지 않은 메서드는 사용되지 않았을 것이 확실하기 때문이다.

그러나, 참조변수 타입을 ArrayList로 했다면, 선언문 이후의 문장들을 검토해야 한다.

Collection에 정의되지 않은 메서드를 호출했을 수 있기 때문이다.
```

## List

List는 기존의 Vector를 개선 한 것으로, 데이터의 저장순서가 유지되고 중복을 허용한다는 특징을 갖는다.

## ArrayList

ArrayList의 경우, Object 배열을 이용해서 데이터를 순차적으로 저장한다.

배열에 더 이상 저장할 공간이 없으면 보다 큰 새로운 배열을 생성해서 기존의 배열에 저장된 내용을 새로운 배열로 복사한 다음에 저장한다.

```java
package collectionFramework;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class ListTest {
    public void basicList(){
        List list = new ArrayList();

        // 0부터 100까지 숫자를 list에 담는다.
        for(int idx=0; idx<101; idx++){
            list.add(idx);
        }
        list.add("A");

        System.out.println("1. firstValue : "+Integer.valueOf(list.get(0).toString())); // 0
        System.out.println(list.indexOf(0)); // 0
        System.out.println(list.lastIndexOf("A")); // 101

        // 0번째 index를 제거
        list.remove(0);
        // "A"라는 Object를 제거
        list.remove("A");

        System.out.println("2. firstValue : "+Integer.valueOf(list.get(0).toString())); // 1
        System.out.println(list.indexOf(0)); // -1
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

        System.out.println("collection size : "+collection.size()); // collection size : 100

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
```

## LinkedList

배열은 가장 기본적인 형태의 자료구조로 구조가 간단하며, 사용하기 쉽다.

그러나, 크기를 변경할 수 없고, 비순차적인 데이터의 추가 또는 삭제에 시간이 많이 걸린다.

이러한 배열의 단점을 보완하기 위해 LinkedList라는 자료구조가 고안되었다.

```
 ✔️ LinkedList : 배열과 달리 모든 데이터가 연속적으로 존재하는 것이 아니라, 불연속적으로 존재하는 
 
 데이터를 서로 연결(link)한 형태로 구성되어 있다.
```

<img src="https://www.nextree.co.kr/content/images/2021/01/jdchoi_20140225_arrayvslinkedlist11.png">

- 이미지 출처 : [자료구조: Linked List 대  ArrayList](https://www.nextree.co.kr/p6506/)

링크드 리스트에서 데이터 삭제는 이전 요소가 삭제하고자 하는 다음 요소를 참조하도록 변경한다.

**🤔 ArrayList와 LinkedList 누가 더 빠를까?**

```
순차적으로 추가/삭제하는 경우 : ArrayList > LinkedList

중간 데이터를 추가/삭제하는 경우 : LinkedList > ArrayList
```

## Queue & Stack

<img src="https://images.velog.io/images/leejuhwan/post/6f85b3af-132b-4b25-90df-b0dae6baf370/Computer-science-fundamentals_6.1.png" width="500">


<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGj4MMrt-PY73RHcL_z2fwIuOM0UpdpNzQow&usqp=CAU" width="500">

Stack : LIFO (Last In First Out)

Queue : FIFO (First In First Out)

- FIFO인 큐는 항상 첫 번째 저장된 데이터를 삭제하므로, ArrayList와 같은 배열 기반의 컬렉션 클래스를 사용한다면 데이터를 꺼낼 때마다 빈 공간을 채우기 위해 데이터 복사가 발생하므로 비효율적 => 따라서 LinkedList()를 사용

```java
package collectionFramework;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class StackQueueTest {
    public static void main(String args[]){
        Stack stack = new Stack();
        Queue queue = new LinkedList();

        stack.push("0");
        stack.push("1");
        stack.push("2");

        queue.offer("0");
        queue.offer("1");
        queue.offer("2");

        System.out.println("=== Stack ===");
        while(!stack.isEmpty()){
            System.out.print(stack.pop()+", "); // 2, 1, 0,
        }

        System.out.println();
        System.out.println("=== Queue ===");
        while(!queue.isEmpty()){
            System.out.print(queue.poll()+", "); // 0, 1, 2, 
        }
    }
}
```

- 스택과 큐 활용 예시

```
스택 : 수식 계산, 수식 괄호검사, 워드프로세서의 undo/redo, 웹브라우저의 뒤로/앞으로

큐 : 인쇄작업 대기목록, 버퍼(buffer)
```

## PriorityQueue

Queue 인터페이스의 구현체 중 하나로, 저장한 순서와 관계없이 우선순위(priority)가 높은 것부터 꺼내게 된다는 특징이 있다. (null을 저장 할 수 없다.)

```
PriorityQueue는 저장공간으로 배열을 사용하며, 각 요소를 '힙(heap)'이라는 자료구조의 형태로 저장한다.
```

```java
package collectionFramework;

import java.util.PriorityQueue;
import java.util.Queue;

public class PriorityQueueTest {
    public static void main(String args[]){
        Queue pq = new PriorityQueue<>();
        pq.offer(3);
        pq.offer(1);
        pq.offer(5);
        pq.offer(2);
        pq.offer(4);

        Object obj = null;
        // 우선 순위 : 숫자가 작을수록 높음
        while((obj = pq.poll()) != null){
            System.out.print(obj+", "); // 1, 2, 3, 4, 5, 
        }
    }
}
```

## Dequq(Double - Ended Queue)

Queue의 변형으로, 한 쪽 끝으로만 추가/삭제 할 수 있는 Queue와 달리, Deque(덱 또는 디큐라고 읽음)은 양쪽 끝에 추가/삭제가 가능하다.

- Deque의 조상은 Queue이며, 구현체로는 ArrayDeque와 LinkedList 등이 있다.

✔️ Queue

<img src="https://www.happycoders.eu/wp-content/uploads/2022/05/queue-data-structure.v4-600x174.png" width="700">


✔️ Deque

<img src="https://www.happycoders.eu/wp-content/uploads/2022/05/deque-data-structure.v4-800x135.png" width="700">



Deque는 스택과 큐를 하나로 합쳐놓은 것과 같으며 스택으로 사용할 수도 있고, 큐로 사용할 수도 있다.

|Deque|Queue|Stack|
|--|--|--|
|offerLast()|offer()|push()|
|pollLast()|-|pop()|
|pollFirst()|poll()|-|
|peekFirst()|peek()||
|peekLast()|-|peek()|

```
=== Stack 메서드 ===

pop() : Stack의 맨 위의 객체를 꺼낸다.

peek() :  Stack의 맨 위에 저장된 객체를 반환, pop()과 달리 Stack에서 객체를 꺼내지는 않음

push(Object item) : Stack에 객체(item)를 저장한다.

=== Queue의 메서드 ===

add(Object o) : 지정된 객체를 Queue에 추가한다.

offer(Object) : Queue에 객체를 저장

remove() : Queue에서 객체를 꺼내 반환 (비어있으면 NoSuchElementException 발생)

poll() : Queue에서 객체를 꺼내서 반환 (비어있으면 null을 반환)

element() :  삭제없이 요소를 읽어온다. (비어있으면 NoSuchElementException 발생)

peek() : 삭제없이 요소를 읽어온다. (비어있으면 null을 반환)
```

# Lambda Expression

- Stream에 들어가기 전에 Lambda Expression에 대해  알아보기

```
JDK 1.5 이후 : generics 등장

JDK 1.8 이후 : lambda expression 등장
```


**✔️ 람다식이란?**

```
메서드를 하나의 식(expression)으로 표현한 것


ex) 

반환타입 메서드이름(매개변수 선언){
    문장들
}

=> 

(매개변수 선언) -> { 문장들 }
```

✔️ 설명 예시

```java
int max(int a, int b){
    return a > b ? a : b;
}

// =>

(int a, int b) -> {
    return a > b ?  a : b;
}

// => 

(int a, int b) -> a > b ? a : b
// 문장(statement)가 아닌 식이므로 끝에 ;를 붙이지 않는다.

// => 

(a, b) -> a > b ? a : b

// 다른 예시
(a) -> a * a

// =>

a -> a * a

// return 문이 경우 괄호 {}를 생략할 수 없다.

(int a, int b) -> {return a > b ? a : b;} // OK

(int a, int b) -> return a > b ? a : b;
```

✔️ 자바 코드 예시

Before : 람다식 사용 이전

- interface : MyFunction
```java
package LambdaExpression;

@FunctionalInterface
public interface MyFunction {
    int max(int a, int b);
}
```

- class : LambdaExTest1
```java
package LambdaExpression;

public class LambdaExTest1 {

    public static void main(String args[]){
        MyFunction func = new MyFunction() {
            @Override
            public int max(int a, int b) {
                return a > b ? a : b;
            }
        };

        int big = func.max(1, 2);
        System.out.println("big >> : "+big);
        // big >> : 2
    }
}
```

After : 람다식 사용 이후

```java
package LambdaExpression;

public class LambdaExTest1 {

    public static void main(String args[]){
        MyFunction func = (int a, int b) -> a > b ? a : b;

        int big = func.max(1, 2);
        System.out.println("big >> : "+big);
        // big >> : 2
    }
}
```

**✔️ java.util.function 패키지**

일반적으로 자주 쓰이는 형식의 메서드를 함수형 인터페이스로 미리 정의해놓았다.

|함수형 인터페이스|메서드|설명|
|--|:--:|--|
|java.lang.Runnable| void run() | 매개변수도 없고, 반환값도 없음 |
| Supplier<T> |  T get() | 매개변수는 없고, 반환 값만 있음 |
| Consumer<T> |  void accept(T t) | Supplier와 반대로 매개변수만 있고, 반환 값이 없음 |
| Function<T, R> | R apply(T t) | 일반적인 함수, 하나의 매개변수를 받아서 결과를 반환 |
| Predicate <T> | boolean test(T t) | 조건식을 표현하는 데 사용됨. 매개변수는 하나, 반환 타입은 boolean |


**✔️ 매개변수가 두 개인 함수형 인터페이스**

|함수형 인터페이스| 메서드 | 설명|
|--|:--:|--|
|BiConsumer<T, U> | void accept(T t, U u)|두 개의 매개변수만 있고, 반환값이 없음|
|BiPredicate<T, U> | boolean test(T t, U u) | 조건식을 표현하는데 사용됨. 매개변수는 둘, 반환값은 boolean |
|BiFunction<T, U, R> | R apply(T t, U u) | 두 개의 매개변수를 받아서, 하나의 결과를 반환 |

- Supplier는 매개변수는 없고 반환값만 존재하는데, 메서드는 두 개의 값을 반환할 수 없으므로 BiSupplier가 없는 것이다.

**✔️ 컬렉션 프레임웍과 함수형 인터페이스**

|인터페이스| 메서드 | 설명|
|--|:--:|--|
|Collection| boolean removeIf(Predicate<E> filter | 조건에 맞는 요소를 삭제 |
|List| void replaceAll(UnaryOperator<E> operator) | 모든 요소를 변환하여 대체 |
|Iterable| void forEach(Consumer<T> action) | 모든 요소에 작업 action을 수행 |
| Map | V compute(K key, BiFunction<K, V, V> f) | 지정된 키의 값에 작업 f를 수행 |
| Map | V computeIfAbsent(K key, Function<K,V> f) |  키가 없으면, 작업 f 수행 후 추가 |
| Map | V computeIfPresent(K key, BiFunction<V, V, V> f) | 지정된 키가 있을 때, 작업 f 수행 |
| Map | V merge(K key, V value, BiFunction<V, V, V> f) | 모든 요소에 병학작업 f를 수행|
| Map | void forEach(BiConsumer<K, V> action) | 모든 요소에 작업 action을 수행 |
 | Map | void replcaceAll(BiFunction<K, V, V> f) | 모든 요소에 치환작업 f를 수행 |


**✔️ 메서드 참조?**


```
Function<String, Integer> f = (String s) -> Integer.parseInt(s);
```

이를 역으로 생각하면 다음과 같다.

```java
Integer wrapper(String s){
    return Integer.parseInt(s);
}
```

함수 wrapper가 하는 일은 String을 Integer로 바꿔줄 뿐이다.

이를 간략하게 표현하기 위해 메서드 참조를 쓴다.

```
Function<String, Integer> f =  Integer::parseInt
```

- 예시

```java
BiFunction<String, String, Boolean> f = (s1, s2) -> s1.equals(s2);

// =>

BiFunction<String, String, Boolean> f = String::equals; // 메서드 참조
```

- 하나의 메서드만을 호출하는 람다식은 '클래스이름::메서드이름' 또는 '참조변수::메서드이름'으로 바꿀 수 있다.

# Stream

이전에는 컬렉션이나 배열에 데이터를 담고 원하는 결과를 얻기 위해 for문과 Iterator를 이용해서 코드를 
작성해왔다.

스트림은 데이터 소스를 추상화하고, 데이터를 다루는데 자주 사용되는 메서드들을 정의해 놓았다. 

데이터 소스를 추상화하였다는 것은, 데이터 소스가 무엇이던 간에 같은 방식으로 다룰 수 있게 되었다는 것과

코드의 재사용성이 높아진다는 것을 의미한다.


















