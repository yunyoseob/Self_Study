package test;

public class Test1 {
    public void primeNumber(){
        int p=0;

        for (int i=2; i<100; i++){
            int t=(int)Math.sqrt(i);
            for(int j=2; j<=t; j++){
                if(i%j==0){
                    break;
                }
                if(j==t){
                    p=i;
                }
            }
            System.out.println(p);
        }
    }

    public void quiz2(){
        int i=0, j=0;
        for(int k=0; k<3; k++){
            System.out.println(k+"번째 i >>> : "+i);
            System.out.println(k+"번째 j >>> : "+j);

            if((++i>1) && (++j>1)){
                System.out.println("if 안의 i >>> : "+i);
                System.out.println("if 안의 j >>> : "+j);
                i++;
            }
        }
        System.out.println(i+""+j);
    }

    public void quiz3(int[] a, int n){
        int i,j;
        int min, temp;
        for(i=0; i<n-1; i++){
            min=i;

            for(j=i+1; j<n; j++){
                if(a[j]<a[min]){
                    min=j;
                }

                temp=a[min];
                a[min]=a[i];
                a[i]=temp;
            }
        }

    }

    public static void main(String[] args){
        Test1 test1=new Test1();
        // test1.primeNumber();
        // test1.quiz2();
        int[] a={3,2,5,1,4};
        test1.quiz3(a, 5);
        for(int i=0; i<a.length; i++){
            System.out.print(a[i]);
        }
    }
}
