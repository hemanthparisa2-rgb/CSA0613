#include <stdio.h>

int main()
{
    int arr[] = {-10, 2, 3, -4, 5};
    int n = 5;
    int i, max;

    max = arr[0];

    for(i = 1; i < n; i++)
    {
        if(arr[i] > max)
            max = arr[i];
    }

    printf("%d", max);
getchar();
    return 0;
}
