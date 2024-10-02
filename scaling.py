from sympy import *
x=eval(input("Enter the first point: "))
y=eval(input("Enter the secoin point: "))
z=0
p=Point(x,y)

T=Matrix([[eval(input()),eval(input()),0],[eval(input()),eval(input()),0],[0,0,1]])
P1=p.transform(T)
print(P1)
