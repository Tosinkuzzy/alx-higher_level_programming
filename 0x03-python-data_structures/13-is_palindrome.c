#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

size_t listint_len(const listint_t *h)
{
int length = 0;

while (h != NULL)
{
++length;
h = h->next;
}

return (length);
}

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
listint_t *current = head;
unsigned int times = 0;

if (head)
{
while (current != NULL)
{
if (times == index)
return (current);

current = current->next;
++times;
}
}

return (NULL);
}

int is_palindrome(listint_t **head)
{
listint_t *start = NULL, *end = NULL;
unsigned int i = 0, len = 0;

if (head == NULL)
return (0);

if (*head == NULL)
return (1);

len = listint_len(*head);

for (; i < len; i++)
{
start = get_nodeint_at_index(*head, i);
end = get_nodeint_at_index(*head, len-i-1);
if (start->n != end->n)
return (0);
}

return (1);
}

