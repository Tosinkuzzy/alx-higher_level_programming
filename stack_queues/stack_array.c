#!/bin/bash
#include <stdlib.h>
#include <stdio.h>

#define SIZE 4

int top = -1, inp_array[SIZE];
void push();
void pop();
void show();

int main()
{
int choice;

while(1)
{
printf("\nPerform operation on the stacks:");
