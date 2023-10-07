// taken from Algorithms, 4th edition by Sedgewick and Wayne
// based on example 13-0 some methods and Linkedlist class were reused.

// Ben Farrell
// CSCI 232 section 2, Professor Cummings
// Lab 1


// class to create linked list and nodes
public class LinkedList<E>{

    // creating private nodes, E hold the node's data and next leads to the next node in list
    private Node<E> head;
    private Node<E> cur;
    private static class Node<E> {
        private E E;
        private Node<E> next;

        public Node(E E) {
            this.E = E;
            this.next = null;
        }
    }

    // initialize linked list
    public LinkedList() {
        head = null;
        cur = head;
    }

    // method to delete the head of the linked list, checks if exists and then changes head pointer to next node.
    public E deleteHead() {
        if(head != null) {
            head = head.next;
        }
        return null;
    }

    // method to check if the pointer is at the last node of the list. Checks if pointer is pointing to a node, if not returns null, meaning end of list. If not just returns the node
    public E atEndOfList() {
        if (cur == null) {
            return null;
        } else {
            return cur.E;
        }
    }

    // method used to go to the head of the linked list. Given the scope of the problem the pointer should not be moving past what we want to be the head node,
    // meaning simply setting the current(cur) node to head works.
    public E GoToHead() {
        cur = head;
        return null;
    }

    //prints the data value of the current node
    public void printList() {
        System.out.println(cur.E);
    }


    // prints the class type of the data value of the current node
    public void printClass() {
        if(cur != null) {
            System.out.println("The data type for the data in this linked list is " + cur.E.getClass());
        }
    }


    // basically a boolean version of atEndOfList
    public boolean nextData() {
        if (cur != null) {
            cur = cur.next;
        }
        return (cur != null); // false means no next data to move to
                              // in other words, at end of list
    }

    // checks if current node is empty
    public boolean isEmpty() {
        return cur == null;
    }

    // inserts new node to list and moves original head down the list
    public void insert(E E) {
        Node<E> oldhead = head;
        head = new Node<E>(E);
        head.next = oldhead;
        cur = head;
    }

    
}
