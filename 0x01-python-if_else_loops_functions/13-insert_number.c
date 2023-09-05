#include "lists.h"

/**
 * insert_node - insert node into sorted singly linked list
 * @head: pointer to head
 * @number: new data
 * Return: address of number, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *apo = *head, *neau;

	neau = malloc(sizeof(listint_t));
	if (neau == NULL)
		return (NULL);
	neau->n = number;

	if (apo == NULL || apo->n >= number)
	{
		neau->next = apo;
		*head = neau;
		return (neau);
	}

	while (apo && apo->next && apo->next->n < number)
		apo = apo->next;

	neau->next = apo->next;
	apo->next = neau;

	return (neau);	
}
