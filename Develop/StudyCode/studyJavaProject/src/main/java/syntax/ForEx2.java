package syntax;

public class ForEx2 {
    public static void main(String args[]) {

        System.out.println("for문 시작");
        for (int i = 2; i <= 9; i++) {
            for (int j=1; j<=9; j++){
                if(j==5)
                    break;
                System.out.println(i+"*"+j+"="+i*j);
            }
            System.out.println();
        }
        // 2~9단 까지 i*4까지 출력된다. 중첩 for문은 break가 되지만, 밖에 있는 for문은 break가 되지 않는다.

        // 이름 붙은 반복문
        System.out.println("이름 붙은 for문 시작");
        Loop1: for (int i = 2; i < 9; i++) {
            for (int j=1; j<=9; j++){
                if(j==5)
                    break Loop1;
                System.out.println(i+"*"+j+"="+i*j);
            }
            System.out.println();
        }
        // 밖에 있는 for문까지 break가 된다.
    }
}
