package com.company;

public class LinkedList {


    private Node head;
    private Node dlList;
    private int count;
    LinkedList() {
        count = 0;
    }

    public void addNode(int value) {
        Node newNode = new Node(value);

        if(count == 0) {
            dlList = newNode;
            dlList.next = dlList;
            dlList.prev = dlList;
            head = dlList;


        } else {
            newNode.prev = dlList.prev;
            newNode.next = dlList;
            dlList.prev.next = newNode;
            dlList.prev = newNode;

            head = dlList;
        }
        count++;
    }



    public void insert(int position, int value) {
        if(position > count) {
            System.out.println("Position out of index");
            return;
        }
        Node newNode = new Node(value);
        Node current = head;
        int i = 0;
        while (i < position) {
            i++;
            current = current.next;
        }
        newNode.prev = current.prev;
        newNode.next = current;
        current.prev.next = newNode;
        current.prev = newNode;
        count++;

    }


    public void delete(int position) {
        if(position > count) {
            System.out.println("Position out of index");
            return;
        }
        if (position == 0) {
            Node current = head;
            int i = 0;
            while (i < position) {
                i++;
                current = current.next;
            }
            current.prev.next = current.next;
            current.next.prev = current.prev;
            count--;
            head = current.next;
        } else {
            Node current = head;
            int i = 1;
            while (i < position) {
                i++;
                current = current.next;
            }
            current.prev.next = current.next;
            current.next.prev = current.prev;
            count--;
        }
    }
    private class Node {
        Node next;
        Node prev;
        int value;


        Node(int value) {
            this.value = value;
        }
    }



    public void print() {
        if(count == 0) {
            System.out.println("Empty List");
            return;
        }
        Node current = head;
        do {
            System.out.println(current.value);
            current = current.next;

        } while (current != head);
    }

    public int index(int value) {
        Node current = head;
        int i = 0;
        while (current.value != value) {
            i++;
            current = current.next;
        }
        return i;
    }



    public int traverse_k(int start, int num) {
        // start has to be index of number not number
        Node current = head;
        int i = 0;
        while (i < start) {
            i++;
            current = current.next;
        }
        i = 1;
        while (i < num) {
            i++;
            current = current.next;

        }
        return current.value;

    }

    public int traverse_m(int start, int num) {
        Node current = head;
        int i = 0;
        while (i < start) {
            i++;
            current = current.next;
        }
        i = 1;
        while (i < num+1) {
            i++;
            current = current.prev;
        }
        return current.value;

    }




    public static void main(String[] args) throws Exception
    {



        LinkedList list = new LinkedList();
        for(int i = 1; i < 11; i++) {
            list.addNode(i);
        }
        //list.print();

        int k = 4;
        int m = 3;
        int ks = 1;
        int ms = 10;
        // first time only
        // first traverse one more than k value to be get number one clockwise of number being deleted
        // traverse one more than m value to be get number one counterclockwise of number being deleted
        // delete number to be deleted
        // get index of number gotten in step 1 and 2
        // use that index for start(after modifying for index) in traverse functions
        // repeat
        ks = list.traverse_k(0, k+1);
        ms = list.traverse_m(9, m);

        int dk = list.traverse_k(0, k);
        int mk = list.traverse_m(9, m);
        list.delete(dk);
        list.delete(mk);
        list.print();
        int ik = list.index(ks);
        int im = list.index(ms);
        ks = list.traverse_k(ik, k+1);
        ms = list.traverse_m(im, m);
        dk = list.traverse_k(ks, k-1);
        mk = list.traverse_m(ms, m);
        System.out.println("ik " + ik);
        System.out.println("im " + im);
        System.out.println("dk " + dk);
        System.out.println("mk " + mk);
        list.delete(dk);
        list.delete(mk);
        //list.print();












        //list.print();


        // System.out.println(list.traverse_C(3, 4)); // 7
        // System.out.println(list.traverse_CC(3, 4)); // 9






    }
}
