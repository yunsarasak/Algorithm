
int sqrt(long long sqaured_num)
{
    long long cur = 0;
    int answer = 0;

    while(1)
    {
        if( cur * cur > sqaured_num)
        {
            break;
        }
        else
        {
            cur++;
        }
    }

    answer = (int)(cur - 1);
    
    return answer;
}