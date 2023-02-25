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
        while((obj = pq.poll()) != null){
            System.out.print(obj+", ");
        }
    }
}
