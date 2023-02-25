package LambdaExpression;

public class LambdaExTest1 {

    public static void main(String args[]){
        MyFunction func = (int a, int b) -> a > b ? a : b;

        int big = func.max(1, 2);
        System.out.println("big >> : "+big);
    }
}
