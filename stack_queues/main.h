#ifndef MAIN_H
#define MAIN_H

#include <stdlib.h>
#include <stdio.h>

#define SIZE 4

struct Stack
{
    int top;
    int inp_array[SIZE];
};

void push(struct Stack* stack);
void pop(struct Stack* stack);
void show(struct Stack* stack);

#endif /* MAIN_H *\
