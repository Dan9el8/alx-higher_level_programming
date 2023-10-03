#include "lists.h"

/**
*insert_node - function that insert nodes in linkedl ist
*@head: A pointer to the head
*@number: number to insert
*
*Return: fail null else new node
*/

listint_t *insert_node(list_t **head, int number)
{
listint_t *node = *head, *new;

new = malloc(sizeof(listint_t));
if (new ==NULL)
return (NULL);
new->n= number;

if (node == NULL || node->n >= number)
{
new-> next = node;
*head = new;
return (new);
}

while (node && node->next && node->next->n < number)
node = node->next;

new->next = node->next;
node->next = new;

return (new);
}
