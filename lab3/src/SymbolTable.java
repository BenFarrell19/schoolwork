// Ben Farrell
// CSCI 232 section 2, Professor Cummings
// Lab 3

import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

// creating Symbol Table class and making generic with key being comparable for use in TreeMap
public class SymbolTable <Key extends Comparable<Key>, Value> {

    // initiating Treemap data structure
    TreeMap<Key, Value> tree = new TreeMap<>();

    //method to insert data into tree map as key value pairs
    public void put(Key key, Value value) {
        tree.put(key, value);
    }

    // method to return the value of a key from the symbol table/tree map
    public Value get(Key key) {
       return tree.get(key);
    }

    // method to delete a key from the symbol table/tree map
    public void delete(Key key) {
        tree.remove(key);
    }

    // tree map keys are sorted least to greatest by default, so last key of the tree map is the max key of the symbol table
    public Key max() {
        return tree.lastKey();
    }

    // same as above, first key is the minimum
    public Key min() {
       return tree.firstKey();
    }

    // checking if a key exists in the symbol table with tree map .containsKey method
    public boolean exists(Key key) {
        return tree.containsKey(key);
    }


    //https://stackoverflow.com/questions/46898/how-do-i-efficiently-iterate-over-each-entry-in-a-java-map
    // method used to iterate over and return each of the key value pairs of the tree map
    // returns as "Set<Map.Entry<Key, Value>>" because that is the default for Treemap's .entrySet() method and allows the use of .getValue and .getKey
    // while iterating over the key, value pairs in main
    public Set<Map.Entry<Key, Value>> entrySet() {
        return tree.entrySet();
    }

}

//
class driver {
    public static void main(String[] args) throws FileNotFoundException {

        // reading in file with numbers data
        Scanner in = new Scanner(new File("C:/Users/benf7/IdeaProjects/lab3/src/lab3in.txt"));

        // creating symbol table "st" with Integer data type
        SymbolTable<Integer, Integer> st = new SymbolTable<>();

        // reading file data into symbol table as integers, treemap overrides duplicate keys automatically
        while(in.hasNextInt()){
            st.put(in.nextInt(), in.nextInt());
        }

        // checking if key 5 exists then printing its value and then deleting it
        if(st.exists(5)) {
            System.out.println("Key 5 was found, value is: " + st.get(5));
            st.delete(5);
        }

        //https://stackoverflow.com/questions/46898/how-do-i-efficiently-iterate-over-each-entry-in-a-java-map
        // var entry represents a single key value pair of the treemap,
        // and can be used to get the key or value by itself with .getKey and .getValue as seen in the println
        // st.entrySet() returns the key value pairs in a set format, meaning you can iterate over/access both keys and values with one for loop
        for (var entry : st.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }

        // printing out min and max key value pairs
        System.out.println("Min Key: "+st.min() + ", Value: " + st.get(st.min()));
        System.out.println("Max Key: "+st.max() + ", Value: " + st.get(st.max()));
    }
}
