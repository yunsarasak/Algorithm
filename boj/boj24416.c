#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int f[41];
int recCount = 0;
int dpCount = 0;

int fib(int n)
{
    if ( n == 1 || n == 2)
    {
        recCount++;
        return 1;
    }
    else{
        return ( fib(n - 1) + fib(n - 2));
    }
}

int fibonacci(int n)
{
    int i = 0;
    f[1] = f[2] = 1;

    for( i=3; i < n; i++)
    {
        dpCount++;
        f[i] = f[i - 1] + f[i - 2];
    }

    return f[n];
}

int main()
{
    int N = 0;
    memset(f, 0x00, sizeof(int) * 41);

    scanf("%d", &N);

    fib(N);
    fibonacci(N);

    printf("%d %d\n", recCount, dpCount+1);

    return 0;
}