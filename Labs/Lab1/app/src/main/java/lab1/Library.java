package lab1;

public class Library {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        System.out.println(new Library().getGreeting());
        System.out.println(add(1, 2));
    }

    public static int add(int a, int b) {
        return a + b;
    }
}
