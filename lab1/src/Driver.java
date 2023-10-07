// based on driver in example 13-0

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

class Driver {
    public static void main(String[] args) throws FileNotFoundException {

        // reading in file with numbers data
        Scanner in = new Scanner(new File("C:/Users/benf7/IdeaProjects/lab1/src/dnums.txt"));

        // initializing linked list with data type double
        LinkedList<Double> list = new LinkedList<Double>();

        // reading in numbers from file in linked list
        while(in.hasNextDouble()){
           list.insert(in.nextDouble());
        }

        // print data type of linked list elements
        list.printClass();


        // checks if list is empty, goes to head and deletes the current head
        while (list.isEmpty() != true) {
            // prints the list until at the end of the list then breaks.
            while (list.atEndOfList() != null) {
                list.printList();
                if (list.nextData() == false) {
                    break;
                }
            }
            list.GoToHead();
            list.deleteHead();
            System.out.println("List is: ");
        }
    }
}
