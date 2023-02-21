import sys
input = sys.stdin.readline
 
# CODE FOR https://dmoj.ca/problem/ccc22s2
x = int(input())
same_group = []
for i in range(x):
  a, b = input()[:-1].split(' ')
  same_group.append([a, b])
 
y = int(input())
dif_group = []
for i in range(y):
  a, b = input()[:-1].split(' ')
  dif_group.append([a, b])
 
group_assignments = {}
g = int(input())
for i in range(g):
  a, b, c = input()[:-1].split(' ')
  group_assignments[a] = i
  group_assignments[b] = i
  group_assignments[c] = i
 
violations = 0
for i in range(x):
  a = same_group[i][0]
  b = same_group[i][1]
  a_group = group_assignments[a]
  b_group = group_assignments[b]
  if a_group != b_group:
    violations += 1
 
for i in range(y):
  a = dif_group[i][0]
  b = dif_group[i][1]
  a_group = group_assignments[a]
  b_group = group_assignments[b]
  if a_group == b_group:
    violations += 1
 
print(violations)