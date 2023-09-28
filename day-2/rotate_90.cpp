#include<stdio.h>
int main()
{
	int a[10][10],i,j,n;
	printf("\n enter n value");
	scanf("%d",&n);
	printf("\n enter matrix elements");
	for (i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for (i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d",a[i][j]);
		}
	}
}
