package com.company;


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class lab9 extends JFrame {

    public static JFrame f = new JFrame("Color Switcher");



    public static void main(String[] args) throws Exception {

        f.setSize(500, 500);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.getContentPane().setBackground(Color.BLACK);


        JButton red = new JButton("Red");
        red.setBounds(10, 10, 80, 30);
        f.add(red);

        red.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                f.getContentPane().setBackground(Color.RED);
            }
        });

        JButton blue = new JButton("Blue");
        blue.setBounds(95, 10, 80, 30);
        f.add(blue);
        blue.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                f.getContentPane().setBackground(Color.BLUE);
            }
        });

    }
}