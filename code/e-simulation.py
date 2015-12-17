#!/usr/bin/python
# -*- coding:utf-8 *-*

import sys
import math
import random


def RunExp():
  sum = 0
  n = 0
  while sum < 1:
    sum += random.uniform(0,1)
    n += 1
  return n 

def RunExp2():
  sum = 0
  n = 0
  while sum < 1:
    sum += random.sample(range(1,51),1)[0] / 50.0
    n += 1
  return n 


def CalcExpectation(d, N):
  avg = 0
  for n, count in d.items():
    avg += 1.0 * n * count / N 
  return avg

def main(argv):
  d = {}
  N = 0
  for i in range(111150):
    n = RunExp()
    if n in d:
      d[n] += 1
    else:
      d[n] = 1
    N += 1
  print d 
  print CalcExpectation(d, N)
  
if __name__ == '__main__':
  main(sys.argv)

