package com.company;

public class Driver {
    public static void main(String [] args)
    {

        employee eOne = new employee("John", "Smith", 1234);
        System.out.println(eOne.getFirstName());
        System.out.println(eOne.getLastName());
        System.out.println(eOne.getIdNumber());

        hourlyEmployee heOne = new hourlyEmployee(15, 40);
        System.out.println(heOne.getWage());
        System.out.println(heOne.getHours());

        commissionEmployee ceOne = new commissionEmployee(100, 500);
        System.out.println(ceOne.getCommissionRate());
        System.out.println(ceOne.getGrossSales());

        commissionBase cbOne = new commissionBase(50000);
        System.out.println(cbOne.getBaseSalary());

    }

}
