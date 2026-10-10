import java.util.*;

public class posNegZero
{
    public static void main(String args[])
    {
       Scanner sc= new Scanner(System.in);
       int num=sc.nextInt();
       if (num<0)
        {
            System.out.print("negative");
        } 
        else if(num>0)
        {
            System.out.print("positive");
        }
        else if(num==0)
        {
            System.out.print("zero value");
        }
        else
        {
            System.out.print("invalid");
        }
    }
}