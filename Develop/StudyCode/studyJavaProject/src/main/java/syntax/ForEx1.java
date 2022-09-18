package syntax;

import java.util.Arrays;
import java.util.Collection;

public class ForEx1 {
    public static void main(String args[]) {
        int[] arr = {10, 20, 30, 40, 50};

        // 기존 for문
        for (int i = 0; i < arr.length; i++) {
            System.out.println("for문 >>> : "+arr[i]);
        }

        // 향상된 for문
        for (int temp : arr) {
            System.out.println("향상된 for문 >>> : "+temp);
        }

        int[] arr2={10,30,20,60,50};
        arr2= Arrays.stream(arr2).sorted().toArray();

        // 기존 for문은 인덱스 번호가 int i에 저장되어 있다.
        for (int i = 0; i < arr.length; i++) {
            System.out.println(i+"번째 >>> : "+arr2[i]);
        }

        // 향상된 for문은 인덱스 번호를 알 수 없다.
        for (int temp2 : arr2){
            System.out.println("향상된 for문 >>> : "+temp2);
        }

    }
}
