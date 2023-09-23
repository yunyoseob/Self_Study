package collectionFramework;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class StackQueueTest {
    public static void main(String args[]){
        Stack stack = new Stack();
        // FIFO인 큐는 항상 첫 번째 저장된 데이터를 삭제하므로,
        // ArrayList와 같은 배열 기반의 컬렉션 클래스를 사용한다면
        // 데이터를 꺼낼 때마다 빈 공간을 채우기 위해 데이터 복사가 발생하므로
        // 비효율적 => 따라서 LinkedList()를 사용
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
