#include <stdio.h>
#include <string.h>

int isPalindrome(char str[])
{
    int i, len = strlen(str);

    for(i = 0; i < len / 2; i++)
    {
        if(str[i] != str[len - i - 1])
            return 0;
    }
    return 1;
}

int main()
{
    char words[][20] = {"abc", "car", "ada", "racecar", "cool"};
    int n = 5;
    int i, found = 0;

    for(i = 0; i < n; i++)
    {
        if(isPalindrome(words[i]))
        {
            printf("First Palindromic String: %s", words[i]);
            found = 1;
            break;
        }
    }

    if(!found)
        printf("No Palindromic String Found");
        getchar();

    return 0;
}
