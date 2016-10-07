import numpy as np
import pylab as pl
Number_A = [ ]
Number_B = [ ]
t = [ ]
print 'The Number of A atom ->'
number_a = input( )
Number_A.append(number_a)
print 'The Number of B atom ->'
number_b = input( )
Number_B.append(number_b)
print 'The time of decay ->'
t_decay = input()
print 'the time step ->'
dt = input()

def Bigger(a,b):
  if a>b:
      return a
  else:
      return b
def Smaller(a,b):
  if a>b:
      return b
  else:
      return a
big=Bigger(Number_A[0],Number_B[0])
small=Smaller(Number_A[0],Number_B[0])
t.append(0.0)
for i in range(100):
    NA = Number_A[i] + ((Number_B[i] - Number_A[i]) / t_decay) * dt
    NB = Number_B[i] + ((Number_A[i] - Number_B[i]) / t_decay) * dt
    tadd = t[i] + dt
    Number_A.append(NA)
    Number_B.append(NB)
    t.append(tadd)
    t_max=t[-1]

pl.plot(t,Number_A,'r')
pl.plot(t,Number_B,'b')
pl.title('the decay between A and B')
pl.xlabel('the time of decay')
pl.ylabel('number of atoms')
pl.xlim(0.0,t_max)
pl.ylim(small,big)
pl.show
