#include <stdio.h>


int IsCenter(int _x, int _y, int _size)
{
	int step = _size / 3;


	if (( (step <= _x) && (_x <= 2*step-1) ) && (  (step <= _y) && (_y <= 2*step-1) ))
	{
		return 1;
	}
	else
	{
		if ( _size == 3)
			return 0;
		else
			return IsCenter(_x%step, _y%step, _size/3);
	}
}


int main()
{
	int nSize = 0;
	int i=0, j=0;



	scanf("%d" ,&nSize);


	for(i = 0; i< nSize; i++)
	{
		for(j = 0; j < nSize; j++)
		{
			if( IsCenter(i, j, nSize) )
			{
				printf(" ");
			}
			else
			{
				printf("*");
			}
		}
		printf("\n");
	}

	

	return 0;
}
