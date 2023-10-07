import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


// class to implement binary search tree with symbol table
public class BST <Key extends Comparable<Key>, Value> {

    // Node object as root of bst
    private Node root;

    private class Node {
        // key and value pair fields, node links to subtrees
        private Key key;
        private Value val;
        private Node left, right;
        // int n serves to number of nodes in subtree
        private int n;

        // node constructor
        public Node(Key key, Value val, int n) {
            this.key = key; this.val = val; this.n = n;
        }
    }
    // get size of bst
    public int size() {
        return size(root);
    }

    // get size of subtree of a certain root (node x)
    private int size(Node x) {
        if(x==null) return 0;
        else return x.n;
    }

    // get value from key
    public Value get(Key key) {
        return get(root, key);
    }

    // get value from key by comparing key to the node's key, if less than it will traverse the left subtree, and right subtree if greater than zero.
    private Value get(Node x, Key key) {
        if(x==null) return null;
        int cmp = key.compareTo(x.key);
        if (cmp < 0) return get(x.left, key);
        else if (cmp > 0 ) return get(x.right, key);
        else return x.val;
    }

    // put key value pair in bst
    public void put(Key key, Value val) {
        root = put(root, key, val);
    }

    // same method as with get() but inserts
    private Node put(Node x,  Key key, Value val) {
        if (x==null) return new Node(key, val, 1);
        int cmp = key.compareTo(x.key);
        if (cmp < 0)  x.left = put(x.left, key, val);
        else if (cmp > 0) x.right = put(x.right, key, val);
        else x.val = val;
        x.n = size(x.left) + size(x.right) + 1;
        return x;
    }
}

class driver {
    public static void main(String[] args) throws FileNotFoundException {

        // reading in file with numbers data
        Scanner in = new Scanner(new File("C:/Users/benf7/IdeaProjects/lab4/src/lab4in.txt"));

        // creating symbol table "bst" with Integer data type
        BST<Integer, Integer> bst = new BST<>();


        // reading file data into symbol table as integers
        int i = 1;
        while(in.hasNext()){
            System.out.println(i);
            bst.put(i, i*5);
            i++;
        }

    }
}

