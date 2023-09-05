#include "lists.h"

/**
 * insert_node - insert node into sorted singly linked list
 * @head: pointer to head
 * @number: new data
 * Return: address of number, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *apo, *current, *neau;

	if (!head)
		return (NULL);

	neau = malloc(sizeof(listint_t));
	if (neau == NULL)
		return (NULL);
	neau->n = number;
	neau->next = NULL;

	if (head == NULL || head->n >= number)
	{
		neau->next = head;
		*head = neau;
		return (neau);
	}
	apo = *head;
	current = (*head)->next;
	while (current != NULL && current->n < number)
	{
		apo = current;
		current = current->next;
	}
	apo->next = neau;
	neau->next = current;

	return (neau);	
}
