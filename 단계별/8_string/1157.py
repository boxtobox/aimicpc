# A 65 a 97 ? 63
import sys

word = str(sys.stdin.readline().rstrip())

alphabet_count = [0] * 26

for letter in word:
    code = ord(letter)
    if code >= 97:
        code -= 32
    alphabet_count[code-65] += 1

max_count = 0
result = -1

# for i in range(len(alphabet_count)):
#     count = alphabet_count[i]
#     if count > max_count:
#         result = i
#         max_count = count
#     elif count == max_count:
#         result = -1
if sorted(alphabet_count, reverse=True)[0] == sorted(alphabet_count, reverse=True)[1]:
    print('?')
else:
    result = alphabet_count.index(max(alphabet_count))
    print(chr(result + 65))

# if result == -1:
#     print('?')
# else:
#     print(chr(result + 65))
