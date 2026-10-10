import java.util.*;

public class mul
{
    public static int mulOfNumbers(int a,int b)
    {
        return a*b;
}
public static void main(String args[])
{
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b= sc.nextInt();
    System.out.println("multiplication of two numbers:"+ mulOfNumbers(a, b));
}
}
