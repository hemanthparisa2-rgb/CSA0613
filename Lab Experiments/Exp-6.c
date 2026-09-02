#include <stdio.h>

int main()
{
    int arr[] = {3, 3, 3, 3, 3};   // Change input here
    int n = 5;
    int i, j, temp;

    if(n == 0)
    {
        printf("List is empty");
        return 0;
    }

    // Bubble Sort
    for(i = 0; i < n - 1; i++)
    {
        for(j = 0; j < n - i - 1; j++)
        {
            if(arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    printf("Maximum Element: %d", arr[n - 1]);
getchar();
    return 0;
}
