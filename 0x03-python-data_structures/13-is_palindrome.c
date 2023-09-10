#include "lists.h"

#define NULL ((void *)0)

/**
 * comp_lists - compares 2 linked lists
 * @l1: pointer to the head of the 1st list
 * @l2: pointer to the head of the 2nd list
 * Return: 1 if lists are identical, 0 otherwise
 *
 * int comp_lists(listint_t *l1, listint_t *l2)
 * {
 * 	while (l1 != NULL && l2 != NULL)
 * 	{
 * 		if (l1->n != l2->n)
 * 			return (0);
 * 
 * 		l1 = l1->next;
 * 		l2 = l2->next;
 * 	}
 * 
 * 	return (l1 == NULL && l2 == NULL);
 * }
 */

/**
 * rev_list - reverses a singly linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *rev_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *nxt = NULL;

	while (current != NULL)
	{
		nxt = current->next;
		current->next = prev;
		prev = current;
		current = nxt;
	}

	return (prev);
}

/**
 * comp_half - compares halves
 * @fh: pointer to 1st half
 * @sec_h: pointer to 2nd half
 * Return: nothing
 */
int comp_half(listint_t *fh, listint_t *sec_h)
{
	while (sec_h != NULL)
	{
		if (fh->n != sec_h->n)
			return (0);

		fh = fh->next;
		sec_h = sec_h->next;
	}
	return (1);
}


/**
 * is_palindrome - checks for a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head;
	listint_t *f = *head;
	listint_t *sh = NULL;
	listint_t *ps = *head;
	listint_t *mid_nd = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (f != NULL && f->next != NULL)
		{
			f = f->next->next;
			ps = s;
			s = s->next;
		}

		if (f != NULL)
		{
			mid_nd = s;
			s = s->next;
		}

		sh = rev_list(s);
		/*ps->next = sh;*/
		is_palindrome = comp_half(*head, sh);

		ps->next = mid_nd;
		if (mid_nd != NULL)
			mid_nd->next = rev_list(sh);
		else
			*head = rev_list(sh);
	}
	return (is_palindrome);
}
