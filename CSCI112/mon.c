/*Ben Farrell
 * classwork week4 
 * 2/12/2022
 */

#include <stdio.h>

int main(void) {
    
    int n;
    int a;
    int b;
    int c;
    int d;
    int e;
    int digits[5];
    printf("Enter a five digit number: ");
    scanf("%d", &n);
        a = n/10000;
        b = (n/1000)%10;
        c = (n/100)%10;
        d = (n/10)%10;
        e = n%10;
    digits[0] = a; 
    digits[1] = b; 
    digits[2] = c;
    digits[3] = d; 
    digits[4] = e;
    for( int i = 0; i < 5; i++) {
        printf("digits[%d] is %d\n",i, digits[i]);
        }
        return(0);
    }



        

