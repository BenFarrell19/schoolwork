// Ben Farrell Inlab5 3/1/22


package com.company;

import java.util.Scanner;
    public class Inlab5 {

        public static String sentence() {
            Scanner scan = new Scanner(System.in);
            System.out.println("Give me your String: ");

            String n = scan.nextLine();

            return n;
        }


        public static int menuScanner() {
            Scanner scan = new Scanner(System.in);
            System.out.println("Press 1 to count the occurrence of a particular letter.\n");
            System.out.println("Press 2 to count the total words in your input sentence.\n");
            System.out.println("Press 3 to change your input sentence.\n");
            System.out.println("Press 4 to exit.\n");
            System.out.println("What do you want to do?\n");
            int n = scan.nextInt();

            return n;
        }

        public static void one(String s) {
            String sns = s.replaceAll("\\s", "");;
            Scanner scan = new Scanner(System.in);
            System.out.println("What letter do you want to count?\n");
            String n = scan.nextLine();

            int occ = sns.length() - sns.replace(n, "").length();
            System.out.println("The letter " + n + " was found " + occ + " times.\n");
        }

        public static void two(String s) {
            String sns = s.replaceAll("\\s", " ");
            String n2 = s.replaceAll("\\s", "");

            int z = sns.length() - n2.length() + 1;
            System.out.println("There are " + z + " words in the input");
        }

        public static void three() {
            Scanner scan = new Scanner(System.in);
            System.out.println("What is your new input sentence?\n");
            String n = scan.nextLine();
            System.out.println("Your input sentence has been changed to " +  "\"" + n + "\"\n\n");
        }


        public static void main(String[] args) {

           String s = sentence();

           int n = menuScanner();

           if(n == 1) {
                one(s);
           } else if (n == 2) {
                two(s);
           } else if(n==3) {
                three();
           } else {
               System.out.println("Goodbye");
               System.exit(0);
           }
           while (n != 4) {
               n = menuScanner();
               if(n == 1) {
                   one(s);
               } else if (n == 2) {
                   two(s);
               } else if(n==3) {
                    three();
               }
           }
            System.out.println("Goodbye");
        }

    }
