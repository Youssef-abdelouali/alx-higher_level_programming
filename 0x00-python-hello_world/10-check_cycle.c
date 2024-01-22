#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *sl_ = list;
	listint_t *fa_ = list;

	if (!list)
		return (0);

	while (sl_ && fa_ && fa_->next)
	{
		sl_ = sl_->next;
		fa_ = fa_->next->next;
		if (sl_ == fa_)
			return (1);
	}

	return (0);
}
