#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# vanya ahmed Siddiqui
# 200901095
# BSCS-01 (B)

from collections import deque
#defining stack classs
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def is_empty(self):
        return len(self.container)==0
    def top(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
stack = Stack()
#to take the input of the equation:
A = input("ENTER YOUR EQUATION")
Condition=True
count=0
try:
    for i in A:
        if i =='[' or i=='{' or i == '(':
            stack.push(i)
        elif i==']' or i=='}' or i==')':
            stack.pop()
    if stack.size() == 0:
        for i in range(0,len(A)):
            if A[i]=='"':
                if count%2==0:     # to check whether the quotation marks in the parenthesis are in even or odd we will
                    count+=1
                    if A[i+1]==']' or A[i+1] =='}' or A[i+1]==')' or A[i+1]=='"':
                        condition= False
                    else:
                        condition= True
                else:
                    condition=True
                    count+=1
# to check the answer            
    if count%2==0:
        condition= True
    else:
        condition= False
    if condition:
        print("valid")
    else:
        print("not valid")
except:
    print("not valid")

