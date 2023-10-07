package com.company;

public class hourlyEmployee extends employee{
    private int wage;
    private int hours;

    public hourlyEmployee() {
        wage = 0;
        hours = 0;
    }

    public hourlyEmployee(int Wage, int Hours) {
        wage = Wage;
        hours = Hours;
    }

    public void setWage(int Wage){
        wage = Wage;
    }

    public void setHours(int Hours) {
        hours = Hours;
    }

    public int getWage(){
        return wage;
    }

    public int getHours(){
        return hours;
    }
}
