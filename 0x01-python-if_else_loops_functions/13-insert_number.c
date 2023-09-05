#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

#define NULL ((void *)0)

/**
 * insert_node - insert node into sorted singly linked list
 * @head: pointer to head
 * @number: new data
 * Return: address of number, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *apo, *curr, *neau;
	int v;

	v = 0;
	curr = apo = *head;
	neau = malloc(sizeof(listint_t));
	if (neau == NULL)
		return (NULL);
	neau->n = number;
	neau->next = *head;

	if (*head == NULL)
	{
		*head = neau;
		return (neau);
	}
	while (curr != NULL)
	{
		v++;
		if (curr->n >= number)
		{
			if (v == 1)
				*head = neau;
			else
				apo->next = neau;
			neau->next = curr;
			return (neau);
		}
		apo = curr;
		curr = curr->next;
	}

	apo->next = neau;
	neau->next = NULL;

	return (neau);	
}
