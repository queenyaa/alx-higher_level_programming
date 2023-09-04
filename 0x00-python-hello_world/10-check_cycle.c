#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to head of linked list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tort = list;
	listint_t *hare = list;

	if (!list)
		return (0);

	while (tort && hare && hare->next)
	{
		tort = tort->next;		/*move tort one step*/
		hare = hare->next->next;	/*move hare two steps*/

		if (tort == hare)	/*if they meet, there is a cycle*/
			return (1);
	}

	return (0); /*if we reach the end, there's no cycle*/
}
