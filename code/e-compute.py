#!/usr/bin/python
# -*- coding:utf-8 *-*

import math

def ComputeE():
  print 'math.pow(1 + 1.0/n, n)'
  for n in [2, 4, 10, 50, 100, 1000, 10000, 100000]:
    e = math.pow(1 + 1.0/n, n)
    print n, e

  print 'time math.pow(1 + 1.0/n, n)'
  for n in [1, 2, 3, 12, 365/7,  365, 365*24,  365*24*60, 365*24*60*60]:
    e = math.pow(1 + 1.0/n, n)
    print n, e


  print 'math.pow(1 - 1.0/n, n)'
  for n in [2, 4, 10, 50, 100, 1000]:
    e = math.pow(1 - 1.0/n, n)
    print n, e


  print 'math.pow(1 - 1.0/n, -n)'
  for n in [2, 4, 10, 50, 100, 1000]:
    e = math.pow(1 - 1.0/n, -n)
    print n, e


def ComputeEReciprocal(n):
  result = 0
  factorial = 1
  for r in range(2,n):
    factorial *= r
    term = 1.0 / factorial
    if r % 2 == 1:
      term = -1 * term
    result += term
  return result


for n in [10, 100]:
  print ComputeEReciprocal(n)





