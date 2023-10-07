package com.company;


public class commissionBase extends commissionEmployee{
    private int baseSalary;

    public commissionBase() {
        baseSalary = 0;
    }

    public commissionBase(int BaseSalary) {
        baseSalary = BaseSalary;
    }

    public void setBaseSalary(int BaseSalary){
        baseSalary = BaseSalary;
    }

    public int getBaseSalary(){
        return baseSalary;
    }
}
