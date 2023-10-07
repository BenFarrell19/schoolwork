package com.company;

public class employee {
    private String firstName;
    private String lastName;
    private int idNumber;

    public employee() {
        firstName = "";
        lastName = "";
        idNumber = 0;
    }

    public employee(String FirstName, String LastName, int IdNumber) {
        firstName = FirstName;
        lastName = LastName;
        idNumber = IdNumber;
    }

    public void setFirstName(String FirstName){
        firstName = FirstName;
    }

    public void setLastName(String LastName) {
        lastName = LastName;
    }

    public void setIdNumber(int IdNumber) {
        idNumber = IdNumber;
    }

    public String getFirstName(){
        return firstName;
    }
    public String getLastName(){
        return lastName;
    }
    public int getIdNumber(){
        return idNumber;
    }
}
