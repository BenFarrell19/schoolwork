// based on driver in example 13-0

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

class StringDriver {
    public static void main(String[] args) throws FileNotFoundException {

        // reading in file with strings data
        Scanner in = new Scanner(new File("C:/Users/benf7/IdeaProjects/lab1/src/strings.txt"));

        // internalizing linked list for stings
        LinkedList<String> list = new LinkedList<String>();

        // reading in file data line by line, I changed strings.txt to be line by line instead of all on one line
        while(in.hasNext()){
            list.insert(in.nextLine());
        }

        // prints class type of linked list elements
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
            System.out.println("List is ");
        }
    }
}
