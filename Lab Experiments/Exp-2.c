#include <stdio.h>

int main()
{
    int nums1[] = {4, 3, 2, 3, 1};
    int nums2[] = {2, 2, 5, 2, 3, 6};

    int n = 5;
    int m = 6;

    int answer1 = 0, answer2 = 0;
    int i, j, found;

    // Count elements of nums1 present in nums2
    for(i = 0; i < n; i++)
    {
        found = 0;
        for(j = 0; j < m; j++)
        {
            if(nums1[i] == nums2[j])
            {
                found = 1;
                break;
            }
        }
        if(found)
            answer1++;
    }

    // Count elements of nums2 present in nums1
    for(i = 0; i < m; i++)
    {
        found = 0;
        for(j = 0; j < n; j++)
        {
            if(nums2[i] == nums1[j])
            {
                found = 1;
                break;
            }
        }
        if(found)
            answer2++;
    }

    printf("[%d, %d]\n", answer1, answer2);
    getchar();

    return 0;
}
