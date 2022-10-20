public class ArrayMax {
    public static void main(String[] args) {
        int[] intArray = {24, 2, 0, 34, 12, 110, 2};

        int maxNum = intArray[0];

        for (int j : intArray) {
            if (j > maxNum)
                maxNum = j;
        }

        System.out.println("Maximum number = " + maxNum);
    }
}
