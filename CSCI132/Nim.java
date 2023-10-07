/* Ben Farrell
   2/17/2022
   cs132
 */

package com.company;

import java.util.Random;
import java.util.Scanner;
import java.lang.Math;

public class Nim {


// create stack of marble or random size
    public int genStack() {
        Random rand = new Random();

        return rand.nextInt(10, 101);
    }

    // function for who goes first at random
    public int first() {

        // 0 = human, 1 = computer
        Random rand = new Random();

        return rand.nextInt(2);
    }

    // random determination of computer smart or stupid
    public int ss() {

        // 0 = stupid, 1 = smart
        Random rand = new Random();

        return rand.nextInt(2);
    }

    // stupid computer function just chooses random legal number
    public int computerTurn0(int n) {
        Random rand = new Random();

        return rand.nextInt(n / 2) + 1;
    }

    // smart computer function loops through all possible number of marbles to take and finds best mathematical choice
    public double computerTurn1(int n) {
        double c = 0;
        for(int t = 1; t <= n/2; t++) {
            for (double i = 1; i < 7; i++) {
                if (n-t == Math.pow(2, i) - 1) {
                    if (t > c) {
                        c = t;
                    }
                }
            }
        }
        c = (int) c;
        // random legal choice if no good mathematical choice available
        if (c == 0) {
            Random rand = new Random();
            c = rand.nextInt(n/2) + 1;
        }
        System.out.println("Computer takes " + (int) c + " marbles");
        return c;
    }

    // user turn reads in single number
    public int humanTurn() {
        Scanner scan = new Scanner(System.in);
        System.out.println("How many marbles would you like to take? ");

        int n = scan.nextInt();

        return n;
    }


    public static void main(String[] args) {
        // create instance of game
        Nim game = new Nim();

       int nMarbs = game.genStack();
       System.out.println("The starting amount of marbles will be: " + nMarbs);

        int ss = game.ss();

        System.out.println("Stupid(0) or smart(1): " + ss);
        int starter = game.first();

        if (starter == 1) {
            System.out.println("Computer goes first");
        } else {
            System.out.println("Human goes first");
        }

        int c;
        c = starter;
        double tMarbs = 0;

       while(nMarbs > 1) {
            // check whose turn it is
           if(c % 2 == 0) {
               System.out.println("There are " + nMarbs + " marbles in the stack.");
               System.out.println("You can take between 1 and " + nMarbs / 2 + " marbles");
               tMarbs = game.humanTurn();
               System.out.println("There are " + ((int) (nMarbs - tMarbs)) + " left.");
           } else {
               if(ss == 0) {
                   tMarbs = game.computerTurn0(nMarbs);
                   System.out.println("Computer takes " + (int) tMarbs + " marbles");
               } else {
                  tMarbs = (int) game.computerTurn1(nMarbs);
               }
           }
           c++;
            nMarbs = (int) (nMarbs - tMarbs);

       }
       // winning end statements
    if(nMarbs == 1) {
        if (c % 2 == 0) {
        System.out.println("Computer wins!");
            } else {
            System.out.println("Human wins!");
            }
        }
    }
}






