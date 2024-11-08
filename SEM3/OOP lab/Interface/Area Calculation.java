// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.io.*;
import java.util.Scanner;

interface Shape {
    double calculateArea();
}

class Circle implements Shape {
    double radius;
    public Circle(double radius) {
        this.radius = radius;
    }
    @Override
    public double calculateArea() {
        return 3.14 * radius * radius;
    }
}

class Triangle implements Shape {
    double base;
    double height;
    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }
    @Override
    public double calculateArea() {
        return 0.5 * base * height;
    }
}

class Rectangle implements Shape {
    double length;
    double height;
    public Rectangle(double length, double height) {
        this.length = length;
        this.height = height;
    }
    @Override
    public double calculateArea() {
        return length * height;
    }
}

class Rhombus implements Shape {
    double base;
    double height;
    public Rhombus(double base, double height) {
        this.base = base;
        this.height = height;
    }
    @Override
    public double calculateArea() {
        return base * height;
    }
}

public class HelloWorld{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Enter radius of circle: ");
        int circle_rad = scan.nextInt();
        System.out.print("Enter base of triangle: ");
        int tri_base = scan.nextInt();
        System.out.print("Enter height of triangle: ");
        int tri_height = scan.nextInt();
        System.out.print("Enter length of rectangle: ");
        int rect_length = scan.nextInt();
        System.out.print("Enter height of rectangle: ");
        int rect_height = scan.nextInt();
        System.out.print("Enter the base of rhombus: ");
        int rhombus_base = scan.nextInt();
        System.out.print("Enter height of rhombus: ");
        int rhombus_height = scan.nextInt();
        
        System.out.println("\nOUTPUTS====>");
        Shape circle = new Circle(circle_rad);
        Shape triangle = new Triangle(tri_base, tri_height);
        Shape rectangle = new Rectangle(rect_length, rect_height);
        Shape rhombus = new Rhombus(rect_length, rect_height);
        
        System.out.println("Area of circle is: "+circle.calculateArea());
        System.out.println("Area of triangle is: "+triangle.calculateArea());
        System.out.println("Area of rectangle is: "+rectangle.calculateArea());
        System.out.println("Area of rhombus is: "+rhombus.calculateArea());
    }
}
