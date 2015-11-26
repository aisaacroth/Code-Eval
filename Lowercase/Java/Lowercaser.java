import java.io.*;
import java.util.*;

public class Lowercaser {

    public static void main(String[] args) {
        if (args.length != 1) {
            printArguments();
        } 
        try {
            Lowercaser lowercaser = new Lowercaser();
            List<String> lines = lowercaser.retrieveLinesFromFile(args[0]);
            List<String> lowercaseStrings = lowercaser.convertToLowercase(lines);
            printList(lowercaseStrings);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void printArguments() {
        System.out.println("java Lowercaser <file_path>");
        System.exit(1);
    }

    private List<String> retrieveLinesFromFile(String filename) 
        throws IOException {
        File readFile = new File(filename);
        BufferedReader input = new BufferedReader(new FileReader(readFile));
        List<String> lines = new ArrayList<String>();
        String line = null;
        while ((line = input.readLine()) != null) {
            lines.add(line);
        }
        input.close();
        return lines;
    }

    private List<String> convertToLowercase(List<String> strings) {
        List<String> lowercaseList = new ArrayList<String>();
        for (String string : strings) {
            lowercaseList.add(string.toLowerCase());
        }
        return lowercaseList;
    }

    private static void printList(List<String> stringList) {
        for (String string : stringList) {
            System.out.println(string);
        }
    }
}
