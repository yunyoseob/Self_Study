package syntax;

public class IfSwitchEx {
    public static void main(String args[]) {
        int score = 80;

        if (score >= 90) {
            System.out.println("90점 이상 : A");
        } else if (score >= 80) {
            System.out.println("80점 이상 : B");
            // 80점 이상 : B
        } else if (score >= 70) {
            System.out.println("70점 이상 : C");
        } else if (score >= 60) {
            System.out.println("60점 이상 : D");
        } else {
            System.out.println("재시험 대상");
        }

        // break문이 없는 switch
        switch (score) {
            case 90:
                System.out.println("90점 이상 : A");
            case 80:
                System.out.println("80점 이상 : B");
                // 80점 이상 : B
            case 70:
                System.out.println("70점 이상 : C");
                // 70점 이상 : C
            case 60:
                System.out.println("60점 이상 : D");
                // 60점 이상 : D
            default:
                System.out.println("당신의 스코어는 >>> : "+score);
                // 당신의 스코어는 >>> : 80
        }

        // break문이 있는 switch
        switch (score) {
            case 90:
                System.out.println("90점 이상 : A");
                break;
            case 80:
                System.out.println("80점 이상 : B");
                // 80점 이상 : B
                break;
            case 70:
                System.out.println("70점 이상 : C");
                break;
            case 60:
                System.out.println("60점 이상 : D");
                break;
            default:
                System.out.println("당신의 스코어는 >>> : "+score);
        }
    }
}
