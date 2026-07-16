#include <stdio.h>

int main()
{
    printf("=============================================\n");
    printf(" SMART GRID ENERGY DISTRIBUTION SYSTEM\n");
    printf("=============================================\n\n");

    printf("Recurrence Relation:\n");
    printf("T(n) = 4T(n/2) + nlogn\n\n");

    printf("Master Theorem Parameters:\n");
    printf("a = 4\n");
    printf("b = 2\n");
    printf("f(n) = nlogn\n\n");

    printf("Step 1:\n");
    printf("n^(log2 4) = n^2\n\n");

    printf("Step 2:\n");
    printf("nlogn grows slower than n^2\n\n");

    printf("Step 3:\n");
    printf("Master Theorem Case 1 is applicable.\n\n");

    printf("Result:\n");
    printf("Time Complexity  : Theta(n^2)\n");
    printf("Space Complexity : Theta(log n)\n\n");

    printf("Performance Analysis:\n");
    printf("As the energy network grows, execution time increases\n");
    printf("quadratically. This is suitable for small and medium-sized\n");
    printf("networks but becomes more expensive for very large systems.\n");
printf("\nPress Enter to exit...");
getchar();
    return 0;
}
