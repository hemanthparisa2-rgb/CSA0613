#include <stdio.h>

int main()
{
    int nums[] = {1, 2, 1};
    int n = 3, sum = 0;
    int i,j;

    for( i = 0; i < n; i++)
    {
        int freq[100] = {0}, distinct = 0;

        for(j = i; j < n; j++)
        {
            if(freq[nums[j]] == 0)
                distinct++;

            freq[nums[j]]++;
            sum += distinct * distinct;
        }
    }

    printf("%d", sum);
    getchar();

    return 0;
}
