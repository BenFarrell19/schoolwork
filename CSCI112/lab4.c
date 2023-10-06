/*Ben Farrell 
 * Lab 2
 * 2/12/2022
 */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>


// program takes user number input, takes sum of digits and checks if divisible by 9
//
int get_length (int n, int arr[]) {
    int length = (int)log10(n)+1;
    int i;
    for(i = 0; i < length; i++){
        arr[i] = (int)(n/pow(10,length-i-1))%10;
    }
    return length;
}

int calc_sum(int arr[], int length) {
    // calculate sum of numbers digits added together
    int i;
    int s = 0;
    for(i = 0; i < length; i++) {
        s += arr[i];
        }
    return s;
    }
    


int main(void) {
    //main fucntion takes user input 
    int n;
    printf("Enter number to check (0 to end): ");
    scanf("%d", &n);
    int arr[100];
    int len = get_length(n, arr);

    int sum = calc_sum(arr, len);
    if(n == 0) {
        exit(0);
    }
    // calculating if number is divisble by after getting sum of digits
    if(sum%9){
        printf("Since %d is not divisible by 9, %d is not divisible by 9\n", sum, n);
    }
    else {
        printf("Since %d is divisible by 9, %d is divisible by 9\n", sum, n);
     } 
     
    while(n > 0){

        printf("Enter number to check (0 to end): ");
        scanf("%d", &n);
        if(n == 0){
            break;
            }
        int arr[100];
        int length = get_length(n, arr);

        int sum = calc_sum(arr, length);
        if(sum%9){
            printf("Since %d is not divisible by 9, %d is not divisible by 9\n", sum, n);
            }
        else {
            printf("Since %d is divisible by 9, %d is divisible by 9\n", sum, n);
            }
        }
    return 0;   
}


    


