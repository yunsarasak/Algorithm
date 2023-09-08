#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ABS(X) _Generic((X), \
                  default: abs,  \
                    double: absf  \
              )(X)

int abs(int a)
{
    int result = 0;

    if( a < 0 )
    {
        result = a * -1;
    }
    else
    {
        result = a;
    }

    return result;
}

double absf(float a)
{
    double result = 0;

    if( a < 0 )
    {
        result = a * -1;
    }
    else
    {
        result = a;
    }

    return result;
}

int main()
{
    char strInput[50] = {0,};
    double fInput = 0;
    int nInput = 0;

    scanf("%s", strInput);

    int isFloat = 0;

    if( strstr(strInput, ".") != NULL )
    {
        //float
        fInput = atof(strInput);
        if( fInput < 0)
            fInput*=-1;
        printf("%g\n", fInput);
    }
    else
    {
        //int
        nInput = atoi(strInput);
        if(nInput < 0)
            nInput*=-1;
        printf("%d\n", nInput);
    }

    return 0;
}