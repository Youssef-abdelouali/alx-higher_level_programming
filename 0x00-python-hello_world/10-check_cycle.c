#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @list: Linked list to check.
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't.
 */
int check_cycle(listint_t *list)
{
	/* Initialize slow and fast pointers to the start of the list */
	listint_t *slow = list;
	listint_t *fast = list;

	/* Check if the list is NULL */
	if (!list)
		return (0);

	/* Traverse the list using a do-while loop */
	do {
		/* Move slow pointer one step at a time */
		slow = slow->next;

		/* Move fast pointer two steps at a time, if possible */
		fast = fast->next ? fast->next->next : NULL;

		/* Check if slow and fast pointers meet, indicating a cycle */
		if (slow == fast)
			return (1);

	/* Continue looping while both pointers are not NULL */
	} while (slow && fast);

	/* Return 0 if no cycle is found in the list */
	return (0);
}
