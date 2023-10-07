// Ben Farrell
// CSCI 232 section 2, Professor Cummings
// Lab 2

import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;


// class to find two numbers closest to each other in an array
public class ClosestNums {
    //creating private data members
    private static Double d = 100.0;
    private static Double num1 = 0.0;
    private static Double num2 = 0.0;

    // initializing array
    private static ArrayList<Double> list = new ArrayList<>();



    public static void main(String[] args) throws FileNotFoundException {

        // reading in file of numbers to be compared
        Scanner in = new Scanner(new File("C:/Users/benf7/IdeaProjects/ex14-5/src/lab2in.txt"));

        // reading in by line
        while (in.hasNextDouble()) {
            list.add(in.nextDouble());
        }

        //this function works by first sorting the list in ascending order, it then loops through the list and sees if the current index
        // minus the next index is less than the last comparison, if so that difference becomes the new difference value, untill every comparison has be made

        Collections.sort(list);

        for(int i = 0; i < list.size()-1; i++) {
            if(list.get(i+1) - list.get(i) < d) {
                d = list.get(i+1) - list.get(i);
                num1 = list.get(i);
                num2 = list.get(i+1);
            }
        }
        // collections.sort has the time complexity of O(n*log(n)) // https://stackoverflow.com/questions/4254122/what-is-the-time-complexity-of-java-util-collections-sort-method
        //this loop has the time complexity of O(n) given that the constants are dropped and we loop through the entire list only once.
        // together the entire function has a time complextiy of O(n*log(n))

        // printing out the two closest numbers and the difference between them to six decimal points
        System.out.println("The numbers " + num1 + " and " + num2 + " are the clostest pair with a difference of " + String.format("%.6f", d));
    }
}
