import java.util.*;

public class eligibleVote
{
    public static int Vote(int age)
    {
        if(age>18||age==18)
        {
            System.out.println("eligible to vote");
            return age;
        }
        else
        {
            System.out.print("not eligible to vote");
            return age;
        }
    }
    public static void main(String args[])
    {
        Scanner sc =new Scanner(System.in);
        int age = sc.nextInt();
        System.out.print(Vote(age));
    }
}