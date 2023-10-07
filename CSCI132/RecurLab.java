// Ben Farrell Inlab7 3/29/22

package com.company;

public class RecurLab {
    public static int largestArrayItem(int [] numbers)
    {
        return largestArrayItemRecursive(numbers, 0);
    }

    private static int largestArrayItemRecursive(int [] numbers, int index) {
        if (index == numbers.length) {
            return 0;
        } else {
            return max(numbers[index], largestArrayItemRecursive(numbers, index + 1));
        }
    }
    private static int max(int a, int b)
    {
        return Math.max(a, b);
    }

    public static void main(String [] args)
    {
        int [] numbers1 = {8, 6, 10, 4, 2};
        int [] numbers2 = {9, 1, 7, 3, 5, 6};
        int [] numbers3 = {2, 4, 6, 7, 5, 3, 1, 8};

        System.out.println("In Lab: Recursion");
        System.out.println("-----------------\n");

        System.out.println("\nLargest Array Item Method ... \n");

        System.out.println("The largest array item is " + RecurLab.largestArrayItem(numbers1));
        System.out.println("The largest array item is " + RecurLab.largestArrayItem(numbers2));
        System.out.println("The largest array item is " + RecurLab.largestArrayItem(numbers3));
    }
}
