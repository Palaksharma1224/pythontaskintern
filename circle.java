import java.util.*;

public class circle
{
    public static int GreaterNum(int radius)
    {
        double pie = 3.14;
        double result=2*pie*radius;
        System.out.print("circumfrenece of circle"+result);
        return radius;
    }

public static void main(String args[])
{
    Scanner sc=new Scanner(System.in);
    int radius=sc.nextInt();
    System.out.print(GreaterNum(radius));
}
}