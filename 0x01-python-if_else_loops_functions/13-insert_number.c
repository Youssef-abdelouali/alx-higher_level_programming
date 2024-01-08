#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the sorted linked list.
 * @number: The number to be inserted.
 * Return: If successful, a pointer to the newly inserted node; otherwise, NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current = *head, *new_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;

    if (current == NULL || current->n >= number)
    {
        new_node->next = current;
        *head = new_node;
        return (new_node);
    }

    for (; current && current->next && current->next->n < number; current = current->next)
        continue;

    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}
