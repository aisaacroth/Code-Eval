import java.util.ArrayList;
import java.util.List;

public class BitChecker {

    public static void main(String[] args) {
        if (args.length != 3) {
            printArguments();
        } else {
            int number = Integer.parseInt(args[0]);
            int firstPosition = Integer.parseInt(args[1]);
            int secondPosition = Integer.parseInt(args[2]);
            BitChecker checker = new BitChecker();

            List<Integer> binaryList = checker.decimalToBinary(number);
            String answer = checker.matchCheck(checker.checkBits(binaryList, 
                        firstPosition, secondPosition));
            System.out.println(answer);
        }
    }

    private static void printArguments() {
        System.out.println("java BitChecker <number> <bit 1> <bit 2>\n");
        System.exit(1);
    }

    private List<Integer> decimalToBinary(int number) {
        List<Integer> binaryList = new ArrayList<Integer>();

        int remainder = number % 2;
        int value = number;

        while (value > 0) {
            binaryList.add(0, remainder);
            value /= 2;
            remainder = value % 2;
        }

        return binaryList;
    }

    private boolean checkBits(List<Integer> numberList, int firstPosition, 
            int secondPosition) {
        int end = numberList.size();
        return numberList.get(end - firstPosition) == numberList.get(end - 
                secondPosition);
    }

    private String matchCheck(boolean check) {
        return check ? "true" : "false";
    }
}

