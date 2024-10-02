from pulp import *
Z=LpProblem('problem',LpMaximize)
x1=LpVariable('x1',lowBound=0)
x2=LpVariable('x2',lowBound=0)
x3=LpVariable('x3',lowBound=0)
Z+=3*x1+5*x2+4*x3
Z+=2*x1+3*x2<=8
Z+=2*x2+5*x3<=10
Z+=3*x1+2*x2+4*x3<=15
print(Z)
Z.solve()
print('x1',value(x1),'\nx2',value(x2),'\nx3',value(x3),'\nZmax=',value(Z.objective),)
