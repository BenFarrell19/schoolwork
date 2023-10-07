package com.company;


public class commissionEmployee extends employee{
    private int commissionRate;
    private int grossSales;

    public commissionEmployee() {
        commissionRate = 0;
        grossSales = 0;
    }

    public commissionEmployee(int CommissionRate, int GrossSales) {
        commissionRate = CommissionRate;
        grossSales = GrossSales;
    }

    public void setCommissionRate(int CommissionRate){
        commissionRate = CommissionRate;
    }

    public void setGrossSales(int GrossSales) {
        grossSales = GrossSales;
    }

    public int getCommissionRate(){
        return commissionRate;
    }

    public int getGrossSales(){
        return grossSales;
    }
}
