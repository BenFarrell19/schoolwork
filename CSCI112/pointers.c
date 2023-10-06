/* Ben Farrell
 * 2/14/2022
 * week5 classwork
 */

#include <stdio.h>
#include <stdlib.h>


int main() {
    int *x;
    x = malloc(sizeof(int));
    *x = 5;
    printf("address of x is %p\n", &x);
    printf("Value: %d\n", *x);


    double *y;
    y = malloc(sizeof(double));
    *y = 2.5;
    printf("Address of y is %p\n", &y);
    printf("Value: %lf\n", *y);
    
    char *z;
    z = malloc(sizeof(char));
    *z = 'z';
    printf("address of z is %p\n", &z);
    printf("Value: %c\n", *z); 
                                    
    return(0);

    free(z);
    free(y);
    free(x);
}
