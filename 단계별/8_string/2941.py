import sys
import re

word = str(sys.stdin.readline().rstrip())

list2 = re.findall('c=|c-|d-|lj|nj|s=|(?<![d])z=', word)
list3 = re.findall('dz=', word)
word_len = len(word) - len(list2) - 2 * len(list3)
print(word_len)
