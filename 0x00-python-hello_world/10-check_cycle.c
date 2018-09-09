#include "lists.h"

/**
 *check_cycle- checks if a linked list goes in a loop
 *@list: the list that is checked
 *Return: 0 if no cycle 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *faster = NULL;
	listint_t *slower = NULL;

	if (list == NULL)
		return(0);

	faster = list;
	slower = list;
	while (1)
	{
		faster = faster->next;
		if (faster == NULL)
			return (0);
		faster = faster->next;
		slower = slower->next;
		if (faster == NULL || slower == NULL)
			return (0);
		if (faster == slower)
			return (1);
	}
}
