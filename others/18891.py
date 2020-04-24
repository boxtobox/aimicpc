import sys


total_party, total_votes = map(int, sys.stdin.readline().split())
vote_for_party = []
not_in_party = 253

for _ in range(total_party):
    name, region, proportional = map(str, sys.stdin.readline().split())
    region = int(region)
    proportional = int(proportional)
    not_in_party -= region
    vote_for_party.append((name, region, proportional))

print("name     region      prop")

for data in vote_for_party:
    print(data[0], data[1], data[2])

print(f'not in party: {not_in_party}')