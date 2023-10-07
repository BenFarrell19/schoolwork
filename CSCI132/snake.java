package com.company;

import java.util.List;
import java.util.Random;
import java.util.*;


public class snake {

    public static List<Integer> createGame() {
        Random rand = new Random();
        int apl_col = rand.nextInt(0, 40 / 2) * 2;
        ;
        String s = ". . . . . . . . . . . . . . . . . . . .";
        StringBuilder string = new StringBuilder(s);
        string.setCharAt(apl_col, 'X');
        int apl_row = rand.nextInt(0, 20);
        int sn_row = 10;
        String sn = ". . . . . . . . . . . . . . . . . . . .";
        StringBuilder snake = new StringBuilder(sn);
        snake.setCharAt(20, 'S');
        while (apl_row == sn_row) {
            apl_row = rand.nextInt(0, 20);
        }
        for (int i = 0; i <= 20; i++) {
            if (i == apl_row) {
                System.out.println(string);
            }
            if (i == sn_row) {
                System.out.println(snake);
            } else {
                System.out.println(". . . . . . . . . . . . . . . . . . . .");
            }
        }
        int sn_col = 20;

        return Arrays.asList(apl_col, apl_row, sn_row, sn_col);
    }

    public static List<Integer> move(int apl_col, int apl_row, int sn_row, int sn_col) {
        Scanner myObj = new Scanner(System.in);
        System.out.println("Press key: ");
        String key = myObj.nextLine();
        System.out.println(key);
        if (Objects.equals(key, "w")) {
            sn_row -= 1;
            return Arrays.asList(apl_col, apl_row, sn_row, sn_col);
        } else if (Objects.equals(key, "s")) {
            sn_row += 1;
            return Arrays.asList(apl_col, apl_row, sn_row, sn_col);
        } else if (Objects.equals(key, "a")) {
            sn_col -= 2;
            return Arrays.asList(apl_col, apl_row, sn_row, sn_col);
        } else if (Objects.equals(key, "d")) {
            sn_col += 2;
            return Arrays.asList(apl_col, apl_row, sn_row, sn_col);

        } else {
            return null;
        }
    }

    public static List<Integer> update(int apl_col, int apl_row, int sn_row, int sn_col) {
        Random rand = new Random();
        String s = ". . . . . . . . . . . . . . . . . . . .";
        StringBuilder string = new StringBuilder(s);
        string.setCharAt(apl_col, 'X');
        String sn = ". . . . . . . . . . . . . . . . . . . .";
        StringBuilder snake = new StringBuilder(sn);
        snake.setCharAt(sn_col, 'S');
        while (apl_row == sn_row) {
            apl_row = rand.nextInt(0, 20);
        }
        for (int i = 0; i <= 20; i++) {
            if (i == apl_row) {
                System.out.println(string);
            }
            if (i == sn_row) {
                System.out.println(snake);
            } else {
                System.out.println(". . . . . . . . . . . . . . . . . . . .");
            }
        }
        return Arrays.asList(apl_col, apl_row, sn_row, sn_col);
    }




    public static void main(String[] args) {

        List<Integer> arr = createGame();
        List<Integer> game = move(arr.get(0), arr.get(1),arr.get(2),arr.get(3));
        for(int i = 0; i < 20; i++) {
            System.out.println(arr.get(0));
            System.out.println(arr.get(1));
            System.out.println(arr.get(2));
            System.out.println(arr.get(3));
            update(game.get(0), game.get(1), game.get(2), game.get(3));
            game = move(arr.get(0), arr.get(1),arr.get(2),arr.get(3));
        }


    }
}




/*
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter Filepath");

        String filePath = myObj.nextLine();
        FileReader fr = new FileReader(filePath);
        int i;
        while ((i = fr.read()) != -1)
            System.out.print((char)i);

 */
