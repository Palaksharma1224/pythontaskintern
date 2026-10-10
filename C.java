class A
{
    void look()
    {
        System.out.println("Hello");
    }
}

class B extends A
{
    void paint()
    {
        System.out.println("BCA");
    }
}

public class C
{
    public static void main(String []args)
    {
        B B1 = new B();
        B1.look();
        B1.paint();    
    }
}