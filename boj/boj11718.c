#include <stdio.h>

int main()
{
    int ch = 0;
    while(1)
    {
        ch = getchar();
        if ( ch == EOF )
        {
            break;
        }
        putchar();
    }
    
    return 0;
}