#include <stdio.h>

int main()
{
    int nums[] = {3,1,2,2,2,1,3};
    int n = 7;
    int k = 2;
    int i, j, count = 0;

    for(i = 0; i < n; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            if(nums[i] == nums[j] && (i * j) % k == 0)
                count++;
        }
    }

    printf("%d", count);
getchar();
    return 0;
}
