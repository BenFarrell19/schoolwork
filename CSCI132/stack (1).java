import java.util.Scanner;

class Stack{  
    static char[] stack_array = new char[20];
    static int size = 0;

    public static boolean isEmpty() {
        if (size == 0) {
            return true;
        } else {
            return false;
        }
    }

    public static void push(char c) {
        if (size >= 0) {
            stack_array[size] = c;
        }
        size = size + 1;
    }

    public static void pop() {
        if (!isEmpty()) {
            for (int i = 0; i < size-1; i++) {
                stack_array[i] = stack_array[i+1];
            }
            size = size - 1;
        } else {
            size = size - 1;
        }  
    }

    public static void makeEmpty() {
        size = 0;
    }

    public static int runMethod(String str) {
        size = 0;
        for (int i = 0; i < str.length(); i++) {
            if ('0' == str.charAt(i)) {
                push(str.charAt(i));
            } else {
                pop();
            }
        }
        return size;
    }
    public static void main(String args[]){  
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("Give a string");
            String user_input = scanner.nextLine();

            if (user_input.equals("-1")) {
                break;
            }
            int result = runMethod(user_input);

            if (result == 0) {
                System.out.println("Accept String " + user_input);
            } else {
                System.out.println("Reject String: " + user_input + " " + result);
            }

        }
        
        scanner.close();
    }  
} 