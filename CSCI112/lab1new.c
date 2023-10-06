#include <stdio.h>

/* Ben Farrell 
 * CSCI 112 Lab 1
 * 2/5/2022
 */


// program calculates discounts for miltary members as well as tax and total cost


double tax(double total) {
    // function to calculate total cost after taxes
    double final;
    final = total*1.05;

    return final;
}



int main(void) {
    // main function takes user input and performs additional calculation and prints final output
    double spend;
    char mil;
    // taking user input
    printf("Cost of purchase:\t\t$");
    scanf("%lf", &spend);
    printf("In military (y or n)?\t\t");
    scanf(" %c", &mil);
    // interpreting user input to give correct response
    if(mil=='y'||mil=='Y') {
        if(spend < 150) {
            // calculations and print for military members spending less than $150
            printf("Military discount (10%%):\t$%0.2f\n", spend-spend*.9);
            printf("Discounted total\t\t$%0.2f\n", spend*.9);
            printf("Sales tax (5%%)\t\t\t$%0.2f\n", tax(spend*.9)-spend*.9);
            printf("Total:\t\t\t\t$%0.2f\n", tax(spend*.9));
        }
        
        else if(spend >= 150) {
             // calculations and print for military members spending more than $150
            printf("Military discount (15%%):\t$%0.2f\n", spend-spend*.85);
            printf("Discounted total\t\t$%0.2f\n", spend*.85);
            printf("Sales tax (5%%):\t\t\t$%0.2f\n", tax(spend*.85)-spend*.85);
            printf("Total:\t\t\t\t$%0.2lf\n", tax(spend*.85));   
        }
        else {
            // user input error handing
            printf("Error: bad input");
        }
    }
    else if(mil=='n'||mil=='N') {
        // calculations and printing for non military members
        printf("Sales tax (5%%):\t\t\t$%0.2f\n", tax(spend) - spend);
        printf("Total:\t\t\t\t$%0.2f\n", tax(spend));  
    }

    else {
        // more error handling
        printf("Error: bad input\n");
        }


}




