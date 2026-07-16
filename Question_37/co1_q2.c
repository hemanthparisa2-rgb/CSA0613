
#include <stdio.h>

int main()
{
    printf("=====================================\n");
    printf(" AI-BASED CHATBOT PROCESSING\n");
    printf("=====================================\n\n");

    printf("Recurrence Relation:\n");
    printf("T(n) = T(n/2) + log n\n\n");

    printf("Master Theorem Parameters:\n");
    printf("a = 1\n");
    printf("b = 2\n");
    printf("f(n) = log n\n\n");

    printf("Step 1:\n");
    printf("n^(log2 1) = n^0 = 1\n\n");

    printf("Step 2:\n");
    printf("f(n) = log n = Theta(n^0 log n)\n\n");

    printf("Step 3:\n");
    printf("Master Theorem Case 2 is applicable.\n\n");

    printf("Result:\n");
    printf("Time Complexity  : Theta((log n)^2)\n");
    printf("Space Complexity : Theta(log n)\n\n");

    printf("Performance Analysis:\n");
    printf("The chatbot divides user queries into smaller subproblems.\n");
    printf("Response time grows very slowly as the number of queries increases,\n");
    printf("making the chatbot efficient for large-scale applications.\n");
printf("\nPress Enter to exit...");
getchar();
    return 0;
}
