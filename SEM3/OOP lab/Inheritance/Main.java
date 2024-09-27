package Inheritance;
import java.io.*;
class Main {
    int a = 1;
    int b = 20;
    String name = "Abbilaash";

    public static void main(String[] args)throws IOException {
        InputStreamReader read = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(read);
        System.out.print("\nEnter a number : ");
        int x = Integer.parseInt(in.readLine());
        System.out.println("The number is " + x);
        B obj = new B();
        System.out.println("a+b is " + (obj.a + obj.b));
        obj.printSum();
    }
}

class B extends Main {
    int c = 30;

    void printSum() {
        System.out.println("a+b+c is " + (a + b + c));
        System.out.println("Hello " + name);
    }
}