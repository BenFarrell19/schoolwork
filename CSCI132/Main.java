package com.company;

public class Main {
    public class Broncos
    {
        private int wins;
        private double rating;
        public Broncos(double r)
        {
            rating = r;
            wins = 10;
        }
        public Broncos(double r, int p)
        {
            wins = p;
            rating = r;
        }
        public Broncos()
        {
            wins = 5;
            rating = 6.5;
        }
        public double getRating()
        {
            return rating;
        }
        public boolean getTruth(double r)
        {
            Broncos d1 = new Broncos(99.6);
            return (d1.getRating() > 50);
        }
        public int watchGame(int amnt)
        {
            int cost;
            cost = wins * amnt;
            return cost;
        }
    }
}


