#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LIMIT 20

int g_stack[1000];
int g_top;
int g_size;

void InitStack()
{
    g_top = -1;
    g_size = 100;
    //g_stack = calloc(g_size, sizeof(int));

    return;
}

#if 0
void DestroyStack()
{
    free(g_stack);

    return;
}
#endif

int Count()
{
    return g_top+1;
}

int isEmpty()
{
    if (g_top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void push(int _num)
{
    #if 0
    if( g_top == g_size -1 )
    {
        g_size = g_size * 2;
        g_stack = realloc(g_stack, g_size);
    }
    #endif
    g_stack[++g_top] = _num;

    return;
}

int peek()
{
    if(isEmpty())
    {
        return -1;
    }
    else
    {
        return g_stack[g_top];
    }
}

int pop()
{
    if(isEmpty())
    {
        return -1;
    }
    else
    {
        return g_stack[g_top--];
    }
}


int main()
{
    int lineCount = 0;
    char str[MAX_LIMIT] = {0,};
    int op = 0;
    int val = 0;
    InitStack();
    
    scanf("%d", &lineCount);
    lineCount++;

    while( lineCount-- )
    {
        memset(str, 0x00, sizeof(str));
        fgets(str, MAX_LIMIT, stdin);

        switch ( str[0] )
        {
            case '1':
            {
                op = 0;
                val = 0;
                sscanf(str, "%d %d", &op, &val);
                push(val);
                break;
            }
            case '2':
            {
                printf("%d\n", pop());
                break;
            }
            case '3':
            {
                printf("%d\n", Count());
                break;
            }
            case '4':
            {
                printf("%d\n", isEmpty());
                break;
            }
            case '5':
            {
                printf("%d\n", peek());
                break;
            }
            default:
            break;

        }
    }

    //DestroyStack();
    return 0;
}