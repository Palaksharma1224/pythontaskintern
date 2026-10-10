import java.util.*;

public class power
{
    public static void main(String args[])
    {
         System.out.print("enter value of x");
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        System.out.print("enter value of n");
        int n = sc.nextInt();
        int result =1;
        for(int i=1;i<=n;i++)
        {
            result=result*x;
            System.out.println(result);
        }
    }
}