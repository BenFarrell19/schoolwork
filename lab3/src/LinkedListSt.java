import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class LinkedListSt<Key extends Comparable<Key>, Value> {

    TreeMap<Key, Value> tree = new TreeMap<>();

    public void put(Key key, Value value) {
        tree.put(key, value);
    }

    public Value get(Key key) {
        return tree.get(key);
    }

    public void delete(Key key) {
        tree.remove(key);
    }

    public Key max() {
        return tree.lastKey();
    }

    public Key min() {
        return tree.firstKey();
    }

    public boolean exists(Key key) {
        return tree.containsKey(key);
    }


    //https://stackoverflow.com/questions/46898/how-do-i-efficiently-iterate-over-each-entry-in-a-java-map
    public Set<Map.Entry<Key, Value>> entrySet() {
        return tree.entrySet();
    }

}

class dv {
    public static void main(String[] args) throws FileNotFoundException {

        // reading in file with numbers data
        Scanner in = new Scanner(new File("C:/Users/benf7/IdeaProjects/lab3/src/lab3in.txt"));

        SymbolTable<Integer, Integer> st = new SymbolTable<>();

        while(in.hasNextInt()){
            st.put(in.nextInt(), in.nextInt());
        }

        if(st.exists(5)) {
            System.out.println("Key 5 was found, value is: " + st.get(5));
            st.delete(5);
        }

        //https://stackoverflow.com/questions/46898/how-do-i-efficiently-iterate-over-each-entry-in-a-java-map
        for (var entry : st.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }

        System.out.println("Min Key: "+st.min() + ", Value: " + st.get(st.min()));
        System.out.println("Max Key: "+st.max() + ", Value: " + st.get(st.max()));
    }
}
