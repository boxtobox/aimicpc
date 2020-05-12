from sys import stdin
from math import pi

r = int(stdin.readline())
euclid_circle = r**2*pi
taxicab_circle = (r*2)**2 / 2
print(euclid_circle)
print(taxicab_circle)
