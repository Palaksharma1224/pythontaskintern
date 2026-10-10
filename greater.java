import java.util.*;

public class greater
{
    public static int  greaterNum(int a , int b)
    {
        if(a>b||b<a)
        {
            System.out.print("a is greater");
            return a;
        }
        else
        {
            System.out.print("b is greater");
            return b;
        }
    }
    public static void main(String args[])
    {
        Scanner sc= new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(greaterNum(a,b));
    } 
}