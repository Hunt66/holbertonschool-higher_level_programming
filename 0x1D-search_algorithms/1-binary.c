#include <stdio.h>
#include <stdlib.h>
#include "search_algos.h"



/**
 *binary_help: helper function for binary search tree
 *@array: int array to search
 *@left: the left limit of this rotation
 *@right: the right limit of this rotation
 *@value: value searched for
 */

int binary_help(int *array, size_t left, size_t right, int value)
{
	size_t i, mid;

	mid = (right - left) / 2 + left;
	printf("Searching in array: ");
	for (i = left; i < right; i++)
		printf("%d, ", array[i]);
	printf("%d\n", array[i]);
	if (right - left == 0 && array[mid] != value)
		return (-1);
	if (array[mid] == value)
		return (value);
	if (array[mid] > value)
		right = (right / 2) - 1;
	if (array[mid] < value)
		left = left + ((right - left) / 2) + 1;
	return (binary_help(array, left, right, value));
}


/**
 *binary_search- uses a binary search to find a value in an array
 *@array: the sorted int array to be searched
 *@size: size_t size of array
 *@value: the value searched for
 */

int binary_search(int *array, size_t size, int value)
{
	return(binary_help(array, 0, size - 1, value));
}








/*	size_t i, k, j = 0;

	while (1)
	{
		i = size/2 + j;
		printf("%lu\n", i);
		if (size/2 == 0 && array[i] != value)
			return(-1);
		printf("Searching in array: ");
		for (k = j; k < size + j - 1; k++)
			printf("%d, ", array[k]);
		printf("%d\n", array[k]);
		if (array[i] == value)
			return(i);
		if (array[i] < value)
		{
			j = i;
			size = size/2;
		}
		if (array[i] > value)
		{
			size = size/2 - 1;
		}
	}
	}*/
