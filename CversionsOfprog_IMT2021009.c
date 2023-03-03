/*Following is the C version of the programs I did*/

#include<stdio.h>

/* 1. Simple Addition */
int main()
{
	int x,y,z;
	scanf("%i %i",&x,&y);
	z=x+y;
}

/* 2. Simple Subtraction */
int main()
{
	int a,b,c;
	scanf("%i %i",&a,&b);
	c=b-a;
}

/* 3. Average of twelve numbers */
int main()
{
	int a[11],c,i;
	scanf("%i %i %i %i %i %i %i %i %i %i %i %i",&a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8],&a[9],&a[10],&a[11]);
	c=(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11])/12;
}

/* 4. Product of thirteen numbers */
int main()
{
	int a[12],c,i;
	scanf("%i %i %i %i %i %i %i %i %i %i %i %i %i",&a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8],&a[9],&a[10],&a[11],&a[12]);
	c=(a[0]*a[1]*a[2]*a[3]*a[4]*a[5]*a[6]*a[7]*a[8]*a[9]*a[10]*a[11]*a[12]);
}


