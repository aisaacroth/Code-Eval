import java.io.File;

public class FizzBuzzTester {

    public static void main(String[] args) {
	    if (args.length != 1) {
	        print_arguments();
	    }

        String filename = args[0];
        File sourceFile = new File(filename);
    }

    public static void print_arguments() {
	    System.out.println("java FizzBuzzTester <filename>");
    }
}
