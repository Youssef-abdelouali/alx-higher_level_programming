#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the first node in the list.
 *
 * Return: Pointer to the first node in the reversed list.
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *reversed = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			reversed = slow->next;
			break;
		}
		if (!fast->next)
		{
			reversed = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_list(&reversed);

	while (reversed && temp)
	{
		if (temp->n == reversed->n)
		{
			reversed = reversed->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!reversed)
		return (1);

	return (0);
}
