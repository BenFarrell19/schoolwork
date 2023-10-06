#include <stdio.h>

/* Ben Farrell
 * CSCI 112, week3 classwork
 *2/4/2022
 */

int main()
{
    int num_1;
    int num_2;
    printf("Enter integer one: ");
    scanf("%d", &num_1);
    printf("Enter integer two: ");
    scanf("%d", &num_2);

    if(num_1 > num_2)
    {
        printf("Number 1 is greater than number 2");
    }
    else if(num_2 > num_1)
    {
        printf("Number 2 is greater than number 1");
    }
    else if (num_2==num_1)
    {
        printf("The two numbers are equal");
    }
    
    return 0;
}
