/* Ben Farrell
   3/3/2022
   cs132
 */

package com.company;

import java.util.*;


public class yahtzee {

    // dice roll function outputs random number between 1 and 6
    public static int diceRoll() {
        Random rand = new Random();

        return rand.nextInt(1, 7);
    }

    // checks for yahtzee by seeing if there are 5 of any number 1 - 6
    public static boolean checkYahtzee(ArrayList<Integer> lst) {
        int i = 0;
        while(i <= 6 && !(Collections.frequency(lst, i) == 5)) {
            i++;
            if(Collections.frequency(lst, i) == 5) {
                return true;
            }
        }
        return false;
    }

        // checks for four of a kind with while loop that ends when the frequency of a number in the arraylist is exactly 4 and between 1 and 6
    public static boolean checkFourOfAKind(ArrayList<Integer> lst) {
        int i = 0;
        while(i <= 6 && !(Collections.frequency(lst, i) == 4)) {
            i++;
            if(Collections.frequency(lst, i) == 4) {
                return true;
            }
        }
        return false;

    }

    // checks for full house by first check if there are 3 of the same number then checking if there are 2 of the same number but cant duplicate as frequency must equal exactly 2 or exactly 3
    public static boolean checkFullHouse(ArrayList<Integer> lst) {
        int t1 = 0;
        int t2 = 0;
        for(int i = 0; i < 6; i++) {
            if(Collections.frequency(lst, i) == 3) {
                t1 = 1;
            }
            if(Collections.frequency(lst, i) == 2) {
                t2 = 1;
            }
        }
        return t1 == 1 && t2 == 1;
    }

    // checks for straight by seeing if the index number + 1 equals the next number or index + 1 number, after sorting the list
    public static boolean checkStraight(ArrayList<Integer> lst) {
        Collections.sort(lst);
        int c = 2;
        for(int i = 0; i < 4 ; i++) {
            if(lst.get(i) + 1 == lst.get(i+1)) {
                c = 1;
            } else {
                c = 0;
                break;
            }
        }
        return c == 1;
    }

    // checks for three of kind same way as four of kind just with ==3
    public static boolean checkThreeOfAKind(ArrayList<Integer> lst) {
        int i = 0;
        while(i <= 6 && !(Collections.frequency(lst, i) == 3)) {
            i++;
            if(Collections.frequency(lst, i) == 3) {
                return true;
            }
        }
        return false;
    }




    public static void main(String[] args) {
        // initializing counts of each roll
        int Y = 0;
        int fk = 0;
        int fh = 0;
        int S = 0;
        int tk = 0;
        int L = 0;
        int n;
        // 5000 rolls creates new list which will be the 6 die and rolls and adds to list
        for (n = 0; n < 5000; n++) {
            ArrayList<Integer> lst = new ArrayList<>();
            for (int i = 0; i < 5; i++) {
                lst.add(diceRoll());
            }
            // checking for rolls
            if(checkYahtzee(lst)){
                Y++;
                continue; }
            if(checkFourOfAKind(lst)){
                fk++;
                continue;}
            if(checkFullHouse(lst)){
                fh++;
                continue;}
            if(checkStraight(lst)){
                S++;
                continue;}
            if(checkThreeOfAKind(lst)){
                tk++;
            } else {
                L++;
            }
        }
        // printing out rolls
        System.out.println("Number of Rolls: " + n );
        System.out.println("----------------------");
        System.out.println("Number of Yahtzees: " + Y);
        double a = Y;
        double b = n;
        System.out.println("Yahtzee Percent: " + String.format("%.2f", a/b * 100) + "%\n");
        System.out.println("Number of Full Houses: " + fh);
        a = fh;
        System.out.println("Full House Percent: "+ String.format("%.2f", a/b * 100) + "%\n");
        System.out.println("Number of Large Straights: " + S);
        a = S;
        System.out.println("Large Straight Percent: "+ String.format("%.2f", a/b * 100) + "%\n");
        System.out.println("Number of Four of a Kind: " + fk);
        a = fk;
        System.out.println("Four of a Kind Percent: "+ String.format("%.2f", a/b * 100) + "%\n");
        System.out.println("Three of a Kind : " + tk);
        a = tk;
        System.out.println("Three of a Kind percentage : "+ String.format("%.2f", a/b * 100) + "%\n");
        System.out.println("Number of Losers: " + L);
        a = L;
        System.out.println("Losers Percentage: " + String.format("%.2f", a/b * 100) + "%\n");

    }
}