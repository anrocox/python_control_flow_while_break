#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

How to end a while loop in Python?

¿Cómo terminar un ciclo while en Python?
'''

#break statement terminates the current loop and resumes execution at the next
#statement

#create a integer
n = 1

#iterates whilst the value of n is less than 5
while n < 5:
    print('n = ' + str(n))

    #checks if the remainder of the division by three is equal to 0
    #if n is a multiple of 3 ends the cycle
    if n % 3 == 0:
        break

    #adds 1 to value n
    n += 1

print('the final value of n is ' + str(n))
