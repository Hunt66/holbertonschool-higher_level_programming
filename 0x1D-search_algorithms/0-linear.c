#include <stdio.h>
#include <stdlib.h>
#include "search_algos.h"


/**
 *lnear_search- a linear search for a number in an array
 *@array: int array to search
 *@size: size_t size of the array
 *@value: int value searched for
 *Return: he first index where value is located or -1 if not there
 */

int linear_search(int *array, size_t size, int value)
{
	size_t i;

	if (array == NULL)
		return(-1);
	for (i = 0; i < size; i++)
	{
		printf("Value checked array[%lu] = [%d]\n", i, array[i]);
		if (array[i] == value)
			return(i);
	}
	return(-1);
}
