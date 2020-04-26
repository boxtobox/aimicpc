# 'a' // 97
# 'z' // 122

import sys


string = str(sys.stdin.readline().rstrip())
occurrences = [-1] * 26

for i in range(len(string)):
    alphabet_code = ord(string[i]) - 97
    if occurrences[alphabet_code] == -1:
        occurrences[alphabet_code] = i

for occur in occurrences:
    print(occur, end=' ')
