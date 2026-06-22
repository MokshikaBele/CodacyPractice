import java.util.Scanner;

public class LibraryManagement {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String book = null;

        int unusedVariable = 100;

        System.out.println("Enter book name:");
        String input = scanner.nextLine();

        // Incorrect String comparison
        if (input == "Java") {
            System.out.println("Java Book Selected");
        }

        // Possible NullPointerException
        try {
            System.out.println(book.length());
        } catch (Exception e) {
            // Empty catch block
        }

        System.out.println("Program Finished");
    }
}