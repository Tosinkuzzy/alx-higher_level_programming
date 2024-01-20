#include <stdlib.h>
#include <stdio.h>

#define SIZE 4

struct Stack {
    int top;
    int inp_array[SIZE];
};

void push(struct Stack* stack);
void pop(struct Stack* stack);
void show(struct Stack* stack);

int main(void)
{
struct Stack stack = {-1};
int choice;

while(1)
{
printf("\nPerform operation on the stacks:");
printf("\n1.Push the element\n2.Pop the element\n3.Show\n4.End");
printf("\n\nEnter the choice: ");
scanf("%d", &choice);

switch(choice)
{
case 1:
    push(&stack);
    break;
case 2:
    pop(&stack);
    break;
case 3:
    show(&stack);
    break;
case 4:
    exit(0);
    break;
default:
    printf("\nInvalid choice!!");
}
}
}

/* Pushes an element onto the stack */
void push(struct Stack* stack)
{
int x;

if (stack->top == SIZE - 1)
{
printf("\nOverflow!!");
}
else
{
printf("\nEnter the element to be added to the stack: ");
scanf("%d", &x);
stack->top = stack->top + 1;
stack->inp_array[stack->top] = x;
}
}

/* Pops an element from the stack */
void pop(struct Stack* stack)
{
if (stack->top == -1)
{
printf("\nUnderflow!!");
}
else
{
printf("\nPopped element: %d", stack->inp_array[stack->top]);
stack->top = stack->top - 1;
}
}

/* Displays the elements of the stack */
void show(struct Stack* stack)
{
if (stack->top == -1)
{
printf("\nUnderflow!!");
}
else
{
printf("\nElements present in the stacks: \n");
for (int i = stack->top; i >= 0; i--)
printf("%d\n", stack->inp_array[i]);
}
}

