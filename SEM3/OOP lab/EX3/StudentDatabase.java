import java.util.ArrayList;
import java.util.Scanner;

class Student {
    private int rollNumber;
    private String name;
    private int age;

    public Student(int rollNumber, String name, int age) {
        this.rollNumber = rollNumber;
        this.name = name;
        this.age = age;
    }

    public int getRollNumber() {
        return rollNumber;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Roll Number: " + rollNumber + ", Name: " + name + ", Age: " + age;
    }
}

public class StudentDatabase {
    private static ArrayList<Student> students = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n--- Student Database Menu ---");
            System.out.println("1. Add Student");
            System.out.println("2. Find Student by Roll Number");
            System.out.println("3. Remove Student by Roll Number");
            System.out.println("4. Display All Students");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    findStudent();
                    break;
                case 3:
                    removeStudent();
                    break;
                case 4:
                    displayAllStudents();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addStudent() {
        System.out.print("Enter Roll Number: ");
        int rollNumber = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        System.out.print("Enter Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter Age: ");
        int age = scanner.nextInt();

        students.add(new Student(rollNumber, name, age));
        System.out.println("Student added successfully.");
    }

    private static void findStudent() {
        System.out.print("Enter Roll Number to find: ");
        int rollNumber = scanner.nextInt();
        for (Student student : students) {
            if (student.getRollNumber() == rollNumber) {
                System.out.println("Student found: " + student);
                return;
            }
        }
        System.out.println("Student with Roll Number " + rollNumber + " not found.");
    }

    private static void removeStudent() {
        System.out.print("Enter Roll Number to remove: ");
        int rollNumber = scanner.nextInt();
        for (Student student : students) {
            if (student.getRollNumber() == rollNumber) {
                students.remove(student);
                System.out.println("Student removed successfully.");
                return;
            }
        }
        System.out.println("Student with Roll Number " + rollNumber + " not found.");
    }

    private static void displayAllStudents() {
        if (students.isEmpty()) {
            System.out.println("No students in the database.");
        } else {
            System.out.println("--- All Students ---");
            for (Student student : students) {
                System.out.println(student);
            }
        }
    }
}
