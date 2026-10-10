import java.util.*;

public class sumOddNumber
{
    public  static void  sumOfOdd(int n)
    {
        int sum=0;
        for(int i=1;i<=n;i++)
        {
            if(i%2!=0)
            {
                sum=i+sum;
                System.out.println(sum);
            }
        }
        System.out.println(sum);
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sumOfOdd(n);
    }
}