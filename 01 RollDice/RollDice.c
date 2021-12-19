#include <stdio.h>

int ft_mini_atoi(char *str);

int main (int argc, char **argv)
{
	int cases;
	cases = ft_mini_atoi(argv[1]);

	int count;
	count = 0;

	/*
	int testInt = 0;
	while (testInt < argc)
	{
		printf("The input %i is %s \n", testInt, argv[testInt]);
		testInt++;
	}
	*/



}

int ft_mini_atoi(char *str)
{
	return (str[0] - '0');
}